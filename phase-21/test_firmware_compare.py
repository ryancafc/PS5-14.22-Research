"""Independent synthetic SLB2 fixtures; no Sony bytes or executable payloads."""
import contextlib, hashlib, io, json, os, struct, tempfile, unittest
from pathlib import Path
import firmware_compare as fc

def fixture(entries=((1,17,'one'),), total=1536):
    d=bytearray(total)
    struct.pack_into('<4s4I',d,0,b'SLB2',3,0x10000,len(entries),total//512)
    for i,(sector,size,name) in enumerate(entries):
        struct.pack_into('<II8x32s',d,32+i*48,sector,size,name.encode())
        start=sector*512
        if start+size<=len(d):d[start:start+size]=bytes((j%251)+1 for j in range(size))
    return d

class ContainerTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
    def tearDown(self):self.tmp.cleanup()
    def write(self,d,name='a.pup'):
        p=self.root/name;p.write_bytes(d);return p
    def reject(self,d,word):
        with self.assertRaisesRegex(fc.FormatError,word):fc.inspect(self.write(d))
    def test_valid_identity_boundaries_and_preservation(self):
        data=fixture();p=self.write(data);before=p.stat();r=fc.inspect(p)
        self.assertEqual(r['sha256'],hashlib.sha256(data).hexdigest())
        self.assertEqual((r['entries'][0]['offset'],r['entries'][0]['size']),(512,17))
        self.assertEqual(r['gaps'][0]['size'],1007)
        self.assertTrue(r['gaps'][0]['all_zero'])
        self.assertEqual((p.read_bytes(),p.stat().st_mtime_ns),(data,before.st_mtime_ns))
    def test_magic(self):self.reject(b'XXXX'+fixture()[4:],'not an SLB2')
    def test_short_header(self):self.reject(b'SLB2','truncated range')
    def test_version(self):
        d=fixture();struct.pack_into('<I',d,4,9);self.reject(d,'unsupported')
    def test_zero_count(self):
        d=fixture();struct.pack_into('<I',d,12,0);self.reject(d,'entry count')
    def test_huge_count(self):
        d=fixture();struct.pack_into('<I',d,12,0xffffffff);self.reject(d,'entry count')
    def test_truncated_table(self):
        d=fixture();struct.pack_into('<I',d,12,40);self.reject(d,'truncated entry table')
    def test_truncated_file(self):self.reject(fixture()[:-1],'block count')
    def test_wrong_blocks(self):
        d=fixture();struct.pack_into('<I',d,16,1);self.reject(d,'block count')
    def test_header_overlap(self):
        d=fixture();struct.pack_into('<I',d,32,0);self.reject(d,'overlaps header')
    def test_outside_offset(self):
        d=fixture();struct.pack_into('<I',d,32,0xffffffff);self.reject(d,'bounds')
    def test_oversized_entry(self):
        d=fixture();struct.pack_into('<I',d,36,0xffffffff);self.reject(d,'bounds')
    def test_zero_size(self):
        d=fixture();struct.pack_into('<I',d,36,0);self.reject(d,'zero size')
    def test_overlapping_entries(self):self.reject(fixture(((1,40,'a'),(1,20,'b'))),'overlapping entry')
    def test_unterminated_name(self):
        d=fixture();d[48:80]=b'A'*32;self.reject(d,'unterminated')
    def test_non_ascii_name(self):
        d=fixture();d[48]=255;self.reject(d,'non-ASCII')
    def test_empty_name(self):
        d=fixture();d[48:80]=b'\0'*32;self.reject(d,'empty name')
    def test_multi_entry_gaps(self):
        r=fc.inspect(self.write(fixture(((1,17,'a'),(2,19,'b')))))
        self.assertEqual([g['size'] for g in r['gaps']],[495,493])
    def test_nonzero_padding_is_measured(self):
        d=fixture();d[-1]=7;r=fc.inspect(self.write(d));self.assertFalse(r['gaps'][-1]['all_zero'])
    def test_exact_window_diff(self):
        d=fixture();a=self.write(d);d[1023]=9;d[1024]=11;b=self.write(d,'b.pup')
        r=fc.compare_window(a,b,1000,24)
        self.assertEqual((r['differing_bytes'],r['first_differing_offsets']),(1,[1023]))
    def test_window_bounds(self):
        p=self.write(fixture())
        with self.assertRaises(fc.FormatError):fc.compare_window(p,p,1500,40)
    def test_window_limits(self):
        for s in ['-1:1','0:0','0:0x1000001','wrong']:
            with self.assertRaises(Exception):fc.window_arg(s)
    def test_json_csv_and_partial_failure(self):
        a=self.write(fixture());bad=self.write(b'bad','bad.pup');j=self.root/'out.json';c=self.root/'out.csv'
        with contextlib.redirect_stdout(io.StringIO()),contextlib.redirect_stderr(io.StringIO()):
            rc=fc.main([str(a),str(bad),'--json',str(j),'--csv',str(c)])
        self.assertEqual(rc,2);r=json.loads(j.read_text());self.assertEqual(len(r['packages']),1);self.assertEqual(len(r['errors']),1)
        self.assertIn('entry_sha256',c.read_text())
    def test_output_aliases_refused(self):
        p=self.write(fixture());link=self.root/'hardlink';os.link(p,link);symlink=self.root/'symlink';symlink.symlink_to(p)
        for out in [p,link,symlink]:
            with contextlib.redirect_stderr(io.StringIO()),self.assertRaises(SystemExit) as cm:fc.main([str(p),'--json',str(out)])
            self.assertEqual(cm.exception.code,2)
        self.assertEqual(p.read_bytes(),fixture())
    def test_outputs_must_be_distinct(self):
        p=self.write(fixture());out=self.root/'out'
        with contextlib.redirect_stderr(io.StringIO()),self.assertRaises(SystemExit):fc.main([str(p),'--json',str(out),'--csv',str(out)])
    def test_missing_output_directory_has_clear_error(self):
        p=self.write(fixture());err=io.StringIO()
        with contextlib.redirect_stderr(err):rc=fc.main([str(p),'--json',str(self.root/'absent/out.json')])
        self.assertEqual(rc,2);self.assertIn('ERROR:',err.getvalue())
    def test_overlap_rejected_before_streaming(self):
        from unittest.mock import patch
        p=self.write(fixture(((1,40,'a'),(1,20,'b'))))
        with patch.object(fc,'scan_range',side_effect=AssertionError('must not stream invalid extents')):
            with self.assertRaisesRegex(fc.FormatError,'overlapping'):fc.inspect(p)

if __name__=='__main__':unittest.main()
