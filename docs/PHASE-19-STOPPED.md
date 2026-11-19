# Phase 19 — Planned Canvas matrix; not executed

**19 November 2026 project closeout.** This phase was **started but not completed**. Its Linux-only HTML file was created and hashed, but no Phase 19.2 patched MiniBrowser output or Phase 19.3 vulnerable-build comparison was submitted.

## Purpose

Compare the expected behaviour of reentrant Canvas `getContext()` requests when only **2D and BitmapRenderer** are involved, using instrumented Linux WebKit builds. The test is **not for execution on PS5**, since unpatched native engines can be destabilised by the reentrancy sequence.

| Outer context | Inner during options getter | Intended patched invariant |
|---|---|---|
| 2D | 2D | Outer returns same context as inner |
| 2D | BitmapRenderer | Outer returns null |
| BitmapRenderer | 2D | Outer returns null |
| BitmapRenderer | BitmapRenderer | Outer returns same context as inner |

A JavaScript options getter calls the inner `getContext()` while the outer call converts its options dictionary. The test retained contexts and recorded getter counts and return-value identities. It did not include heap spraying or explicitly force GC. Even without those actions, reentrancy could invoke unsafe native code in a vulnerable build.

## Actual completed work

- Created local file `~/ps5-research/phase19/phase19-canvas-matrix.html`.
- User-reported SHA-256: `cebe5219a2cc3f8e1892ccdb0cda6358af293a10d3d724c3c8220ac7a26f0c18`.
- Prepared an invocation of the patched `wkdev` MiniBrowser and ASan logging.
- **No actual Phase 19 matrix output or ASan result was provided.** The expected four passes were predictions only.

The user chose to stop the firmware-specific research project, citing continuing firmware updates. Therefore Phase 19 is recorded **STOPPED / NOT RUN**, not PASS, FAIL or COMPLETE.

See [Phase 15–16 Linux evidence](PHASES-15-16-LINUX-ASAN.md) and [project closeout](PROJECT-CLOSEOUT-2026-11-19.md).
