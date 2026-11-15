# Phase 8 — Firmware package provenance and checksum discrepancy

**Status:** Reported complete, 15 November 2026  
**Scope:** Public firmware catalogue records and read-only metadata validation. **No PS5 connection, retail firmware package download, package hashing, or firmware modification occurred.**

> Evidence status: This document summarises the user's Phase 8 Codex report and checks against public metadata indexes. The original six Phase 8 local deliverables and the 30-record working dataset are **not uploaded or independently reprocessed here**.

## Main finding — PS5 firmware 14.10

The most plausible explanation for the conflicting SHA-256 records is a **standard-update/recovery copy error in the PS5 Developer Wiki**, where the recovery digest appears in both rows.

Build reported: `26.06-14.10.00.03-00.00.00.0.1`.

| Class | MewX SHA-256 | MewX reported bytes |
|---|---|---:|
| Standard update | `c17384946df6e5c85b2d72cbeee2057b165bf90279d9e2a86d527d0778cdaaf6` | 1,261,408,256 |
| Recovery / reinstall | `9f3a0b8811c00ab52b092d2e9f0f13dd4515f018361ff38e4be43fd8c18b21de` | 1,418,890,240 |

Both the [MewX pinned list](https://github.com/MewX/ps5-official-firmware-list/blob/6f4bc337885d51280529b729fed69ae11754066a/README.md) and Midnight's [PS5 standard firmware index](https://archive.midnightchannel.net/SonyPS/Firmware/?cat=ps5sys&legacy=1) and [PS5 recovery index](https://archive.midnightchannel.net/SonyPS/Firmware/?cat=ps5rec&legacy=1) place the respective digests in the correct package classes. The [PS5 Developer Wiki firmware index](https://www.psdevwiki.com/ps5/Official_Firmware) and [historical revision reference](https://www.psdevwiki.com/ps5/index.php?title=System_Software&oldid=4828) were reported to display the recovery digest in both classes. The original direct historical wiki URL was reportedly inaccessible during the local Phase 8 run; the workflow used a page identifying itself as revision 4828.

This is **catalogue corroboration**, not independent validation of the underlying download bytes. The two lists may share sources, and the historical Sony packages were not acquired or hashed in this research.

## Reported local validation

Phase 8 produced a machine-readable register covering firmware versions **13.60, 14.00, 14.10, 14.20 and 14.22**, with standard update and recovery classes separated.

Its read-only validator reportedly processed:

| Check | Reported result |
|---|---:|
| Source records | 30 |
| Firmware build/package-class groups | 10 |
| Groups with conflicting reported digest | 1 |
| Cross-class duplicate digest cases | 1 |

Both anomalies concern **14.10**. This does not imply the other nine groups were authenticated against package bytes; it only describes agreement or disagreement among the selected metadata records.

The original local report set includes:

1. `Firmware-14.10-Checksum-Verification.md`
2. `PS5-Package-Identity-Research.md`
3. `Firmware-13.60-to-14.22-Metadata.csv`
4. `Firmware-Source-Reliability.md`
5. `Official-Package-Verification-Feasibility.md`
6. `Phase8-Research-Conclusions.md`

These filenames describe local deliverables, **not GitHub-hosted attachments**.

## What can be concluded

**Corroborated from public catalogues**
- Separate standard and recovery entries exist for 14.10.
- MewX and Midnight agree on the 14.10 standard and recovery digest values.
- A duplicated recovery value plausibly explains the wiki's apparent standard-entry discrepancy.

**Reported by the local analysis**
- Thirty metadata records were validated across ten package-class groups.
- A single conflicting group and single cross-class duplicate were detected.
- Previous phase folders were left unchanged.

**Unresolved**
- Whether the catalogues are fully independent of one another.
- Whether an official, historically authentic 14.10 package matches either digest.
- Whether historical Sony-hosted package URLs remain live.
- Whether catalogue-reported historical byte lengths match authentic package bytes.
- The security changes inside retail 14.22; hash differences alone do not establish named fixes.

## Next step — Phase 9 independent evidence audit

Conduct a **separate, reproducible review** of the Phase 1–8 claims and available files: verify source URLs and revisions; detect duplicated evidence; recalculate hashes of *already-held, authorised* local artefacts only; audit file and metadata counts; and clearly identify any claims that remain based solely on Codex self-report.

Do **not** download retail firmware PUPs, perform console operations, or convert catalogue claims into statements of exploitability.

See [Research status](RESEARCH-STATUS.md), [sources and roadmap](SOURCES-AND-NEXT-STEPS.md), and [Phase 7 source provenance](PHASE-7-UPSTREAM-CORRELATION.md).
