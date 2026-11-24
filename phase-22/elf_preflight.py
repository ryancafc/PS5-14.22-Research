#!/usr/bin/env python3
"""Bounded read-only ELF64 little-endian metadata preflight, not a runtime loader.
Rejects malformed ranges before handing files to Ghidra. Never applies relocations.
SCE tag numbers/relative addressing follow the pinned public GhidraProspero source.
"""
from pathlib import Path
import argparse,collections,hashlib,json,struct,sys
MAX_BYTES=64*1024*1024
SCE={'hash':0x61000025,'jmprel':0x61000029,'pltrel':0x6100002b,'pltrelsz':0x6100002d,'rela':0x6100002f,'relasz':0x61000031,'relaent':0x61000033,'strtab':0x61000035,'strsz':0x61000037,'symtab':0x61000039,'syment':0x6100003b,'symtabsz':0x6100003f}
STD={'hash':4,'jmprel':23,'pltrel':20,'pltrelsz':2,'rela':7,'relasz':8,'relaent':9,'strtab':5,'strsz':10,'symtab':6,'syment':11,'rel':17,'relsz':18,'relent':19}
KNOWN_RELOCATIONS={0,1,2,4,6,7,8,9,10,11,16,17,18,24,37,41,42}
class InvalidELF(ValueError):pass
def parse(data):
 n=len(data)
 def bounds(offset,size,label):
  if offset<0 or size<0 or offset>n or size>n-offset:raise InvalidELF(label+' outside file bounds')
 def unpack(fmt,offset,label):
  bounds(offset,struct.calcsize(fmt),label);return struct.unpack_from(fmt,data,offset)
 bounds(0,64,'ELF header')
 if data[:4]!=b'\x7fELF':raise InvalidELF('bad ELF magic')
 if data[4:7]!=bytes([2,1,1]):raise InvalidELF('only ELF64 little-endian version 1 supported')
 typ,machine,ver,entry,phoff,shoff,flags,ehsize,phentsize,phnum,shentsize,shnum,shstr=unpack('<HHIQQQIHHHHHH',16,'ELF header')
 if ver!=1 or ehsize!=64:raise InvalidELF('invalid ELF header version/size')
 if machine!=62:raise InvalidELF('only x86-64 metadata supported')
 if phnum>4096 or shnum>4096:raise InvalidELF('table count exceeds bounded policy')
 if phnum and phentsize!=56:raise InvalidELF('invalid program header entry size')
 if shnum and shentsize!=64:raise InvalidELF('invalid section header entry size')
 bounds(phoff,phnum*phentsize,'program header table');bounds(shoff,shnum*shentsize,'section header table')
 segments=[]
 for i in range(phnum):
  t,f,o,v,p,fs,ms,a=unpack('<IIQQQQQQ',phoff+i*56,'program header')
  bounds(o,fs,'segment')
  if t==1 and fs>ms:raise InvalidELF('PT_LOAD file size exceeds memory size')
  if a not in (0,1) and a&(a-1):raise InvalidELF('segment alignment is not a power of two')
  segments.append(dict(type=t,flags=f,offset=o,vaddr=v,filesz=fs,memsz=ms,align=a))
 sections=[]
 for i in range(shnum):
  name,t,f,a,o,s,link,info,align,ent=unpack('<IIQQQQIIQQ',shoff+i*64,'section header')
  if t!=8:bounds(o,s,'section')
  sections.append(dict(index=i,name_index=name,type=t,flags=f,address=a,offset=o,size=s,link=link,info=info,align=align,entry_size=ent))
 ds=[p for p in segments if p['type']==2];sce_segments=[p for p in segments if p['type']==0x61000000]
 if len(ds)>1:raise InvalidELF('duplicate PT_DYNAMIC')
 if len(sce_segments)>1:raise InvalidELF('duplicate PT_SCE_DYNLIBDATA')
 load=[p for p in segments if p['type']==1]
 def locate(value,length,sce=False):
  if sce and sce_segments:
   p=sce_segments[0]
   if value>p['filesz'] or length>p['filesz']-value:raise InvalidELF('SCE relative table outside segment')
   result=p['offset']+value;bounds(result,length,'SCE dynamic table');return result
  matches=[p['offset']+value-p['vaddr'] for p in load if p['vaddr']<=value and value-p['vaddr']<=p['filesz'] and length<=p['filesz']-(value-p['vaddr'])]
  if len(set(matches))!=1:raise InvalidELF('dynamic virtual range not uniquely file-backed')
  result=matches[0];bounds(result,length,'dynamic table');return result
 dynamic=[];tags={};warnings=[]
 if ds:
  p=ds[0]
  terminated=False
  for off in range(p['offset'],p['offset']+p['filesz']-15,16):
   tag,value=unpack('<qQ',off,'dynamic entry');dynamic.append({'tag':tag,'value':value})
   if tag==0:terminated=True;break
   if tag in tags and tag in set(STD.values())|set(SCE.values()):raise InvalidELF('duplicate singleton dynamic tag')
   tags.setdefault(tag,[]).append(value)
  if not terminated:raise InvalidELF('missing DT_NULL inside PT_DYNAMIC extent')
 def get(name):
  if name in SCE and SCE[name] in tags:return tags[SCE[name]][0],True
  if name in STD and STD[name] in tags:return tags[STD[name]][0],False
  return None,False
 def string_at(raw,index):
  if index>=len(raw):raise InvalidELF('string index outside table')
  end=raw.find(b'\0',index)
  if end<0:raise InvalidELF('unterminated string')
  return raw[index:end].decode('utf8',errors='replace')
 strings=None;str_ptr,str_sce=get('strtab');str_sz,_=get('strsz')
 if (str_ptr is None)!=(str_sz is None):raise InvalidELF('incomplete dynamic string table metadata')
 if str_ptr is not None:
  offset=locate(str_ptr,str_sz,str_sce);strings=data[offset:offset+str_sz]
 needed=[]
 for value in tags.get(1,[]):
  if strings is None:raise InvalidELF('DT_NEEDED without string table')
  needed.append(string_at(strings,value))
 sym_ptr,sym_sce=get('symtab');sym_ent,_=get('syment');sym_sz,_=get('symtabsz');symbols=[]
 if sym_ptr is not None:
  if strings is None:raise InvalidELF('symbol table without strings')
  if sym_ent!=24:raise InvalidELF('invalid or missing symbol entry size')
  if sym_sce and sym_sz is None:raise InvalidELF('missing SCE_SYMTABSZ')
  if sym_sz is None:
   dynsym=[s for s in sections if s['type']==11]
   if dynsym:sym_sz=dynsym[0]['size']
   else:
    hval,hsce=get('hash')
    if hval is None:raise InvalidELF('cannot bound dynamic symbol count without section/hash')
    h=locate(hval,8,hsce);nbucket,nchain=unpack('<II',h,'hash header');locate(hval,4*(2+nbucket+nchain),hsce);sym_sz=nchain*24
  if sym_sz%24:raise InvalidELF('unaligned symbol table size')
  offset=locate(sym_ptr,sym_sz,sym_sce)
  for off in range(offset,offset+sym_sz,24):
   name,info,other,section,value,size=unpack('<IBBHQQ',off,'symbol')
   symbols.append({'name':string_at(strings,name),'binding':info>>4,'type':info&15,'section':section,'value':value,'size':size})
 relocs=[];seen=set()
 def rel_table(ptr,size,entsize,sce,rela,label):
  expected=24 if rela else 16
  if ptr is None or size is None or entsize!=expected or size%expected:raise InvalidELF('incomplete/malformed '+label+' metadata')
  offset=locate(ptr,size,sce)
  if (offset,size) in seen:return
  seen.add((offset,size))
  for off in range(offset,offset+size,expected):
   target,info=unpack('<QQ',off,'relocation');symbol=info>>32;kind=info&0xffffffff
   if symbol>=len(symbols) and symbol!=0:raise InvalidELF('relocation symbol index outside table')
   if kind and not any(p['vaddr']<=target and target-p['vaddr']<p['memsz'] for p in load):raise InvalidELF('relocation target outside PT_LOAD memory')
   if kind not in KNOWN_RELOCATIONS:warnings.append('unrecognized relocation type '+str(kind))
   relocs.append({'format':'RELA' if rela else 'REL','type':kind,'symbol':symbol,'offset':target})
 for label,rela in [('rela',True),('rel',False)]:
  ptr,sce=get(label);size,_=get(label+'sz');entsize,_=get(label+'ent')
  if ptr is not None or size is not None:rel_table(ptr,size,entsize,sce,rela,label)
 ptr,sce=get('jmprel');size,_=get('pltrelsz');form,_=get('pltrel')
 if ptr is not None or size is not None:
  if form not in (7,17):raise InvalidELF('unsupported DT_PLTREL record format')
  rel_table(ptr,size,24 if form==7 else 16,sce,form==7,'PLT')
 eligible=machine==62 and data[8] in (2,3) and (typ in {0xfe00,0xfe01,0xfe04,0xfe0c,0xfe10,0xfe18} or (typ==2 and load and min(p['vaddr'] for p in load)>=2**63))
 return {'size':n,'sha256':hashlib.sha256(data).hexdigest(),'architecture':'x86-64','osabi':data[7],'abi':data[8],'elf_type':typ,'entry':entry,'program_headers':segments,'section_headers':sections,'dynamic_entries':dynamic,'dynamic_layout':'SCE relative segment' if sce_segments else 'ordinary PT_LOAD VA' if ds else 'none','libraries':needed,'dynamic_symbol_count':len(symbols),'relocation_count':len(relocs),'relocation_formats':dict(collections.Counter(r['format'] for r in relocs)),'relocation_types':dict(collections.Counter(str(r['type']) for r in relocs)),'expected_prospero_eligible':bool(eligible),'warnings':warnings,'status':'UNSUPPORTED' if warnings else 'PASS','scope':'Bounded metadata preflight only; does not apply relocations, validate runtime behavior or decode protected firmware.'}
def inspect(path):
 p=Path(path);before=p.stat()
 if before.st_size>MAX_BYTES:raise InvalidELF('file exceeds 64 MiB preflight policy')
 with p.open('rb') as f:data=f.read(MAX_BYTES+1)
 if len(data)>MAX_BYTES:raise InvalidELF('file exceeds 64 MiB preflight policy')
 result=parse(data);after=p.stat()
 if (before.st_size,before.st_mtime_ns)!=(after.st_size,after.st_mtime_ns):raise InvalidELF('input changed during inspection')
 result['input_stat_preserved']=True;return result
if __name__=='__main__':
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('input',type=Path);args=ap.parse_args()
 try:print(json.dumps(inspect(args.input),indent=2))
 except (OSError,InvalidELF) as e:print('ERROR: '+str(e),file=sys.stderr);sys.exit(2)
