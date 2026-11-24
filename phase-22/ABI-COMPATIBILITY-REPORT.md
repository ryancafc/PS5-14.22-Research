# ABI and actual loader compatibility

**Genuine ABI 3 compatibility: BLOCKED.** The existing detector accepts machine 0x3e, ABI 2 or3 and its supported SCE types (0xfe00/fe01/fe04/fe0c/fe10/fe18); kernel-type 2 additionally needs a signed-high-base candidate. There is no explicit equality guard for OSABI9. Ordinary ET_DYN is not accepted merely because its ABI is2.

| Fresh experimental import | Kind | Selected loader | External records | Relocations | Sample decompile |
| --- | --- | --- | --- | --- | --- |
| elfldr-ps5.elf | upstream homebrew | Executable and Linking Format (ELF) | 24 | {'APPLIED': 164} | 8/8 |
| freebsd-control.elf | compiler control | Executable and Linking Format (ELF) | 0 | {} | 2/2 |
| freebsd-control.o | compiler control | Executable and Linking Format (ELF) | 0 | {} | 2/2 |
| sdk-imports.elf | SDK-generated | Prospero ELF | 5 | {'APPLIED': 3, 'FAILURE': 10} | 8/8 |
| sdk-minimal.elf | SDK-generated | Prospero ELF | 3 | {'APPLIED': 3, 'FAILURE': 8} | 7/7 |
| sharpemu-demo-0.elf | upstream homebrew | Executable and Linking Format (ELF) | 19 | {'APPLIED': 20} | 8/8 |
| sharpprospero-sample-5dfdb4b-eboot.elf | upstream homebrew | Prospero ELF | 165 | {'APPLIED': 567} | 8/8 |
| unsupported-relocation.elf | synthetic fixture | Prospero ELF | 1 | {'UNSUPPORTED': 1} | 0/0 |
| valid-abi3-synthetic.elf | synthetic fixture | Prospero ELF | 1 | {'APPLIED': 1} | 0/0 |
| valid-sce-relative.elf | synthetic fixture | Prospero ELF | 1 | {'APPLIED': 1} | 0/0 |

The unchanged installed loader and isolated diagnostic build both select Prospero for the two new ABI 2 SCE SDK outputs. Both produce **3 APPLIED /8 FAILURE** for sdk-minimal (11 records), and **3 APPLIED /10 FAILURE** for sdk-imports (13 records). The two-line diagnostic change neither fixes nor worsens these results. Imported symbol counts/libraries are3/one and5/two; successful decompilation of7/7 and8/8 selected bodies is not complete binary compatibility.

Relocation diagnostics show default-space GOT addresses such as01008018 with FAILURE and no block there. Memory exports show missing default-space GOT coverage and an overlay `.data` block. Three successfully applied RELATIVE targets lie in the separately mapped process-parameter area. This localizes an observed mapping/relocation limitation; responsibility between the writer layout and loader mapping is not conclusively assigned. No speculative mapping patch is shipped.

The existing ABI 2 SharpProspero baseline still has 165 external records, six actual libraries and **567 APPLIED**. Generic ABI 2/ET_DYN sharpemu still has 19 externals/five libraries and20 APPLIED. ABI 0 elfldr still has 24 externals/three libraries and 164 APPLIED. Both compiler controls select generic ELF and decompile2/2 sampled bodies. Loader selection is taken from actual headless logs and the Prospero marker, not solely the generic executable-format property string.

The synthetic ABI 3 file obtains one Prospero load spec, creates memory/import records and applies one relocation; **zero initialized function bodies were selected/decompiled**. This establishes only a synthetic parser/import path. It does not establish genuine ABI 3 executable compatibility, source agreement or console behavior. The same restriction applies to the synthetic SCE-relative layout fixture. No acquired header was edited.

Selected source comparison finds the literal `return 7` structure in sdk-minimal's decompilation and the original message/counter/call structure in sdk-imports. Imported call resolution remains limited by the relocation failures; it is not represented as full source recovery. Raw decompilation artifacts remain local. `source-comparison.json`, full memory-block JSON and address/status diagnostics support these statements.
