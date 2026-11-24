# Browser diagnostics audit

Result: **PASS for source assessment and bounded desktop controls; retail PS5 behavior remains unverified.** All ten HTML pages were reviewed. Only atomics-probe, iframe-sandbox, typedarray-edge's views-only mode and wasm-basic were run from the original repository, after their relevant source was read. Independent small controls supplemented them. No pressure, full/aggressive/slow chain or console test ran.

## Page inventory

| Page | Features or behavior | Assessment |
|---|---|---|
| index.html | Navigation and diagnostic labels | README Quick Scan description is stale |
| webkit-sniff.html | UA/platform, screen, feature presence, optional memory data | Availability is not conformance or vulnerability evidence |
| atomics-probe.html | Nine non-shared integer load/store/RMW operations, isLockFree | Wrong expected TypeError produces nine false anomaly labels |
| typedarray-edge.html | Allocation ramp, overlapping views, buffer transfer, BigInt/Atomics | Views-only mode is small; safe-ramp/ceiling labels are unsupported |
| iframe-sandbox.html | Same-origin versus opaque sandbox document access | Expected null is styled as failure; sandbox messaging is skipped |
| wasm-basic.html | Empty module compile/instantiate, memory grow | Valid small desktop capability check; no JIT/exploit conclusion |
| alloc-pressure.html | Forty retained allocations at selectable step sizes | 2.5/5/10 GiB maxima; not run |
| chain.html | BigInt, Atomics, ImageBitmap, console errors and allocation | Not an exploit chain; final green state can overwrite earlier failures |
| slow-chain.html | Retained allocation ramps and retries | Up to 905 MiB retained; Stop does not clear held buffers |
| notes.html | Run guidance, symptom recording and attribution | A restart alone cannot be classified as a kernel panic |

## Standards correction and observed controls

Current [ECMAScript Atomics algorithms](https://tc39.es/ecma262/multipage/structured-data.html#sec-atomics.add) permit ordinary integer typed-array load/store/read-modify-write operations on non-shared backing buffers. Waiting has a separate shared-buffer requirement; notify on a non-shared buffer returns zero. The original page instead expects TypeError for the nine tested ordinary operations. In sandboxed Chromium **150.0.7871.181**, all nine succeed and all nine receive its unexpected-success label (B01). A separate control confirms the expected TypeError for wait and invalid float-array input, and RangeError for an out-of-range index. No native memory-corruption or PS5 observation follows.

The [HTML iframe model](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-iframe-sandbox) explains the opaque origin created without allow-same-origin. The original page sees an accessible ordinary frame and a null sandbox contentDocument, marking the latter as failure (B07). It returns before sending the sandbox message. The independent small echo control receives an opaque-origin reply even while document access is blocked (B08). These outcomes are compatible, not evidence of sandbox escape.

The views-only test and independent MessageChannel control detach a transferred sender buffer while preserving the receiver's 512 bytes and marker 42 (B09–B10). This agrees with [HTML transfer semantics](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializewithtransfer). Missing ArrayBuffer.transfer support would be a separate capability result, not a vulnerability.

The reviewed Wasm page compiles and instantiates an empty module, grows from one to eleven 64 KiB pages, and reports the previous size as one (B11). This is ordinary [WebAssembly memory growth](https://webassembly.github.io/spec/js-api/index.html#dom-memory-grow). It does not test whether Sony enabled JIT or whether the console exposes Wasm. The largest original Wasm backing store used in the check is 704 KiB.

The independent HTTP loopback control is a secure context without cross-origin isolation and exposes no SharedArrayBuffer constructor. Adding COOP/COEP produces an isolated context with the constructor exposed. The [Secure Contexts specification](https://www.w3.org/TR/secure-contexts/#is-origin-trustworthy) permits trustworthy loopback contexts. Secure-context status and isolation are different measurements; record them with origin and headers (B12).

## Memory accounting and label problems

Static arithmetic, without large allocations:

- Slow-chain warm-up retains 1+2+4+8 = 15 MiB. Its ramp retains 16+48+96+160+240+320 = 880 MiB. Five later 2 MiB buffers bring the requested retained extent to **905 MiB**, not a 320 MiB total cap (B03).
- The largest pressure option retains up to 40 × 256 MiB = **10,240 MiB**, or 10 GiB. The smaller step options can reach 2.5 and 5 GiB (B04).
- These are requested backing-store extents, not measured resident memory. Endpoint writes are not a complete physical-page commitment measurement. Garbage collection and allocator/process state make a universal firmware ceiling inference invalid (B05–B06).
- The full chain catches some failures and ultimately calls paintStatus(true) unconditionally. The slow chain also has clean-finish messaging despite caught inner-stage failures. A green status is not a validated conjunction of results (B13).
- Stop sets a flag and controls but leaves the global held array populated. It is neither a memory-release operation nor a guaranteed interrupt of a blocking allocation.
- Current log labels, static target strings, missing features, console.error output, UI overlays and restarts do not identify a security vulnerability or kernel panic by themselves (B02, B15–B16).

## Reproduction boundaries

The auditor harness used an ephemeral loopback-only server and a fresh sandboxed headless Chromium process. It loaded only a four-page allowlist from the reviewed checkout. Larger modes were never invoked. All positive observations are desktop-specific; one Chromium build is not cross-engine testing and is not a PS5 firmware compatibility matrix. B has no explicit redistribution licence, so its pages are linked rather than included in publication (B17).

Evidence: `browser-results.json`, `browser-allocation-accounting.json`, the source-located B rows, and the local `browser-audit.mjs` harness. Original diagnostic text is represented by derived outcomes and hashes rather than copied HTML.
