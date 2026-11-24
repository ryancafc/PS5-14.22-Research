// Calls the actual installed Prospero parser on bounded synthetic test files.
// @category PS5.Research
import ghidra.app.script.GhidraScript;
import ghidra.app.util.bin.*;
import ghidra.app.util.bin.format.elf.*;
import ghidra.app.util.opinion.*;
import com.google.gson.GsonBuilder;
import java.nio.file.*;
import java.io.*;
import java.util.*;
import java.util.function.Consumer;
import java.lang.reflect.*;
public class ParserProbes extends GhidraScript {
 public void run() throws Exception {
  String[] args=getScriptArgs();Path dir=Paths.get(args[0]);List<Object> results=new ArrayList<>();
  Class<?> cls=Class.forName("prospero.elf.ProsperoElfHeader");
  for(Path path:(Iterable<Path>)Files.list(dir).filter(x->x.toString().endsWith(".elf")).sorted()::iterator){
   Map<String,Object> r=new LinkedHashMap<>();r.put("file",path.getFileName().toString());List<String> messages=new ArrayList<>();r.put("messages",messages);long start=System.nanoTime();
   try(FileByteProvider bp=new FileByteProvider(path.toFile(),null,java.nio.file.AccessMode.READ)){
    try {Object obj=cls.getConstructor(ByteProvider.class,Consumer.class).newInstance(bp,(Consumer<String>)messages::add);ElfHeader h=(ElfHeader)obj;
     h.parse();r.put("accepted",true);r.put("dynamicTablePresent",h.getDynamicTable()!=null);r.put("stringTablePresent",h.getDynamicStringTable()!=null);r.put("symbolTablePresent",h.getDynamicSymbolTable()!=null);
     r.put("relocationTableCount",h.getRelocationTables().length);
    }catch(Throwable t){while(t instanceof InvocationTargetException&&t.getCause()!=null)t=t.getCause();r.put("accepted",false);r.put("exceptionClass",t.getClass().getName());r.put("exception",String.valueOf(t.getMessage()));r.put("checkedFailure",t instanceof IOException||t instanceof ElfException);List<String> causes=new ArrayList<>();for(Throwable c=t;c!=null;c=c.getCause())causes.add(c.getClass().getName()+": "+c.getMessage());r.put("causes",causes);}
    try{for(Loader l:LoaderService.getAllLoaders())if(l.getName().equals("Prospero ELF"))r.put("eligibleSpecs",l.findSupportedLoadSpecs(bp).size());}catch(Throwable t){r.put("eligibilityError",t.toString());}
   }
   r.put("elapsedMs",(System.nanoTime()-start)/1e6);results.add(r);
  }
  Files.writeString(Paths.get(args[1]),new GsonBuilder().setPrettyPrinting().create().toJson(results)+"\n");println("Probed "+results.size()+" synthetic inputs");
 }
}
