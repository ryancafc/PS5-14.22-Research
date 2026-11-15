# PS5 firmware 14.22 — final research dossier

**Publication synthesis, 15 November 2026**  
**Project:** Independent, AI-assisted PlayStation 5 firmware research  
**Review outcome:** **PUBLICATION READY WITH QUALIFICATIONS** (reported Phase 10 result)  
**Status:** All ten planned research phases reported complete. No complete 14.22 jailbreak demonstrated.

> **Provenance notice:** This is a GitHub publication synthesis assembled from the project's Phase 1–10 completion reports provided in conversation, the earlier GitHub research pages, and identifiable public sources. **It is not a byte-for-byte upload of the separately prepared, Windows-local Phase 10 dossier.** The original locally generated source archives, reports and CSV registers were not made available for direct inspection during this GitHub publication. The reproductions cited below are therefore **reported results of the local Codex workflow**, not independent reproduction by this publisher.

## Executive summary

The project systematically investigated what can be established about PS5 firmware **14.22** using publicly documented exploit history, firmware release information, source-level WebKit comparisons, upstream source provenance and package-metadata records.

The strongest reproducible contribution is a local, hash-based comparison of Sony's published **13.00–13.60** and **14.00 onward** WebKit source distributions. The initial result was subsequently checked by dedicated classification, provenance and audit phases. The local audit reported identical final counts after explicitly correcting a first-run manifest-renaming classification error.

**No public source in the reviewed set identifies the exact security fixes inside retail 14.22.** The public Relapse implementations stop listing supported firmware at 13.60, but their support lists do not prove that a particular flaw was patched in 14.00. The S3-resume hypervisor issue has an attributable researcher statement naming 14.10, while the first independently established fixed retail build remains unknown. A firmware 14.10 checksum conflict was narrowed to a likely standard-vs-recovery catalogue mistake without hashing authentic historical package bytes.

## 1. Objectives and scope

The research sought to:
- Establish accurately documented historical browser, kernel and hypervisor support boundaries.
- Characterise what Sony publicly discloses about 13.60, 14.00, 14.10, 14.20 and 14.22.
- Reproduce differences between Sony-published WebKit source distributions.
- Correlate source changes with publicly attributable upstream revisions and advisories, where possible.
- Assess the provenance and correctness of historical firmware package identity records.
- Audit methodology, sources, claims and reproducibility before publication.

**Excluded:** console penetration testing, retail firmware installation or downgrade, exploit or payload execution, retrofitting exploit chains, firmware package downloading/unpacking, and claims of a working 14.22 jailbreak.

## 2. Methods and evidence standard

The local project used public original-source research, pinned repository revisions, revision-index comparison, deterministic content hashing, CSV path inventories, cross-catalogue metadata review, and a final evidence audit.

A claim's source must be distinguished from its **verification status**:
- **Confirmed from primary public source:** an identifiable original document directly says the narrow thing claimed.
- **Reproduced in the local research:** the Codex audit reported repeating the computation against retained inputs. Those original inputs are not independently hosted here.
- **Corroborated catalogue claim:** multiple public indexes agree; they may share an upstream data source.
- **Researcher-reported:** a dated, attributable statement without a directly demonstrated retail build comparison.
- **Hypothesis / unknown:** plausible explanation or insufficient evidence.

The local Phase 9 audit reportedly reviewed **14 major claims**, confirming **six**, including **four computationally reproduced**. The precise item-by-item classifications of that *original* 14-claim register are not available to this publication synthesis; the [public evidence register](FINAL-EVIDENCE-REGISTER.csv) is a **new summarising register**, not a claimed copy of those 14 entries.

## 3. Security architecture context

PS5 security cannot be reduced to a single browser vulnerability:
1. A **browser/userland entry point** may provide application-context execution without kernel privileges.
2. The **GameOS kernel** imposes a separate privilege boundary.
3. The **hypervisor** imposes another boundary and may depend on prior kernel compromise for published research techniques.
4. An end-user **jailbreak/homebrew environment** additionally requires implementation, compatibility and reliability evidence.

Documentation of one boundary's weakness does not prove that all later boundaries can be crossed on 14.22.

## 4. Historical Relapse findings

Two public implementations document support through **13.60**:
- [Relapse original](https://github.com/ntfargo/Relapse-Exploit), [pinned README](https://github.com/ntfargo/Relapse-Exploit/blob/dd8e4e0914c5e9d066ee1f9b056be76cb992c8e0/README.md)
- [Relapse alternative](https://github.com/soniciso1/relapse), [pinned README](https://github.com/soniciso1/relapse/blob/112dbe5949e9c3de923bb0909289c58a9c082151/README.md)

The alternative README enumerates individual versions and some gaps. [Issue #3](https://github.com/soniciso1/relapse/issues/3) requests a 14.00 release, rather than documenting a specific technical incompatibility.

**Conclusion:** **Published implementation support ends at 13.60.** A specific patch boundary, underlying vulnerable component, or reason for the absent 14.00 release remains **unknown**.

## 5. Hypervisor S3-resume attribution

[Byepervisor-Reborn](https://github.com/PS5Dev/Byepervisor-Reborn) is a developer-oriented hypervisor research base with published support for 13.20/13.60 (13.00 marked untested in its README), not a complete generic end-user jailbreak.

An [original technical write-up](https://github.com/soniciso1/ps5-hv-writeups/blob/e4d8b98390754d7eba7c4ea307a168a7d2e9962d/s3-resume-startup_mp-ap-launch.md) describes a historical S3-resume/AP-startup isolation issue. An [archived Sonic_Iso statement dated 12 October 2026](https://teapawt.net/Sonic_Iso/status/2109626943213638032) attributes the fix to **14.10**. The original social post was not available in the research view; the statement is evidence of attribution via an archival mirror.

A [Tom's Hardware article by Jowi Morales published **27 October 2026**](https://www.tomshardware.com/video-games/playstation/hacker-awarded-usd50k-bounty-for-reporting-bug-to-sony-that-allowed-ps5-linux-exploit-move-sparks-backlash-from-jailbreaking-community) refers to a **21 October 2026** 14.20 firmware release and associates the fix with 14.20. These dates and attributions must not be conflated.

**Conclusion:** 14.10 is the stronger **researcher-reported attribution**; a first fixed retail build has **not** been independently established from version-specific tests or vendor advisories.

## 6. Sony's firmware disclosures

[Sony's public UK system-software notes](https://www.playstation.com/en-gb/support/hardware/ps5/system-software-info/) describe security fixes for 14.10 and 14.22 but do not identify a specific affected component or CVE in these general notes. The absence of a named fix in a brief changelog is not evidence that no fixes were shipped.

**Conclusion:** a claimed complete retail 13.60-to-14.22 security diff, or a particular vulnerability first fixed by 14.22, is **not supported** by the reviewed public record.

## 7. Sony WebKit source distribution comparison

Sony's [PS5 WebKit source catalogue](https://www.playstation.com/en-us/oss/ps5/webkit/) provides separate distributions for **13.00–13.60** and **14.00 onward**. Both locally examined archives reportedly declared WebKit **`616.1.27.211.1`**.

The hash-based comparison was reported as follows:

| Classification | Relative paths |
|---|---:|
| Added in 14.x source group | 985 |
| Removed from 14.x source group | 2 |
| Present in both, content changed | 54 |
| Present in both, content unchanged | 393,117 |
| **Union of relative paths** | **394,158** |

The Phase 6 checks reportedly rehashed every added, removed and changed path against original ZIP contents and extracted copies, identifying no duplicate paths, case collisions, missing or extra extraction output. The local Phase 9 audit reportedly rehashed **787,329 ZIP members** and reproduced all four counts.

**Audit correction:** The first Phase 9 audit run misclassified a renamed Sony manifest. Its corrected run accounted for that rename and reported **zero remaining classification discrepancies**. The initial error and its correction remain part of the published audit history, not a hidden failure.

Of **54 changed paths**, **27** were classified as production-tree source: **18 JavaScriptCore**, **8 WebCore**, and **1 PlayStation WebKit UI-process file**. The remaining **27** were build/tooling configuration, tests, fixtures, or manifest material. File location alone does not demonstrate changed runtime semantics or compiled retail behaviour.

**Conclusion:** The two published source distributions differ even though their declared version number is equal. This does **not** establish a named exploit fix or the exact WebKit binary in retail 14.22.

## 8. Upstream provenance and public advisories

The local Phase 7 investigation compared the 27 changed production-tree source files with selected pinned upstream WebKit revisions:
- **26 of 27** had an upstream **path counterpart**.
- **None** had an exact byte-content match to either Sony copy at the **sampled upstream revisions**.
- The remaining `PlayStationWebView.cpp` was identifiable as PlayStation UI integration, with unverified change purpose and runtime effect.
- **No sampled public advisory** was directly linked to a verified Sony source change.

A shared path suggests component ancestry, not the precise origin of a change. Zero matches in selected upstream snapshots is **not** an exhaustive historical search. An upstream CVE is not automatically a confirmed fix in a specified PS5 firmware.

Useful public reference sources: [WebKit upstream](https://github.com/WebKit/WebKit), [WebKit security policy](https://webkit.org/security-policy/), [WebKit bugs](https://bugs.webkit.org/) and [Apple security releases](https://support.apple.com/en-us/100100).

## 9. Historical 14.10 firmware package metadata

For build `26.06-14.10.00.03-00.00.00.0.1` the [pinned MewX catalogue](https://github.com/MewX/ps5-official-firmware-list/blob/6f4bc337885d51280529b729fed69ae11754066a/README.md) reports:

| Class | Reported SHA-256 | Reported bytes |
|---|---|---:|
| Standard update | `c17384946df6e5c85b2d72cbeee2057b165bf90279d9e2a86d527d0778cdaaf6` | 1,261,408,256 |
| Recovery | `9f3a0b8811c00ab52b092d2e9f0f13dd4515f018361ff38e4be43fd8c18b21de` | 1,418,890,240 |

The [Midnight archive's public firmware index](https://archive.midnightchannel.net/SonyPS/Firmware/index.php/info/info/?cat=ps5sys&legacy=1) was reported to agree with the package-class split. The [PS5 Developer Wiki index](https://www.psdevwiki.com/ps5/Official_Firmware) appeared to repeat the recovery digest for both classes.

The local Phase 8/9 audits reportedly examined **30 metadata records across ten build/package-class groups**, finding one conflicting digest group and one cross-class duplicate, both involving 14.10.

**Conclusion:** A wiki transcription/copy error is the leading **hypothesis**. Agreement between two catalogues does not prove independent acquisition and hashing of authentic historical PUP bytes, which were not obtained or verified.

## 10. Integrity and audit outcome

Phase 9 reported:
- **42** previous-phase deliverables present and SHA-256 fingerprinted, with no byte-identical duplicates.
- Full WebKit ZIP rehashing of **787,329** archive members.
- Corrected, zero-discrepancy file classifications.
- **6 of 14** claims confirmed, **4** of those by computational reproduction.
- Overall verdict: **PASS WITH QUALIFICATIONS**.

Phase 10 reported:
- Full review and reconciliation of Phase 9's 14 claim classifications.
- Original inventories rechecked for central counts.
- **53** prior top-level file fingerprints and both extraction-tree file counts preserved.
- Overall verdict: **PUBLICATION READY WITH QUALIFICATIONS**.

These are **reported self-audit results**. They must not be described as replication performed by an independent third party.

## 11. Limitations and alternative explanations

The published Sony WebKit source catalogue is not an authenticated version-to-retail-binary map. Unchanged version strings do not guarantee identical sources or binaries. Change classifications do not prove patch intent. A repository README's support limit does not prove that an underlying bug was fixed. A press report does not determine the first fixed retail firmware. Community indexes can share original data and duplicate mistakes. This GitHub synthesis does not itself contain the input archives and original local phase outputs.

A 14.22 jailbreak has not been demonstrated by this project. The report cannot determine that no undisclosed vulnerability exists.

## 12. Final conclusions and recommended follow-up

**What this project establishes best:** an extensively validated local *published-source* comparison, a bounded upstream provenance assessment, a traceable package-catalogue conflict, and a documented audit trail.

**What remains unresolved:** the Relapse support-boundary mechanism; the first fixed S3-resume build; named fixes in 14.22; exact retail source-to-binary mapping; and byte-verified historical 14.10 package digests.

Further work is valuable only with new original documentation, independently reviewable local comparison artefacts, vendor disclosures, or separately authorised authentic package-byte verification. Repeating the same public searches would not by itself close these gaps.

**Overall publication verdict: PUBLICATION READY WITH QUALIFICATIONS.** This is an evidence-driven historical security research report, **not an exploit release**.

## Companion material and citations

- [Executive summary](EXECUTIVE-SUMMARY.md)
- [Public-facing evidence register](FINAL-EVIDENCE-REGISTER.csv)
- [Reproducibility and integrity](REPRODUCIBILITY-AND-INTEGRITY.md)
- [Outstanding questions](UNRESOLVED-QUESTIONS.md)
- [Research status and phase history](RESEARCH-STATUS.md)
- [Earlier public reports](WEBKIT-COMPARISON.md), [Phase 6](PHASE-6-COMPARISON-VALIDATION.md), [Phase 7](PHASE-7-UPSTREAM-CORRELATION.md), [Phase 8](PHASE-8-FIRMWARE-METADATA.md), and [Phase 9](PHASE-9-INDEPENDENT-AUDIT.md)

This synthesis was prepared for public release from the available research summaries; it does **not replace or claim to be identical to** the user's eight original Windows-local Phase 10 files.
