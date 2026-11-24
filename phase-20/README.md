# Phase 20 — external research audit

Date: 24 November 2026. **Overall verdict: PASS for the audit scope, with material evidence limitations. Jailbreak probability remains UNKNOWN.**

This phase audited incorporated copies of [Repository A](https://github.com/ccclosed/ps5-1422-research/tree/7d7fcbb448b2376c396376038b1250437ca5092b) and [Repository B](https://github.com/karter-captain/ps5-14.22-browser-probes/tree/d0702131ff94d40bd8c408452ccac4c94f2af00e), independently rechecked the existing firmware files, reviewed the earlier Ghidra evidence, and ran only bounded, reviewed desktop browser diagnostics. It did not run exploit chains, trigger payloads, emulators, key-search code or console tests.

## Claim results

54 claim units were reviewed: 37 from A and 17 from B. Classifications are exclusive primary labels; they are not counts of independent experiments.

| Evidence classification | Claims |
|---|---:|
| Independently verified | 11 |
| Reproduced locally | 4 |
| Source-supported | 10 |
| Author-reported | 6 |
| Simulation only | 2 |
| Unverified | 13 |
| Contradicted | 6 |
| Blocked | 2 |

Thus **11 claims were independently verified**, **4 were reproduced locally on desktop Chromium**, and **19 were classified Unverified or Contradicted**. The other 20 comprise source-supported, author-reported, simulation-only and blocked claims. A locally reproduced browser behavior is not retail PS5 evidence.

## Most consequential findings

- A's standard-update identity, SLB2 fields, extraction extent and 387 zero padding bytes match the local files (A01–A09). Recovery/cross-version comparisons lack required local inputs (A14–A15).
- B's non-shared Atomics expectation is wrong. Its original small diagnostic produces nine false anomaly labels on a normal desktop browser (B01).
- B's nominal 320 MB slow-chain cap can retain **905 MiB**, and its largest pressure option can request **10 GiB**. These pressure modes were not executed (B03–B06).
- Mock/TCP completion is simulation evidence. A's optional-dependency branches can count skipped checks as PASS, and its reported stage/test counts drift (A20–A21, A32–A33).
- Older-kernel/source defaults, shared container signatures, user-agent strings and API availability do not establish retail 14.22 executable behavior.

## Deliverables

- [Repository audit](REPOSITORY-AUDIT.md)
- [Claim audit](CLAIM-AUDIT.csv) and [full evidence register](EVIDENCE-REGISTER.csv)
- [Firmware verification](FIRMWARE-VERIFICATION.md)
- [Ghidra review](GHIDRA-REVIEW.md)
- [Browser diagnostics review](BROWSER-DIAGNOSTICS-REVIEW.md)
- [Limitations](LIMITATIONS.md) and [final report](PHASE-20-FINAL-REPORT.md)
- SHA256SUMS.txt, supporting JSON evidence, logs and auditor-authored read-only/benign scripts

Source locations and commits are recorded per claim. `evidence/claim-summary.json` defines the counts. Check the files with `sha256sum -c SHA256SUMS.txt` from this directory. The checksum file does not hash itself.

## Objective status

| Objective | Status | Evidence |
|---|---|---|
| 20A: inventory both repositories | PASS | Pinned commits, file inventories, licences, dependencies and missing inputs |
| 20B: classify significant claims | PASS | 54 source-located claims with method, observation, limits and verdict |
| 20C: independently verify existing 14.22 package metadata | PASS | Two full hashes, range hash, bounds, padding and alignment |
| Cross-version/recovery package claims | BLOCKED | Required other packages and original raw comparisons are absent |
| 20D: review executable documentation against existing samples | PASS | Fresh header/import/relocation decoding and review of prior Ghidra exports |
| 20E: assess diagnostic source and bounded desktop semantics | PASS | All ten HTML pages reviewed; four small diagnostic pages tested |
| Retail PS5 browser/executable reproduction | BLOCKED | No controlled hardware experiment or plaintext retail 14.22 code in scope |
| 20F: evidence register and integrity manifest | PASS | Two validated CSVs and file digests |
| Publication preparation and change review | PASS | Documentation-only branch based on current official main; publication review record |

The BLOCKED rows qualify the underlying research claims. They do not imply that the permitted audit or desktop checks were left unperformed.
