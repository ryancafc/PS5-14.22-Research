// Export failure evidence from an already analysed project, read-only.
// @category PS5.Research
import ghidra.app.script.GhidraScript;
import com.google.gson.GsonBuilder;
import java.util.*;
import java.nio.file.*;
public class RelocationDiagnostics extends GhidraScript {
 public void run() throws Exception {
  Map<String,Object> result=new LinkedHashMap<>();List<Object> relocs=new ArrayList<>();var iter=currentProgram.getRelocationTable().getRelocations();
  while(iter.hasNext()){var r=iter.next();Map<String,Object> x=new LinkedHashMap<>();x.put("address",r.getAddress().toString());x.put("status",r.getStatus().toString());x.put("type",r.getType());x.put("symbol",r.getSymbolName());x.put("values",r.getValues());var block=currentProgram.getMemory().getBlock(r.getAddress());x.put("blockAtAddress",block==null?null:block.getName());relocs.add(x);}
  List<Object> errors=new ArrayList<>();var bookmarks=currentProgram.getBookmarkManager().getBookmarksIterator("Error");
  while(bookmarks.hasNext()){var mark=bookmarks.next();Map<String,Object>x=new LinkedHashMap<>();x.put("address",mark.getAddress().toString());x.put("category",mark.getCategory());x.put("comment",mark.getComment());errors.add(x);}
  result.put("name",currentProgram.getName());result.put("relocations",relocs);result.put("errorBookmarks",errors);
  Files.writeString(Paths.get(getScriptArgs()[0],currentProgram.getName()+"-diagnostics.json"),new GsonBuilder().setPrettyPrinting().create().toJson(result)+"\n");
 }
}
