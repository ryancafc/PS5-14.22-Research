# Phase 9 — Independent research integrity and evidence audit

**Outcome:** **PASS WITH QUALIFICATIONS**  
**Reported completed:** 15 November 2026  
**Scope:** Audit of the 42 deliverables from Phases 1–8, plus a publication-readiness assessment.

> **Evidence handling:** This page summarises the user's reported Phase 9 Codex audit. The original seven Windows-local reports, the raw source archives and the complete data inventories have **not** been uploaded to or independently examined through this GitHub repository. A successful local rerun improves reproducibility confidence but is not independent third-party replication.

## Audit results

| Metric | Reported audit result |
|---|---:|
| Expected earlier-phase deliverables | 42 |
| Present and SHA-256 fingerprinted | 42 |
| Byte-identical duplicate deliverables | 0 |
| ZIP members rehashed | 787,329 |
| WebKit added paths | 985 |
| WebKit removed paths | 2 |
| WebKit changed paths | 54 |
| WebKit unchanged paths | 393,117 |
| Final comparison discrepancies | 0 |
| Major claims reviewed | 14 |
| Claims confirmed | 6 |
| Confirmed claims reproduced computationally | 4 |

**Correction during audit:** The first reproduction attempt misclassified Sony's renamed distribution manifest. The corrected second run reportedly accounted for that rename and reproduced every published path-classification count with no discrepancies. The first failed result is an important audit trail and should remain documented, not silently omitted.

The firmware metadata audit reproduced the 14.10 catalogue checksum conflict and the duplicate recovery digest appearing in the wiki's standard-update entry. This does **not** establish authentic 14.10 package hashes from official file bytes; no retail package downloads or file-byte verification were carried out.

## High-impact conclusions

- **Confirmed / supported:** Both public Relapse implementation descriptions list firmware through 13.60; the Sony WebKit source groups differ; Sony's public release notes mention security changes for 14.10 and 14.22; the local file-comparison counts were reproducible.
- **Researcher-reported:** An archived Sonic_Iso statement attributes the S3-resume hypervisor fix to 14.10. An October 2026 press article claims 14.20, but does not demonstrate an independently verified first fixed build.
- **Unresolved:** Why Relapse lacks documented 14.00 support; which retail version first fixed the S3-resume vulnerability; which named vulnerabilities were addressed specifically in 14.22; exact public WebKit-source-to-retail-binary correspondence.

**Publication correction:** [Tom's Hardware's article](https://www.tomshardware.com/video-games/playstation/hacker-awarded-usd50k-bounty-for-reporting-bug-to-sony-that-allowed-ps5-linux-exploit-move-sparks-backlash-from-jailbreaking-community) by **Jowi Morales was published 27 October 2026**. It references the **21 October 2026** release of firmware 14.20. These dates must not be conflated. The publication date does not validate the article's patch attribution.

## Findings that still require qualification

- The 14-claim audit confirms six claims; it does not imply that the remaining eight were disproven. They must retain their own reported, hypothesised or unknown status as supported by the full local audit.
- Verification of local archive content and digests by Codex is distinguishable from independent researcher replication and from correspondence with Sony's shipped retail binaries.
- Multiple catalogue listings can reflect a common upstream source rather than independent checksum computation.
- The archive-source comparison does **not** demonstrate a complete security diff, a named exploit patch, or a working jailbreak for PS5 14.22.

## Local Phase 9 deliverables (not uploaded here)

1. `Phase9-Master-Evidence-Audit.md`
2. `Phase9-Source-Verification-Register.csv`
3. `Phase9-WebKit-Reproducibility-Audit.md`
4. `Phase9-Firmware-Metadata-Audit.md`
5. `Phase9-Contradictions-and-Corrections.md`
6. `Phase9-GitHub-Publication-Review.md`
7. `Phase9-Final-Readiness-Assessment.md`

## Publication readiness and next step

**PASS WITH QUALIFICATIONS** means the project may prepare a Phase 10 **draft**, with these conditions:

1. Keep first-hand, catalogued, computationally reproduced and still unverified claims separately labelled.
2. Correct the press-article date and superseded Phase 1–5 GitHub status summaries.
3. Preserve source provenance and discrepancies in the final report.
4. Do not publish claims of a retail 14.22 binary security diff or functional jailbreak.

Read the [current research status](RESEARCH-STATUS.md), [WebKit comparison](WEBKIT-COMPARISON.md), and [source register and open questions](SOURCES-AND-NEXT-STEPS.md).
