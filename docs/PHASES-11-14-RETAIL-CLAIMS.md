# Phases 11–14 — Retail browser baselines, claim review and Canvas witness

**Recorded:** 16 November 2026. **Research target:** PS5 system software 14.22. **Evidence type:** operator-submitted observations and local claim reviews. **Do not interpret these reports as native-code execution or a jailbreak.**

## Phase 11 — Benign browser runtime baseline

- **11B / diagnostic v3.0:** 10 of 10 ordinary capability checks reported PASS on a PS5 14.22 browser view: Canvas, ResizableArrayBuffer, TypedArrays, BigInt, WeakRef, FinalizationRegistry, exceptions, JSON, Promise and Worker.
- **11C / diagnostic v4.0:** three fresh sessions, 14 checks per session, **42/42 PASS with zero reported differences**. The repeatability observation covers ordinary API behaviour, not memory-safety under adversarial input.
- Nothing here establishes the exact shipped WebKit revision, underlying binary mitigations, arbitrary memory access or firmware exploitability.

## Phase 12 — Claim classification

The project classified **20 research claims**, distinguishing primary upstream WebKit evidence from third-party PS5 reports and unverified firmware implications.

- The upstream Canvas `getContext()` reentrancy problem (WebKit Bug 313175, discussed under CVE-2026-43720) has an identifiable upstream fix.
- A third-party description of Canvas alias behaviour on 14.22 was treated as **reported**, not independently confirmed by Phase 12.
- Sony's public 14.22 notes did not establish a named fix for this defect.
- No claim of native PS5 use-after-free, 14.22 exploit chain or released jailbreak was accepted.

The original 20-row local claim register is **not included** in this repository.

## Phase 13 — Claim-quality audit

A subsequent **13-claim audit** rejected several unsupported escalations:
- A claimed **1,651-pointer address leak** was not substantiated: the raw beacon reviewed reportedly contained **zero candidate pointers**.
- A claimed working JIT capability was **withdrawn**.
- A FontFace-related log was **empty**; no successful memory-safety result followed.
- An address-region attribution did not establish a firmware-specific address layout.
- No demonstrated address disclosure, arbitrary read/write, userland code execution or jailbreak resulted.

This is an audit of evidence quality. Negative evidence is bounded to the inspected inputs; it does not establish the global absence of vulnerabilities.

## Phase 14 — PS5 Canvas reentrancy behavioural witness

A user-reported retail PS5 14.22 browser test (14A) produced:

```text
getterCalls=1
inner2dCreated=true
outerBitmapCreated=true
```

A separate **14B** retail run reportedly reproduced the same three values. A Chromium control reportedly returned `outerBitmapCreated=false` in the analogous test.

This is **behavioural evidence** consistent with a reentrant outer context request creating a different context after an inner `2d` context was constructed. The record does **not** include a native crash trace, stale-wrapper access, forced garbage collection, heap spray, arbitrary memory read/write or code execution on PS5.

The two PS5 observations support investigating the suspected missing post-conversion guard, but do not prove a use-after-free on firmware 14.22. Source and compiler/build differences may affect the explanation. The exact original 14A/14B page source and raw server logs are retained only in local project history, not in this GitHub archive.

## Relationship to subsequent phases

- Phase 15/16 reproduced and compared the defect on **Linux upstream WebKit**, a different runtime platform.
- Phase 17 examined **Sony's public 14.00 source**, not an authenticated 14.22 binary.
- Phase 18 established the ordinary feature/getter surface independently without triggering nested context creation.
- Phase 19 was prepared but not executed; the project stopped 19 November 2026.

See [Linux ASan](PHASES-15-16-LINUX-ASAN.md), [Sony source audit](PHASE-17-SONY-SOURCE-AUDIT.md), [retail capability checks](PHASE-18-RETAIL-CAPABILITY-TESTS.md) and [closeout](PROJECT-CLOSEOUT-2026-11-19.md).
