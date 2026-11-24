# Fresh GhidraProspero regression

**PARTIAL for corpus breadth; PASS for the repaired baseline and tested loader selection.** Ghidra 12.2 performed four fresh static imports in a separate Phase21 project. No target executable was run and no ELF header was modified. `RegressionExport.java` records eligibility probes, actual loader selection, external symbols, relocation types/statuses and eight-or-fewer initialized-function decompilation samples.

| Input | OSABI | ABI | Type | Selected loader | External records | Relocation statuses | Decompile sample |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sharpprospero-sample-5dfdb4b-eboot.elf | 9 | 2 | 0xfe10 | Prospero ELF | 165 | {'APPLIED': 567} | 8/8 |
| sharpemu-demo-0.elf | 9 | 2 | 0x3 | Executable and Linking Format (ELF) | 19 | {'APPLIED': 20} | 8/8 |
| freebsd-control.o | 9 | 0 | 0x1 | Executable and Linking Format (ELF) | 0 | {} | 2/2 |
| freebsd-control.elf | 0 | 0 | 0x2 | Executable and Linking Format (ELF) | 0 | {} | 2/2 |

The positive SharpProspero sample is the unchanged GPL-3.0 homebrew at pinned revision `5dfdb4b0b166e83dc9ae275001afb695f12c7174`, SHA-256 `aa011c6e1e8db0940e1bac2523e6076c8624275d494f4c9d422542702e2f0236`. The installed repaired JAR still hashes to `73da132910d1102fc1e3548458cd8eb95ffada7f829bf65db036f5d7365be494`. This is a newly performed regression, unlike Phase 20's review of saved results: **165 external records, six actual libraries, 402 RELATIVE +165 JUMP_SLOT, all 567 APPLIED**. Eight selected bodies decompile; this does not validate all 2,655 function records.

New [sharpemu-demo homebrew](https://github.com/sharpemu/sharpemu-demo/tree/49e6b3b25678f14ec57a70b907ee215fddb608d8) comes from the author's release archive and declares GPL-2.0-or-later. Its unchanged ELF is 69,248 bytes, SHA-256 `05c414993d1cd9e7182bbf5647be1ffad72c6ed6b6f5399d01af27281fef48b8`. It is x86-64 / OSABI 9 / ABI 2 but **ET_DYN (3)**, so Prospero advertises zero load specs and the generic ELF loader is selected. Generic analysis records 19 external symbols, five actual libraries and 20 APPLIED relocations: 19 GLOB_DAT plus one RELATIVE. Eight sampled functions decompile. ABI 2 alone is not specialized-loader eligibility, and generic-loader success is not evidence of additional SCE-format support.

The original `freebsd-control.c` is compiled with `clang --target=x86_64-unknown-freebsd -ffreestanding -fno-stack-protector -c`. Its object is OSABI 9 / ABI 0 / ET_REL. GNU ld then produces the linked `freebsd-control.elf`, which is OSABI 0 / ABI 0 / ET_EXEC. The latter is explicitly a System V linked control, despite its inherited filename; it is not represented as a FreeBSD runtime executable. Both select generic ELF, with zero imports and zero remaining relocations. Two functions each decompile. A separate readelf check confirms this particular object also has no raw relocation entries; no unobserved relocation handling is claimed.

The Prospero detector requires machine 0x3e, accepted SCE type and ABI 2/3; kernel-type candidates also have a signed-high-base condition. Its format-property string alone is not sufficient to identify the selected loader: this audit uses headless `Using Loader` records and the Prospero marker. External library counts exclude the `<EXTERNAL>` placeholder.

Baseline analysis reports existing-style entry-point, address-segment and p-code-flow warnings. All four imports and analyses report success; the bounded selected decompilations complete. Warnings are retained in `evidence/ghidra-regression.json` and logs, not hidden or recast as proof all functions are correct.

The bounded search covered current SharpProspero, its v0.6 archive, ps5link-sdk, PS5SDK and ps5-payload-dev/sdk snapshots. It yielded no additional suitable SCE-positive or ABI 3 binary. The old SDK archive contains shader ELFs, not extra x86-64 application samples used here. This is a search limitation, not proof such samples do not exist. `sample-provenance.json` and `sample-downloads.json` give pinned sources, licence declarations, archive hashes, member paths and negative results. Broader dynamic-table layout and ABI 3 compatibility remain unverified.

Replay in a new project with `analyzeHeadless`, the unchanged inputs, `-analysisTimeoutPerFile 120 -max-cpu 2 -scriptPath . -postScript RegressionExport.java /path/to/results <input paths>`. The original Phase 20 projects/notes were untouched. Source, compiler controls, hashes, actual selection and warning records are provided; third-party binary/archive bytes and the local project database are not published.
