# Phase 21 — firmware comparison and technical validation

24 November 2026. **Overall: PARTIAL, with substantial new verified results.** The missing historical 14.10 package and unfilled ABI 3/additional SCE-positive coverage prevent a complete comparison/regression matrix. No protected firmware code was analysed; jailbreak probability remains **UNKNOWN**.

New measurements reproduce the 14.20→14.22 **115-byte difference in [0, 0x440)** and establish that recovery's first entry matches the standard update's inner entry. The original utility passes **27 tests**. Fresh Ghidra imports validate the repaired baseline and expose why a new ABI 2 / ET_DYN sample correctly takes the generic ELF loader. Both Chromium and Firefox pass **21 checks in two header modes**.

## Objectives

| Objective | Grade | Evidence |
| --- | --- | --- |
| 21A: authentic acquisition and availability | PARTIAL | 14.20 standard and 14.22 recovery acquired; existing 14.22 reused; 14.10 endpoint is empty |
| 21B: available-input metadata comparison | PASS | Three complete package identities; 14.20/14.22 window and recovery entry checks |
| 14.10 comparisons | BLOCKED | Exact historical package unavailable at checked official endpoints |
| 21C: reusable firmware utility | PASS | 27 synthetic tests, real package JSON/CSV and input preservation |
| 21D: Ghidra regression breadth | PARTIAL | Fresh positive baseline plus three new negative controls; no new SCE-positive or ABI 3 sample |
| Repaired loader baseline | PASS | Prospero selected; 165 externals, 567 APPLIED, eight sampled decompilations complete |
| 21E: original corrected diagnostics | PASS | Bounded original suite with accurate statuses, JSON export and explicit limits |
| 21F: cross-engine desktop validation | PASS | Chromium and Firefox, two header modes, 84/84 expected passes |
| 21G: evidence/integrity review | PASS | Source, file, CSV and prior-file preservation checks; final package/publication review |
| Publication preparation | PASS | Separate branch stacked on pending Phase 20; UNKNOWN retained |

## Read and reproduce

- [Acquisition](FIRMWARE-ACQUISITION.md), [container comparison](FIRMWARE-COMPARISON.md), [metadata CSV](FIRMWARE-METADATA.csv)
- [Ghidra regression](GHIDRA-REGRESSION-REPORT.md)
- [Browser report](BROWSER-DIAGNOSTICS-REPORT.md), [cross-browser CSV](CROSS-BROWSER-RESULTS.csv)
- [Evidence register](EVIDENCE-REGISTER.csv), [limitations](LIMITATIONS.md), [final report](PHASE-21-FINAL-REPORT.md)

From this directory:

```sh
python3 -m unittest -v test_firmware_compare
python3 firmware_compare.py /path/to/14.20-standard.PUP /path/to/14.22-standard.PUP --window 0:0x440 --json comparison.json --csv metadata.csv
python3 run_browser_tests.py --suite browser --output browser-test-output
sha256sum -c SHA256SUMS.txt
```

The utility needs Python's standard library only. The native browser harness expects `/usr/bin/chromium` and `/usr/bin/firefox-esr`; it uses fresh temporary profiles and enables neither browser's sandbox-disable flags. Logs/result JSON are written only to the chosen output directory. Serve the interactive page with `python3 -m http.server 8000 --bind 127.0.0.1 --directory browser`, then open `http://127.0.0.1:8000/index.html`; an unspecified isolation expectation is SKIP. Export JSON with the page button.

Firmware and homebrew binaries are deliberately outside the publication/package. Reproduction requires independently obtained matching inputs. Paths in public evidence use `~/PS5-Research` and `AUDIT_WORKSPACE` placeholders. Local and publication manifests each cover their own contents and exclude themselves. Pending Phase 20 is preserved unchanged; the final publication receipt records the actual branch and PR status.
