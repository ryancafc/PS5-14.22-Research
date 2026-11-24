# Reproducible builds and isolated replay

The actual recorded builds used Ghidra 12.2, Java 25.0.5 and Gradle 9.2.1. Existing repaired JAR rebuilt byte-identically; the diagnostic build changes one class. Preserve a known working extension and use a NEW source/config/project directory. These instructions do not install into the working user configuration.

## Extension

```sh
git clone https://github.com/shadps5-emu/GhidraProspero.git GhidraProspero-phase22
cd GhidraProspero-phase22
git checkout e529ef4dd3edbb78400f30492db7c82802a1a117
git apply /absolute/path/to/phase-22/existing-repair.patch
# Build here first to reproduce the preserved existing repair.
gradle -g /tmp/phase22-gradle-replay --no-daemon -PGHIDRA_INSTALL_DIR=/absolute/path/to/ghidra_12.2_PUBLIC buildExtension
# Then apply the isolated new diagnostic change and rebuild.
git apply /absolute/path/to/phase-22/proposed-parser-diagnostics.patch
gradle -g /tmp/phase22-gradle-replay --no-daemon -PGHIDRA_INSTALL_DIR=/absolute/path/to/ghidra_12.2_PUBLIC buildExtension
```

Use the produced extension only in a new XDG_CONFIG_HOME tree under `ghidra/ghidra_12.2_PUBLIC/Extensions/GhidraProspero/`; retain the normal installation. The actual run copied the known installed extension layout to that separate tree and replaced its lib/GhidraProspero.jar with the experimental JAR. Set XDG_CONFIG_HOME only for the headless command. The build archive/project-folder name may differ; JAR identity and loaded code-source path are recorded separately.

Run `run_regression.py --ghidra /absolute/ghidra --work /new/run --config /new/config`. The current expected raw result is14/26 strict checks, with exit1, plus30/30 independent preflight unit tests. Run ordinary static imports separately with RegressionExport.java; use a new project and never execute target code. RelocationDiagnostics.java exports statuses and default-space block presence from saved read-only projects.

## SDK-generated corpus

Clone Rufidj/ps5link-sdk at ea771e535378740b6a058b8e5419eb8a0e0e0ec8. Review its Makefile/host code, then build only `make linker/link_real`. Compile the original sdk-minimal.c/sdk-imports.c and upstream linker/crt1.S with:

```sh
clang --target=x86_64-unknown-freebsd -ffreestanding -fPIC -fno-stack-protector -fno-asynchronous-unwind-tables -O1 -c INPUT -o OUTPUT.o
```

Link `linker/link_real NEW-SAMPLE.elf crt1.o SAMPLE.o`. This uses the unmodified SDK linker to write a whole native SCE output, not an acquired-header patch. No signing/console steps are required or performed. `sdk-build.json` records exact actual paths/commands and output identities. Embedded output paths mean hashes can change when rebuilding elsewhere. Real sample binaries are intentionally excluded from publication; preserve upstream GPL-3.0 terms when redistributing derived binaries. The original C/tool/fixture source licence is separate from the upstream linker licence.
