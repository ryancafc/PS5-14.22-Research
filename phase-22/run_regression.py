#!/usr/bin/env python3
"""Reproduce preflight tests and actual Ghidra parser probes in a NEW work directory.
Never executes target code. Nonzero exit also records known raw-parser validation gaps.
"""
from pathlib import Path
import argparse,json,os,subprocess,sys
import fixtures
def compare(manifest,records):
 byname={r['file']:r for r in records};rows=[]
 for case in manifest:
  r=byname[case['file']]
  if case['expected']=='reject':passed=not r['accepted'] and r.get('checkedFailure',False)
  else:passed=r['accepted'] and bool(r.get('eligibleSpecs',0))==case['expected_eligible']
  rows.append({'case':case['name'],'synthetic':True,'expected':case['expected'],'status':'PASS' if passed else 'FAIL','accepted':r['accepted'],'checked_failure':r.get('checkedFailure'), 'eligible_specs':r.get('eligibleSpecs'),'elapsed_ms':r['elapsedMs'],'explanation':r.get('exception','Metadata accepted; relocation application is tested separately')})
 return {'cases':len(rows),'passed':sum(r['status']=='PASS' for r in rows),'failed':sum(r['status']=='FAIL' for r in rows),'rows':rows,'scope':'Strict metadata-rejection expectations, not genuine compatibility or a security assessment.'}
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--ghidra',type=Path,required=True);ap.add_argument('--work',type=Path,required=True);ap.add_argument('--config',type=Path);a=ap.parse_args()
 if a.work.exists():ap.error('--work must be a new directory to preserve previous results')
 root=Path(__file__).resolve().parent;work=a.work.resolve();work.mkdir();(work/'projects').mkdir()
 manifest=fixtures.generate(work/'fixtures')
 with (work/'unit-tests.log').open('w') as log:
  r=subprocess.run([sys.executable,str(root/'test_elf_preflight.py'),str(work/'preflight-results.json')],stdout=log,stderr=subprocess.STDOUT)
  if r.returncode:return r.returncode
 env=os.environ.copy()
 if a.config:env['XDG_CONFIG_HOME']=str(a.config.resolve())
 cmd=[str(a.ghidra.resolve()/'support/analyzeHeadless'),str(work/'projects'),'ParserRegression','-import',str(work/'fixtures/ordinary-etdyn.elf'),'-noanalysis','-scriptPath',str(root),'-postScript','ParserProbes.java',str(work/'fixtures'),str(work/'raw-parser.json'),'-log',str(work/'headless.log')]
 with (work/'console.log').open('w') as log:r=subprocess.run(cmd,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=180)
 if r.returncode:return r.returncode
 report=compare(manifest,json.loads((work/'raw-parser.json').read_text()));(work/'raw-validation-results.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:v for k,v in report.items() if k!='rows'},indent=2))
 return 1 if report['failed'] else 0
if __name__=='__main__':sys.exit(main())
