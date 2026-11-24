# Executable corpus and provenance

**PASS for expanding/documenting the corpus.** There are eight non-synthetic inventory files: three existing upstream homebrew executables, three existing compiler controls and **two newly built public-SDK-generated programs**. Twenty-six synthetic malformed/format fixtures are a separate population. The34-row CSV labels the kind on every row; JSON contains complete program/section headers, raw dynamic entries and validation results.

| New sample | Bytes | SHA-256 | ABI/type |
| --- | --- | --- | --- |
| sdk-minimal.elf | 82648 | 234071c6731e9df08fd21a596d1545c411ba788a27a51819389f829be1472593 | OSABI9 /ABI 2 /0xfe10 |
| sdk-imports.elf | 82648 | 97df4ad56083e1de2422476a6ddaba1c320734110cd86de24bfad84c5d6ffb8c | OSABI9 /ABI 2 /0xfe10 |

The native linker is [Rufidj/ps5link-sdk at ea771e5](https://github.com/Rufidj/ps5link-sdk/tree/ea771e535378740b6a058b8e5419eb8a0e0e0ec8), GPL-3.0. Its Makefile, host driver, input reader, resolver, startup and ELF writer were reviewed before use. Only the host linker target was built. It reads original freestanding objects and writes complete SCE files; no signing, installation or console action occurred. Installed clang targeting x86_64-unknown-freebsd substitutes for the unavailable prospero-clang wrapper for these small objects. The public linker/CRT are unchanged. The samples are legitimate local SDK outputs, **not prebuilt console-tested programs** and not hand-constructed parser fixtures.

`sdk-minimal.c` returns7; startup imports three libc functions. `sdk-imports.c` adds a string, counter, puts and getpid, producing five imports across libc.prx/libkernel.prx. The actual full files are82,648 bytes each. The linker's smaller stdout “wrote” number is not used as file-size evidence; stat/read bytes are authoritative. The output path is embedded in comment metadata, so reproducing at another path can change the full-file hash.

Existing SharpProspero at 5dfdb4b (GPL-3.0), elfldr v0.28 (GPL-3.0) and sharpemu-demo at 49e6b3b (GPL-2.0-or-later) retain their recorded provenance. Phase 21 FreeBSD ET_REL and linked SystemV ET_EXEC controls retain their exact files; the linked control is not mislabeled a FreeBSD runtime. The earlier original Linux test is inventory/host-bootstrap evidence, not a newly acquired PS5 program. No commercial game, vendor system library or decrypted retail firmware was acquired.

The bounded ABI 3 search covered the referenced source families, current native-linker/tooling trees, prior sample sources and targeted primary GitHub results. A header-spoofer writeup/vendor-module discussion was excluded as genuine evidence; no spoofing tool or vendor module was used. No suitable genuine ABI 3 sample was obtained. This is a recorded search limitation, not proof no lawful sample exists. `corpus-search.json` records sources/commits and exclusions.

The independent preflight records architecture, OSABI/ABI, type, full hash/size, headers, dynamic layout, needed libraries, symbol counts and relocation formats/types for bounded supported inputs. Rejected fixtures retain unvalidated raw-header fields clearly marked as such. It does not turn a load-spec match into full compatibility. See `executable-inventory.json`, `sdk-build.json` and `sample` rows in the CSV for provenance and exact build commands.
