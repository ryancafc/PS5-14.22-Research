# GhidraProspero source, backups and builds

**PASS for the review and isolated diagnostic improvement; broader compatibility remains partial.** Installed extension version 12.2, source revision `e529ef4dd3edbb78400f30492db7c82802a1a117`, Ghidra 12.2, Java 25.0.5 and Gradle 9.2.1 were checked without reinstalling software.

The pre-existing working repair is preserved in `existing-repair.patch`: ordinary PT_LOAD virtual-address fallback when PT_SCE_DYNLIBDATA is absent, and standard relocation fallback where appropriate. The source checkout's existing diff remains byte-identical to the captured diff. Original23November extension/source backups exist; a fresh installed-JAR copy and original repaired-header copy were made before experimentation.

Rebuilding the existing repair in an independent source worktree/cache produces **exactly the installed JAR SHA-256**:

`73da132910d1102fc1e3548458cd8eb95ffada7f829bf65db036f5d7365be494`

The isolated two-line checked-error build has SHA-256:

`e8061d69ba5e76adaa2726cb26bf25c6cf2a57588557395b7b87839b7ddf1699`

Zip-entry comparison finds exactly one changed class: ProsperoElfHeader.class. Extension discovery in fresh static runs confirms the experimental config/JAR path; normal installed runs retain their original path. A separate XDG_CONFIG_HOME, projects and build outputs keep original/experimental states distinct. No working extension is overwritten or promoted.

The full regression after the diagnostic patch preserves567/567,20/20 and 164/164 APPLIED results and both previous compiler controls. The newly discovered SDK partial-import counts are identical before/after. The patch does not claim to fix mapping gaps, validate all malformed files, support ABI 3 genuinely or analyse protected retail code.

`extension-review.json` records hashes, backup identities, patch hashes and unchanged installation/source status. Build/version/parse/import logs are retained. The original-repair rebuild and new diagnostic rebuild completed successfully; a restricted-shell version query and an early path mistake were routine orchestration issues, not extension defects. Only successful builds are used as reproducibility evidence.

See [build instructions](BUILD-REPRODUCTION.md) for the exact pinned source, ordered patches, compiler commands and isolated configuration. Ghidra-derived patches retain GPL-3.0 and upstream attribution; original audit tools/fixtures use MIT. Binary extension archives and local project databases are excluded from publication.
