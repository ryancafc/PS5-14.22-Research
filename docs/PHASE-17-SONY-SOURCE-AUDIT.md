# Phase 17 — Sony-published WebKit 14.00 Canvas source audit

**Date:** 19 November 2026. **Input:** the user's locally held Sony `WebKit_1400.zip` source archive. **Method:** read-only ZIP inventory, SHA-256 of selected files, line-numbered inspection, comparison with vulnerable and patched upstream WebKit. This is a **published-source audit, not retail-binary verification**.

## Exact observed archive and source identifiers

| Item | SHA-256 |
|---|---|
| `WebKit_1400.zip` archive | `e645974579c88ec09c3036ce882fcaea2b0380f9ae4596b163811501d3be9db0` |
| `Source/WebCore/html/HTMLCanvasElement.cpp` | `2455ac5a07e66ac803d101e195af33c7b7a0bd330c29808fdf3eceb6a2d77787` |
| `Source/WebCore/html/OffscreenCanvas.cpp` | `cc62e28adab9dc3d4472ad426080cdeae8618d5e4c35c2d122a0f202cfcc81b3` |
| `Source/WebCore/html/canvas/CanvasRenderingContext2DSettings.idl` | `10e6fae44a87434d93409cb98f7b8ca7fbc93a5c57e3ac55f5f23b95d14b422e` |

The archive contains a `WebKit-1400/WebKit-1400/` prefix in the inspected members. The SHA-256 beginning `2455ac5a` refers to **HTMLCanvasElement.cpp**, not to the entire ZIP.

## HTMLCanvasElement: critical call ordering

The published source checks `m_context` at **line 226**, before calling JS-options dictionary conversion.

| Outer context | Dictionary conversion | Subsequent creator |
|---|---:|---:|
| 2D | `HTMLCanvasElement.cpp:268` | `createContext2d` at 271 |
| BitmapRenderer | :279 | `createContextBitmapRenderer` at 282 |
| WebGL (compile-gated) | :291 | `createContextWebGL` at 294 |

No repeat of the `m_context` guard is present between those conversions and creator calls in the inspected function. The creation helpers themselves contain `ASSERT(!m_context)` followed by assignment, rather than a runtime post-conversion guard:

- `createContext2d`: assertion line 348, assignment **350**.
- `createContextWebGL`: assertion line 412, assignment **436**.
- `createContextBitmapRenderer`: assertion line 482, assignment **484**.

Assertions are not a substitute for a production runtime condition, although final assertions behaviour depends on build configuration.

## OffscreenCanvas source

In `OffscreenCanvas.cpp` an initial detached-state check occurs at **245** and per-type `m_context` checks occur before conversion. The 2D conversion at **256** precedes assignment **259**; BitmapRenderer conversion at **272** precedes assignment **275**; WebGL attributes conversion **294** precedes creator call **297**. The WebGL helper (line 221) has an assertion at 223 and assignment at 238.

The upstream patched version rechecks existing/detached state after conversion. Sony's shown implementation does not have those protections in the corresponding paths. OffscreenCanvas runtime availability is addressed below.

## IDL and PlayStation feature configuration

The Sony Canvas 2D dictionary contains an **unconditional** `boolean desynchronized = false` property; its `alpha` field is commented out; `colorSpace` is gated behind `CanvasColorSpaceEnabled`. The BitmapRenderer dictionary contains an unconditional `boolean alpha = true` property. Property getters on supplied JavaScript option objects are therefore candidate reentrancy entry points even without WebGL.

- `OptionsPlayStation.cmake:272` sets **`ENABLE_WEBGL` default OFF**.
- `PlatformEnable.h` defines OffscreenCanvas-related compile-time defaults, which do **not** by themselves establish runtime exposure.
- `HTMLCanvasElement.idl:48` declares `getContext`; 2D and BitmapRenderer types are in the union independently of the conditional WebGL members.
- `OffscreenCanvas.idl` is gated by `OFFSCREEN_CANVAS` and `OffscreenCanvasEnabled` (with an additional workers condition).
- `UnifiedWebPreferences.yaml:1469–1483` assigns `CanvasColorSpaceEnabled` default **false** outside Cocoa for applicable components.
- `UnifiedWebPreferences.yaml:4758–4774` and `4776–4792` assign `OffscreenCanvasEnabled` and `OffscreenCanvasInWorkersEnabled` default **false** outside Cocoa.

These are **source and preference defaults**; they can be affected by final build settings, runtime overrides and firmware-specific changes.

## Source-audit assessment

**Supported:** the published Sony 14.00 code contains a potentially unsafe Canvas context replacement pattern consistent with the missing post-conversion guard in upstream vulnerable WebKit, and its 2D/BitmapRenderer option dictionaries permit JavaScript getter evaluation.

**Not supported by the archive alone:** an exact mapping from Sony's published 14.00 source to the firmware **14.22 binary**; proof of retail native UAF; claim that WebGL or OffscreenCanvas is exposed in retail; arbitrary memory access; or a PS5 jailbreak.

See [Linux ASan control](PHASES-15-16-LINUX-ASAN.md) and [retail capability observations](PHASE-18-RETAIL-CAPABILITY-TESTS.md).
