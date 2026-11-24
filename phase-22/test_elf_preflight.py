"""Synthetic metadata robustness tests; never run fixture machine code."""
import hashlib,json,subprocess,sys,tempfile,time,unittest
from pathlib import Path
import elf_preflight as parser
import fixtures

class PreflightTests(unittest.TestCase):
 def test_file_preserved(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/'input.elf';p.write_bytes(fixtures.make());s=p.stat();digest=hashlib.sha256(p.read_bytes()).hexdigest()
   r=parser.inspect(p)
   self.assertTrue(r['input_stat_preserved']);self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),digest);self.assertEqual(p.stat().st_mtime_ns,s.st_mtime_ns)
 def test_oversize_file_refused(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/'sparse.elf'
   with p.open('wb') as f:f.truncate(parser.MAX_BYTES+1)
   with self.assertRaisesRegex(parser.InvalidELF,'64 MiB'):parser.inspect(p)
 def test_cli_missing_file(self):
  r=subprocess.run([sys.executable,str(Path(parser.__file__)),'/nonexistent/phase22-missing.elf'],text=True,capture_output=True)
  self.assertEqual(r.returncode,2);self.assertIn('ERROR:',r.stderr);self.assertNotIn('Traceback',r.stderr)
 def test_known_rel_and_rela_metadata(self):
  for rel in [False,True]:
   r=parser.parse(fixtures.make(rel=rel))
   self.assertEqual(r['libraries'],['libtest.prx']);self.assertEqual(r['dynamic_symbol_count'],2)
   self.assertEqual(r['relocation_count'],1);self.assertEqual(r['relocation_formats'],{'REL' if rel else 'RELA':1});self.assertEqual(r['relocation_types'],{'6':1})

def make_test(case):
 def test(self):
  if case['expected']=='reject':
   with self.assertRaises(parser.InvalidELF):parser.parse(case['data'])
  else:
   r=parser.parse(case['data'])
   self.assertEqual(r['expected_prospero_eligible'],case['expected_eligible'])
   self.assertEqual(r['status'],'UNSUPPORTED' if case['expected']=='diagnose' else 'PASS')
 return test
for case in fixtures.cases():setattr(PreflightTests,'test_fixture_'+case['name'].replace('-','_'),make_test(case))

class RecordingResult(unittest.TextTestResult):
 def startTest(self,test):super().startTest(test);self.started=time.perf_counter()
 def addSuccess(self,test):super().addSuccess(test);self.records.append({'test':test.id(),'status':'PASS','elapsed_ms':(time.perf_counter()-self.started)*1000})
 def addFailure(self,test,err):super().addFailure(test,err);self.records.append({'test':test.id(),'status':'FAIL','elapsed_ms':(time.perf_counter()-self.started)*1000,'error':self._exc_info_to_string(err,test)})
 def addError(self,test,err):super().addError(test,err);self.records.append({'test':test.id(),'status':'ERROR','elapsed_ms':(time.perf_counter()-self.started)*1000,'error':self._exc_info_to_string(err,test)})
 def __init__(self,*a,**kw):super().__init__(*a,**kw);self.records=[]
if __name__=='__main__':
 output=Path(sys.argv[1]) if len(sys.argv)>1 else Path('preflight-results.json')
 result=unittest.TextTestRunner(verbosity=2,resultclass=RecordingResult).run(unittest.defaultTestLoader.loadTestsFromTestCase(PreflightTests))
 output.write_text(json.dumps({'tests':result.testsRun,'passed':len(result.records)-len(result.failures)-len(result.errors),'failures':len(result.failures),'errors':len(result.errors),'records':result.records},indent=2)+'\n')
 sys.exit(0 if result.wasSuccessful() else 1)
