# Phase 6 — WebKit source-comparison validation

**Status:** Completed, 15 November 2026  
**Nature of evidence:** Reported local reproducibility checks from the Codex research workflow. The original ZIP archives, 336 MB full inventory, 1,041-row subset, and five local Phase 6 reports have not been uploaded to this repository for separate inspection.

## Reproduced classification counts

| Classification | Verified in the local Phase 6 run |
|---|---:|
| Added paths | 985 |
| Removed paths | 2 |
| Changed by content hash | 54 |
| Unchanged | 393,117 |
| **Union of compared paths** | **394,158** |
| **Changed-only inventory** | **1,041 rows** |

The reported validation rehashed **every added, removed, and changed file** against both the relevant ZIP archive and its extracted copy. It found no duplicate archive paths, case collisions, missing files, or extra extracted outputs. Every extracted path matched its original ZIP inventory. The Phase 5 complete CSV reportedly retained the same SHA-256 before and after the Phase 6 checks.

## Changed-file categories

Of the **54 changed files**, the Phase 6 review classified:

| Category | Count |
|---|---:|
| JavaScriptCore production-tree source | 18 |
| WebCore production-tree source | 8 |
| PlayStation WebKit UI-process production-tree source | 1 |
| Build/tooling, tests, fixtures, distribution manifest, etc. | 27 |
| **Total** | **54** |

These are **path-role classifications**, not proof of changed runtime behaviour. A file being in a production source directory does not by itself establish a compiled binary difference.

Among the most concrete reported differences were JavaScriptCore build metadata, four benchmark plans and fifteen HLS-related fixtures. The source distributions still declared WebKit version `616.1.27.211.1`.

## Scope of validation

- **Supported by local comparison:** Published archive trees differ by content hash; the initial counts are reproducible in the same research environment.
- **Not established:** Exact PS5 retail 14.22 binary equivalence, named vulnerability remediation, security impact, or why Relapse public support stops at 13.60.
- **Archive maintenance note:** Phase 5 reported an output collision; Phase 6 later confirmed the original complete CSV's hash was unchanged.

Phase 6 produced five local deliverables: change classification, changed-only CSV, 54-file review, validation/recovery report, and conclusions. These original local files are **not available from this repository**.

## Next step

Phase 7 investigates provenance of the **27 production-tree source differences** and whether any of them are attributable to public upstream WebKit security advisories.

See [Phase 7 provenance findings](PHASE-7-UPSTREAM-CORRELATION.md) and [WebKit comparison overview](WEBKIT-COMPARISON.md).
