"""Run the original suite in fresh native Chromium and Firefox profiles."""
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path
import threading, tempfile, subprocess, secrets, json, time, urllib.parse, shutil
import argparse
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--suite',type=Path,default=Path(__file__).resolve().parent/'browser')
ap.add_argument('--output',type=Path,default=Path('browser-test-output'))
a=ap.parse_args();base=a.output;suite=a.suite;received={};events={}
(base/'logs').mkdir(parents=True,exist_ok=True);(base/'evidence').mkdir(parents=True,exist_ok=True)
class Handler(BaseHTTPRequestHandler):
    def log_message(self,*args):pass
    def do_GET(self):
        path=urllib.parse.urlparse(self.path).path
        name=path.rsplit('/',1)[-1]
        if name not in {'index.html','suite.js'} or not path.startswith(('/plain/','/isolated/')):
            self.send_error(404);return
        data=(suite/name).read_bytes();self.send_response(200)
        self.send_header('Content-Type','text/html; charset=utf-8' if name.endswith('html') else 'text/javascript; charset=utf-8')
        self.send_header('Cache-Control','no-store')
        if path.startswith('/isolated/'):
            self.send_header('Cross-Origin-Opener-Policy','same-origin')
            self.send_header('Cross-Origin-Embedder-Policy','require-corp')
        self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)
    def do_POST(self):
        token=self.path.removeprefix('/results/')
        n=int(self.headers.get('Content-Length','0'))
        if not self.path.startswith('/results/') or token not in events or not 0<n<200000:
            self.send_error(400);return
        try:received[token]=json.loads(self.rfile.read(n))
        except ValueError:self.send_error(400);return
        self.send_response(204);self.end_headers();events[token].set()
server=ThreadingHTTPServer(('127.0.0.1',0),Handler);threading.Thread(target=server.serve_forever,daemon=True).start()
records=[]
try:
 for engine,binary in [('Chromium','/usr/bin/chromium'),('Firefox','/usr/bin/firefox-esr')]:
  version=subprocess.check_output([binary,'--version'],text=True,stderr=subprocess.STDOUT).strip()
  for isolated,control in [(False,'normal'),(True,'normal')]+([(False,'wrong-header-expectation'),(False,'no-header-expectation')] if engine=='Chromium' else []):
   token=secrets.token_hex(16);events[token]=threading.Event();mode=('isolated' if isolated else 'plain')+('' if control=='normal' else '-'+control)
   served_mode='isolated' if isolated else 'plain'
   expected='true' if control=='wrong-header-expectation' else str(isolated).lower()
   expectation='' if control=='no-header-expectation' else '&expectedIsolation='+expected
   url=f'http://127.0.0.1:{server.server_port}/{served_mode}/index.html?autorun=true&submit=true&run={token}'+expectation
   with tempfile.TemporaryDirectory(prefix='phase21-'+engine.lower()+'-') as profile:
    logpath=base/'logs'/f'browser-{engine.lower()}-{mode}.log'
    args=[binary,'--headless','--no-remote','--profile',profile,url] if engine=='Firefox' else [binary,'--headless','--no-first-run','--disable-background-networking','--disable-default-apps','--user-data-dir='+profile,url]
    with logpath.open('w') as log:
     process=subprocess.Popen(args,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
     try:
      success=events[token].wait(55)
      record={'engine':engine,'version':version,'mode':mode,'control':control,'sandbox_disabled':False,'fresh_profile':True,'received_result':success}
      if success:
       result=received[token];record['result']=result
       (base/'evidence'/f'browser-{engine.lower()}-{mode}.json').write_text(json.dumps(record,indent=2)+'\n')
       print(engine,mode,result['summary'],flush=True)
      else:record['error']='No result before 55-second deadline';print(engine,mode,record['error'],flush=True)
      records.append(record)
     finally:
      import os,signal
      try:os.killpg(process.pid,signal.SIGTERM);process.wait(timeout=8)
      except (ProcessLookupError,subprocess.TimeoutExpired):
       try:os.killpg(process.pid,signal.SIGKILL)
       except ProcessLookupError:pass
       process.wait(timeout=8)
finally:
 server.shutdown();server.server_close()
 (base/'evidence/cross-browser-results.json').write_text(json.dumps(records,indent=2)+'\n')
