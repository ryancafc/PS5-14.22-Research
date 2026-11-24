# Firmware acquisition

**PARTIAL.** Disk preflight found about 64 GB free on the research volume. Existing copies were located before download. A new `~/PS5-Research/14.22/firmware-comparison/phase-21/` directory holds only new downloads; the original verified 14.22 file was reused unchanged.

| Version/type | Expected and verified bytes | Complete SHA-256 | Outcome |
| --- | --- | --- | --- |
| 14.10 standard | 1261408256 | c17384946df6e5c85b2d72cbeee2057b165bf90279d9e2a86d527d0778cdaaf6 | BLOCKED: official object length 0 |
| 14.20 standard | 1266086912 | 0f81be6fd890bc04925b3953e0862dfc2ead68edfdc33f31c3c60d0c267f68e4 | Verified new download |
| 14.22 standard | 1266091008 | b0d5818d5ce26e2537d1e2febaebd9a3bef1bb1cf8e9898ddf099773706a810b | Reused, rehashed |
| 14.22 recovery | 1423697408 | 42ea0e5aad1361e098837d40157863c4c519f0bbc66eb03c04dbaaf339b063fb | Verified new download |

All successful inputs also match the reference MD5, used as a secondary identity check. SHA-256 and file sizes come from the community-maintained [MewX reference at pinned commit](https://github.com/MewX/ps5-official-firmware-list/blob/7eaa071d558e8f700ea74712fd86bc05f76657c5/README.md) and its archived Sony update XML. The standard-update `sys_` URL component matches the published SHA-256. Recovery uses the separately identified `rec_` URL and size; it is never substituted for a standard update.

The current [Sony support page](https://www.playstation.com/en-gb/support/hardware/ps5/system-software/) links the official HTTPS `pc.ps5.update.playstation.net` download host, currently advertising 14.23. This phase did not substitute that current version. Historical archive URLs use `dus01`; their HTTPS certificates failed hostname verification here. Verification was retained. The corresponding official `pc` HTTPS paths served matching-size 14.20 standard and 14.22 packages. The recovery path was derived from the published build/date/hash and checked by HTTP size plus full downloaded identity.

The exact 14.10 historical path returned **HTTP 200 with Content-Length 0**, both on checked `pc` HTTPS and original `dus01` HTTP. A bounded GET requesting bytes 0–31 received zero bytes, confirming that status 200 alone does not establish availability. No empty or unrelated file was admitted as 14.10. This is an observed endpoint/time limitation, not proof that no legitimate archive exists anywhere.

The downloads were streamed to new `.part` files with size caps, verified, then renamed. No installation/flashing occurred. Authenticity here means matching public metadata and delivery from checked official endpoints, not independent validation of Sony's cryptographic signatures. Community metadata and archived XML are provenance references, not a fresh signed internal version assertion.

Evidence: `evidence/acquisition-plan.json`, `acquisition-results.json`, `1410-http-availability.json`, `1410-range-response.json`; `logs/acquisition.log`. Original acquisition scripts are retained locally under `scripts/` for provenance. The official package bytes are not published.
