# Phase 20 final report

24 November 2026. **Overall verdict: PASS for the permitted external-research audit.** Several underlying compatibility, decryption, patch-attribution and hardware claims remain unverified or blocked. **No working retail 14.22 jailbreak was demonstrated. Probability remains UNKNOWN.**

## Claim totals

54 significant claim units were reviewed: 37 from Repository A and 17 from B. **11 independently verified; 4 reproduced locally on desktop; 13 unverified; 6 contradicted.** The remaining 20 are 10 source-supported, 6 author-reported, 2 simulation-only and 2 blocked. Each has a source file, pinned source commit, line locator, method, observation, limitation and verdict in the evidence register.

## Findings

1. Fresh complete-file hashes and a separate outer-range hash corroborate the existing firmware identities and extraction. SLB2 version 3, one entry at 0x400, sector-count arithmetic and 387 zero padding bytes agree with A. No firmware was changed or decrypted.
2. B's ordinary non-shared Atomics expectation is wrong. The original diagnostic gives nine false anomaly labels under normal desktop behavior. Its sandbox page also calls expected isolation a failure and skips sandbox messaging. Controlled tiny tests reproduced these findings without console access.
3. The slow-chain source can retain 905 MiB despite its 320 MB total-cap implication. The pressure page can request 10 GiB. Neither large mode was executed. Final green/clean labels are not reliably linked to all stage outcomes.
4. A's TCP demonstration explicitly uses a mock-kernel backend. Some optional checks are counted as PASS when skipped. The documentation contains incompatible stage/test summaries without a single pinned run manifest. None is evidence of successful retail exploitation.
5. Kernel comparisons concern older 13.60 inputs that are absent here. Public JIT defaults, CVE descriptions, source findings and SDK address arithmetic do not map automatically to retail 14.22. A's numerical jailbreak estimate is unsupported.
6. Fresh static ELF decoding confirms the previous homebrew library names and relocation types: elfldr has 140 RELATIVE plus 24 GLOB_DAT; the compatible sample has 402 RELATIVE plus 165 JUMP_SLOT. Earlier Ghidra APPLIED/decompilation results were preserved and reviewed, not newly rerun.

## Corrections and preserved history

Use ordinary non-shared Atomics success as an expected result. Distinguish secure context, isolation and API availability. Report cumulative allocation requests in MiB and do not equate them with resident memory. Limit the 117/115 differing-byte metric to its documented 0x000–0x440 window. Keep prologue field widths, shared magic and segment-count formula hypotheses explicit. Separate loader-helper BSS behavior from startup initialization. Keep older-build/source claims separate from retail 14.22 behavior.

Both incorporated checkouts and prior research inputs were preserved. Historical Phases 1–19 were not rewritten. Publication was prepared from the current official main commit `9622db46f50a8ab4cc540f39b315dd9cb0e2752e` in a separate branch, preserving the existing local checkout. The README update is additive; the status file retains UNKNOWN with the audit basis. `PUBLICATION-REVIEW.md` records the reviewed scope and exclusions; the final chat records the actual publication location/status.

## Files created and checks

All ten requested deliverables are present: README.md, REPOSITORY-AUDIT.md, CLAIM-AUDIT.csv, FIRMWARE-VERIFICATION.md, GHIDRA-REVIEW.md, BROWSER-DIAGNOSTICS-REVIEW.md, EVIDENCE-REGISTER.csv, LIMITATIONS.md, PHASE-20-FINAL-REPORT.md and SHA256SUMS.txt. Additional JSON evidence, selected logs and auditor scripts support reproduction. The two CSVs were authored/inspected with the bundled Artifact Tool, read back, reconciled by Claim ID and classification counts, and checked for complete source locators. Their counts were not taken from hardcoded prose alone.

## Objective status and remaining work

Inventory, claim classification, existing-14.22 container verification, executable-document review, benign desktop diagnostic assessment, evidence registration and publication preparation: **PASS**. Older/recovery-package comparisons and retail PS5 reproduction: **BLOCKED** by specific absent inputs/environment. Cross-engine breadth: **PARTIAL**, one desktop engine tested. The detailed status table is in README.md.

Phase 21 should correct the small diagnostic expectations, add another desktop engine, acquire missing permissible provenance/raw evidence and expand lawful loader regression coverage. Protected firmware code, retail patch boundaries and a numerical jailbreak probability remain outside what this evidence establishes.
