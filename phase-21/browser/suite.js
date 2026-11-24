/* Original Phase 21 standards checks; no third-party diagnostic source reused. */
'use strict';
const LIMITS = Object.freeze({asyncTimeoutMs:3000,wasmMaximumPages:2,transferBytes:512,typedArrayBytes:16,maxLiveIframes:2,explicitBackingStoreBudgetBytes:262144});
const params = new URLSearchParams(location.search);
let latest=null,running=false;
function equal(actual,expected){if(actual!==expected)throw new Error(`expected ${JSON.stringify(expected)}, observed ${JSON.stringify(actual)}`);return {actual,expected};}
function exception(fn,name){try{fn();}catch(e){return equal(e.name,name);}throw new Error(`expected ${name}, no exception thrown`);}
async function runSuite(){
 if(running)return;running=true;document.querySelector('#run').disabled=true;
 const result={schemaVersion:1,date:new Date().toISOString(),userAgent:navigator.userAgent,platform:navigator.platform,url:location.href,isSecureContext:globalThis.isSecureContext,crossOriginIsolated:globalThis.crossOriginIsolated,limits:LIMITS,limitations:['One desktop browser/context per run; not a security or retail firmware test.','Explicit backing-store budget excludes engine/JIT/process overhead.','No allocation ceiling or memory pressure is measured.'],tests:[]};
 document.querySelector('#rows').replaceChildren();
 async function test(id,fn,available=true,skip=false){let r={id,status:'UNSUPPORTED',observed:{reason:'Required API unavailable'}};
  if(skip){r={id,status:'SKIP',observed:await fn()};}
  else if(available){let timeout;try{r={id,status:'PASS',observed:await Promise.race([Promise.resolve().then(fn),new Promise((_,reject)=>{timeout=setTimeout(()=>reject(new Error('check timed out')),LIMITS.asyncTimeoutMs);})])};}catch(e){r={id,status:'FAIL',observed:{name:e.name,message:e.message}};}finally{clearTimeout(timeout);}}
  result.tests.push(r);const tr=document.createElement('tr');for(const v of [id,r.status,JSON.stringify(r.observed)]){const td=document.createElement('td');td.textContent=v;tr.append(td);}tr.className=r.status;document.querySelector('#rows').append(tr);return r;
 }
 const features=Object.fromEntries(['Atomics','SharedArrayBuffer','MessageChannel','WebAssembly','structuredClone'].map(k=>[k,typeof globalThis[k] !== 'undefined']));
 await test('feature-availability',()=>features);
 await test('secure-context',()=>{if(['127.0.0.1','localhost','[::1]'].includes(location.hostname))return equal(isSecureContext,true);return {observed:isSecureContext,expectation:'Recorded; no trustworthiness assumption for arbitrary origin'};});
 if(params.has('expectedIsolation'))await test('cross-origin-isolation',()=>equal(crossOriginIsolated,params.get('expectedIsolation')==='true'));
 else await test('cross-origin-isolation',()=>({value:crossOriginIsolated,reason:'No response-header expectation supplied'}),true,true);
 const ops=[['load',a=>Atomics.load(a,0),8,8],['store',a=>Atomics.store(a,0,5),5,5],['add',a=>Atomics.add(a,0,3),8,11],['sub',a=>Atomics.sub(a,0,3),8,5],['and',a=>Atomics.and(a,0,3),8,0],['or',a=>Atomics.or(a,0,3),8,11],['xor',a=>Atomics.xor(a,0,3),8,11],['exchange',a=>Atomics.exchange(a,0,4),8,4],['compareExchange',a=>Atomics.compareExchange(a,0,8,6),8,6]];
 for(const [name,fn,returned,stored] of ops)await test(`atomics-normal-${name}`,()=>{const a=new Int32Array(1);a[0]=8;equal(fn(a),returned);equal(a[0],stored);return {returned,stored,shared:false};},features.Atomics);
 await test('atomics-float-TypeError',()=>exception(()=>Atomics.add(new Float32Array(1),0,1),'TypeError'),features.Atomics);
 await test('atomics-bounds-RangeError',()=>exception(()=>Atomics.load(new Int32Array(1),1),'RangeError'),features.Atomics);
 await test('atomics-wait-nonshared-TypeError',()=>exception(()=>Atomics.wait(new Int32Array(1),0,0,0),'TypeError'),features.Atomics&&typeof Atomics.wait==='function');
 await test('atomics-notify-nonshared-zero',()=>equal(Atomics.notify(new Int32Array(1),0),0),features.Atomics&&typeof Atomics.notify==='function');
 await test('typedarray-overlap',()=>{const b=new ArrayBuffer(16);const u=new Uint8Array(b);const d=new DataView(b);u.set([0x11,0x22,0x33,0x44]);equal(d.getUint32(0,true),0x44332211);return {littleEndianValue:d.getUint32(0,true),bytes:16};});
 await test('arraybuffer-transfer',()=>new Promise((resolve,reject)=>{const channel=new MessageChannel();const b=new ArrayBuffer(LIMITS.transferBytes);new Uint8Array(b)[0]=42;const timer=setTimeout(()=>{channel.port1.close();channel.port2.close();reject(new Error('transfer timed out'));},LIMITS.asyncTimeoutMs);channel.port2.onmessage=e=>{clearTimeout(timer);channel.port1.close();channel.port2.close();try{equal(b.byteLength,0);equal(e.data.byteLength,512);equal(new Uint8Array(e.data)[0],42);resolve({senderBytes:0,receiverBytes:512,firstByte:42});}catch(err){reject(err);}};channel.port1.postMessage(b,[b]);}),features.MessageChannel);
 async function frameCheck(sandboxed){
  const frame=document.createElement('iframe');if(sandboxed)frame.sandbox='allow-scripts';
  const token=crypto.getRandomValues(new Uint32Array(2)).join('-');
  // Echo only a unique string; no cross-origin document access is attempted.
  frame.srcdoc='<script>addEventListener("message",e=>{if(e.source===parent&&typeof e.data==="string")parent.postMessage(e.data,"*")})<\/script>';
  let listener,timer;
  try{return await new Promise((resolve,reject)=>{
   timer=setTimeout(()=>reject(new Error('iframe message timed out')),LIMITS.asyncTimeoutMs);
   listener=e=>{if(e.source!==frame.contentWindow||e.data!==token)return;try{equal(frame.contentDocument===null,sandboxed);equal(e.origin,sandboxed?'null':location.origin);resolve({sandboxed,contentDocumentNull:frame.contentDocument===null,messageOrigin:e.origin,echoAcknowledged:true});}catch(err){reject(err);}};
   addEventListener('message',listener);frame.onload=()=>frame.contentWindow.postMessage(token,'*');document.body.append(frame);
  });}finally{clearTimeout(timer);removeEventListener('message',listener);frame.remove();}
 }
 await test('iframe-same-origin-and-postMessage',()=>frameCheck(false));
 await test('iframe-opaque-origin-and-postMessage',()=>frameCheck(true));
 await test('wasm-empty-module-and-bounded-growth',async()=>{const bytes=new Uint8Array([0,97,115,109,1,0,0,0]);const m=await WebAssembly.compile(bytes);await WebAssembly.instantiate(m);const memory=new WebAssembly.Memory({initial:1,maximum:2});const old=memory.buffer;equal(memory.grow(1),1);equal(memory.buffer.byteLength,131072);equal(old.byteLength,0);return {moduleBytes:8,initialPages:1,finalPages:2,maximumPages:2,oldBufferDetached:true};},features.WebAssembly);
 result.summary=Object.fromEntries(['PASS','FAIL','SKIP','UNSUPPORTED'].map(s=>[s,result.tests.filter(t=>t.status===s).length]));
 latest=result;globalThis.phase21Result=result;document.querySelector('#context').textContent=JSON.stringify({userAgent:result.userAgent,isSecureContext:result.isSecureContext,crossOriginIsolated:result.crossOriginIsolated,summary:result.summary},null,2);document.querySelector('#state').textContent='Completed';document.querySelector('#export').disabled=false;document.querySelector('#run').disabled=false;running=false;
 if(params.get('submit')==='true'){await fetch('/results/'+encodeURIComponent(params.get('run')),{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(result)});}
 return result;
}
document.querySelector('#run').onclick=runSuite;
document.querySelector('#export').onclick=()=>{const url=URL.createObjectURL(new Blob([JSON.stringify(latest,null,2)],{type:'application/json'}));const a=document.createElement('a');a.href=url;a.download='browser-standards-results.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);};
if(params.get('autorun')==='true')runSuite().catch(e=>{document.querySelector('#state').textContent=e.stack;globalThis.phase21Fatal=String(e);});
