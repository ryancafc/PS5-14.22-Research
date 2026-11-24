# Independent firmware metadata verification

Result: **PASS for the existing standard-update package and its extracted first fragment.** Source claims A01–A09 are corroborated. Recovery and earlier-version comparisons remain blocked (A14–A15).

| File | Bytes | Complete SHA-256 |
|---|---:|---|
| firmware/PS5UPDATE.PUP | 1,266,091,008 | b0d5818d5ce26e2537d1e2febaebd9a3bef1bb1cf8e9898ddf099773706a810b |
| analysis/inner/PS5UPDATE1.PUP | 1,266,089,597 | 7056fe13f5242b146d4941a277ca758a91c885c7aef5f3db0ffdee84b7f668b1 |

The independent verifier streamed both complete files and separately hashed exactly the declared entry range in the outer file. That range digest equals the complete inner digest. It opened inputs read-only and checked unchanged size/mtime during the run. No replacement package was downloaded.

## Container facts

- Magic SLB2; version 3; flags 0x00010000; one 48-byte entry after the 32-byte fixed header.
- Entry PS5UPDATE1.PUP begins at sector 2 × 512 = 1024 (0x400), is 1,266,089,597 bytes long and ends at 1,266,090,621.
- Entry reserved bytes are zero. Its start is sector aligned and its entire extent is in bounds.
- Block count 2,472,834 × 512 equals the outer size exactly. Outer size modulo 512 is zero.
- All 387 trailing bytes are zero. The inner entry itself is not required to end on a sector boundary.
- The digest-like slots discussed by A match the observed bytes. Their cryptographic functions, keys and coverage remain unknown; they are not authenticated checksums in this audit.

## Accessible inner metadata

The 16-byte prologue is `5414f5ee1001013204000000b005e00d`. The raw magic is 0xEEF51454; u16 fields at 0x0c/0x0e are 1456/3552. The bytes at 0x04–0x07 can be grouped as u32 0x32010110, u16 272 followed by u16 12801, or four bytes 16/1/1/50. Those are descriptions of the same bytes under different layouts. None is the firmware version 14.22.

The protected bytes after 0x10 cannot be accepted as plaintext metadata: interpreting them as file size yields 7,778,815,604,992,573,160; the would-be entry count is 54,760. A 1 MiB sample at inner offset 0x4000 has entropy 7.999833752 bits/byte. This is consistent with high-entropy protected data, but entropy alone neither proves a particular encryption algorithm nor proves absence of every plaintext region.

The shared PUP/SELF-family magic does not establish an accessible executable (A11). The formula yielding 44 segments remains a hypothesis (A10). Visible field similarity does not prove identical keys/protection (A12), and failed candidate decryption tests do not prove a universal impossibility theorem (A13). No decryption, key-search or bypass was attempted.

## Comparison scope and attribution

A's detailed document limits the 117/115 differing-byte metric to the header window 0x000–0x440. Preserve that scope whenever quoting the metric (A16). It is not a whole-package difference count, a kernel diff or a changed-code size.

14.22 identity here is established relative to the expected hashes and matching documented package metadata. It is not a fresh verification of a Sony digital signature or an authenticated plaintext internal version field. No 14.20 package or recovery package was locally available for the requested independent comparisons; their claimed deltas/equivalence were not reproduced.

Evidence: `evidence/firmware-verification.json`, `logs/firmware-verification.log`, and the source-pinned CSV rows. The auditor-authored `scripts/verify_firmware.py` records the method. Historical research files were not overwritten.
