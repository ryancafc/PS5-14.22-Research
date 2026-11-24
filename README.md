# PS5 Firmware 14.22 — Security Research

**Independent PlayStation 5 firmware 14.22 security research, vulnerability analysis, WebKit investigation and AI-assisted development.**

---

## About the Project

Welcome to **PS5 14.22 Jailbreak Research**, an open-source research initiative dedicated to investigating the security architecture, vulnerabilities and potential homebrew capabilities of PlayStation 5 system software version **14.22**.

Our goal is to bring together developers, security researchers and AI-assisted research workflows to better understand the technical challenges involved in PS5 security research.

The project focuses on:

- WebKit browser security and memory safety
- Public vulnerability and CVE analysis
- PS5 firmware architecture
- Browser functionality and security restrictions
- Research into existing publicly documented exploits
- AI-assisted source code analysis
- Reproducible security testing
- Documentation and collaboration

**This is an experimental research project, not a released jailbreak.**

## Historical research — 19 November 2026 (Phases 1–19)

**Status: Research resumed. No PS5 firmware 14.22 jailbreak or native UAF on retail PS5 has been demonstrated.**

The **15 November publication below is the historical Phase 1–10 milestone**, not the final project state. Further work through **Phases 11–18** covered benign console browser checks, evidence review, Sony WebKit source, an instrumented Linux upstream heap-use-after-free comparison, and successful retail User's Guide diagnostics. **Phase 19 was prepared but not run.**

- **[Project closeout and full phase index](docs/PROJECT-CLOSEOUT-2026-11-19.md)** — phases 1–19, status, provenance, limits.
- **[Phases 11–14: retail baselines, claims and Canvas witness](docs/PHASES-11-14-RETAIL-CLAIMS.md)** — 10/10 and 42/42 benign checks; 20/13-claim reviews; two reported reentrancy witnesses.
- **[Phases 15–16: controlled Linux AddressSanitizer research](docs/PHASES-15-16-LINUX-ASAN.md)** — upstream vulnerable-build UAF report and patched-build comparison; **not** a PS5 UAF.
- **[Phase 17: Sony published WebKit 14.00 audit](docs/PHASE-17-SONY-SOURCE-AUDIT.md)** — missing post-conversion guard pattern and source-feature defaults; no 14.22 binary mapping.
- **[Phase 18: retail PS5 capability observations](docs/PHASE-18-RETAIL-CAPABILITY-TESTS.md)** — seven observed tests received through a local HTTPS User's Guide page.
- **[Phase 19: planned test, stopped](docs/PHASE-19-STOPPED.md)** — test HTML created and hashed; no recorded MiniBrowser results.
- **[Evidence register for Phases 11–19](docs/PHASES-11-19-EVIDENCE-REGISTER.csv)** — each claim's verification class and limitation.

All new entries are **documentation syntheses of user-supplied reports**, not uploads of the original source archives, ASan logs, raw test programs or console binaries. These historical records remain available for reproducibility; current research is active.

---

## Phase 21 technical validation — 24 November 2026

**Overall PARTIAL; jailbreak possibility remains UNKNOWN.** New standard 14.20 and recovery 14.22 downloads match published size/SHA-256/MD5 on official Sony HTTPS delivery. The existing standard 14.22 file remains unchanged. Historical 14.10's checked official object returns HTTP 200 with zero content; no substitute was used.

- Independent 14.20→14.22 comparison reproduces **115 differing bytes in [0,0x440)**, +4,096 outer bytes, +4,128 inner-entry bytes and 32 fewer padding bytes. The inner 16-byte prefix is unchanged.
- Recovery contains two entries; its first matches standard 14.22's inner entry by complete SHA-256. No protected executable content was decoded.
- Original read-only firmware comparison utility: **27/27 synthetic tests pass**, with streaming hashes, validated bounds, scoped windows and JSON/CSV output.
- Fresh Ghidra regression again applies **567/567** relocations for the compatible sample. New ABI 2 /ET_DYN homebrew correctly selects generic ELF and applies **20/20** relocations. FreeBSD-object/System V controls are also correctly rejected by Prospero. Additional eligible SCE/ABI 3 coverage remains incomplete.
- Original bounded diagnostics pass **21 checks in Chromium and Firefox under two header modes: 84 normal results**. Deliberate wrong/missing header controls produce FAIL/SKIP and are counted separately. No console or stress tests ran.

Read the [Phase 21 final report](phase-21/PHASE-21-FINAL-REPORT.md), [firmware comparison](phase-21/FIRMWARE-COMPARISON.md), [Ghidra regression](phase-21/GHIDRA-REGRESSION-REPORT.md), [browser report](phase-21/BROWSER-DIAGNOSTICS-REPORT.md) and [evidence register](phase-21/EVIDENCE-REGISTER.csv). Phases 1–20 remain preserved. This update is stacked on the still-pending Phase 20 publication; it does not imply a merge into main.

---

## Phase 20 external audit — 24 November 2026

**Audit completed with qualifications. Jailbreak possibility remains UNKNOWN.**

The audit reviewed the incorporated external repositories at pinned commits: **54 claims**, comprising **11 independently verified**, **4 reproduced on desktop Chromium**, **13 unverified** and **6 contradicted**. The remaining claims are source-supported, author-reported, simulation-only or blocked. These are claim counts, not independent hardware experiments.

- Existing 14.22 package hashes, SLB2 entry boundaries and **387 zero padding bytes** were independently checked without altering or decrypting firmware.
- The browser diagnostic's non-shared Atomics expectation was corrected: nine ordinary operations succeed normally, but the original page labels each as an anomaly. Expected sandbox isolation is also mislabelled.
- Static accounting found that the nominal 320 MB slow chain can retain **905 MiB**; pressure modes were not executed.
- Mock/TCP success, older kernel results and public source defaults do not establish retail 14.22 exploitability. No exploit chain, trigger payload or console test was run.
- Earlier homebrew Ghidra evidence was reviewed; fresh metadata decoding confirms the library names and relocation types. This is not a new retail firmware analysis or a rerun of the complete Ghidra workflow.

Read the [Phase 20 final report](phase-20/PHASE-20-FINAL-REPORT.md), [evidence register](phase-20/EVIDENCE-REGISTER.csv), [browser review](phase-20/BROWSER-DIAGNOSTICS-REVIEW.md) and [limitations](phase-20/LIMITATIONS.md). Historical Phases 1–19 remain unchanged. Published evidence excludes firmware/game/system binaries, private keys and executable exploitation tools.

---

## Latest research — 24 November 2026

Research has resumed with a Kali Linux static-analysis environment. The maintainer reports the following milestones from local Codex-assisted work; independent replication is welcome.

| Milestone | Reported result |
|---|---|
| Analysis environment | Ghidra 12.2, Java 25.0.5, Gradle 9.2.1 verified |
| Standard ELF test | Linux sample imported, disassembled and decompiled |
| GhidraProspero | Loader registration verified; dynamic-table parsing defect repaired with backup |
| Compatible public PS5 sample | 165 imports across six libraries; 567/567 relocations applied |
| elfldr v0.28 | Entry point recovered, source-backed annotations added, 123 initialized function bodies decompiled |
| Firmware container | Official 14.22 SLB2 structure and extraction identity checked; original and extracted SHA-256 hashes preserved |
| Evidence preservation | Six local notes, repair artifacts, backups and annotated project snapshot saved; snapshot reopened successfully |

The original ABI-0 homebrew ELF was not a valid test of the specialized Prospero loader. A separate compatible public sample was used for validation. Protected firmware 14.22 executable code remains unanalysed. No working jailbreak has been demonstrated. Phase 20 reviews the saved local evidence and independently rechecks selected metadata. It does not claim independent human replication; the full earlier local bundle remains outside this publication.

### External references incorporated locally

- [ccclosed/ps5-1422-research](https://github.com/ccclosed/ps5-1422-research) — third-party firmware-container research; claims require independent validation.
- [karter-captain/ps5-14.22-browser-probes](https://github.com/karter-captain/ps5-14.22-browser-probes) — browser diagnostics reference, not proof of exploitation.
- [GhidraProspero](https://github.com/shadps5-emu/GhidraProspero) and [elfldr](https://github.com/ps5-payload-dev/elfldr) — upstream analysis references.

### Research status tracking

See [jailbreak possibility status](exploits/jailbreak-possibility-percentage.txt). No numerical probability can be justified by current evidence; commit activity is not a measure of exploitability.

---

## Research publication — 15 November 2026

**All 10 planned phases are reported complete — 57 Windows-local research deliverables.** The reported Phase 9 review concluded **PASS WITH QUALIFICATIONS**; Phase 10 concluded **PUBLICATION READY WITH QUALIFICATIONS**.

**Main findings**

- The [published Sony WebKit 13.x and 14.x source groups](https://www.playstation.com/en-us/oss/ps5/webkit/) differ by **985 added, 2 removed, 54 content-changed and 393,117 unchanged paths** in the local hash-based comparison. The corrected Phase 9 audit reported **787,329 ZIP members rehashed** and zero final classification discrepancies.
- Of the 54 changed files, **27** are in production-source trees; **26 of those 27** have upstream path counterparts, but **none** matched exactly at the sampled upstream revisions. No public advisory in the reviewed sample was directly linked to a verified Sony change.
- The public [Relapse implementations](https://github.com/ntfargo/Relapse-Exploit) list support through **13.60**. The reason they do not document support for 14.00 remains **unknown**.
- A dated [researcher attribution](https://teapawt.net/Sonic_Iso/status/2109626943213638032) associates an S3-resume hypervisor fix with **14.10**; the first fixed retail build is **unverified**. Later [press reporting published 27 October 2026](https://www.tomshardware.com/video-games/playstation/hacker-awarded-usd50k-bounty-for-reporting-bug-to-sony-that-allowed-ps5-linux-exploit-move-sparks-backlash-from-jailbreaking-community) cites 14.20 but does not supply an independent first-fixed-build demonstration.
- The [MewX firmware index](https://github.com/MewX/ps5-official-firmware-list) and a reported Midnight archive record distinguish 14.10 standard-update and recovery digests. A repeated recovery digest in the PS5 Developer Wiki's standard update row is the **leading metadata-error hypothesis**; authentic package bytes have not been hashed.
- Sony [announces security fixes in 14.22](https://www.playstation.com/en-gb/support/hardware/ps5/system-software-info/) without identifying the exact vulnerabilities in its general public notes. **This project has not demonstrated a 14.22 jailbreak**.

### Read the completed public research publication

| Publication document | Description |
|---|---|
| [Final research dossier](docs/FINAL-RESEARCH-DOSSIER.md) | Consolidated findings, sources, uncertainties and final conclusions |
| [Executive summary](docs/EXECUTIVE-SUMMARY.md) | Concise project findings |
| [Public evidence register](docs/FINAL-EVIDENCE-REGISTER.csv) | Claim-by-claim source, classification and limitation register |
| [Reproducibility & integrity](docs/REPRODUCIBILITY-AND-INTEGRITY.md) | Source archive and checksum methodology, audit history |
| [Unresolved questions](docs/UNRESOLVED-QUESTIONS.md) | Research gaps and material needed to resolve them |
| [Research status](docs/RESEARCH-STATUS.md) | Ten-phase history and published notes |
| [Publication manifest](docs/PUBLICATION-MANIFEST.md) | Published file inventory and provenance limits |

**Publication provenance:** The documents linked above are **GitHub publication syntheses**, not direct uploads of the eight original Windows-local Phase 10 files. The original local ZIPs, full 336 MB file inventory, detailed CSVs and all 57 local phase reports are not in this repository. File-comparison and audit metrics are described as *results reported by the Codex local workflow*, not independent third-party replication.

**Research limitations:** No retail firmware download, console access, exploit execution or payload deployment occurred in the reported phases. A source-difference finding does **not** prove a named fix or working jailbreak in retail firmware 14.22.

---

## Current Research Status

| Research component | Status |
|---|---|
| Ghidra and GhidraProspero | Validated on public samples (maintainer report) |
| 14.22 PUP container | Hashes and extraction verified (maintainer report) |
| Protected 14.22 executable code | Not analysed |
| Historical public exploit research | Documented with pinned source references |
| Firmware release and patch attribution | Documented; key fix boundaries unresolved |
| Sony 13.x vs 14.x WebKit source comparison | Locally reproduced and audited (reported) |
| Changed-source classification | Completed |
| Upstream WebKit provenance | Bounded sampling completed; exact change origins unverified |
| 14.10 package metadata discrepancy | Corroborated catalogue conflict; original bytes unverified |
| Phase 9 independent evidence audit | PASS WITH QUALIFICATIONS (reported) |
| Phase 10 final research draft | PUBLICATION READY WITH QUALIFICATIONS (reported) |
| Complete 14.22 jailbreak | **Not demonstrated** |

## Research Objectives

### 1. Understand Firmware 14.22

Investigate the firmware's publicly observable characteristics, supported browser features and differences from previously researched versions.

Document findings and identify areas requiring further investigation.

### 2. Analyse Existing Security Research

Review publicly available PS5 security research, including findings associated with previous firmware versions.

Research topics include:

- Use-after-free vulnerabilities
- Memory corruption
- WebKit security fixes
- Browser sandboxing
- Runtime memory protections
- Exploit mitigations
- Firmware-specific differences

Findings from other firmware versions must be independently validated before being described as applicable to 14.22.

### 3. AI-Assisted Security Research

Use AI models as research assistants for:

- Reading and explaining complex source code
- Reviewing technical documentation
- Identifying inconsistencies in existing research
- Comparing public vulnerability reports
- Developing safe experimental test plans
- Analysing crash reports
- Producing reproducible technical reports

AI-generated conclusions are **not considered verified evidence** without independent review.

### 4. Develop a Public Research Knowledge Base

Maintain accessible documentation for researchers interested in PS5 firmware security.

The repository aims to record successful experiments, unsuccessful experiments, technical limitations and open questions.

Sharing failed experiments is important because it prevents researchers from repeatedly investigating the same unsuccessful approaches.

## Existing Research

This initiative draws inspiration from earlier PlayStation 5 security research, particularly:

**[PS5 14.20 Jailbreak Research — devravik](https://github.com/devravik/PS5-14.20-Jailbreak-Research)**

The referenced project documents experiments involving WebKit, browser memory safety and CVE-2026-43720.

However, these reports concern firmware 14.20.

**Results documented for 14.20 must not be assumed to work on 14.22.**

Any adapted code, research or documentation should be appropriately attributed and used in accordance with its original licence.

## Research Methodology

Our research follows five stages.

### Stage 1 — Reconnaissance

Document the target firmware, browser environment and publicly observable system characteristics.

### Stage 2 — Source Analysis

Compare available source code, vulnerability advisories and previous security research.

### Stage 3 — Hypothesis Development

Form research questions supported by technical evidence rather than speculation.

### Stage 4 — Controlled Validation

Conduct authorised, non-destructive tests in appropriate environments, recording results and limitations.

### Stage 5 — Documentation and Review

Publish findings with reproducible evidence and clearly distinguish observations from interpretations.

## Proposed Repository Structure

The following directory structure is planned and may change as the project develops.

| Directory | Purpose |
|---|---|
| `docs/` | Technical documentation and research notes |
| `research/` | Investigations, hypotheses and findings |
| `cve-analysis/` | Public vulnerability reviews |
| `webkit/` | Browser research and source analysis |
| `tests/` | Safe, reproducible test cases |
| `results/` | Experiment results and logs |
| `tools/` | Research and analysis utilities |
| `ai-research/` | AI-assisted reviews and verification |
| `references/` | External sources and acknowledgements |

Directories will be added when corresponding research or tools are available.

## Research Verification Standards

All major findings should include:

1. The firmware version tested.
2. A clear description of the experiment.
3. The expected and observed results.
4. Relevant logs or other supporting evidence.
5. Reproduction conditions.
6. Known limitations.
7. Independent confirmation, where available.

Findings will use these status labels:

| Status | Meaning |
|---|---|
| Proposed | Hypothesis awaiting testing |
| Investigating | Research or testing in progress |
| Observed | Behaviour recorded in an experiment |
| Reproduced | Result repeated under documented conditions |
| Independently verified | Confirmed by a separate researcher |
| Inconclusive | Insufficient evidence |
| Blocked | Progress prevented by a documented limitation |
| Disproven | Evidence contradicts the hypothesis |

**AI-generated explanations, hypotheses and code do not automatically qualify as confirmed findings.**

## How to Contribute

Contributions from researchers, developers and interested community members are welcome.

You can contribute by:

- Reviewing public vulnerability reports
- Correcting inaccurate documentation
- Sharing reproducible research findings
- Identifying missing references
- Providing safe proof-of-concept tests in isolated environments
- Reviewing AI-generated technical analysis
- Improving research tools and documentation

Before opening a pull request, provide a clear description of your changes and any supporting evidence.

Avoid submitting unverified claims or reporting a complete jailbreak without independently reproducible proof.

## Responsible Security Research

This project is intended for educational, defensive and authorised security research.

Research must be conducted only on systems you own or have permission to test.

Contributors should:

- Respect applicable laws and security research guidelines.
- Avoid testing against other people's devices or services without permission.
- Avoid publishing private keys, credentials or personal information.
- Clearly disclose experimental risks.
- Follow responsible vulnerability disclosure practices.
- Avoid presenting unstable code as safe for public use.

Research software may cause browser crashes, application instability or data loss. Experimental work should not be performed on valuable devices without understanding the risks.

## Frequently Asked Questions

### Is there a working PS5 14.22 jailbreak in this repository?

No. This repository does not currently provide or claim to demonstrate a working 14.22 jailbreak.

### Can firmware 14.22 be downgraded to 13.60?

This project does not provide a verified downgrade procedure. Research into firmware vulnerabilities should not be confused with a working downgrade method.

### Can AI discover a new PS5 vulnerability?

AI can assist researchers by reviewing code, finding inconsistencies and generating hypotheses. However, practical discoveries require appropriate testing and independent verification.

### Will this project release a jailbreak?

There is no confirmed release schedule. A public jailbreak cannot be promised as a result of this research.

### Can beginners contribute?

Yes. Documentation, source verification, testing methodology and technical writing can all benefit from community contributions.

## Disclaimer

This project is not affiliated with, endorsed by or sponsored by Sony Interactive Entertainment.

PlayStation and PS5 are trademarks of their respective owners.

All research is provided for educational and informational purposes.

The authors and contributors make no guarantee that any vulnerability is exploitable, that a jailbreak will be developed or that experimental software will function safely.

**Research first. Verify everything. Document the results.**

---

**PS5 Firmware 14.22 — Security Research Initiative**

*Independent research. Open collaboration. Evidence-driven development.*
