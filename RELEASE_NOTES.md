# OSTF 3.4.0 — Native Core Metadata & Composition Interchange

Official specification publication package. Tag: `v3.4.0`.

This release removes private Player-metadata dependencies for common composition information and defines named Core storage for key/modulation, default scales, languages, provenance and shared editing relationships. Concrete saved notes remain the performance authority; import never regenerates or reapplies effects.

## Included

- Complete Japanese and English manuals, parameter references and a complete English specification translation.
- Authoritative Japanese specification and unchanged 3.4 schema from the established release baseline.
- 54 focused standalone examples and 11 complete demo songs, all `.ostf` version 3.4.0.
- Witnesses for all 296 current storage declarations, all 119 explicit enum values and all 3 constants.
- Unchanged 3.0–3.3 schemas, explicit migration/device contracts, source inventory and static reports.
- Exactly 100 extracted files, with no nested archives.

## Compatibility

This is a format release, not a Player/Composer/Editor update. Existing 3.3 devices must be adapted. Read old files as old versions; do not change only the root version string. Unknown data must be retained or saving refused; downgrades require path-level loss reporting.

## Verification boundary

Schema and selected semantic invariants, sample witnesses, source preservation, local links and distribution hashes are checked statically. No DAW/device/UI/audio/MIDI-hardware execution was performed. The included checker is not a certified universal validator or migration engine.

See [readiness](RELEASE_READINESS.ja.md), [coverage](docs/COVERAGE.md) and [license terms](LICENSE.md). Separately supplied musical demos are not relicensed by migration. This prepared archive has not itself been uploaded to GitHub.
