#!/usr/bin/env python3
"""Read-only SLB2 v3 metadata comparison. No decryption or code extraction.

Python 3 standard library only. Offsets and lengths accept decimal or 0x hex.
Windows are half-open [offset, offset+length), bounded to 16 MiB each.
"""
import argparse
import csv
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import struct
import sys
from collections import Counter

CHUNK = 1024 * 1024
MAX_WINDOW = 16 * CHUNK

class FormatError(ValueError):
    """Invalid or unsupported container layout."""

def read_at(f, start, size):
    f.seek(start)
    data = f.read(size)
    if len(data) != size:
        raise FormatError(f'truncated range at {start:#x}: need {size}, got {len(data)}')
    return data

def scan_range(f, start, size):
    digest = hashlib.sha256()
    zeros = True
    f.seek(start)
    remaining = size
    while remaining:
        data = f.read(min(CHUNK, remaining))
        if not data:
            raise FormatError('input truncated during streaming read')
        digest.update(data)
        zeros = zeros and not any(data)
        remaining -= len(data)
    return {'sha256': digest.hexdigest(), 'all_zero': zeros}

def snapshot(stat):
    return (stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns)

def inspect(path):
    path = Path(path)
    with path.open('rb') as f:
        before = os.fstat(f.fileno())
        size = before.st_size
        head = read_at(f, 0, 32)
        magic, version, flags, count, blocks = struct.unpack_from('<4s4I', head)
        if magic != b'SLB2': raise FormatError('not an SLB2 package')
        if version != 3: raise FormatError(f'unsupported SLB2 version {version}; only v3 is implemented')
        if not 1 <= count <= 4096: raise FormatError(f'invalid entry count {count}')
        table_end = 32 + count * 48
        if table_end > size: raise FormatError('truncated entry table')
        if blocks * 512 != size: raise FormatError('block count does not match complete file size')
        entries = []
        for i in range(count):
            raw = read_at(f, 32 + i * 48, 48)
            sector, length = struct.unpack_from('<II', raw)
            start = sector * 512
            if length == 0: raise FormatError(f'entry {i}: zero size')
            if start < table_end: raise FormatError(f'entry {i}: offset overlaps header/table')
            if start > size or length > size - start: raise FormatError(f'entry {i}: extent exceeds file bounds')
            name_bytes = raw[16:48]
            if b'\0' not in name_bytes: raise FormatError(f'entry {i}: unterminated name')
            try: name = name_bytes.split(b'\0', 1)[0].decode('ascii')
            except UnicodeDecodeError as e: raise FormatError(f'entry {i}: non-ASCII name') from e
            if not name: raise FormatError(f'entry {i}: empty name')
            prefix = read_at(f, start, min(16, length))
            entry = dict(index=i, name=name, sector=sector, offset=start, size=length, end=start+length,
                         sector_aligned=True, reserved_zero=not any(raw[8:16]),
                         prefix16_hex=prefix.hex())
            if len(prefix) == 16:
                entry['raw_u16_04_06_08_0a_0c_0e'] = list(struct.unpack_from('<6H',prefix,4))
            entries.append(entry)
        ordered = sorted(entries,key=lambda e:e['offset'])
        for a,b in zip(ordered,ordered[1:]):
            if a['end'] > b['offset']: raise FormatError('overlapping entry extents')
        # Validate all extents before expensive hashing or sample reads.
        for entry in entries:
            start, length = entry['offset'], entry['size']
            entry['sha256'] = scan_range(f,start,length)['sha256']
            sample_offset = min(0x4000, length)
            sample = read_at(f,start+sample_offset,min(CHUNK,length-sample_offset))
            distribution = Counter(sample)
            entry['sample'] = dict(relative_offset=sample_offset, bytes=len(sample),
                sha256=hashlib.sha256(sample).hexdigest(),
                entropy_bits_per_byte=-sum((n/len(sample))*math.log2(n/len(sample)) for n in distribution.values()) if sample else None,
                byte_counts=[distribution.get(b,0) for b in range(256)])
        gaps = []
        for i, e in enumerate(ordered):
            end = ordered[i+1]['offset'] if i+1<len(ordered) else size
            gap = dict(offset=e['end'],size=end-e['end'],kind='inter_entry_gap' if i+1<len(ordered) else 'trailing_padding')
            gap.update(scan_range(f,gap['offset'],gap['size']));gaps.append(gap)
        full = scan_range(f,0,size)['sha256']
        after = os.fstat(f.fileno())
        if snapshot(before) != snapshot(after) or snapshot(after) != snapshot(path.stat()):
            raise FormatError('input metadata changed during analysis')
    return dict(input=str(path),size=size,sha256=full,magic='SLB2',version=version,flags=flags,
                entry_count=count,block_count=blocks,alignment_remainder=size%512,entries=entries,gaps=gaps,
                input_stat_preserved=True,scope='SLB2 v3 metadata; inner field meanings and protected contents are not decoded')

def compare_window(a,b,offset,length):
    if offset < 0 or not 0 < length <= MAX_WINDOW: raise ValueError('invalid window; length must be 1..16 MiB')
    if any(offset+length > Path(p).stat().st_size for p in [a,b]): raise FormatError('comparison window exceeds input bounds')
    hashes=[hashlib.sha256(),hashlib.sha256()];different=0;first=[]
    with Path(a).open('rb') as fa,Path(b).open('rb') as fb:
        before=[snapshot(os.fstat(f.fileno())) for f in [fa,fb]]
        for pos in range(offset,offset+length,CHUNK):
            n=min(CHUNK,offset+length-pos)
            x=read_at(fa,pos,n);y=read_at(fb,pos,n)
            hashes[0].update(x);hashes[1].update(y)
            for j,(u,v) in enumerate(zip(x,y)):
                if u!=v:
                    different+=1
                    if len(first)<16:first.append(pos+j)
        if before != [snapshot(os.fstat(f.fileno())) for f in [fa,fb]]:
            raise FormatError('input changed during window comparison')
    return dict(left=str(a),right=str(b),offset=offset,length=length,end_exclusive=offset+length,
                differing_bytes=different,first_differing_offsets=first,sha256=[h.hexdigest() for h in hashes])

def window_arg(s):
    try:
        start,length=(int(v,0) for v in s.split(':'))
        if start<0 or not 0<length<=MAX_WINDOW:raise ValueError()
        return start,length
    except ValueError as e: raise argparse.ArgumentTypeError('window must be OFFSET:LENGTH; 0<LENGTH<=0x1000000') from e

def run(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('inputs',nargs='+',type=Path)
    ap.add_argument('--window',action='append',default=[],type=window_arg)
    ap.add_argument('--json',dest='json_out',type=Path)
    ap.add_argument('--csv',dest='csv_out',type=Path)
    args=ap.parse_args(argv)
    if len(args.window)>32:ap.error('at most 32 windows')
    outputs=[p for p in [args.json_out,args.csv_out] if p]
    resolved=[p.resolve() for p in args.inputs]
    for p in outputs:
        if p.resolve() in resolved or any(p.exists() and i.exists() and os.path.samefile(p,i) for i in args.inputs):
            ap.error('output aliases an input; refusing to modify it')
    if len({p.resolve() for p in outputs})!=len(outputs) or (len(outputs)==2 and all(p.exists() for p in outputs) and os.path.samefile(*outputs)):
        ap.error('JSON and CSV outputs must be distinct')
    result={'schema_version':1,'packages':[],'comparisons':[],'errors':[]}
    for p in args.inputs:
        try: result['packages'].append(inspect(p))
        except (OSError,ValueError,struct.error) as e: result['errors'].append({'input':str(p),'error':str(e)})
    for a,b in itertools.combinations(result['packages'],2):
        for offset,length in args.window:
            try: result['comparisons'].append(compare_window(a['input'],b['input'],offset,length))
            except (OSError,ValueError) as e:result['errors'].append({'comparison':[a['input'],b['input']],'error':str(e)})
    if args.json_out:args.json_out.write_text(json.dumps(result,indent=2)+'\n')
    if args.csv_out:
        fields=['input','size','sha256','version','flags','block_count','entry_count','entry_index','entry_name','entry_offset','entry_size','entry_sha256','prefix16_hex','following_gap_size','following_gap_zero']
        with args.csv_out.open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
            for p in result['packages']:
                for e in p['entries']:
                    gap=next(g for g in p['gaps'] if g['offset']==e['end'])
                    row={k:p[k] for k in fields[:7]}
                    row.update(entry_index=e['index'],entry_name=e['name'],entry_offset=e['offset'],entry_size=e['size'],entry_sha256=e['sha256'],prefix16_hex=e['prefix16_hex'],following_gap_size=gap['size'],following_gap_zero=gap['all_zero'])
                    w.writerow(row)
    for p in result['packages']:
        print(f"{p['input']}: {p['size']} bytes SHA256={p['sha256']} SLB2 v{p['version']} entries={p['entry_count']}")
        for e in p['entries']:print(f"  {e['name']}: [{e['offset']:#x}, {e['end']:#x}) size={e['size']} SHA256={e['sha256']}")
    for c in result['comparisons']:print(f"WINDOW {c['left']} vs {c['right']} [{c['offset']:#x},{c['end_exclusive']:#x}): {c['differing_bytes']} differing bytes")
    for e in result['errors']:print('ERROR: '+json.dumps(e),file=sys.stderr)
    return 2 if result['errors'] else 0

def main(argv=None):
    try: return run(argv)
    except (OSError, ValueError, struct.error) as e:
        print(f'ERROR: {e}', file=sys.stderr)
        return 2

if __name__=='__main__':sys.exit(main())
