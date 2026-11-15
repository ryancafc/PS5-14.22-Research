# Research status — PS5 firmware 14.22

**Status as of 15 November 2026:** Phases 1–5 complete; Phase 6 planned. This is an independent, AI-assisted documentary and source-comparison project, **not a working jailbreak**.

> **Evidence note:** The five phases produced 26 local research deliverables. This public summary is based on the submitted phase reports and selected public sources checked independently. The original local reports, source archives, and 336 MB comparison inventory have **not** been uploaded to this repository. File counts and local extraction checks below are therefore reported results, not a separately audited reproduction.

## Executive summary

- Sony officially describes **security fixes** for **14.10** and **14.22**, but does not identify specific patched components or CVEs in its public PS5 release notes.
- The original and alternative **Relapse** implementations publicly document support through **13.60**. That ceiling does **not** itself establish that a particular vulnerability was fixed in 14.00.
- **Byepervisor-Reborn** lists **13.20** and **13.60** as fully supported, with **13.00** untested, and discusses hypothetical 14.00 applicability without a supported release. The S3-resume hypervisor issue has a researcher attribution to **14.10**, but the first fixed retail build has not been independently confirmed.
- Sony publishes separate PS5 WebKit source groups for **13.00–13.60** and **14.00 onward**. A local hash-based comparison reported **985 added**, **2 removed**, **54 changed**, and **393,117 unchanged** relative paths. The declared WebKit version remained **616.1.27.211.1**.
- Community indexes disagree on the **14.10 standard-update SHA-256**. The Developer Wiki appears to repeat the recovery package digest in both package rows, but the standard-update digest has not been checked against official bytes.
- The reviewed evidence does **not** demonstrate a complete publicly available 14.22 jailbreak or a complete retail 13.60-to-14.22 binary security diff.

## Phase history

| Phase | Scope | Status | Outcome |
|---|---|---|---|
| 1 | Historical exploits and official release history | Complete | Exploit timeline and preliminary firmware matrix |
| 2 | Patch attribution and Relapse/Byepervisor evidence | Complete | Narrowed claims about 14.10 and 14.20 |
| 3 | Independent evidence validation | Complete | Strengthened 14.10 attribution; preserved unknowns |
| 4 | Technical comparison feasibility | Complete | Identified WebKit source split and checksum conflict |
| 5 | WebKit source and package-metadata comparison | Complete | Reproducible local source inventories reported |
| 6 | Changed-source review | Planned | Classify the 54 content-changed files |
| 7 | Upstream WebKit/security advisory mapping | Planned | Check attributable upstream fixes |
| 8 | Firmware package identity verification | Planned | Resolve 14.10 digest discrepancy with authorised evidence |
| 9 | Independent evidence audit | Planned | Review reproducibility and contradictions |
| 10 | Final research assessment | Planned | Consolidated conclusions and limitations |

## Evidence status definitions

- **Confirmed:** A public primary source directly supports a specific, limited claim (for example, Sony's release note explicitly mentions security fixes).
- **Reported:** An attributable researcher or the project's local analysis reports a result, but independent verification is incomplete.
- **Hypothesis:** A plausible explanation that has not been demonstrated.
- **Unknown:** Evidence currently insufficient.

These are claim-level classifications. A report can be accurate about one capability without proving another.

## Current safety boundaries

Phases 1–5 were described as public-document and local-source analysis. No console access, exploit execution, payload deployment, retail firmware unpacking, or firmware change was performed as part of these research phases.

The project neither provides nor promises a firmware 14.22 jailbreak. It should not equate published source differences, unsupported firmware versions, or archive hashes with proven exploitability.

See [Firmware and exploit evidence](FIRMWARE-AND-EXPLOIT-EVIDENCE.md), [WebKit comparison](WEBKIT-COMPARISON.md), and [sources and next steps](SOURCES-AND-NEXT-STEPS.md).
