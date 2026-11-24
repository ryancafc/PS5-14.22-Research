# External executable documentation and Ghidra review

Result: **PASS for the documentary/static review.** This phase re-read existing homebrew headers and dynamic tables, reviewed saved Ghidra evidence and checked the relevant loader source. It did not rerun the already completed Linux test, rebuild GhidraProspero or reanalyse a project.

## Loader eligibility

GhidraProspero's current ELF loader requires machine 0x3e, one of its accepted SCE types, and ABI 2 or 3. Ordinary ET_DYN (3) is rejected independently of ABI; kernel-type candidates have an additional signed-high-base restriction. No explicit FreeBSD OSABI equality test occurs in that detection method. The original elfldr remains ABI 0 / ET_DYN; the compatible sample remains ABI 2 / 0xfe10. Both raw headers and hashes match the prior evidence. Neither file was altered.

These specialized-loader requirements differ from the runtime elfldr program's accepted ET_EXEC/ET_DYN types. A's freestanding trigger files being valid ELF64 ET_EXEC does not establish their console ABI/syscall compatibility or successful execution (A28). They were not submitted to Ghidra or run.

## Fresh static checks of the existing samples

| Sample | Dynamic table entries | Independently decoded relocation types | Recorded Ghidra status |
|---|---:|---|---|
| elfldr v0.28 | 164 RELA records | 140 R_X86_64_RELATIVE + 24 R_X86_64_GLOB_DAT | 164 APPLIED in prior export |
| SharpProspero sample | 402 ordinary RELA + 165 PLT RELA records | 402 R_X86_64_RELATIVE + 165 R_X86_64_JUMP_SLOT | 567 APPLIED in prior export |

The type counts above were freshly decoded from the existing binaries, independently of the prior Ghidra export. The APPLIED statuses remain evidence of the earlier Ghidra run, not a newly executed relocation test. RELA describes an explicit-addend entry format; it does not mean every entry is R_X86_64_RELATIVE. The [ELF relocation specification](https://gabi.xinuos.com/elf/06-reloc.html) distinguishes format, symbol index and operation type.

Fresh DT_NEEDED decoding confirms elfldr's libkernel_web.sprx, libSceLibcInternal.sprx and libSceNet.sprx. The compatible sample names libc.prx, libkernel.prx, libScePad.prx, libSceSystemService.prx, libSceUserService.prx and libSceVideoOut.prx. Both naming conventions occur in these homebrew files; neither suffix identifies a particular retail firmware build.

The saved compatible-sample export has 165 external symbol records and six actual library names. It contains 2,655 function records including externals, with 2,490 address records and 101 selected decompiled bodies. The elfldr export has 171 records including 24 externals, with 147 address records and 123 decompiled initialized bodies. These are distinct measurements. They do not mean 2,655 validated source functions or 165 library implementations were reverse engineered.

## Loading and initialization terminology

Use each PT_LOAD's p_offset/p_vaddr relationship to translate file locations and memory addresses. Do not extrapolate a single file-minus-0x4000 formula to unrelated binaries. The [ELF program-loading specification](https://gabi.xinuos.com/elf/07-pheader.html) distinguishes file size from memory size and describes zero-filled extra memory.

A's narrow elfldr observation is source-supported: the v0.28 data_load helper copies p_filesz bytes without explicitly zeroing the tail of its malloc-backed mirror. The previously decompiled homebrew startup independently clears its own BSS. Record both facts instead of generalizing one helper into a universal firmware behavior or payload rule (A29). No loader payload was run to test runtime effects.

## Annotation provenance and proposed note improvements

The existing main, elfldr_sanity_check, elfldr_exec, elfldr_find_pid and notify names are source-backed analyst annotations, compared to upstream elfldr v0.28. The descriptive payload_entry name was added at the recorded RVA-zero entry. Preserve the annotation/source version and distinguish role inference from an original symbol. The existing notes already qualify the misleading syscall-stub constant returns; keep that caveat.

Recommended additions to the earlier note set are this phase's exact relocation-type breakdown, the helper-versus-startup BSS qualification, explicit field-width alternatives in the shared container prologue, and the distinction between newly decoded metadata and reviewed prior Ghidra results. Previous notes and project databases were preserved; no historical record was silently rewritten.

Evidence: `elf-metadata-verification.json`, `prior-ghidra-evidence-review.json`, the current loader source, and the pre-existing 23 November session exports. The installed extension JAR still hashes to 73da132910d1102fc1e3548458cd8eb95ffada7f829bf65db036f5d7365be494. No firmware-specific executable behavior was established.
