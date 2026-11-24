# Third-engine WebKitGTK validation

**PASS for additional desktop validation, with the original failures preserved.** Installed WebKitGTK package 2.52.6-1 was used through MiniBrowser in a private context on a temporary Xvfb display; no browser was reinstalled and no sandbox-disable flag was used. Software display/DRI3 warnings are recorded. The UA contains605.1.15/Version 60.5 tokens; those do not identify a retail PS5 engine build.

The unchanged Phase 21 suite first produced **20 PASS /1 FAIL in each header mode**,40/42 total. In both runs the ordinary same-origin iframe echo timed out. All other checks, including opaque-frame messaging, passed. These results remain in `webkit-original-results.json` and are not relabelled successful.

Four independent bounded iframe controls (ordinary onload, explicit ready acknowledgement, visible onload, opaque onload) then passed in each mode: **8/8**. Their added readiness/trace messages change task timing, so they do not establish a definitive engine root cause. They do establish that ordinary same-origin messaging can succeed in this environment.

Phase 22's original suite adds one unique-token **child-ready acknowledgement before sending the echo request**. It keeps the same expected standards behavior, source-window/origin checks, cleanup and resource limits. With that change, Chromium 150.0.7871.181, Firefox 140.15.0esr and WebKitGTK 2.52.6-1 each pass21/21 checks in plain and COOP/COEP-isolated loopback contexts: **126/126 normal results** across six runs. Chromium's deliberate FAIL/SKIP controls remain separate; no result is an unconditional green indicator.

Both header modes are secure loopback contexts. Only the isolated mode reports crossOriginIsolated/exposes SharedArrayBuffer in these runs. Normal non-shared Atomics succeed; expected Float32/wait errors and bounds errors match. TypedArray overlap,512-byte transfer acknowledgement/detachment, sandbox document isolation, standard messaging and bounded WebAssembly growth all pass. No semantic expectation was relaxed to obtain the successful final result.

The suite retains a 256 KiB explicit backing-store budget,128 KiB maximum WebAssembly memory, tiny buffers and sequential iframe checks with 3-second timeouts. Browser/engine/process/DOM overhead is outside that explicit budget. The independent controls use at most one iframe at a time. No pressure ceiling, stress mode, memory-corruption trigger, exploit chain or console test ran.

Before results40/42, independent controls8/8 and final normal126/126 are different datasets; they are not summed as independent security experiments. The underlying timing cause remains unproven. This is a diagnostic robustness improvement, not proof of a WebKit security defect or retail14.22 behavior. `browser-summary.json`, full result JSON, controls and original/new source hashes provide traceability.
