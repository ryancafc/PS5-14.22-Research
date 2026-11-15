# Executive summary — PS5 firmware 14.22 security research

**Research completed:** 15 November 2026  
**Ten phases:** reported complete  
**Conclusion:** **PUBLICATION READY WITH QUALIFICATIONS**  
**Product status:** No complete 14.22 jailbreak demonstrated.

> This is a **public-facing synthesis** of reported Phase 1–10 results and selected primary-source links, not the original Windows-local Phase 10 executive-summary document.

## What was investigated

The project reviewed published PS5 security research (Relapse, Byepervisor-Reborn), Sony firmware changelogs, published Sony WebKit source archives, upstream WebKit history and advisories, and historical firmware package metadata. Dedicated follow-up phases reproduced source-comparison counts and audited evidence classifications.

## Five key findings

1. **Published exploit support is not a patch boundary.** The two Relapse implementations advertise firmware support through **13.60**. Why their documented support stops before 14.00 remains unknown. [Original Relapse](https://github.com/ntfargo/Relapse-Exploit) · [alternative implementation](https://github.com/soniciso1/relapse).
2. **Hypervisor fix attribution is disputed.** An [archived Sonic_Iso statement](https://teapawt.net/Sonic_Iso/status/2109626943213638032) attributes the S3-resume fix to **14.10**, while [press coverage published 27 October 2026](https://www.tomshardware.com/video-games/playstation/hacker-awarded-usd50k-bounty-for-reporting-bug-to-sony-that-allowed-ps5-linux-exploit-move-sparks-backlash-from-jailbreaking-community) discusses **14.20**. The *first fixed retail build* is unverified.
3. **WebKit source distributions measurably differ.** The reported local comparison of Sony's [13.x and 14.x published source groups](https://www.playstation.com/en-us/oss/ps5/webkit/) produced **985 added, 2 removed, 54 changed, 393,117 unchanged** relative paths, despite the same declared `616.1.27.211.1` version. The corrected local audit reported **787,329 ZIP members rehashed** and zero final classification discrepancies. These are *source-distribution* findings, not a retail 14.22 binary diff.
4. **Upstream provenance remained bounded.** For **27** changed production-tree files, **26** had upstream path counterparts; none matched exactly at the sampled pinned revisions. No sampled public advisory was demonstrably linked to a particular Sony source change.
5. **14.10 checksum conflict is likely a metadata error.** The [MewX index](https://github.com/MewX/ps5-official-firmware-list/blob/6f4bc337885d51280529b729fed69ae11754066a/README.md) and reported Midnight entries distinguish standard and recovery hashes. The [Developer Wiki](https://www.psdevwiki.com/ps5/Official_Firmware) appears to duplicate the recovery digest. Authentic historical package bytes have not been hashed.

## Central unresolved questions

Sony's [general release notes](https://www.playstation.com/en-gb/support/hardware/ps5/system-software-info/) confirm security fixes for **14.22** without naming specific fixes. The precise fixes, source-to-retail mapping, Relapse support-gap mechanism, first fixed hypervisor build and byte-authenticated 14.10 package checksums are all unresolved.

## Audit and publication basis

Phase 9 reportedly fingerprinted all **42** earlier deliverables and confirmed **six of fourteen** audited claims (four computationally reproduced). Phase 10 reported rechecking **53** prior top-level file fingerprints and returning **PUBLICATION READY WITH QUALIFICATIONS**.

This repository hosts summaries but not the original large local archives, 336 MB inventory, full working CSVs or source-level input files. It therefore does not independently reproduce the local computational analysis.

**Read the [final dossier](FINAL-RESEARCH-DOSSIER.md), [evidence register](FINAL-EVIDENCE-REGISTER.csv), [reproducibility report](REPRODUCIBILITY-AND-INTEGRITY.md), and [open questions](UNRESOLVED-QUESTIONS.md).**
