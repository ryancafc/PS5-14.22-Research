# Phases 15–16 — Instrumented upstream WebKit comparison (Linux)

**Dates:** November 2026. **Platform:** WSL-hosted WebKitGTK builds in a `wkdev` container, **not PS5**. **Purpose:** isolate the upstream Canvas reentrancy regression and validate the guard added by its fix.

## Revisions and reported environment

| Build | Revision | Description |
|---|---|---|
| Vulnerable | `cab8cdc40a` | Upstream revision preceding the targeted guard |
| Patched | `040ef6e21ffac03b6d6098e0e12354bdb5469ad1` | Revision with post-dictionary-conversion reentrancy checks |

Reported worktrees: `~/ps5-research/phase15/WebKit` and `~/ps5-research/phase15/WebKit-patched`, with a separate local `evidence` directory. WebKitGTK was built with AddressSanitizer. The recorded environments were **not perfectly configuration-identical**: `ENABLE_WK_WEB_EXTENSIONS` was ON in one and OFF in the other. This limits any claim of a fully controlled binary A/B comparison.

## Relevant upstream defect mechanism

Conversion of a JavaScript options dictionary can execute user-defined property getters. A getter may call `getContext()` recursively, create an inner Canvas context and return to the outer call. Without a post-conversion state check, the outer call may replace the Canvas-owned context while a JS wrapper referring to the old native context survives. The patch rechecks existing context state after dictionary conversion; its OffscreenCanvas path also accounts for detach state.

The upstream issue was tracked as **WebKit Bug 313175** and researched in connection with **CVE-2026-43720**. Source attribution here does not constitute a Sony firmware advisory.

## Baseline test, adjustment and observations

The upstream regression file was `LayoutTests/fast/canvas/canvas-getContext-reentrant.html`, covering **32 combinations** across HTMLCanvas and OffscreenCanvas, four outer context types and four inner context types.

In this Linux build, the original test produced only **24/32** expected matches: all eight cases with outer 2D did not execute the intended reentrant getter, because `alpha` was commented out in the local 2D settings IDL and `colorSpace` was controlled by a disabled setting.

For the controlled retest, **the test HTML only** was modified to use the unconditional 2D `willReadFrequently` dictionary getter; the engine source was not modified for that adjustment. The probe was named `canvas-reentrant-2d-probe.html`.

- **Patched build:** all **32/32** observed outputs matched the official expected behaviour with the modified test. No ASan error report was emitted under the chosen log path.
- **Vulnerable build:** a recorded **AddressSanitizer heap-use-after-free** occurred; the final report identified an **8-byte read in `WebCore::CanvasRenderingContext::deref() const`** during JS wrapper destruction/GC, following native context replacement. An earlier log showed a related UAF path during WebGL opaque-root marking.
- These are operator-reported local reproductions, not independent publication of raw stack traces.

## ASan/WSL diagnostic caveats

Unrelated JavaScriptCore conservative-root scanning crashes were reproducible even with a simple `jsc -e 'gc();'` invocation in both builds under the initial ASan setup. Disabling ASan stack-use-after-return detection (`detect_stack_use_after_return=0`) resolved that unrelated test failure without recompilation.

The WSL/container runtime needed local software rendering and, for trusted local test files only, `WEBKIT_DISABLE_SANDBOX_THIS_IS_DANGEROUS=1` because of nested bubblewrap restrictions. This override is **not recommended for normal browsing** and must not be treated as an exploit mitigation or proof.

## Integrity pointers

These digests are from reported local commands and identify *local artifacts*, which are **not themselves uploaded here**.

| Artifact | SHA-256 |
|---|---|
| `webkit-asan-cab8cdc40a.log` | `efd1a1f593cacdc4f9e2465b26de808d0875955c8d0a1c942bab28f86e3beba9` |
| `webkit-vulnerable-final.35647` | `9c88eea8e7e77ea33c2432893d547cf30d1f38cac09098fe6b139509b53dd418` |
| `canvas-reentrant-2d-probe.html` | `9677328a977148c6245509e7bdb8f8fdeba5df5663b7e712ba61931ada6adec6` |

## Conclusion

The upstream Linux WebKit experiment supports a **reproduced memory-safety defect in the selected vulnerable build** and **expected behaviour without a reported ASan error in the selected patched build**, under the stated modified test and environment limitations.

**It does not establish that a PS5 14.22 binary contains the vulnerable revision or that native code execution is possible on retail PS5.**

Related: [Phase 14 witness](PHASES-11-14-RETAIL-CLAIMS.md), [Sony source](PHASE-17-SONY-SOURCE-AUDIT.md), [project closeout](PROJECT-CLOSEOUT-2026-11-19.md).
