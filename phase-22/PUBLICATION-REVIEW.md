# Publication review

PASS for this reviewed subset; the research verdict remains PARTIAL.

- Phase 20 PR3 and Phase 21 PR4 were unmerged. New Phase 22 base is exact Phase 21 head db552e5000f76581b34e48be5d80daeb2aca3f47. Earlier branches/documents are preserved; no merge, close or force push is performed.
- Root README adds verified results and explicit failures/blockers. Status retains UNKNOWN and historical Phase 20/21 counts. Existing automatic status workflow is unchanged.
- Original source tests/tools, focused GPL-derived patches, licence notices, reports/CSVs and sanitized JSON/selected logs are included. All three CSVs were inspected and exact-readback reconciled with the bundled Artifact Tool, with 34/12/22 rows.
- Binary files are ONLY the 26 tiny from-scratch synthetic ELF cases listed with hashes in fixtures/manifest.json. They are parser test data, not acquired executable compatibility evidence or exploitation tools. Each is at most 2048 bytes and is never executed.
- No real SDK/homebrew ELF, firmware package, protected key, credential, proprietary executable, third-party release archive, JAR or Ghidra database is published. Private paths/usernames are replaced with placeholders in derived evidence. Raw original logs and binaries remain local.
- Two checked-error cases improve; raw 14/26 and SDK 3/11,3/13 partial results are not hidden. Original WebKit40/42 remains distinct from the readiness variant126/126. Installed extension is unchanged.
- SHA256SUMS.txt covers this subset excluding itself. Local evidence has a separate manifest. Actual publication URL/commit is recorded in the final local receipt/chat; no main merge is implied.
