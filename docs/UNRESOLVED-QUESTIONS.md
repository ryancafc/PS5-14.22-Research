# Unresolved questions and evidence needed

**Last reviewed:** 15 November 2026  
The research has a publication-ready report but **does not resolve** the following security questions.

| Question | Status | Evidence that would materially help |
|---|---|---|
| Why do public Relapse implementations stop supporting versions after 13.60? | **UNKNOWN** | First-hand maintainer diagnosis, attributable regression analysis, or specific vendor advisory |
| Which is the first fixed retail build for the published S3-resume hypervisor issue? | **UNKNOWN** | Sony advisory, original reporter's technical confirmation, or independently documented and authorised build comparison |
| Which named vulnerabilities were fixed specifically in 14.22? | **UNKNOWN** | Sony coordinated disclosure, CVE advisory tied explicitly to 14.22, or original attributable vulnerability report |
| Do the published Sony 14.x WebKit sources correspond exactly to retail 14.22 binaries? | **UNKNOWN** | Authentic build-specific provenance, vendor mapping or properly authorised independent comparison |
| Are the catalogue hashes for historical 14.10 standard and recovery packages authentic? | **UNKNOWN** | Cryptographic SHA-256 computed from authenticated historical Sony package bytes |
| What is the actual security significance of the 54 source changes? | **UNDETERMINED** | Named upstream fixes linked to actual patches, documented compile/runtime mapping, source history beyond sampled snapshots |
| Does `PlayStationWebView.cpp` affect retail runtime behaviour? | **UNKNOWN** | Build-specific source and corroborating implementation evidence |

## Important negative findings

- There was **no named Sony 14.22 vulnerability fix** supported by the reviewed public record.
- There was **no direct match** between the sampled public WebKit advisories and a verified Sony file change.
- **No** first fixed hypervisor build was independently demonstrated, despite 14.10 researcher attribution.
- The checksum conflict has a credible transcription-error explanation, **not** independent byte verification.
- The research **did not demonstrate a complete 14.22 jailbreak**.

None of these says that an undisclosed flaw cannot exist or that no security changes occurred.

## Conditions for further investigation

Prioritise new **original** Sony or researcher disclosures over repeated general searches. Keep firmware standard and recovery package types separate; preserve source revisions and dates. Obtain separate authorisation before any authentic historical package acquisition or console testing. Respect redistribution licences and avoid publishing device secrets, private data or unreviewed payloads.

See [final research dossier](FINAL-RESEARCH-DOSSIER.md) and [public-facing evidence register](FINAL-EVIDENCE-REGISTER.csv).
