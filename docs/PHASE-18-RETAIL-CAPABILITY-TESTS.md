# Phase 18 — PS5 14.22 retail User's Guide capability and getter checks

**Observed:** 19 November 2026, local report submission at **12:14:50**. **Environment:** the user's PS5 14.22 User's Guide web view, a locally hosted diagnostic page delivered through DNS-based guide routing and HTTPS, and a Windows laptop collecting results. **No firmware change and no deliberate UAF trigger in these seven checks.**

## Submitted results (verbatim values)

```text
18.1 Canvas 2D availability: available=true
18.2 BitmapRenderer availability: available=true
18.3 WebGL availability: available=false
18.4 OffscreenCanvas constructor: available=false
18.5 2D desynchronized getter: getter_calls=1, context=true
18.6 BitmapRenderer alpha getter: getter_calls=1, context=true
18.7 Repeated 2D context identity: same_context=true
```

The server reported `POST /api/results HTTP/1.1` with HTTP **200** and a timestamped local text report. These are **operator-supplied logs**, not a report independently downloaded from the console by the GitHub publisher.

## How the local transport evolved

- Initial Python HTTP hosting returned a **404** due to an incorrect served file/path.
- A local HTTP/DNS User's Guide kit successfully resolved the guide hostname on Windows, but PS5 network access failed when the PC was configured as primary DNS.
- Windows tests reported ordinary DNS forwarding and local guide redirection; private-network firewall rules were enabled.
- Restoring the PS5's previous trusted DNS restored its internet connection.
- A revised **DNS + HTTPS** guide host subsequently loaded in the PS5 User's Guide.
- A follow-up host added a **Send Results to Laptop** button. The PS5 web view submitted the seven recorded checks successfully and the Windows server saved them.

The recorded local network addresses, Windows username and report folder have been deliberately omitted from this public version; they are unnecessary to evaluate the diagnostic result. The original kits, HTTPS certificate and receipt text are not uploaded here. A locally trusted test host should not be represented as a secure production web service.

## Interpretation

1. In this tested web view, a 2D context and BitmapRenderer context can each be created.
2. Getter evaluation on `desynchronized` (2D) and `alpha` (BitmapRenderer) occurs during normal options conversion.
3. WebGL and the OffscreenCanvas constructor were **unavailable in the observed test**; this is narrower than proving the feature is absent from every PS5 environment.
4. A repeated ordinary 2D request returned the same context identity.

These checks establish **capability and getter reachability**. They do **not** demonstrate reentrant context replacement, stale native references, forced GC, heap-use-after-free, code execution or a firmware 14.22 jailbreak.

The separate Phase 14 witness describes a reentrant behavioural scenario, with its own provenance and limitations. See [Phase 14](PHASES-11-14-RETAIL-CLAIMS.md), [Sony source](PHASE-17-SONY-SOURCE-AUDIT.md), [closeout](PROJECT-CLOSEOUT-2026-11-19.md).
