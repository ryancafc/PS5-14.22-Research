# Repository inventory and reproducibility audit

## Pinned local copies

| Item | Repository A | Repository B |
|---|---|---|
| Source | [ccclosed/ps5-1422-research](https://github.com/ccclosed/ps5-1422-research/tree/7d7fcbb448b2376c396376038b1250437ca5092b) | [karter-captain/ps5-14.22-browser-probes](https://github.com/karter-captain/ps5-14.22-browser-probes/tree/d0702131ff94d40bd8c408452ccac4c94f2af00e) |
| Commit | `7d7fcbb448b2376c396376038b1250437ca5092b` | `d0702131ff94d40bd8c408452ccac4c94f2af00e` |
| Branch | master | main |
| Initial working tree | Clean | Clean |
| Tracked files | 220 | 11 |
| Tracked file bytes | 2,925,085 | 50,424 |
| Explicit licence | MIT | No explicit grant found in the tracked files |

These are incorporated checkout versions, not assertions that the upstream branches cannot change. Remote commit existence was checked. Neither repository was recloned or updated. Full per-file sizes, SHA-256 values and line counts are in `evidence/repository-A-inventory.json` and `repository-B-inventory.json`.

## Structure and languages

A has README.md, REPORT-1422.md, LICENSE, three docs files, 47 evidence files and 166 files under tools. Its tracked extensions include 57 Markdown, 35 Python, 48 HTML, 25 JavaScript, five MJS, nine shell, seven C, one header, two Lua, eight JSON and ten ELF files. The ELF files are five duplicate trigger pairs, not ten independent implementations. The evidence directory contains 45 Markdown reports plus two NVD JSON snapshots, so the README's 45-report count is consistent with those file types. The report's 32,349-file/5.4 GB number concerns an unshipped private workspace (A35), not this checkout.

B consists of one README and ten self-contained HTML files. Its executable logic is inline JavaScript; presentation is HTML/CSS. It has no tracked dependency manifest, automated test results, hardware run log or explicit licence. The current menu no longer implements the README's Quick Scan, and three newer pages are absent from its list (B14).

## Relevance and reviewed execution policy

| Component | Relevance | Phase 20 treatment |
|---|---|---|
| A tools/pup and container evidence | SLB2/PUP structure, raw metadata, reported comparisons | Source reviewed; independent auditor parser used on existing files |
| A emulation, syscall/dump and SDK reports | Older executable structure and external claims | Documentary/static review; missing dumps and inputs recorded |
| A mock/test/runner sources | Simulation boundaries and metric accounting | Entry points read; no chain or shell suite executed |
| A trigger ELF/C and kernel/userland chains | Potentially destabilising/exploitation code | File/header inventory only; no build, execution or publication |
| B Atomics, iframe, views-only and Wasm pages | Small browser semantics | Fully reviewed selected code paths, then desktop-only execution |
| B allocation, full/aggressive/slow chains | Memory pressure and unreliable success labels | Static accounting only; not executed |
| Both Markdown corpora | Research provenance and limits | Claims paraphrased, source-located and pinned |

## Dependencies

A's container parser imports Python standard-library modules. Other Python sources refer to Unicorn, Capstone, NumPy, cryptography, PyGObject/WebKitGTK and Lupa/Lua 5.1, plus local modules. Shell/test entry points assume Bash, Python and Node; the demo starts a loopback mock service. The trigger Makefile describes a GCC/binutils freestanding path and an alternative external SDK/Clang/lld path. Two tiny package.json files set module mode rather than pinning a complete Node dependency graph. There is no unified lockfile covering all these workflows. Thirty-five Python files passed AST parsing only; that is not runtime testing.

B requires a browser with the relevant APIs. Its scripts also contain BigInt literal syntax, so older parsers can reject an entire script before its runtime feature checks run. Web API exposure depends on origin, embedding and isolation policy; a firmware label is not sufficient context.

Phase 20 used existing Python, Node and sandboxed Chromium 150.0.7871.181 through the bundled Playwright package. No third-party dependency was installed. The initial restricted-shell loopback bind failed with EPERM; the same bounded harness then ran successfully with permission for the loopback server and browser. Chromium's sandbox remained enabled.

## Reproducibility and sensitive material

Eight of nine selected explicit input/output paths are absent, including the older kernel dump/table, game executable, SDK vendor tree and named raw comparison outputs. The self_probe source is present. See `required-input-presence.json`; this is a selected-path check, not an assertion that every reference in every document was checked.

A also tracks a development TLS private-key PEM at `tools/probe/certs/server.key`. Its contents were neither printed nor copied into publication. It is not treated as a Sony firmware key. The inventory records presence only; a publicly shipped test key should not be reused as a private credential.

The publication includes original audit documentation and derived evidence, not either repository's exploit code, ELF triggers, unlicensed HTML, TLS key, firmware, game files or console dumps. B is linked at its pinned source instead of redistributed.
