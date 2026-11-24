# Phase 22 — executable and parser validation

24 November 2026. **Overall PARTIAL.** New corpus, parser, build and third-engine results were produced. Genuine ABI 3, complete SDK-sample relocation compatibility and several raw-parser rejection expectations remain unresolved. **No protected retail firmware code was analysed. Jailbreak probability remains UNKNOWN.**

Highlights: two locally SDK-generated ABI 2 SCE samples; byte-identical rebuild of the existing repaired extension; two reproduced missing-tag diagnostics improved in an isolated two-line patch; **30/30 preflight unit tests**; the original **567/567** relocation baseline preserved; and **126/126** normal desktop checks after an explicit iframe-ready handshake. The SDK samples remain partial at **3/11** and **3/13** APPLIED; this is not hidden by successful import or decompilation labels.

| Objective | Grade | Evidence |
| --- | --- | --- |
| 22A corpus | PASS | Two new SDK-generated ABI 2 SCE programs; eight non-synthetic files inventoried separately from 26 fixtures |
| 22B genuine ABI 3 compatibility | BLOCKED | No eligible provenance-attested genuine ABI 3 sample obtained |
| 22B synthetic ABI 3 parser/import checks | PASS | One accepted load spec, one APPLIED relocation; no decompiled function body; synthetic only |
| 22C dynamic-table validation | PARTIAL | Bounded preflight and REL/RELA/SCE-relative tests; 12 strict raw-parser rejection expectations remain unmet |
| 22D extension review / diagnostic repair | PASS | Byte-identical existing-repair rebuild; two-line isolated checked-error improvement; installed extension preserved |
| New SDK sample full compatibility | PARTIAL | Loader selects both; only 3/11 and3/13 relocations apply, before and after |
| 22E regression framework | PASS | 30 preflight tests, 26 raw cases per build, repeatable JSON/timings/exit status |
| Raw-parser strict rejection matrix | PARTIAL | 12/26 strict checks before,14/26 after; remaining12 gaps are explicit |
| Existing successful samples after repair | PASS | 567/567,20/20,164/164 and both compiler controls reproduced |
| 22F historical14.10 | BLOCKED | Single HEAD still reports HTTP200 /Content-Length0; no body redownload |
| 22G desktop WebKit | PASS | Original40/42; handshake correction then126/126 across three engines/two modes |
| 22H preservation/evidence/publication | PASS | Pinned provenance, reviewed scope, original/synthetic separation and checksum review |

## Deliverables and reproduction

- [Corpus](EXECUTABLE-CORPUS.md), [inventory CSV](EXECUTABLE-INVENTORY.csv), [ABI compatibility](ABI-COMPATIBILITY-REPORT.md)
- [Dynamic tables](DYNAMIC-TABLE-ANALYSIS.md), [extension review](GHIDRA-PROSPERO-REVIEW.md), [Ghidra CSV](GHIDRA-REGRESSION-RESULTS.csv)
- [Regression report](REGRESSION-TEST-REPORT.md), [build instructions](BUILD-REPRODUCTION.md)
- [14.10 availability](FIRMWARE-14.10-AVAILABILITY.md), [WebKit](WEBKIT-VALIDATION.md)
- [Evidence register](EVIDENCE-REGISTER.csv), [limitations](LIMITATIONS.md), [final report](PHASE-22-FINAL-REPORT.md)

From this directory:

```sh
python3 test_elf_preflight.py preflight-results.json
python3 elf_preflight.py /path/to/sample.elf
python3 fixtures.py /path/to/new-fixture-directory
python3 run_regression.py --ghidra /path/to/ghidra_12.2_PUBLIC --work /path/to/new-run-directory
python3 run_browser_tests.py --suite browser --output browser-results
sha256sum -c SHA256SUMS.txt
```

The preflight is a bounded ELF64 little-endian x86-64 metadata validator, not a runtime loader or decrypter. The raw Ghidra regression driver deliberately exits **1** if strict rejection expectations remain unmet; its expected current experimental result is14 PASS /12 FAIL across 26 synthetic cases. The independent preflight suite exits0 with 30 passing tests. Ghidra helper/bootstrap imports and replayed observations are not added to headline compatibility counts.

Fixtures are generated from scratch, small and explicitly synthetic; no acquired executable header is edited. Published binary fixtures are restricted to exactly those manifested synthetic files. Real homebrew/SDK ELF files, firmware, extension JARs and project databases remain local. Original tools/fixtures are MIT; Ghidra-derived patches retain GPL-3.0 terms. The installed extension and historical Phases 1–21 are preserved. Actual PR/commit details are in the publication receipt; no merge into main is implied.
