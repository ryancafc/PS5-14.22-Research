# Corrected diagnostics and cross-engine validation

**PASS.** `browser/index.html` and `browser/suite.js` are original work. No unlicensed external HTML/JavaScript was copied. `run_browser_tests.py` uses a loopback-only server, fresh temporary native browser profiles and ordinary sandboxes. It serves the same suite in two conditions: no isolation headers, and COOP `same-origin` plus COEP `require-corp`.

| Engine version | Header mode | PASS | FAIL | SKIP | UNSUPPORTED |
| --- | --- | --- | --- | --- | --- |
| Chromium 150.0.7871.181 built on Debian GNU/Linux forky/sid | plain | 21 | 0 | 0 | 0 |
| Chromium 150.0.7871.181 built on Debian GNU/Linux forky/sid | isolated | 21 | 0 | 0 | 0 |
| Mozilla Firefox 140.15.0esr | plain | 21 | 0 | 0 | 0 |
| Mozilla Firefox 140.15.0esr | isolated | 21 | 0 | 0 | 0 |

This is **84 passing check results across four normal runs**, comprising 21 checks repeated in two engines/two contexts. They are not 84 independent security experiments. The distributable harness was replayed with explicit suite/output paths and reproduced the results; repeated harness validation is not added to this headline count.

The nine ordinary integer Atomics operations are expected to succeed on an ordinary Int32Array. Float32 input gives TypeError; out-of-bounds access gives RangeError; non-shared wait gives TypeError; non-shared notify returns zero. TypedArray/DataView storage overlaps normally. A 512-byte transfer detaches the sender and is acknowledged with correct receiver size/content. Same-origin and opaque sandbox frames both acknowledge a unique message; only the opaque frame returns null contentDocument and serializes origin as `null`. An empty eight-byte WebAssembly module compiles/instantiates and memory grows from one to two pages, detaching the old buffer. These replace the inaccurate Phase 20 diagnostic expectations.

Both loopback contexts are secure. Only the isolation-header condition reports crossOriginIsolated and exposes SharedArrayBuffer in these runs. There was no expectation-changing semantic difference between the two tested engines. User-agent strings, binary `--version`, header mode, expected values and observations are retained in per-run JSON. Feature absence means UNSUPPORTED, not a vulnerability. An omitted header expectation means SKIP. Observational feature records do not claim conformance/security verification.

## Harness controls and resources

In Chromium, deliberately requesting an isolated-context expectation while sending plain headers yields **20 PASS /1 FAIL**. Omitting the expectation yields **20 PASS /1 SKIP**. These are harness controls, excluded from the 84 normal results. They demonstrate outcome aggregation is not an unconditional green success. All status branches are implemented; an API-unavailable environment was not synthetically forced to claim a native UNSUPPORTED observation.

The suite has no large allocation mode. It uses 16-byte-or-smaller TypedArray work buffers, a 512-byte transfer, at most two tiny frames (sequential in this implementation), and maximum two WebAssembly pages (128 KiB). Explicit backing-store budget is 256 KiB including small controls and growth overhead; engine/process/JIT/DOM memory is outside that budget. Checks are sequential and asynchronous checks have 3-second timeouts. Channels, listeners and iframes are cleaned up. Native processes are terminated after results and temporary profiles removed. JSON export is available from the page.

The expectations are traceable to [ECMAScript Atomics](https://tc39.es/ecma262/multipage/structured-data.html#sec-atomics), [HTML transfer](https://html.spec.whatwg.org/multipage/structured-data.html#structuredserializewithtransfer), [HTML sandboxing](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-iframe-sandbox), [Secure Contexts](https://www.w3.org/TR/secure-contexts/#is-origin-trustworthy) and [WebAssembly JS API](https://webassembly.github.io/spec/js-api/index.html#dom-memory-grow). `standards-references.json` maps checks to sources. Passing standards behavior does not establish exploitability, memory safety, a working jailbreak or retail PS5 behavior.

`CROSS-BROWSER-RESULTS.csv` contains 126 rows: 84 normal checks and 42 explicit harness-control checks. The replay logs retain all six reproduced summaries. No WebKit/PS5 test was performed; two independent desktop engines satisfy this phase's available-engine requirement.
