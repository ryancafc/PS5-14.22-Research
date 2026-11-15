# PS5 Firmware 14.22 — Jailbreak & Security Research

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

## Research update — 15 November 2026

**Phases 1–5 are complete (26 local research deliverables).** The project has documented historical public exploits, reviewed firmware notices, evaluated disputed patch claims, and reported a local hash-based comparison of Sony's published PS5 WebKit 13.x and 14.x source distributions.

- **WebKit source comparison (reported):** 985 added, 2 removed, 54 changed, and 393,117 unchanged source-relative paths. Both source distributions declare version `616.1.27.211.1`. These results do not establish specific retail 14.22 vulnerability fixes.
- **Relapse:** Both public implementations list supported builds only through 13.60; the technical reason support stops before 14.00 remains unconfirmed.
- **Byepervisor-Reborn:** A dated researcher attribution points to a hypervisor fix in 14.10, but the independently demonstrated first fixed retail build remains unknown.
- **14.22:** Sony's public notes mention security fixes without identifying affected components or CVEs.
- **Firmware 14.10 metadata:** Community indexes disagree about the standard-update SHA-256; apparent duplication of the recovery hash is a hypothesis, not yet byte-verified.

**Read the full research update:**

- [Research status and Phase 1–5 summary](docs/RESEARCH-STATUS.md)
- [WebKit 13.x vs 14.x source comparison](docs/WEBKIT-COMPARISON.md)
- [Firmware and public exploit evidence](docs/FIRMWARE-AND-EXPLOIT-EVIDENCE.md)
- [Research sources, checksum issue and Phases 6–10 roadmap](docs/SOURCES-AND-NEXT-STEPS.md)

*Evidence standard:* The GitHub summaries cite public sources and user-provided Codex phase reports; the original local archives and 336 MB inventory have not been independently audited or published here. **No PS5 14.22 jailbreak is demonstrated.**

---

## Latest research update — Phases 6–7 (15 November 2026)

**Seven research phases are now reported complete (36 local deliverables).** Phase 6 reproduced the Sony WebKit archive comparison and reported an integrity check of every changed/added/removed path. Phase 7 compared the 27 changed production-tree paths with sampled upstream WebKit revisions and public security advisories.

- **Phase 6:** Reproduced **985 added, 2 removed, 54 changed and 393,117 unchanged** paths. Its compact changed-only inventory has **1,041 rows**; all changed entries were rehashed against ZIP and extracted copies. Of 54 content-changed files, 27 are in production-source trees (18 JavaScriptCore, 8 WebCore, 1 PlayStation UI-process).
- **Phase 7:** **26/27** production-tree paths have upstream path counterparts, but **0** exact content matches were found at the sampled upstream revisions. The remaining `PlayStationWebView.cpp` is PlayStation integration code with an **unverified** runtime impact. No sampled advisory could be directly mapped to a changed Sony source file.
- **Still unknown:** The meaning of the Relapse 13.60 support ceiling, the precise components fixed in retail 14.22, and the exact source-to-retail build correspondence.

Read [Phase 6 validation](docs/PHASE-6-COMPARISON-VALIDATION.md) and [Phase 7 upstream correlation](docs/PHASE-7-UPSTREAM-CORRELATION.md).

*The numbers and file-level checks above are reported outcomes of the local Codex workflow; the source archives and detailed local CSVs are not included in this GitHub repository. No jailbreak or named security fix is established.*

---

## Current Research Status

**Target firmware:** 14.22

**Platform:** Sony PlayStation 5

**Project status:** Public-source comparison and advisory review completed through Phase 7

**Public jailbreak:** Not demonstrated by this project

| Research component | Status |
|---|---|
| Firmware 14.22 environment analysis | Planned |
| Browser and WebKit identification | Pending verification |
| Existing vulnerability compatibility | Under investigation |
| WebKit source code review | Scoped 13.x/14.x comparison and provenance review complete; retail impact unverified |
| Memory-safety research | Planned |
| Browser code execution | Not demonstrated |
| Kernel-level research | Preliminary |
| Working jailbreak | Not available |
| Public release | Not available |

Status descriptions will be updated only when supported by documented evidence.

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
