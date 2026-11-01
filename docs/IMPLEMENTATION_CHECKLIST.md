# OSTF 3.4.0 — Implementation Checklist / 実装チェックリスト

This checklist is a conformance work plan, **not a claim that any device already passes it**. The normative specification governs. No runtime tests were performed for this publication.

## Reader / 読込

| Contract | Representative example |
|---|---|
| Select exact root version; no silent upgrade, missing-key or genre defaults | 01, 02, 51 |
| Decode UTF-8; reject duplicate keys/BOM/lone surrogates; retain opaque numeric precision | 17, 50 |
| Use song.key at tick 0 and keyChanges later; distinguish atonal/unspecified/unsupported | 03, 24 |
| Keep default and timed scales separate; resolve explicit targets without guessing | 04–06, 39 |
| Preserve author text, open modes/roles/genres/moods/languages | 05, 09, 23, 24 |
| Read existing standard credits/voicing/tempo/meter/primary references | 10, 20, 23, 34, 36 |
| Perform saved notes only; never auto-generate, choose, synchronize or re-swing | 12–15, 42, 45, 46, 52 |
| Distinguish logical Slot ID, kit membership, MIDI mapping and preview sound | 19, 21, 31–33 |
| Honor full gates, disabled data, pickups, overlaps and rational bar arithmetic | 07, 08, 25–30 |
| Preserve unsupported Core and unknown extensions without promoting legacy authority | 17, 49, 50 |

## Writer / 編集・保存

| Contract | Required behavior |
|---|---|
| Stable identity | Moves retain IDs; independent copies get new IDs; template source IDs remain local |
| Explicit scope | A note/track merge does not silently replace shared song metadata |
| Ref integrity | Update dependent references atomically; invalid Core references are not excused by stale |
| Protected notes | Freeze before operation; compare IDs, targets, rational onset, gate, velocity and enabled state |
| Relationship status | Recompute or mark stale/unverified; do not leave unhandled relationships current |
| Phrase replacement | Update every affected instance/map/note together; retain surviving occurrence IDs |
| Velocity semantics | Independent preserves concrete values; linked compares both presence and value |
| Choices | Selection and managed clip.enabled update together; parent mute stays independent |
| Localization | Source field exists in current state; target/field/language unique; inherited dictionaries agree |
| Transpose | Temporary state does not mutate Core; committed edits do not transpose drums or double-transpose linked phrases |
| PPQ conversion | Change every time field exactly; refuse or disclose rounding/limits |
| Save | All-or-nothing; preserve unknown precision and unsupported fields or refuse |

## Migration / 移行

Read an old document under its own schema. Identify exact known profile versions. Preserve source bytes/hashes outside the new file, preview destination mappings, and obtain explicit approval. Map old scoped IDs to new global IDs and update all known references. Do not parse unknown vendor payloads by guesses. Do not infer song scale, primary lyrics or composition credit merely to fill fields. Preserve old status; no unverified-to-current promotion without checking.

## API/DAW boundary / 形式外との境界

The format does not assign a particular Live track, require a specific plug-in, launch external resources or reproduce a generator's internal state. Resource and prompt text are data, not commands. External MIDI may lose slot identity, routing, same-pitch voice identity or timing precision; report the boundary instead of claiming lossless export.

## Release gates / 各デバイスの別工程

Implementers must separately review rendering, file dialogs, cancellation, load/save restoration, audio, MIDI output, UI and host-specific behavior. Static example success does not prove these. Known unsupported features must be visible and protected from destructive writes.

Sources: [normative specification](FORMAT_SPECIFICATION.ja.md), [English translation](FORMAT_SPECIFICATION.en.md), [device contract](DEVICE_CONTRACT.ja.md), [migration rules](MIGRATION_3_3_TO_3_4.ja.md).
