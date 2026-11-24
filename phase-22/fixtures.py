"""Original tiny synthetic ELF parser fixtures, never genuine compatibility evidence.
No acquired executable is modified. All bytes are generated from scratch.
"""
from pathlib import Path
import struct,json,hashlib
BASE=0x400000
SCE={'hash':0x61000025,'rela':0x6100002f,'relasz':0x61000031,'relaent':0x61000033,'strtab':0x61000035,'strsz':0x61000037,'symtab':0x61000039,'syment':0x6100003b,'symtabsz':0x6100003f}
STD={'hash':4,'rela':7,'relasz':8,'relaent':9,'strtab':5,'strsz':10,'symtab':6,'syment':11}
def make(*,abi=2,etype=0xfe10,sce=False,rel=False):
 d=bytearray(2048);ident=b'\x7fELF'+bytes([2,1,1,9,abi])+b'\0'*7
 struct.pack_into('<16sHHIQQQIHHHHHH',d,0,ident,etype,62,1,BASE+0x300,64,0,0,64,56,3 if sce else 2,0,0,0)
 struct.pack_into('<IIQQQQQQ',d,64,1,7,0,BASE,BASE,len(d),len(d),0x1000)
 tags=SCE if sce else STD;ptr=lambda o:o-0x300 if sce else BASE+o
 strings=b'\0libtest.prx\0symbol\0';symbol_name=strings.index(b'symbol')
 dynamic=[(tags['hash'],ptr(0x380)),(tags['strtab'],ptr(0x500)),(tags['strsz'],len(strings)),(tags['symtab'],ptr(0x400)),(tags['syment'],24),(1,1)]
 if sce:dynamic.append((tags['symtabsz'],48))
 if rel:dynamic += [(17,ptr(0x600)),(18,16),(19,16)]
 else:dynamic += [(tags['rela'],ptr(0x600)),(tags['relasz'],24),(tags['relaent'],24)]
 dynamic += [(0,0)]
 struct.pack_into('<IIQQQQQQ',d,120,2,6,0x200,BASE+0x200,BASE+0x200,len(dynamic)*16,len(dynamic)*16,8)
 if sce:struct.pack_into('<IIQQQQQQ',d,176,0x61000000,0,0x300,0,0,0x500,0x500,8)
 for i,(tag,value) in enumerate(dynamic):struct.pack_into('<qQ',d,0x200+i*16,tag,value)
 struct.pack_into('<5I',d,0x380,1,2,1,0,0)
 struct.pack_into('<IBBHQQ',d,0x418,symbol_name,0x12,0,0,0,0)
 d[0x500:0x500+len(strings)]=strings;d[0x300]=0xc3
 struct.pack_into('<QQ',d,0x600,BASE+0x700,(1<<32)|6)
 if not rel:struct.pack_into('<q',d,0x610,0)
 return d
def change_tag(d,tag,newtag=None,value=None):
 for pos in range(0x200,0x300,16):
  t,v=struct.unpack_from('<qQ',d,pos)
  if t==tag:
   struct.pack_into('<qQ',d,pos,tag if newtag is None else newtag,v if value is None else value);return d
 raise ValueError('tag missing')
def cases():
 result=[]
 def add(name,data,expected,eligibility=None,note=''):
  result.append({'name':name,'data':bytes(data),'expected':expected,'expected_eligible':eligibility,'note':note})
 add('valid-standard',make(),'accept',True)
 add('valid-sce-relative',make(sce=True),'accept',True)
 add('valid-abi3-synthetic',make(abi=3),'accept',True,'Synthetic parser acceptance only; not genuine ABI3 compatibility')
 add('ordinary-etdyn',make(etype=3),'accept',False)
 add('unsupported-abi0',make(abi=0),'accept',False)
 add('unsupported-abi4',make(abi=4),'accept',False)
 add('unsupported-type',make(etype=4),'accept',False)
 add('valid-rel-format',make(rel=True),'accept',True)
 d=make();size=struct.unpack_from('<Q',d,152)[0];struct.pack_into('<Q',d,152,size+3);add('valid-dynamic-tail-padding',d,'accept',True,'DT_NULL precedes extra segment tail bytes')
 d=make();d[0:4]=b'BAD!';add('bad-magic',d,'reject')
 add('truncated-ident',b'\x7fELF\x02','reject')
 add('truncated-header',make()[:40],'reject')
 d=make();struct.pack_into('<Q',d,32,0x10000);add('phoff-outside',d,'reject')
 d=make();struct.pack_into('<Q',d,96,0x10000);add('segment-outside',d,'reject')
 d=make();struct.pack_into('<Q',d,128,0x10000);add('dynamic-outside',d,'reject')
 d=make();struct.pack_into('<Q',d,152,15);add('dynamic-unaligned-size',d,'reject')
 d=make();change_tag(d,0,0x60000001,0);add('dynamic-missing-null',d,'reject')
 d=make(sce=True);change_tag(d,SCE['strtab'],0x60000001);add('sce-missing-strtab',d,'reject')
 d=make(sce=True);change_tag(d,SCE['symtabsz'],0x60000001);add('sce-missing-symtabsz',d,'reject')
 d=make();change_tag(d,5,value=BASE+0x10000);add('string-pointer-outside',d,'reject')
 d=make();change_tag(d,10,value=0x10000);add('string-size-outside',d,'reject')
 d=make();struct.pack_into('<I',d,0x418,0xffff);add('symbol-name-outside',d,'reject')
 d=make();struct.pack_into('<Q',d,0x608,(99<<32)|6);add('relocation-symbol-outside',d,'reject')
 d=make();struct.pack_into('<Q',d,0x608,(1<<32)|0xdead);add('unsupported-relocation',d,'diagnose',True,'Parser may retain unknown type; import must not mark it APPLIED')
 d=make();change_tag(d,1,5,BASE+0x500);add('duplicate-singleton-strtab',d,'reject')
 d=make(sce=True);struct.pack_into('<H',d,56,4);struct.pack_into('<IIQQQQQQ',d,232,0x61000000,0,0x300,0,0,0x500,0x500,8);add('duplicate-sce-segment',d,'reject')
 return result
def generate(directory):
 directory=Path(directory);directory.mkdir(parents=True,exist_ok=True);manifest=[]
 for c in cases():
  p=directory/(c['name']+'.elf');p.write_bytes(c['data']);manifest.append({k:v for k,v in c.items() if k!='data'}|{'file':p.name,'sha256':hashlib.sha256(c['data']).hexdigest(),'size':len(c['data']),'synthetic':True})
 (directory/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');return manifest
if __name__=='__main__':
 import sys
 print('Generated',len(generate(sys.argv[1] if len(sys.argv)>1 else 'fixtures')),'synthetic parser cases')
