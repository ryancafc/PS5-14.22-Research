# Sony PS5 WebKit published-source comparison

**Reported local analysis:** Phase 5, 15 November 2026  
**Source:** [Sony PS5 WebKit catalogue](https://www.playstation.com/en-us/oss/ps5/webkit/)

Sony lists separate source archives for system software **13.00–13.60** and **14.00 onward**. The catalogue does not list separate 14.10, 14.20, or 14.22 WebKit source groups as of this review.

## Reported inputs and method

- Official 13.x and 14.x WebKit source ZIPs were downloaded from Sony.
- The local workflow recorded archive SHA-256 values and extracted each archive into its own tree.
- Source-relative paths were classified using file content hashes, not modification times.
- Both extracted trees were reportedly checked against the archive entry counts.
- Both distributions declared WebKit version **616.1.27.211.1**.

Exact archive digests, retrieval metadata, and the complete per-path inventory are retained in the local Phase 5 reports; they are **not reproduced here without access to those records**. This GitHub page does not claim an independent re-hash of the original ZIPs.

## Reported path classification

| Classification | Paths |
|---|---:|
| Added in 14.x | 985 |
| Removed from 14.x | 2 |
| Present in both, content hash changed | 54 |
| Present in both, content hash unchanged | 393,117 |
| **Total unique compared paths** | **394,158** |

The changed/added/removed subset is **1,041** paths. Approximately **99.74%** of the union were unchanged, according to the reported comparison.

Most additions were described as test-related resources. Sampled PlayStation build configuration files were byte-identical; this **does not establish** that all build configuration files are identical or that compiled retail 14.x binaries match these source trees.

## Validation note

During extraction/output handling, an output-name collision was reported. The workflow used exclusive writing to preserve its existing CSV and subsequently read the file back, checking classifications against the recorded digests. This recovery was reported by Codex; a second person has not reviewed the raw output in this GitHub repository.

**Local artefact not uploaded:** the complete WebKit path inventory CSV (approximately **336 MB**). Avoid committing the large inventory or licensed WebKit source archives before deciding on distribution/licensing and storage strategy.

## What the comparison establishes

1. The two published source distributions differ at the file-content level even though the declared WebKit version is identical.
2. The published source catalogues provide an avenue for *source-level* historical comparison.
3. The 54 content-changed files are a manageable starting set for review.

## What it does not establish

- A named vulnerability fixed in 14.00, 14.10, 14.20 or 14.22.
- Why the public Relapse implementations stop at 13.60.
- Exact equivalence between these archives and every retail 14.x firmware build.
- A working 14.22 exploit or a complete firmware binary security diff.

## Next review

Phase 6 should validate the path-classification inventory independently and classify the **54 changed files** before drawing conclusions about their purpose. Phase 7 may compare documented upstream WebKit security advisories with attributable source changes.

See [Research status](RESEARCH-STATUS.md).
