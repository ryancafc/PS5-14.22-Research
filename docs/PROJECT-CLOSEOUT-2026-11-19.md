# Project closeout — PS5 firmware 14.22 security research

**Closed to active investigation:** 19 November 2026. The maintainer decided to stop because the console firmware target is continuously moving. This is a **historical research archive**, not a supported jailbreak project or an ongoing promise of future findings.

## Complete phase index

| Phase | Workstream | Outcome |
|---|---|---|
| 1 | Public exploit history and firmware release timeline | Documented in earlier dossier |
| 2 | Relapse/Byepervisor and patch attribution | Documented, unknowns preserved |
| 3 | Independent claim verification | Documented with qualification |
| 4 | Source comparison feasibility and package hash discrepancy | Documented |
| 5 | Sony 13.x vs 14.x WebKit comparison | Local comparison reported |
| 6 | Changed-source classification and validation | Local audit reported |
| 7 | Upstream provenance and advisory mapping | Bounded, no exact sampled matches |
| 8 | 14.10 firmware package metadata | Catalogue discrepancy, raw PUP unverified |
| 9 | Independent audit | PASS WITH QUALIFICATIONS, reported |
| 10 | First publication review | PUBLICATION READY WITH QUALIFICATIONS, reported |
| 11 | Retail browser benign baselines | 10/10 checks; 42/42 across three repeat sessions, reported |
| 12 | Public and third-party Canvas claim review | 20 claims classified |
| 13 | Evidence quality audit | 13 claims; unsupported leak and JIT assertions withdrawn |
| 14 | Retail Canvas reentrancy behavioural witness | Two reported runs; no native UAF proof |
| 15 | Linux vulnerable WebKit + ASan | Reported heap-use-after-free at selected revision |
| 16 | Linux patched upstream comparison | Modified regression test 32/32 expected; no ASan report in that run |
| 17 | Sony 14.00 source and build preference audit | Missing post-conversion guard pattern; 14.22 binary mapping unknown |
| 18 | Retail 14.22 User's Guide capability tests | Seven checks received and saved over local HTTPS |
| 19 | Four-case Linux Canvas matrix | File created; **no test run submitted; stopped** |

## Strongest differentiated evidence

**Retail console observation**: benign 2D and BitmapRenderer APIs and dictionary getters were present in a tested firmware 14.22 User's Guide session. A separate repeated retail witness reported incompatible outer/inner Canvas creation in a reentrant scenario. Neither result is a native memory-safety proof.

**Upstream Linux reproduction**: ASan in a deliberately vulnerable WebKitGTK build reported a native heap-use-after-free; a patched comparison matched the targeted regression expectations. These observations concern Linux WebKit and have environment limitations.

**Sony public source**: the 14.00 source archive has the same candidate missing-guard/overwriting pattern in inspected Canvas paths. The publication does not authenticate that this source was compiled unchanged into firmware 14.22.

**Historic documentary record**: the Phase 1–10 analysis addressed firmware release history, published exploit support boundaries, Sony source-diff counts and a 14.10 package metadata discrepancy. The prior 15 November dossier should be understood as the **Phase 1–10 publication milestone**, not the final status of all later experiments.

## Evidence and provenance policy

These new documents are prepared from user-shared output and retained conversation notes. **They are summaries, not byte-for-byte uploads** of source ZIPs, Windows-local reports, Linux ASan logs, original test HTML files, scripts, firmware packages or PS5-generated evidence. Reported SHA-256 values are preserved to allow later integrity checks against those original local files, not because the files are contained here.

Do not publish private LAN configuration, temporary security-update-blocking DNS details, credentials, cookies, browser data, PSN account identifiers, copyrighted complete Sony source trees, native crash dumps with private state, or exploit payloads as part of this archive.

## Boundaries and final verdict

- **No confirmed PS5 firmware 14.22 native UAF**, arbitrary read/write or executable exploit chain.
- **No confirmed firmware downgrade** or complete jailbreak.
- No vendor-confirmed mapping of the source code studied to the specific PS5 14.22 retail binary.
- No independent external replication of the full local data or Phase 14/18 console observations.
- Phase 19 was **not executed**.

**Conclusion:** A substantial documented multi-phase research effort with source-level and instrumented-Linux findings, and bounded retail-browser behaviour observations. Research paused/closed **without a confirmed PS5 14.22 jailbreak**.

## Navigation

Historical phases 1–10: [Final research dossier](FINAL-RESEARCH-DOSSIER.md) · [existing evidence register](FINAL-EVIDENCE-REGISTER.csv)

Later phase reports: [11–14](PHASES-11-14-RETAIL-CLAIMS.md) · [15–16](PHASES-15-16-LINUX-ASAN.md) · [17](PHASE-17-SONY-SOURCE-AUDIT.md) · [18](PHASE-18-RETAIL-CAPABILITY-TESTS.md) · [19](PHASE-19-STOPPED.md) · [11–19 evidence register](PHASES-11-19-EVIDENCE-REGISTER.csv)
