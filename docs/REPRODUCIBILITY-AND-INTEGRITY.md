# Reproducibility, audit trail and data integrity

**Scope:** Reported results of the Phase 5–10 local workflow, with limitations explicitly preserved.

## Inputs and provenance

- Official [Sony PS5 WebKit source catalogue](https://www.playstation.com/en-us/oss/ps5/webkit/): separate 13.00–13.60 and 14.00-onward ZIP source groups.
- Public firmware metadata: [MewX pinned index](https://github.com/MewX/ps5-official-firmware-list/blob/6f4bc337885d51280529b729fed69ae11754066a/README.md), [PS5 Developer Wiki](https://www.psdevwiki.com/ps5/Official_Firmware), and [Midnight firmware archive](https://archive.midnightchannel.net/SonyPS/Firmware/index.php/info/info/?cat=ps5sys&legacy=1).
- Public historical exploit source: [Relapse](https://github.com/ntfargo/Relapse-Exploit) and [Byepervisor-Reborn](https://github.com/PS5Dev/Byepervisor-Reborn).

Exact ZIP SHA-256 values, detailed local input paths and the original scripts are reported as retained in Windows-local Phases 5–10, but **were not supplied for this publication**. This page does not invent them or claim that GitHub contains a complete reproducibility bundle.

## Reported comparison procedure

1. Download the two official Sony WebKit source ZIPs from Sony.
2. Record archive SHA-256 and declared component version (`616.1.27.211.1` for both).
3. Inventory archive members using full source-relative paths and content hashes.
4. Extract to separate trees using collision-safe handling and check archive membership against extracted files.
5. Classify each relative path as added, removed, changed, or unchanged by content hashes.
6. Verify the compact non-unchanged inventory.
7. Rehash changed files independently against both the original ZIP members and extracted copies.
8. Rehash all ZIP members in the Phase 9 audit, document errors and correct the classification when justified.

## Reported validation figures

| Measure | Phase 9 result |
|---|---:|
| ZIP members rehashed | 787,329 |
| Added paths | 985 |
| Removed paths | 2 |
| Changed paths | 54 |
| Unchanged paths | 393,117 |
| Total unique paths | 394,158 |
| Compact non-unchanged CSV rows | 1,041 |
| Production-tree changed paths | 27 |

The total archive member count is consistent with the reported classifications: the 13.x tree has **393,173** paths and the 14.x tree has **394,156**; together they total **787,329**.

### Corrections preserved

- **Phase 5:** A reported output collision was resolved without modifying the retained original large CSV; Phase 6 subsequently checked its SHA-256 before and after.
- **Phase 9:** The first audit misclassified a **renamed Sony manifest**. The corrected run reproduced the counts exactly with **zero reported discrepancies**. The initial failure should remain visible in the local audit record.

These checks bolster internal consistency but do not prove that retail PS5 14.22 firmware contains identical compiled WebKit binaries.

## Source-provenance analysis

Phase 7 compared **27 production-tree changed paths** with selected upstream WebKit revisions; **26** had path counterparts, **zero** were byte-identical to sampled copies, and **one** was identified as PlayStation integration (`PlayStationWebView.cpp`). Sampling limits prevent exhaustive origin or patch attribution.

## Firmware package metadata procedure

The Phase 8 validator reportedly covered **30 records in 10 build/package-type groups**, detecting one conflicting SHA-256 group and one cross-class repeated digest (both 14.10).

Metadata consistency is not the same as authentic file identity. No historical retail firmware PUP file was downloaded or hashed. Hashes reproduced from wiki/GitHub catalogues must remain labelled **reported** rather than **byte-verified**.

## Integrity and independent audit limits

- Phase 9: **42 of 42** prior deliverables fingerprinted; zero byte-identical duplicate files.
- Phase 9 claim audit: **6 of 14** claims confirmed; **4** computationally reproduced.
- Phase 10: **53** prior top-level file fingerprints reportedly unchanged; extraction-tree file counts preserved.
- The original local reports, script sources and raw CSVs are **not hosted in this repository**, preventing independent third-party reproduction from GitHub alone.

## Recommended external reproducibility review

Before claiming independent third-party verification, a separate auditor should obtain the original source URLs, exact archive hashes, comparison script, file inventory or compact non-unchanged subset, original Phase 9 claim matrix, and immutable input/output fingerprints (subject to copyright and redistribution policy). That auditor should reproduce counts and check known corrections without relying on the original Codex-generated summaries.

**No exploitation, console modification or retail firmware testing is claimed here.**
