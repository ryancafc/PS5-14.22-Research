# Phase 7 — Upstream WebKit provenance and advisory correlation

**Status:** Completed, 15 November 2026  
**Research mode:** Public documentation, pinned upstream revisions, and local source comparison. This summary reflects the Codex Phase 7 reports supplied to the project; their source inventory and individual path-by-path evidence have **not** been independently audited in this GitHub repository.

## Main result

Of the **27 changed production-tree files** identified in Phase 6:

| Upstream-provenance observation | Files |
|---|---:|
| Matching path exists in sampled upstream WebKit tree | 26 |
| No sampled upstream path counterpart | 1 |
| Exact content matches to either Sony copy at the sampled upstream revisions | **0** |

**Interpretation:** A corresponding upstream path helps establish shared component identity, **not** the provenance, origin, purpose or date of the actual Sony change. Zero byte-for-byte matches at the selected snapshots does **not** prove that the files are wholly PlayStation-specific, that Sony created all changes, or that no matching upstream revision exists elsewhere in history.

The remaining file, `PlayStationWebView.cpp`, is identified as PlayStation-specific UI integration. Its change purpose and retail runtime effect remain unverified.

## Security advisory correlation

The Phase 7 review sampled public advisory records and upstream revision snapshots. **None of the sampled advisories was directly connected to a verified Sony source change.** This means there is *no evidenced advisory-to-change mapping within the sample* — not that the archives contain no security fixes, or that 14.22 is vulnerability-free.

The relevant primary source groups include:

- [Sony PS5 WebKit source catalogue](https://www.playstation.com/en-us/oss/ps5/webkit/)
- [WebKit upstream source repository](https://github.com/WebKit/WebKit)
- [WebKit security policy](https://webkit.org/security-policy/)
- [WebKit bug tracker](https://bugs.webkit.org/)
- [Apple security releases](https://support.apple.com/en-us/100100)
- [Sony PS5 firmware release notes](https://www.playstation.com/en-gb/support/hardware/ps5/system-software-info/)
- [Relapse 14.00 issue](https://github.com/soniciso1/relapse/issues/3)

## Outstanding limitations

1. Upstream analysis was **bounded to selected pinned revisions**; zero exact matches there is not an exhaustive repository-history result.
2. No source-to-retail-binary mapping has been established for firmware 14.22.
3. No particular WebKit file difference has been attributed to a named Sony security fix.
4. The public 13.60 Relapse support ceiling remains unexplained by direct patch evidence.
5. The exact runtime significance of the `PlayStationWebView.cpp` difference remains unknown.

Phase 7 produced five local deliverables: upstream revision report, public advisory matrix, PlayStation-specific analysis, a 27-row provenance CSV, and research conclusions. The original local reports and CSV are **not uploaded here**.

## Recommended next research

- **Phase 8:** firmware package identity and checksum verification, especially the reported standard-vs-recovery 14.10 SHA-256 discrepancy.
- **Phase 9:** independent audit of local comparison inputs, hashes, and evidence quality.
- **Phase 10:** final research dossier preserving explicit uncertainty.

**No new exploit chain, jailbreak, or confirmed retail 14.22 vulnerability fix is demonstrated by this phase.**

See [Phase 6 validation](PHASE-6-COMPARISON-VALIDATION.md), [firmware and exploit evidence](FIRMWARE-AND-EXPLOIT-EVIDENCE.md), and [sources and next steps](SOURCES-AND-NEXT-STEPS.md).
