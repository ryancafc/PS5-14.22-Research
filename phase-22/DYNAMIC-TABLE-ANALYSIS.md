# Dynamic-table validation and findings

**PARTIAL.** Two real SDK outputs extend import configurations but retain an ordinary PT_LOAD-backed virtual-address dynamic layout. Genuine alternate SCE-relative corpus coverage remains missing. The26 from-scratch fixtures separately exercise ordinary and SCE-relative metadata, REL/RELA formats, missing tags, duplicate metadata, invalid pointers/indices and truncation.

## Reproduced checked-error defect and minimal repair

The installed parser throws `ghidra.util.exception.AssertException` when SCE_STRSZ is present but SCE_STRTAB is absent, and when SCE_SYMTAB/SYMENT/HASH are present but SCE_SYMTABSZ is absent. Both are malformed **synthetic** inputs. Root cause: the two missing-value catch sites convert `NotFoundException` into an unchecked assertion, treating incomplete input as an internal invariant failure.

`proposed-parser-diagnostics.patch` changes **two throw statements** to checked `IOException("Incomplete SCE dynamic metadata: …", cause)`. Before/after probes use the exact same finalized fixture manifest/hashes. Both cases change from unchecked AssertException to descriptive IOException with the missing tag number preserved. Only ProsperoElfHeader.class differs between rebuilt JARs. The patch is isolated; the installed working extension is unchanged. This is an input-error reporting correction, not an exploit fix or a general bounds-validation repair.

## Separate defensive preflight

`elf_preflight.py` rejects truncated headers, invalid header-table/segment ranges, duplicate dynamic/SCE segments, missing bounded DT_NULL, duplicate singleton tags, incomplete/out-of-range strings/symbols and out-of-range relocation symbol indices. It explicitly follows file-backed PT_LOAD address translation or a unique SCE-relative segment, validates24-byte ELF64 symbols and16/24-byte REL/RELA records, and retains unrecognized relocation types as UNSUPPORTED metadata. It never applies a relocation.

Preflight checks cover whole referenced table lengths, not just the starting pointer. A terminated dynamic array may have remaining segment-tail bytes: the existing elfldr illustrates why non-multiple-of 16 p_filesz alone is not a valid rejection rule. Reads never cross the declared dynamic extent looking for DT_NULL. The metadata validator is capped at64 MiB and 4096 headers and rejects unsupported ELF classes/endianness/architectures rather than guessing.

## Residual raw-parser behavior

Under a deliberately strict rejection policy the installed parser meets **12/26** expectations and the diagnostic build **14/26**. **Twelve malformed fixtures still proceed at raw parse() stage**; these include truncated/range cases, invalid names/indices and duplicate metadata. This is a measured raw-stage policy gap. Full import rejection was not tested for every malformed file, and permissive partial parsing alone is not a demonstrated memory-safety flaw. The independent preflight rejects those cases before production use; the experimental two-line patch is not claimed to address them.

The unsupported-relocation fixture is retained by the parser and, on actual static import, records **UNSUPPORTED 1 /APPLIED 0**. Synthetic ordinary and SCE-relative fixtures each exercise their expected table paths; the SCE-relative full import applies one record. Real samples use RELA: baseline402 RELATIVE+165 JUMP_SLOT, elfldr140 RELATIVE+24 GLOB_DAT, sharpemu1 RELATIVE+19 GLOB_DAT, SDK programs8 RELATIVE plus3/5 JUMP_SLOT. REL parsing is synthetic-only here.

Source interpretation follows the [ELF dynamic specification](https://gabi.xinuos.com/elf/08-dynamic.html), [symbol table specification](https://gabi.xinuos.com/elf/05-symtab.html), [relocation formats](https://gabi.xinuos.com/elf/06-reloc.html) and pinned public Prospero constants. These sources describe metadata structure, not deployed retail14.22 behavior. Evidence: parser-before/after.json, raw-parser-comparison.json, fixtures/manifest.json, preflight-results.json, ghidra-regression.json and SDK relocation diagnostics.
