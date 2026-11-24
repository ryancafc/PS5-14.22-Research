# Read-only firmware metadata comparison

**PASS for available inputs; 14.10 pairs BLOCKED.** All three available files are SLB2 version 3, flags 0x10000. The two standard updates each have one entry. Recovery has two. The utility validates header/table size, full-file sector count, entry bounds and non-overlap before expensive scans. Every input's size/inode/timestamps remained unchanged during inspection.

| Package | Entry | Start | Bytes | End exclusive | Following gap | Gap zero |
| --- | --- | --- | --- | --- | --- | --- |
| 14.20-standard.PUP | PS5UPDATE1.PUP | 1024 | 1266085469 | 1266086493 | 419 | True |
| PS5UPDATE.PUP | PS5UPDATE1.PUP | 1024 | 1266089597 | 1266090621 | 387 | True |
| 14.22-recovery.PUP | PS5UPDATE1.PUP | 1024 | 1266089597 | 1266090621 | 387 | True |
| 14.22-recovery.PUP | PS5UPDATE2.PUP | 1266091008 | 157606077 | 1423697085 | 323 | True |

Entry starts are multiples of 512 and each outer block count ×512 equals complete size. Gaps are scanned completely; all are zero. Entry ends need not be sector aligned. Bytes between the entry table and first payload may contain container metadata and are not labelled zero padding.

## Independently reproduced 14.20→14.22 facts

- Outer size: **+4,096 bytes**, eight 512-byte sectors.
- Inner entry: **+4,128 bytes**. Trailing padding: **419→387**, a 32-byte reduction.
- Explicit half-open metadata window **[0x000,0x440)**: **115 differing bytes**. The two 32-byte slots [0x200,0x220) and [0x3e0,0x400) each differ in all 32 positions.
- Inner prefix [0x400,0x410): **zero differences**, `5414f5ee1001013204000000b005e00d`.

These reproduce the bounded corresponding claims in Repository A's [pup-diff.md at 7d7fcbb](https://github.com/ccclosed/ps5-1422-research/blob/7d7fcbb448b2376c396376038b1250437ca5092b/evidence/pup-diff.md). Phase 20's A15/A16 classifications remain historical; Phase 21 supplies new evidence for the previously blocked size delta and source-supported window metric. The 117-byte results involving 14.10 remain unreproduced.

## Recovery identity and limits

Recovery entry 1 has exactly the same declared size and complete entry SHA-256 as standard 14.22's inner entry: `7056fe13f5242b146d4941a277ca758a91c885c7aef5f3db0ffdee84b7f668b1`. This is full-range hash corroboration, not a new extraction or decryption. Recovery entry 2 is **157,606,077 bytes**, at offset **1,266,091,008**, SHA-256 `60205c0443eb853e7e02f432549ac63a1a2e2bbdb1d227c6232d75b2aa425579`. Its prefix is `5414f5ee10010132040000004002a005`; raw u16 fields at +0xc/+0xe are 576/1440. Those bytes do not identify a plaintext executable, segment count, vulnerability or cryptographic key. Phase 20's blocked A14 now has a new independent recovery identity check; the old record is not rewritten.

The standard/recovery metadata window [0,0x440) differs in 88 positions even though their first inner entries match. The slot at 0x200 matches; the slot at 0x3e0 differs in 32 positions. Their cryptographic roles remain unknown. A whole outer package cannot be treated as byte-identical merely because one inner entry is identical.

## Distribution and interpretation

For each entry, the utility records the full 256-bin byte histogram and entropy for at most 1 MiB at entry-relative 0x4000. Sample offsets, lengths and SHA-256 are explicit in JSON. High sampled entropy is compatible with protected/compressed/random-looking data; it does not prove whole-image encryption or a particular algorithm. No full-file entropy, signature scan or all-offset ciphertext comparison is claimed.

This phase does not attribute any encrypted-byte or size difference to a vulnerability fix, kernel change or changed executable. The 44-segment formula remains a hypothesis. Accessible raw u16/u32 groupings are not a retail firmware version. No decryption, protected-key acquisition or security-control bypass occurred.

Reproduce with `firmware_compare.py` and the exact identities in acquisition/metadata CSV. JSON includes 12 defined-window pair comparisons, complete hashes, raw entry prefixes, sampled distributions and gap checks. CSV has four entry rows across three packages. Errors produce exit status 2 and explicit messages; windows are bounded to 16 MiB, input/output aliases are rejected, and synthetic fixtures are generated only inside unit-test temporary directories. **27/27 unit tests pass**; `logs/firmware-unit-tests.log` records the run.
