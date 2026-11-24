# Reusable static parser regression results

**PASS for framework/reproducibility; PARTIAL for raw strict rejection.** The framework does not execute guest instructions. `fixtures.py` generates26 deterministic small files from scratch and a SHA-256 manifest. `test_elf_preflight.py` runs26 fixture cases plus file-preservation, oversize-policy, CLI-error and known REL/RELA metadata tests. **30 tests pass, zero failures/errors**; each has recorded execution time.

Actual Ghidra header.parse() and eligibility probes run separately on the same26 files before/after the isolated patch. Their strict matrix is shown below. A rejection counts as meeting policy only if it is a checked input error; unsupported ABI/type cases may still be valid metadata with zero Prospero load specs. Retaining an unknown relocation for an application-stage UNSUPPORTED result is expected.

| Synthetic case | Expected raw behavior | Installed | Experimental |
| --- | --- | --- | --- |
| valid-standard | accept | PASS | PASS |
| valid-sce-relative | accept | PASS | PASS |
| valid-abi3-synthetic | accept | PASS | PASS |
| ordinary-etdyn | accept | PASS | PASS |
| unsupported-abi0 | accept | PASS | PASS |
| unsupported-abi4 | accept | PASS | PASS |
| unsupported-type | accept | PASS | PASS |
| valid-rel-format | accept | PASS | PASS |
| valid-dynamic-tail-padding | accept | PASS | PASS |
| bad-magic | reject | PASS | PASS |
| truncated-ident | reject | PASS | PASS |
| truncated-header | reject | FAIL | FAIL |
| phoff-outside | reject | FAIL | FAIL |
| segment-outside | reject | FAIL | FAIL |
| dynamic-outside | reject | FAIL | FAIL |
| dynamic-unaligned-size | reject | FAIL | FAIL |
| dynamic-missing-null | reject | FAIL | FAIL |
| sce-missing-strtab | reject | FAIL | PASS |
| sce-missing-symtabsz | reject | FAIL | PASS |
| string-pointer-outside | reject | FAIL | FAIL |
| string-size-outside | reject | FAIL | FAIL |
| symbol-name-outside | reject | FAIL | FAIL |
| relocation-symbol-outside | reject | FAIL | FAIL |
| unsupported-relocation | diagnose | PASS | PASS |
| duplicate-singleton-strtab | reject | FAIL | FAIL |
| duplicate-sce-segment | reject | FAIL | FAIL |

Raw totals: **12 PASS /14 FAIL before; 14 PASS /12 FAIL after**. Both missing-SCE-tag cases improve. Twelve accepted malformed raw-stage cases remain open. These are not converted into PASS because a separate tool filters them. The packaged driver was replayed in a new directory and reproduced14/12, with intentional exit code1. The30-case independent preflight suite exits0.

Twelve full-analysis static import rows are in GHIDRA-REGRESSION-RESULTS.csv: two SDK imports before and ten after, of which three after rows are explicitly synthetic. Nine rows are non-synthetic development/homebrew/control observations, with repeated SDK before/after observations rather than nine unique files. Bootstrap no-analysis imports and repeated raw probes are excluded from that count.

The synthetic unknown relocation imports as UNSUPPORTED, never APPLIED. The real SDK imports expose FAILURE records and remain PARTIAL even though Ghidra reports analysis completed. Zero sampled decompilations on synthetic ABI/layout files is explicit. Ghidra warnings, loader selection, imported symbols, memory blocks and relocations remain independently recorded.

Reproduce with README commands. `run_regression.py` requires a new work directory and returns nonzero for unresolved raw-policy failures. Use `--config /path/to/experimental-config` to select a separate extension; otherwise it uses the normal installation. No runtime loader, console action, large allocation or memory-corruption trigger is part of these tests.
