// Static regression metrics only; never executes a guest executable.
// @category PS5.Research
import ghidra.app.script.GhidraScript;
import ghidra.app.util.opinion.*;
import ghidra.app.util.bin.FileByteProvider;
import ghidra.app.decompiler.*;
import ghidra.program.model.listing.*;
import com.google.gson.GsonBuilder;
import java.nio.file.*;
import java.util.*;
import java.io.*;
public class RegressionExport extends GhidraScript {
 public void run() throws Exception {
  String[] args=getScriptArgs();Path out=Paths.get(args[0]);Files.createDirectories(out);
  Map<String,Object> r=new LinkedHashMap<>();
  r.put("name",currentProgram.getName());r.put("format",currentProgram.getExecutableFormat());
  r.put("language",currentProgram.getLanguageID().toString());
  r.put("prosperoMarker",currentProgram.getUsrPropertyManager().getVoidPropertyMap("prospero")!=null);
  List<Object> probes=new ArrayList<>();
  for(Loader l:LoaderService.getAllLoaders())if(l.getName().equals("Prospero ELF")) {
   r.put("prosperoLoaderClass",l.getClass().getName());
   for(int i=1;i<args.length;i++)try(FileByteProvider bp=new FileByteProvider(new File(args[i]),null,java.nio.file.AccessMode.READ)){
    Map<String,Object> p=new LinkedHashMap<>();p.put("file",new File(args[i]).getName());p.put("specs",l.findSupportedLoadSpecs(bp).size());probes.add(p);
   }
  }
  r.put("eligibilityProbes",probes);
  int imports=0;var syms=currentProgram.getSymbolTable().getAllSymbols(true);
  while(syms.hasNext())if(syms.next().isExternal())imports++;
  r.put("externalSymbolRecords",imports);
  r.put("libraries",currentProgram.getExternalManager().getExternalLibraryNames());
  r.put("functionRecords",currentProgram.getFunctionManager().getFunctionCount());
  List<Object> blocks=new ArrayList<>();for(var block:currentProgram.getMemory().getBlocks()){Map<String,Object> x=new LinkedHashMap<>();x.put("name",block.getName());x.put("start",block.getStart().toString());x.put("size",block.getSize());x.put("initialized",block.isInitialized());x.put("read",block.isRead());x.put("write",block.isWrite());x.put("execute",block.isExecute());blocks.add(x);}r.put("memoryBlocks",blocks);
  r.put("parserCodeSource",Class.forName("prospero.elf.ProsperoElfHeader").getProtectionDomain().getCodeSource().getLocation().toString());

  Map<String,Integer> statuses=new TreeMap<>(),types=new TreeMap<>();
  var rels=currentProgram.getRelocationTable().getRelocations();int count=0;
  while(rels.hasNext()){var x=rels.next();count++;statuses.merge(x.getStatus().toString(),1,Integer::sum);types.merge(Integer.toString(x.getType()),1,Integer::sum);}
  r.put("relocationRecords",count);r.put("relocationStatuses",statuses);r.put("relocationTypes",types);
  List<Object> decompiled=new ArrayList<>();StringBuilder bodies=new StringBuilder();DecompInterface di=new DecompInterface();
  try {di.openProgram(currentProgram);var fs=currentProgram.getFunctionManager().getFunctions(true);int attempted=0;
   while(fs.hasNext()&&attempted<8){Function f=fs.next();var block=currentProgram.getMemory().getBlock(f.getEntryPoint());if(block==null||!block.isInitialized())continue;
    var d=di.decompileFunction(f,10,monitor);Map<String,Object> item=new LinkedHashMap<>();item.put("address",f.getEntryPoint().toString());item.put("completed",d.decompileCompleted());item.put("error",d.getErrorMessage());decompiled.add(item);if(d.decompileCompleted()&&d.getDecompiledFunction()!=null)bodies.append("/* "+f.getEntryPoint()+" "+f.getName()+" */\n"+d.getDecompiledFunction().getC()+"\n");attempted++;
   }
  } finally{di.dispose();}
  r.put("decompilationSample",decompiled);Files.writeString(out.resolve(currentProgram.getName()+".c"),bodies.toString());
  Files.writeString(out.resolve(currentProgram.getName()+".json"),new GsonBuilder().setPrettyPrinting().create().toJson(r)+"\n");
  println("Phase21 metrics exported: "+currentProgram.getName());
 }
}
