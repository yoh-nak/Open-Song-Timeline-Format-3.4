# OSTF — Open Song Timeline Format

## Version 3.4.0 · Official specification release

**A structured, open song-timeline format with native Core metadata and editing relationships.**

OSTF stores song structure, tempo, meter, harmony, concrete performance notes, percussion identity, lyrics and shared composition information in UTF-8 JSON files with the **`.ostf`** extension.

In 3.4, common information no longer depends on Player-specific metadata or an additional extension implementation. Initial keys, modulation, default scales, languages, provenance, localization, presentation, relative phrases, generation intent, phrase libraries and clip choices have named, typed Core locations. Unknown legacy payloads may still be preserved; they never override standardized current Core.

[日本語 README](README_JA.md) · [Complete manual](docs/COMPLETE_MANUAL.en.md) · [Complete reference](docs/PARAMETER_REFERENCE.en.md) · [Specification](docs/FORMAT_SPECIFICATION.en.md)

### Read first

| Document | Purpose |
|---|---|
| [Complete manual — EN](docs/COMPLETE_MANUAL.en.md) / [JA](docs/COMPLETE_MANUAL.ja.md) | Authoring workflow plus all feature semantics |
| [Parameter reference — EN](docs/PARAMETER_REFERENCE.en.md) / [JA](docs/PARAMETER_REFERENCE.ja.md) | Every definition, constraint, branch and example pointer |
| [Normative specification — JA](docs/FORMAT_SPECIFICATION.ja.md) / [EN translation](docs/FORMAT_SPECIFICATION.en.md) | Current 3.4 semantic rules |
| [3.4 JSON Schema](schema/ostf-3.4.0.schema.json) | Structural authority; local/offline resolution |
| [Complete coverage index](docs/COVERAGE.md) | All 296 current storage declarations, 119 enum values and 3 constants |
| [54 focused examples](samples/INDEX.md) / [11 complete demo songs](demos/README.md) | 65 standalone `.ostf` documents, all version 3.4.0 |
| [Migration rules](docs/MIGRATION_3_3_TO_3_4.ja.md) / [Device contract](docs/DEVICE_CONTRACT.ja.md) | Explicit conversion, authority, preservation and merge boundaries |
| [Implementation checklist](docs/IMPLEMENTATION_CHECKLIST.md) / [Issue register](docs/ISSUE_REGISTER.ja.md) | Implementation duties and the 28-item design review |

### Key principles

- **One authority for each kind of information.** `song.key` is the initial key; `timeline.keyChanges` contains later changes. Keys, scales and temporary playback transposition are distinct.
- **Concrete notes are the saved performance.** Loading never reruns generation, reapplies swing or materializes chords/templates/choices automatically.
- **Preserve authored data.** Do not replace missing keys with C major, unknown genres with Pop, or original text with interface translations. IDs, timing, gates, velocity and opaque precision matter.
- **Explicit edits and migration.** Shared song metadata is not overwritten by a track-only merge. Unsupported information must be preserved or editing refused; loss requires disclosure and approval.

### Package layout and size

This edition contains **exactly 100 files after extraction**, including the manifest. There are no nested archives or hidden extra sample bundles.

```text
README.md / README_JA.md          Overview and navigation
CHANGELOG.md / RELEASE_NOTES.md   Version and release information
LICENSE.md                       Project terms and demo-rights boundary
RELEASE_READINESS.ja.md           Static release assessment
PACKAGE_MANIFEST.json             Sizes and SHA-256 for the other 99 files
requirements.txt                 Static-documentation tooling dependencies
docs/                            12 documents, including bilingual manuals/references
schema/                          3.4 plus unchanged 3.0–3.3 schemas (5 files)
samples/                         54 standalone examples + index
demos/                           11 complete songs + index
audit/                           5 machine-readable source/coverage/check records
tools/                           3 static documentation/checking programs
```

The earlier package's source archives are not embedded to work around the limit. Their hashes and preservation records are in [source inventory](audit/SOURCE_INVENTORY.json). The previously established Japanese normative specification and all five schemas are retained without semantic changes.

### Static checks

```sh
python -m pip install -r requirements.txt
python tools/check_release.py
```

The checks use bundled schemas, not remote retrieval. `check_package.py` checks data; `build_catalogue.py` regenerates references and witnesses. These are distribution tools, **not a certified universal OSTF validator, player or migration library**.

### Compatibility and scope

Read old files under their original version. Do not relabel 3.3 as 3.4 without migration. A 3.3 device is not automatically a 3.4 device; no updated `.amxd` is included.

CC, Pitch Bend, Aftertouch, MPE, audio clips, continuous tempo curves, plug-in state restoration and complete engraving are outside 3.4. They are not unfinished mandatory extensions.

**No device, DAW, UI, audio or MIDI-hardware runtime testing was performed for this specification publication.** Static results do not certify existing Player/Composer/Editor devices. See [release readiness](RELEASE_READINESS.ja.md) and [machine-readable results](audit/RELEASE_STATIC_CHECK.json).

### Publishing and license

Suggested repository: `Open-Song-Timeline-Format-3.4`. Release tag: `v3.4.0`. See the [publishing guide](docs/GITHUB_PUBLISHING.ja.md). This package is ready to upload; generating it did not publish a remote repository or release.

Specification, schemas, documentation and synthetic examples retain the supplied project's CC BY 4.0 terms; helper programs retain MIT terms. Separately supplied musical demos retain their original applicable rights and are not relicensed by conversion. See [LICENSE](LICENSE.md).
