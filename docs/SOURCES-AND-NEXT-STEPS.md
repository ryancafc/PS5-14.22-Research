# Research sources, outstanding questions and next steps

**Checked/reported through:** 15 November 2026.

## Primary sources

| Source | Reason to consult |
|---|---|
| [Sony PS5 release notes](https://www.playstation.com/en-gb/support/hardware/ps5/system-software-info/) | Officially described firmware changes |
| [Sony PS5 WebKit source catalogue](https://www.playstation.com/en-us/oss/ps5/webkit/) | Published 13.x and 14.x source groups |
| [Relapse original](https://github.com/ntfargo/Relapse-Exploit) | Original implementation support range |
| [Relapse alternative](https://github.com/soniciso1/relapse) | Individual firmware build list |
| [Byepervisor-Reborn](https://github.com/PS5Dev/Byepervisor-Reborn) | Developer-oriented hypervisor research and support |
| [S3-resume write-up](https://github.com/soniciso1/ps5-hv-writeups/blob/e4d8b98390754d7eba7c4ea307a168a7d2e9962d/s3-resume-startup_mp-ap-launch.md) | Primary technical description |
| [Sonic_Iso archived statement](https://teapawt.net/Sonic_Iso/status/2109626943213638032) | Dated 14.10 researcher attribution |

## Community indexes and secondary reporting

- [PS5 Developer Wiki firmware index](https://www.psdevwiki.com/ps5/Official_Firmware), including [pinned old revision](https://www.psdevwiki.com/ps5/index.php?title=System_Software&oldid=4828)
- [MewX firmware list](https://github.com/MewX/ps5-official-firmware-list/blob/6f4bc337885d51280529b729fed69ae11754066a/README.md)
- [PS5 Developer Wiki vulnerability overview](https://www.psdevwiki.com/ps5/Vulnerabilities)
- [PSXHAX](https://www.psxhax.com/) — discovery/secondary reporting only; reported inaccessible in Phase 1
- [Tom's Hardware discussion](https://www.tomshardware.com/video-games/playstation/hacker-awarded-usd50k-bounty-for-reporting-bug-to-sony-that-allowed-ps5-linux-exploit-move-sparks-backlash-from-jailbreaking-community) — **published 27 October 2026** by Jowi Morales; discusses a **21 October 2026** 14.20 release and makes a secondary patch attribution, **not** primary first-fixed-build evidence

## 14.10 standard update vs recovery package identity

The public records for build **26.06-14.10.00.03** are inconsistent.

| Package | MewX SHA-256 (reported) | Developer Wiki record |
|---|---|---|
| Standard update | c17384946df6e5c85b2d72cbeee2057b165bf90279d9e2a86d527d0778cdaaf6 | Records the recovery digest instead |
| Recovery | 9f3a0b8811c00ab52b092d2e9f0f13dd4515f018361ff38e4be43fd8c18b21de | Same digest |

MewX additionally lists different package sizes for the two types. A **duplicated recovery digest in the wiki's standard-update row** is a plausible data-entry explanation. The true standard-package digest remains **unverified against official package bytes**. No retail PUP was downloaded during Phases 1–5.

Do not use either disputed value as a verified standard-update hash until official-byte verification or independently authoritative evidence is available.

## Phase 8 update — catalogue reconciliation

The metadata-only Phase 8 validator reportedly checked 30 records in ten package-class groups (standard update and recovery for 13.60, 14.00, 14.10, 14.20 and 14.22). Its sole conflict and cross-class duplicate concerned 14.10.

[MewX](https://github.com/MewX/ps5-official-firmware-list/blob/6f4bc337885d51280529b729fed69ae11754066a/README.md) and [Midnight's standard](https://archive.midnightchannel.net/SonyPS/Firmware/?cat=ps5sys&legacy=1) and [recovery](https://archive.midnightchannel.net/SonyPS/Firmware/?cat=ps5rec&legacy=1) indexes both assign `c1738494…` to the 14.10 standard update and `9f3a0b88…` to recovery. The wiki appears to repeat the recovery digest in the standard-update row. This supports a **catalogue transcription-error hypothesis**, not a byte-verified checksum correction. Public records may not be independent.

See [Phase 8 package metadata report](PHASE-8-FIRMWARE-METADATA.md).

## Outstanding questions

1. **Relapse 13.60 to 14.00 boundary:** Which component, if any, was actually fixed or made incompatible, and what original evidence establishes this?
2. **S3-resume hypervisor fix:** Can a vendor disclosure or independently documented build comparison establish the *first* fixed retail build?
3. **14.22 patch contents:** Which named flaws, if any, can an attributable disclosure associate specifically with 14.22?
4. **Source-to-binary correspondence:** Which of Sony's WebKit source-distribution differences, if any, are represented in a given retail build?
5. **Package integrity:** Can the 14.10 standard/recovery checksum mismatch be resolved from official package bytes or attributable metadata?

## Proposed roadmap

- **Phase 6:** Validate the Phase 5 comparison and classify all 54 content-changed files; create a small changed-only inventory.
- **Phase 7:** Compare identified source changes against attributable upstream WebKit security advisories.
- **Phase 8 (reported complete):** Documented package identities and hash discrepancies without downloading firmware; authentic bytes remain unverified.
- **Phase 9 (completed):** PASS WITH QUALIFICATIONS; reproduced comparison counts, reviewed 14 claims and identified publication corrections. See [the Phase 9 audit](PHASE-9-INDEPENDENT-AUDIT.md).
- **Phase 10 (reported complete):** Final research dossier, with explicit Phase 9 audit qualifications and an unresolved-questions register. The publicly available [final research dossier](FINAL-RESEARCH-DOSSIER.md) is a publication synthesis, not a direct copy of the original local Phase 10 document.

Broad repeated searches are unlikely to resolve closed-source patch questions absent new official or original-researcher disclosures. A focused source watchlist is more useful.

## Final publication (all ten phases)

The project now has a completed public-facing [research dossier](FINAL-RESEARCH-DOSSIER.md), [executive summary](EXECUTIVE-SUMMARY.md), [evidence register](FINAL-EVIDENCE-REGISTER.csv), [reproducibility report](REPRODUCIBILITY-AND-INTEGRITY.md), [unresolved-questions register](UNRESOLVED-QUESTIONS.md) and [publication manifest](PUBLICATION-MANIFEST.md).

The evidence register is a new selection of public-facing claims and is **not** the original Phase 9 14-claim item-level audit CSV. Those original local files were not available to the GitHub publication process.

## Scope and publication cautions

This repository does not include Sony firmware PUP files, original WebKit ZIPs, private device data or exploit payloads. Phase 5's approximately 336 MB local inventory has not been published here. Do not present these summaries as an independently reproduced audit of local file contents.

Only perform research on systems and materials you are authorised to study; respect original licences and disclosure obligations.
