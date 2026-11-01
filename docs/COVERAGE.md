# OSTF 3.4.0 — 全項目・列挙値・サンプル対応表 / Complete Coverage Index

Authority: [Schema](../schema/ostf-3.4.0.schema.json) and [normative specification](FORMAT_SPECIFICATION.ja.md).

| Metric | Covered / total |
|---|---|
| Current storage-property declarations / 現行実データ宣言 | 296 / 296 |
| Explicit enum values, per declaration / 宣言別列挙値 | 119 / 119 |
| Explicit constants / 定数宣言 | 3 / 3 |
| Current definitions / 現行定義 | 77 |
| Frozen compatibility definitions / 凍結互換定義 | 65 |
| Standalone OSTF 3.4 documents / 独立した.ostf | 65 |

**網羅の定義:** 現行Coreの有限な実データ宣言と明示enumの全値について、実ファイルとJSON Pointerを列挙します。新規項目だけではなく継承項目も含みます。条件判定・制約強化の重複宣言、凍結旧領域、任意の文字列・辞書キー、全組合せ、全数値、全実装の動作は母数に含めません。

**Coverage boundary:** Finite current storage declarations and every explicit enum option, including inherited fields. Predicate/refinement copies, frozen legacy internals, open strings/maps, all numeric values, all combinations and runtime behavior are not claimed as exhaustively tested.

References list all 77 current definitions plus the root and all 65 frozen definitions. [Sample index](../samples/INDEX.md) explains intentional warnings and boundary cases. [Machine-readable report](../audit/FIELD_COVERAGE.json).

## 1. Every current storage declaration / 全実データ宣言

| # | Schema Pointer | `.ostf` witness + JSON Pointer |
|---|---|---|
| 1 | `#/properties/format` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/format` |
| 2 | `#/properties/version` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/version` |
| 3 | `#/properties/ppq` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/ppq` |
| 4 | `#/properties/song` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/song` |
| 5 | `#/properties/timeline` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline` |
| 6 | `#/properties/harmony` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/harmony` |
| 7 | `#/properties/tracks` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/tracks` |
| 8 | `#/properties/soundSlots` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/soundSlots` |
| 9 | `#/properties/lyrics` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/lyrics` |
| 10 | `#/properties/resources` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/resources` |
| 11 | `#/properties/extensions` | [samples/17_legacy_conflict_core_wins.ostf](../samples/17_legacy_conflict_core_wins.ostf) `/extensions` |
| 12 | `#/properties/drumKits` | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/drumKits` |
| 13 | `#/properties/contributors` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/contributors` |
| 14 | `#/properties/document` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document` |
| 15 | `#/properties/relativePhrases` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases` |
| 16 | `#/properties/generation` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation` |
| 17 | `#/properties/presentation` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation` |
| 18 | `#/properties/phraseLibrary` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary` |
| 19 | `#/properties/clipChoices` | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices` |
| 20 | `#/properties/localization` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization` |
| 21 | `#/properties/provenance` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance` |
| 22 | `#/$defs/ref/properties/type` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/appearance/objectColors/0/target/type` |
| 23 | `#/$defs/ref/properties/id` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/appearance/objectColors/0/target/id` |
| 24 | `#/$defs/range/properties/start` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/inputs/0/readRange/start` |
| 25 | `#/$defs/range/properties/duration` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/inputs/0/readRange/duration` |
| 26 | `#/$defs/spelledPitchClass/properties/step` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/key/tonic/step` |
| 27 | `#/$defs/spelledPitchClass/properties/alter` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/key/tonic/alter` |
| 28 | `#/$defs/song/properties/title` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/song/title` |
| 29 | `#/$defs/song/properties/primaryMelodyTrackId` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/primaryMelodyTrackId` |
| 30 | `#/$defs/song/properties/localizedTitles` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/song/localizedTitles` |
| 31 | `#/$defs/song/properties/subtitle` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/song/subtitle` |
| 32 | `#/$defs/song/properties/description` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/song/description` |
| 33 | `#/$defs/song/properties/alternateTitles` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/alternateTitles` |
| 34 | `#/$defs/song/properties/credits` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/credits` |
| 35 | `#/$defs/song/properties/genres` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/genres` |
| 36 | `#/$defs/song/properties/key` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/key` |
| 37 | `#/$defs/song/properties/scale` | [samples/04_scale_without_key.ostf](../samples/04_scale_without_key.ostf) `/song/scale` |
| 38 | `#/$defs/song/properties/languages` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/languages` |
| 39 | `#/$defs/song/properties/primaryLyricDocumentId` | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/song/primaryLyricDocumentId` |
| 40 | `#/$defs/song/properties/moods` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/moods` |
| 41 | `#/$defs/song/properties/rights` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/rights` |
| 42 | `#/$defs/section/properties/id` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/timeline/sections/0/id` |
| 43 | `#/$defs/section/properties/name` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/timeline/sections/0/name` |
| 44 | `#/$defs/section/properties/start` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/timeline/sections/0/start` |
| 45 | `#/$defs/section/properties/duration` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/timeline/sections/0/duration` |
| 46 | `#/$defs/section/properties/role` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/timeline/sections/0/role` |
| 47 | `#/$defs/section/properties/localizedNames` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/timeline/sections/0/localizedNames` |
| 48 | `#/$defs/tempo/properties/at` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/tempoChanges/0/at` |
| 49 | `#/$defs/tempo/properties/bpm` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/tempoChanges/0/bpm` |
| 50 | `#/$defs/meter/properties/at` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/meterChanges/0/at` |
| 51 | `#/$defs/meter/properties/numerator` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/meterChanges/0/numerator` |
| 52 | `#/$defs/meter/properties/denominator` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/meterChanges/0/denominator` |
| 53 | `#/$defs/meter/properties/beatGroups` | [samples/07_pickup_additive_midbar_meter.ostf](../samples/07_pickup_additive_midbar_meter.ostf) `/timeline/meterChanges/0/beatGroups` |
| 54 | `#/$defs/timeline/properties/sections` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/sections` |
| 55 | `#/$defs/timeline/properties/tempoChanges` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/tempoChanges` |
| 56 | `#/$defs/timeline/properties/meterChanges` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/meterChanges` |
| 57 | `#/$defs/timeline/properties/keyChanges` | [samples/03_modulation_atonal_and_unspecified.ostf](../samples/03_modulation_atonal_and_unspecified.ostf) `/timeline/keyChanges` |
| 58 | `#/$defs/timeline/properties/duration` | [samples/07_pickup_additive_midbar_meter.ostf](../samples/07_pickup_additive_midbar_meter.ostf) `/timeline/duration` |
| 59 | `#/$defs/timeline/properties/barOrigin` | [samples/07_pickup_additive_midbar_meter.ostf](../samples/07_pickup_additive_midbar_meter.ostf) `/timeline/barOrigin` |
| 60 | `#/$defs/chord/properties/id` | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/id` |
| 61 | `#/$defs/chord/properties/start` | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/start` |
| 62 | `#/$defs/chord/properties/duration` | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/duration` |
| 63 | `#/$defs/chord/properties/label` | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/label` |
| 64 | `#/$defs/chord/properties/root` | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/root` |
| 65 | `#/$defs/chord/properties/intervals` | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/intervals` |
| 66 | `#/$defs/chord/properties/bass` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/harmony/chords/0/bass` |
| 67 | `#/$defs/chord/properties/voicing` | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/voicing` |
| 68 | `#/$defs/scale/properties/id` | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/id` |
| 69 | `#/$defs/scale/properties/start` | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/start` |
| 70 | `#/$defs/scale/properties/duration` | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/duration` |
| 71 | `#/$defs/scale/properties/label` | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/label` |
| 72 | `#/$defs/scale/properties/tonic` | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/tonic` |
| 73 | `#/$defs/scale/properties/intervals` | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/intervals` |
| 74 | `#/$defs/scale/properties/targets` | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/targets` |
| 75 | `#/$defs/harmony/properties/chords` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/harmony/chords` |
| 76 | `#/$defs/harmony/properties/scales` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/harmony/scales` |
| 77 | `#/$defs/instrument/properties/name` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/instrument/name` |
| 78 | `#/$defs/instrument/properties/family` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/instrument/family` |
| 79 | `#/$defs/instrument/properties/localizedNames` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/instrument/localizedNames` |
| 80 | `#/$defs/note/properties/id` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/notes/0/id` |
| 81 | `#/$defs/note/properties/start` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/notes/0/start` |
| 82 | `#/$defs/note/properties/duration` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/notes/0/duration` |
| 83 | `#/$defs/note/properties/pitch` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/notes/0/pitch` |
| 84 | `#/$defs/note/properties/soundSlotId` | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/tracks/0/clips/0/notes/1/soundSlotId` |
| 85 | `#/$defs/note/properties/velocity` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/notes/0/velocity` |
| 86 | `#/$defs/clip/properties/id` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/id` |
| 87 | `#/$defs/clip/properties/name` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/name` |
| 88 | `#/$defs/clip/properties/start` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/start` |
| 89 | `#/$defs/clip/properties/duration` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/duration` |
| 90 | `#/$defs/clip/properties/enabled` | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/tracks/0/clips/0/enabled` |
| 91 | `#/$defs/clip/properties/notes` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/notes` |
| 92 | `#/$defs/clip/properties/localizedNames` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/clips/0/localizedNames` |
| 93 | `#/$defs/track/properties/id` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/id` |
| 94 | `#/$defs/track/properties/name` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/name` |
| 95 | `#/$defs/track/properties/role` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/role` |
| 96 | `#/$defs/track/properties/instrument` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/instrument` |
| 97 | `#/$defs/track/properties/enabled` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/enabled` |
| 98 | `#/$defs/track/properties/clips` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips` |
| 99 | `#/$defs/track/properties/trackType` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/trackType` |
| 100 | `#/$defs/track/properties/preferredView` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/preferredView` |
| 101 | `#/$defs/track/properties/soundSource` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/soundSource` |
| 102 | `#/$defs/track/properties/localizedNames` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/localizedNames` |
| 103 | `#/$defs/track/properties/drumKitId` | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/tracks/0/drumKitId` |
| 104 | `#/$defs/soundSlot/properties/id` | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/soundSlots/0/id` |
| 105 | `#/$defs/soundSlot/properties/name` | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/soundSlots/0/name` |
| 106 | `#/$defs/soundSlot/properties/role` | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/soundSlots/0/role` |
| 107 | `#/$defs/soundSlot/properties/midiNote` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/soundSlots/0/midiNote` |
| 108 | `#/$defs/soundSlot/properties/midiMapping` | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/soundSlots/0/midiMapping` |
| 109 | `#/$defs/soundSlot/properties/localizedNames` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/soundSlots/0/localizedNames` |
| 110 | `#/$defs/lyricDocument/properties/id` | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/documents/0/id` |
| 111 | `#/$defs/lyricDocument/properties/title` | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/documents/0/title` |
| 112 | `#/$defs/lyricDocument/properties/language` | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/documents/0/language` |
| 113 | `#/$defs/lyricPhrase/properties/id` | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/phrases/0/id` |
| 114 | `#/$defs/lyricPhrase/properties/documentId` | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/phrases/0/documentId` |
| 115 | `#/$defs/lyricPhrase/properties/text` | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/phrases/0/text` |
| 116 | `#/$defs/lyricPhrase/properties/pronunciation` | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/phrases/0/pronunciation` |
| 117 | `#/$defs/lyricPhrase/properties/start` | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/phrases/0/start` |
| 118 | `#/$defs/lyricPhrase/properties/duration` | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/phrases/0/duration` |
| 119 | `#/$defs/lyricUnit/properties/id` | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/units/0/id` |
| 120 | `#/$defs/lyricUnit/properties/phraseId` | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/units/0/phraseId` |
| 121 | `#/$defs/lyricUnit/properties/text` | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/units/0/text` |
| 122 | `#/$defs/lyricUnit/properties/pronunciation` | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/units/0/pronunciation` |
| 123 | `#/$defs/lyricUnit/properties/start` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/lyrics/units/0/start` |
| 124 | `#/$defs/lyricUnit/properties/duration` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/lyrics/units/0/duration` |
| 125 | `#/$defs/lyricAlignment/properties/id` | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/alignments/0/id` |
| 126 | `#/$defs/lyricAlignment/properties/unitIds` | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/alignments/0/unitIds` |
| 127 | `#/$defs/lyricAlignment/properties/noteIds` | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/alignments/0/noteIds` |
| 128 | `#/$defs/lyrics/properties/documents` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/lyrics/documents` |
| 129 | `#/$defs/lyrics/properties/phrases` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/lyrics/phrases` |
| 130 | `#/$defs/lyrics/properties/units` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/lyrics/units` |
| 131 | `#/$defs/lyrics/properties/alignments` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/lyrics/alignments` |
| 132 | `#/$defs/resource/properties/id` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/resources/0/id` |
| 133 | `#/$defs/resource/properties/kind` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/resources/0/kind` |
| 134 | `#/$defs/resource/properties/uri` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/resources/0/uri` |
| 135 | `#/$defs/resource/properties/name` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/resources/0/name` |
| 136 | `#/$defs/resource/properties/sha256` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/resources/0/sha256` |
| 137 | `#/$defs/dependencies/oneOf/0/properties/scope` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/dependencies/scope` |
| 138 | `#/$defs/dependencies/oneOf/1/properties/scope` | [samples/22_explicit_dependency_scopes.ostf](../samples/22_explicit_dependency_scopes.ostf) `/relativePhrases/dependencies/scope` |
| 139 | `#/$defs/dependencies/oneOf/1/properties/refs` | [samples/22_explicit_dependency_scopes.ostf](../samples/22_explicit_dependency_scopes.ostf) `/relativePhrases/dependencies/refs` |
| 140 | `#/$defs/relativeAssignment/properties/noteId` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments/0/noteId` |
| 141 | `#/$defs/relativeAssignment/properties/basis` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments/0/basis` |
| 142 | `#/$defs/relativeAssignment/properties/contextId` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments/0/contextId` |
| 143 | `#/$defs/relativeAssignment/properties/anchorPitch` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments/0/anchorPitch` |
| 144 | `#/$defs/relativeAssignment/properties/index` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments/0/index` |
| 145 | `#/$defs/relativeAssignment/properties/chromaticOffset` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments/0/chromaticOffset` |
| 146 | `#/$defs/generator/properties/id` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/generator/id` |
| 147 | `#/$defs/generator/properties/version` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/generator/version` |
| 148 | `#/$defs/generationInput/properties/role` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/inputs/0/role` |
| 149 | `#/$defs/generationInput/properties/ref` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/inputs/0/ref` |
| 150 | `#/$defs/generationInput/properties/readRange` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/inputs/0/readRange` |
| 151 | `#/$defs/generationProcess/properties/id` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/id` |
| 152 | `#/$defs/generationProcess/properties/generator` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/generator` |
| 153 | `#/$defs/generationProcess/properties/inputs` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/inputs` |
| 154 | `#/$defs/generationProcess/properties/outputs` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/outputs` |
| 155 | `#/$defs/generationProcess/properties/targetRange` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/targetRange` |
| 156 | `#/$defs/generationProcess/properties/protectedNoteIds` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/protectedNoteIds` |
| 157 | `#/$defs/generationProcess/properties/intent` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent` |
| 158 | `#/$defs/roleDefinition/properties/id` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/roleDefinitions/0/id` |
| 159 | `#/$defs/roleDefinition/properties/name` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/roleDefinitions/0/name` |
| 160 | `#/$defs/roleDefinition/properties/baseRole` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/roleDefinitions/0/baseRole` |
| 161 | `#/$defs/objectColor/properties/target` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/appearance/objectColors/0/target` |
| 162 | `#/$defs/objectColor/properties/color` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/appearance/objectColors/0/color` |
| 163 | `#/$defs/phraseTemplate/properties/id` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/id` |
| 164 | `#/$defs/phraseTemplate/properties/duration` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/duration` |
| 165 | `#/$defs/phraseTemplate/properties/notes` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/notes` |
| 166 | `#/$defs/phraseTemplate/properties/name` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/name` |
| 167 | `#/$defs/phraseNoteMapping/properties/templateNoteId` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/noteMap/0/templateNoteId` |
| 168 | `#/$defs/phraseNoteMapping/properties/repeatIndex` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/noteMap/0/repeatIndex` |
| 169 | `#/$defs/phraseNoteMapping/properties/noteId` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/noteMap/0/noteId` |
| 170 | `#/$defs/phraseInstance/properties/id` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/id` |
| 171 | `#/$defs/phraseInstance/properties/templateId` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/templateId` |
| 172 | `#/$defs/phraseInstance/properties/clipId` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/clipId` |
| 173 | `#/$defs/phraseInstance/properties/repeatCount` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/repeatCount` |
| 174 | `#/$defs/phraseInstance/properties/transpose` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/transpose` |
| 175 | `#/$defs/phraseInstance/properties/noteMap` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/noteMap` |
| 176 | `#/$defs/phraseInstance/properties/velocityMode` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/velocityMode` |
| 177 | `#/$defs/clipCandidate/properties/id` | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/candidates/0/id` |
| 178 | `#/$defs/clipCandidate/properties/clipIds` | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/candidates/0/clipIds` |
| 179 | `#/$defs/clipCandidate/properties/name` | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/candidates/0/name` |
| 180 | `#/$defs/clipChoiceGroup/properties/id` | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/id` |
| 181 | `#/$defs/clipChoiceGroup/properties/candidates` | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/candidates` |
| 182 | `#/$defs/clipChoiceGroup/properties/selectedCandidateId` | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/selectedCandidateId` |
| 183 | `#/$defs/clipChoiceGroup/properties/name` | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/name` |
| 184 | `#/$defs/midiMapping/properties/standard` | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/soundSlots/0/midiMapping/standard` |
| 185 | `#/$defs/midiMapping/properties/note` | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/soundSlots/0/midiMapping/note` |
| 186 | `#/$defs/soundSource/properties/kind` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/soundSource/kind` |
| 187 | `#/$defs/soundSource/properties/identifier` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/soundSource/identifier` |
| 188 | `#/$defs/drumKit/properties/id` | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/drumKits/0/id` |
| 189 | `#/$defs/drumKit/properties/name` | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/drumKits/0/name` |
| 190 | `#/$defs/drumKit/properties/localizedNames` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/drumKits/0/localizedNames` |
| 191 | `#/$defs/drumKit/properties/soundSlotIds` | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/drumKits/0/soundSlotIds` |
| 192 | `#/$defs/voicing/properties/pitches` | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/voicing/pitches` |
| 193 | `#/$defs/voicing/properties/velocities` | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/voicing/velocities` |
| 194 | `#/$defs/contributor/properties/id` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/contributors/0/id` |
| 195 | `#/$defs/contributor/properties/name` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/contributors/0/name` |
| 196 | `#/$defs/contributor/properties/kind` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/contributors/0/kind` |
| 197 | `#/$defs/contributor/properties/localizedNames` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/contributors/0/localizedNames` |
| 198 | `#/$defs/credit/properties/id` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/credits/0/id` |
| 199 | `#/$defs/credit/properties/contributorId` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/credits/0/contributorId` |
| 200 | `#/$defs/credit/properties/role` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/credits/0/role` |
| 201 | `#/$defs/credit/properties/label` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/credits/0/label` |
| 202 | `#/$defs/alternateTitle/properties/id` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/alternateTitles/0/id` |
| 203 | `#/$defs/alternateTitle/properties/title` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/alternateTitles/0/title` |
| 204 | `#/$defs/localizationTarget/properties/kind` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries/0/target/kind` |
| 205 | `#/$defs/localizationTarget/properties/id` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries/1/target/id` |
| 206 | `#/$defs/localizationEntry/properties/target` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries/0/target` |
| 207 | `#/$defs/localizationEntry/properties/field` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries/0/field` |
| 208 | `#/$defs/localizationEntry/properties/values` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries/0/values` |
| 209 | `#/$defs/genre/properties/id` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/genres/0/id` |
| 210 | `#/$defs/genre/properties/name` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/genres/0/name` |
| 211 | `#/$defs/genre/properties/externalUri` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/genres/0/externalUri` |
| 212 | `#/$defs/revisionRef/properties/documentId` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/parents/0/documentId` |
| 213 | `#/$defs/revisionRef/properties/revisionId` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/parents/0/revisionId` |
| 214 | `#/$defs/revisionRef/properties/sha256` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/parents/0/sha256` |
| 215 | `#/$defs/software/properties/name` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/createdBy/name` |
| 216 | `#/$defs/software/properties/version` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/createdBy/version` |
| 217 | `#/$defs/documentInfo/properties/id` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/id` |
| 218 | `#/$defs/documentInfo/properties/revisionId` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/revisionId` |
| 219 | `#/$defs/documentInfo/properties/parents` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/parents` |
| 220 | `#/$defs/documentInfo/properties/createdBy` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/createdBy` |
| 221 | `#/$defs/documentInfo/properties/modifiedBy` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/modifiedBy` |
| 222 | `#/$defs/key/properties/state` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/key/state` |
| 223 | `#/$defs/key/properties/tonic` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/key/tonic` |
| 224 | `#/$defs/key/properties/mode` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/key/mode` |
| 225 | `#/$defs/key/properties/label` | [samples/05_custom_mode_and_scale.ostf](../samples/05_custom_mode_and_scale.ostf) `/song/key/label` |
| 226 | `#/$defs/keyChange/properties/id` | [samples/03_modulation_atonal_and_unspecified.ostf](../samples/03_modulation_atonal_and_unspecified.ostf) `/timeline/keyChanges/0/id` |
| 227 | `#/$defs/keyChange/properties/at` | [samples/03_modulation_atonal_and_unspecified.ostf](../samples/03_modulation_atonal_and_unspecified.ostf) `/timeline/keyChanges/0/at` |
| 228 | `#/$defs/keyChange/properties/key` | [samples/03_modulation_atonal_and_unspecified.ostf](../samples/03_modulation_atonal_and_unspecified.ostf) `/timeline/keyChanges/0/key` |
| 229 | `#/$defs/keyChange/properties/label` | [samples/03_modulation_atonal_and_unspecified.ostf](../samples/03_modulation_atonal_and_unspecified.ostf) `/timeline/keyChanges/0/label` |
| 230 | `#/$defs/scaleDefinition/properties/id` | [samples/04_scale_without_key.ostf](../samples/04_scale_without_key.ostf) `/song/scale/id` |
| 231 | `#/$defs/scaleDefinition/properties/tonic` | [samples/04_scale_without_key.ostf](../samples/04_scale_without_key.ostf) `/song/scale/tonic` |
| 232 | `#/$defs/scaleDefinition/properties/intervals` | [samples/04_scale_without_key.ostf](../samples/04_scale_without_key.ostf) `/song/scale/intervals` |
| 233 | `#/$defs/scaleDefinition/properties/label` | [samples/04_scale_without_key.ostf](../samples/04_scale_without_key.ostf) `/song/scale/label` |
| 234 | `#/$defs/scaleTarget/properties/type` | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/targets/0/type` |
| 235 | `#/$defs/scaleTarget/properties/id` | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/targets/0/id` |
| 236 | `#/$defs/mood/properties/id` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/moods/0/id` |
| 237 | `#/$defs/mood/properties/name` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/moods/0/name` |
| 238 | `#/$defs/mood/properties/externalUri` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/moods/0/externalUri` |
| 239 | `#/$defs/rightsStatement/properties/notice` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/rights/notice` |
| 240 | `#/$defs/rightsStatement/properties/licenseUri` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/rights/licenseUri` |
| 241 | `#/$defs/rightsStatement/properties/rightsHolderIds` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/rights/rightsHolderIds` |
| 242 | `#/$defs/grooveIntent/properties/name` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/groove/name` |
| 243 | `#/$defs/grooveIntent/properties/unitTicks` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/groove/unitTicks` |
| 244 | `#/$defs/grooveIntent/properties/longWeight` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/groove/longWeight` |
| 245 | `#/$defs/grooveIntent/properties/shortWeight` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/groove/shortWeight` |
| 246 | `#/$defs/generationIntent/properties/genreNames` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/genreNames` |
| 247 | `#/$defs/generationIntent/properties/moodNames` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/moodNames` |
| 248 | `#/$defs/generationIntent/properties/groove` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/groove` |
| 249 | `#/$defs/generationIntent/properties/prompt` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/prompt` |
| 250 | `#/$defs/generationIntent/properties/seed` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/seed` |
| 251 | `#/$defs/relativePhrases/properties/status` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/status` |
| 252 | `#/$defs/relativePhrases/properties/dependencies` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/dependencies` |
| 253 | `#/$defs/relativePhrases/properties/assignments` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments` |
| 254 | `#/$defs/generation/properties/status` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/status` |
| 255 | `#/$defs/generation/properties/dependencies` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/dependencies` |
| 256 | `#/$defs/generation/properties/processes` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes` |
| 257 | `#/$defs/presentation/properties/status` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/status` |
| 258 | `#/$defs/presentation/properties/dependencies` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/dependencies` |
| 259 | `#/$defs/presentation/properties/roleDefinitions` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/roleDefinitions` |
| 260 | `#/$defs/presentation/properties/sectionRoleAssignments` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/sectionRoleAssignments` |
| 261 | `#/$defs/presentation/properties/appearance` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/appearance` |
| 262 | `#/$defs/presentation/properties/appearance/properties/roleColors` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/appearance/roleColors` |
| 263 | `#/$defs/presentation/properties/appearance/properties/customRoleColors` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/appearance/customRoleColors` |
| 264 | `#/$defs/presentation/properties/appearance/properties/objectColors` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/appearance/objectColors` |
| 265 | `#/$defs/phraseLibrary/properties/status` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/status` |
| 266 | `#/$defs/phraseLibrary/properties/dependencies` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/dependencies` |
| 267 | `#/$defs/phraseLibrary/properties/templates` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates` |
| 268 | `#/$defs/phraseLibrary/properties/instances` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances` |
| 269 | `#/$defs/clipChoices/properties/status` | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/status` |
| 270 | `#/$defs/clipChoices/properties/dependencies` | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/dependencies` |
| 271 | `#/$defs/clipChoices/properties/groups` | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups` |
| 272 | `#/$defs/localization/properties/status` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/status` |
| 273 | `#/$defs/localization/properties/dependencies` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/dependencies` |
| 274 | `#/$defs/localization/properties/entries` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries` |
| 275 | `#/$defs/corePhraseSourceNote/properties/id` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/notes/0/id` |
| 276 | `#/$defs/corePhraseSourceNote/properties/start` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/notes/0/start` |
| 277 | `#/$defs/corePhraseSourceNote/properties/duration` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/notes/0/duration` |
| 278 | `#/$defs/corePhraseSourceNote/properties/pitch` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/notes/0/pitch` |
| 279 | `#/$defs/corePhraseSourceNote/properties/soundSlotId` | [samples/21_native_drum_template_velocity.ostf](../samples/21_native_drum_template_velocity.ostf) `/phraseLibrary/templates/0/notes/0/soundSlotId` |
| 280 | `#/$defs/corePhraseSourceNote/properties/velocity` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/notes/0/velocity` |
| 281 | `#/$defs/provenanceSource/properties/format` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/format` |
| 282 | `#/$defs/provenanceSource/properties/version` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/version` |
| 283 | `#/$defs/provenanceSource/properties/sha256` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/sha256` |
| 284 | `#/$defs/provenanceSource/properties/uri` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/uri` |
| 285 | `#/$defs/provenanceSource/properties/documentId` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/documentId` |
| 286 | `#/$defs/provenanceSource/properties/revisionId` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/revisionId` |
| 287 | `#/$defs/provenanceSource/properties/resourceId` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/resourceId` |
| 288 | `#/$defs/provenanceRecord/properties/id` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/id` |
| 289 | `#/$defs/provenanceRecord/properties/action` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/action` |
| 290 | `#/$defs/provenanceRecord/properties/description` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/description` |
| 291 | `#/$defs/provenanceRecord/properties/tool` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/tool` |
| 292 | `#/$defs/provenanceRecord/properties/sources` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources` |
| 293 | `#/$defs/provenanceRecord/properties/semitones` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/semitones` |
| 294 | `#/$defs/provenanceRecord/properties/beforeKey` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/beforeKey` |
| 295 | `#/$defs/provenanceRecord/properties/afterKey` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/afterKey` |
| 296 | `#/$defs/provenance/properties/records` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records` |

## 2. Every explicit enum value / 全明示列挙値

| # | Schema Pointer | Value | Witness |
|---|---|---|---|
| 1 | `#/$defs/ref/properties/type` | `"section"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/0/target/type` |
| 2 | `#/$defs/ref/properties/type` | `"track"` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/appearance/objectColors/0/target/type` |
| 3 | `#/$defs/ref/properties/type` | `"clip"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/2/target/type` |
| 4 | `#/$defs/ref/properties/type` | `"note"` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/outputs/0/type` |
| 5 | `#/$defs/ref/properties/type` | `"chord"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/4/target/type` |
| 6 | `#/$defs/ref/properties/type` | `"scale"` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/inputs/0/ref/type` |
| 7 | `#/$defs/ref/properties/type` | `"soundSlot"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/6/target/type` |
| 8 | `#/$defs/ref/properties/type` | `"drumKit"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/7/target/type` |
| 9 | `#/$defs/ref/properties/type` | `"lyricDocument"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/8/target/type` |
| 10 | `#/$defs/ref/properties/type` | `"lyricPhrase"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/9/target/type` |
| 11 | `#/$defs/ref/properties/type` | `"lyricUnit"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/10/target/type` |
| 12 | `#/$defs/ref/properties/type` | `"lyricAlignment"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/11/target/type` |
| 13 | `#/$defs/ref/properties/type` | `"resource"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/12/target/type` |
| 14 | `#/$defs/ref/properties/type` | `"genre"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/13/target/type` |
| 15 | `#/$defs/ref/properties/type` | `"contributor"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/14/target/type` |
| 16 | `#/$defs/ref/properties/type` | `"credit"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/15/target/type` |
| 17 | `#/$defs/ref/properties/type` | `"alternateTitle"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/16/target/type` |
| 18 | `#/$defs/ref/properties/type` | `"mood"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/17/target/type` |
| 19 | `#/$defs/ref/properties/type` | `"keyChange"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/18/target/type` |
| 20 | `#/$defs/ref/properties/type` | `"phraseTemplate"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/19/target/type` |
| 21 | `#/$defs/ref/properties/type` | `"phraseInstance"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/20/target/type` |
| 22 | `#/$defs/ref/properties/type` | `"clipChoiceGroup"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/21/target/type` |
| 23 | `#/$defs/ref/properties/type` | `"clipCandidate"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/22/target/type` |
| 24 | `#/$defs/ref/properties/type` | `"roleDefinition"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/23/target/type` |
| 25 | `#/$defs/ref/properties/type` | `"generationProcess"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/24/target/type` |
| 26 | `#/$defs/ref/properties/type` | `"provenanceRecord"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/presentation/appearance/objectColors/25/target/type` |
| 27 | `#/$defs/spelledPitchClass/properties/step` | `"A"` | [samples/24_all_key_modes_and_enharmonic_spellings.ostf](../samples/24_all_key_modes_and_enharmonic_spellings.ostf) `/timeline/keyChanges/5/key/tonic/step` |
| 28 | `#/$defs/spelledPitchClass/properties/step` | `"B"` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/harmony/chords/0/bass/step` |
| 29 | `#/$defs/spelledPitchClass/properties/step` | `"C"` | [samples/03_modulation_atonal_and_unspecified.ostf](../samples/03_modulation_atonal_and_unspecified.ostf) `/song/key/tonic/step` |
| 30 | `#/$defs/spelledPitchClass/properties/step` | `"D"` | [samples/03_modulation_atonal_and_unspecified.ostf](../samples/03_modulation_atonal_and_unspecified.ostf) `/timeline/keyChanges/0/key/tonic/step` |
| 31 | `#/$defs/spelledPitchClass/properties/step` | `"E"` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/key/tonic/step` |
| 32 | `#/$defs/spelledPitchClass/properties/step` | `"F"` | [samples/24_all_key_modes_and_enharmonic_spellings.ostf](../samples/24_all_key_modes_and_enharmonic_spellings.ostf) `/timeline/keyChanges/3/key/tonic/step` |
| 33 | `#/$defs/spelledPitchClass/properties/step` | `"G"` | [samples/24_all_key_modes_and_enharmonic_spellings.ostf](../samples/24_all_key_modes_and_enharmonic_spellings.ostf) `/timeline/keyChanges/4/key/tonic/step` |
| 34 | `#/$defs/meter/properties/denominator` | `1` | [samples/25_all_meter_denominators_and_tempo_changes.ostf](../samples/25_all_meter_denominators_and_tempo_changes.ostf) `/timeline/meterChanges/0/denominator` |
| 35 | `#/$defs/meter/properties/denominator` | `2` | [samples/25_all_meter_denominators_and_tempo_changes.ostf](../samples/25_all_meter_denominators_and_tempo_changes.ostf) `/timeline/meterChanges/1/denominator` |
| 36 | `#/$defs/meter/properties/denominator` | `4` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/meterChanges/0/denominator` |
| 37 | `#/$defs/meter/properties/denominator` | `8` | [samples/07_pickup_additive_midbar_meter.ostf](../samples/07_pickup_additive_midbar_meter.ostf) `/timeline/meterChanges/0/denominator` |
| 38 | `#/$defs/meter/properties/denominator` | `16` | [samples/25_all_meter_denominators_and_tempo_changes.ostf](../samples/25_all_meter_denominators_and_tempo_changes.ostf) `/timeline/meterChanges/4/denominator` |
| 39 | `#/$defs/meter/properties/denominator` | `32` | [samples/25_all_meter_denominators_and_tempo_changes.ostf](../samples/25_all_meter_denominators_and_tempo_changes.ostf) `/timeline/meterChanges/5/denominator` |
| 40 | `#/$defs/meter/properties/denominator` | `64` | [samples/25_all_meter_denominators_and_tempo_changes.ostf](../samples/25_all_meter_denominators_and_tempo_changes.ostf) `/timeline/meterChanges/6/denominator` |
| 41 | `#/$defs/track/properties/trackType` | `"melodic"` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/trackType` |
| 42 | `#/$defs/track/properties/trackType` | `"drum"` | [samples/21_native_drum_template_velocity.ostf](../samples/21_native_drum_template_velocity.ostf) `/tracks/0/trackType` |
| 43 | `#/$defs/track/properties/trackType` | `"mixed"` | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/tracks/0/trackType` |
| 44 | `#/$defs/track/properties/preferredView` | `"auto"` | [samples/30_muted_and_empty_track_types.ostf](../samples/30_muted_and_empty_track_types.ostf) `/tracks/0/preferredView` |
| 45 | `#/$defs/track/properties/preferredView` | `"pianoRoll"` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/preferredView` |
| 46 | `#/$defs/track/properties/preferredView` | `"drumGrid"` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/1/preferredView` |
| 47 | `#/$defs/resource/properties/kind` | `"audio"` | [samples/37_resource_kinds_and_provenance_actions.ostf](../samples/37_resource_kinds_and_provenance_actions.ostf) `/resources/0/kind` |
| 48 | `#/$defs/resource/properties/kind` | `"midi"` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/resources/0/kind` |
| 49 | `#/$defs/resource/properties/kind` | `"text"` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/resources/0/kind` |
| 50 | `#/$defs/resource/properties/kind` | `"other"` | [samples/37_resource_kinds_and_provenance_actions.ostf](../samples/37_resource_kinds_and_provenance_actions.ostf) `/resources/3/kind` |
| 51 | `#/$defs/dependencies/oneOf/0/properties/scope` | `"document"` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/dependencies/scope` |
| 52 | `#/$defs/dependencies/oneOf/0/properties/scope` | `"none"` | [samples/22_explicit_dependency_scopes.ostf](../samples/22_explicit_dependency_scopes.ostf) `/clipChoices/dependencies/scope` |
| 53 | `#/$defs/relativeAssignment/properties/basis` | `"chordTone"` | [samples/53_relative_interval_and_offset_boundaries.ostf](../samples/53_relative_interval_and_offset_boundaries.ostf) `/relativePhrases/assignments/0/basis` |
| 54 | `#/$defs/relativeAssignment/properties/basis` | `"scaleDegree"` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments/0/basis` |
| 55 | `#/$defs/phraseInstance/properties/velocityMode` | `"independent"` | [samples/13_phrase_velocity_independent.ostf](../samples/13_phrase_velocity_independent.ostf) `/phraseLibrary/instances/0/velocityMode` |
| 56 | `#/$defs/phraseInstance/properties/velocityMode` | `"linked"` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/velocityMode` |
| 57 | `#/$defs/midiMapping/properties/standard` | `"gm1"` | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/soundSlots/0/midiMapping/standard` |
| 58 | `#/$defs/midiMapping/properties/standard` | `"custom"` | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/soundSlots/1/midiMapping/standard` |
| 59 | `#/$defs/soundSource/properties/kind` | `"unassigned"` | [samples/31_all_sound_source_kinds.ostf](../samples/31_all_sound_source_kinds.ostf) `/tracks/0/soundSource/kind` |
| 60 | `#/$defs/soundSource/properties/kind` | `"gm1"` | [samples/31_all_sound_source_kinds.ostf](../samples/31_all_sound_source_kinds.ostf) `/tracks/1/soundSource/kind` |
| 61 | `#/$defs/soundSource/properties/kind` | `"externalMidi"` | [samples/31_all_sound_source_kinds.ostf](../samples/31_all_sound_source_kinds.ostf) `/tracks/2/soundSource/kind` |
| 62 | `#/$defs/soundSource/properties/kind` | `"plugin"` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/soundSource/kind` |
| 63 | `#/$defs/soundSource/properties/kind` | `"hostManaged"` | [samples/31_all_sound_source_kinds.ostf](../samples/31_all_sound_source_kinds.ostf) `/tracks/4/soundSource/kind` |
| 64 | `#/$defs/contributor/properties/kind` | `"person"` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/contributors/0/kind` |
| 65 | `#/$defs/contributor/properties/kind` | `"organization"` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/contributors/1/kind` |
| 66 | `#/$defs/contributor/properties/kind` | `"other"` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/contributors/0/kind` |
| 67 | `#/$defs/localizationTarget/properties/kind` | `"song"` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries/0/target/kind` |
| 68 | `#/$defs/localizationTarget/properties/kind` | `"alternateTitle"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/localization/entries/5/target/kind` |
| 69 | `#/$defs/localizationTarget/properties/kind` | `"contributor"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/localization/entries/6/target/kind` |
| 70 | `#/$defs/localizationTarget/properties/kind` | `"credit"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/localization/entries/20/target/kind` |
| 71 | `#/$defs/localizationTarget/properties/kind` | `"section"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/localization/entries/7/target/kind` |
| 72 | `#/$defs/localizationTarget/properties/kind` | `"track"` | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/localization/entries/1/target/kind` |
| 73 | `#/$defs/localizationTarget/properties/kind` | `"clip"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/localization/entries/10/target/kind` |
| 74 | `#/$defs/localizationTarget/properties/kind` | `"soundSlot"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/localization/entries/11/target/kind` |
| 75 | `#/$defs/localizationTarget/properties/kind` | `"drumKit"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/localization/entries/12/target/kind` |
| 76 | `#/$defs/localizationTarget/properties/kind` | `"lyricDocument"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/localization/entries/21/target/kind` |
| 77 | `#/$defs/localizationTarget/properties/kind` | `"resource"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/localization/entries/13/target/kind` |
| 78 | `#/$defs/localizationTarget/properties/kind` | `"phraseTemplate"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/localization/entries/14/target/kind` |
| 79 | `#/$defs/localizationTarget/properties/kind` | `"clipCandidate"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/localization/entries/15/target/kind` |
| 80 | `#/$defs/localizationTarget/properties/kind` | `"clipChoiceGroup"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/localization/entries/16/target/kind` |
| 81 | `#/$defs/localizationTarget/properties/kind` | `"roleDefinition"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/localization/entries/17/target/kind` |
| 82 | `#/$defs/localizationTarget/properties/kind` | `"genre"` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries/1/target/kind` |
| 83 | `#/$defs/localizationTarget/properties/kind` | `"mood"` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries/2/target/kind` |
| 84 | `#/$defs/localizationTarget/properties/kind` | `"keyChange"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/localization/entries/22/target/kind` |
| 85 | `#/$defs/localizationTarget/properties/kind` | `"scale"` | [samples/38_all_reference_and_localization_targets.ostf](../samples/38_all_reference_and_localization_targets.ostf) `/localization/entries/24/target/kind` |
| 86 | `#/$defs/key/properties/state` | `"tonal"` | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/key/state` |
| 87 | `#/$defs/key/properties/state` | `"atonal"` | [samples/03_modulation_atonal_and_unspecified.ostf](../samples/03_modulation_atonal_and_unspecified.ostf) `/timeline/keyChanges/1/key/state` |
| 88 | `#/$defs/key/properties/state` | `"unspecified"` | [samples/03_modulation_atonal_and_unspecified.ostf](../samples/03_modulation_atonal_and_unspecified.ostf) `/timeline/keyChanges/2/key/state` |
| 89 | `#/$defs/scaleTarget/properties/type` | `"section"` | [samples/39_all_scale_target_types_and_overlap.ostf](../samples/39_all_scale_target_types_and_overlap.ostf) `/harmony/scales/0/targets/0/type` |
| 90 | `#/$defs/scaleTarget/properties/type` | `"track"` | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/targets/0/type` |
| 91 | `#/$defs/scaleTarget/properties/type` | `"clip"` | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/1/targets/0/type` |
| 92 | `#/$defs/scaleTarget/properties/type` | `"chord"` | [samples/39_all_scale_target_types_and_overlap.ostf](../samples/39_all_scale_target_types_and_overlap.ostf) `/harmony/scales/0/targets/3/type` |
| 93 | `#/$defs/scaleTarget/properties/type` | `"note"` | [samples/39_all_scale_target_types_and_overlap.ostf](../samples/39_all_scale_target_types_and_overlap.ostf) `/harmony/scales/0/targets/4/type` |
| 94 | `#/$defs/relativePhrases/properties/status` | `"current"` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/status` |
| 95 | `#/$defs/relativePhrases/properties/status` | `"stale"` | [samples/18_stale_missing_relation.ostf](../samples/18_stale_missing_relation.ostf) `/relativePhrases/status` |
| 96 | `#/$defs/relativePhrases/properties/status` | `"unverified"` | [samples/40_empty_unverified_core_objects.ostf](../samples/40_empty_unverified_core_objects.ostf) `/relativePhrases/status` |
| 97 | `#/$defs/generation/properties/status` | `"current"` | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/status` |
| 98 | `#/$defs/generation/properties/status` | `"stale"` | [samples/41_stale_core_relationships_preserved.ostf](../samples/41_stale_core_relationships_preserved.ostf) `/generation/status` |
| 99 | `#/$defs/generation/properties/status` | `"unverified"` | [samples/40_empty_unverified_core_objects.ostf](../samples/40_empty_unverified_core_objects.ostf) `/generation/status` |
| 100 | `#/$defs/presentation/properties/status` | `"current"` | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/status` |
| 101 | `#/$defs/presentation/properties/status` | `"stale"` | [samples/41_stale_core_relationships_preserved.ostf](../samples/41_stale_core_relationships_preserved.ostf) `/presentation/status` |
| 102 | `#/$defs/presentation/properties/status` | `"unverified"` | [samples/40_empty_unverified_core_objects.ostf](../samples/40_empty_unverified_core_objects.ostf) `/presentation/status` |
| 103 | `#/$defs/phraseLibrary/properties/status` | `"current"` | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/status` |
| 104 | `#/$defs/phraseLibrary/properties/status` | `"stale"` | [samples/41_stale_core_relationships_preserved.ostf](../samples/41_stale_core_relationships_preserved.ostf) `/phraseLibrary/status` |
| 105 | `#/$defs/phraseLibrary/properties/status` | `"unverified"` | [samples/40_empty_unverified_core_objects.ostf](../samples/40_empty_unverified_core_objects.ostf) `/phraseLibrary/status` |
| 106 | `#/$defs/clipChoices/properties/status` | `"current"` | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/status` |
| 107 | `#/$defs/clipChoices/properties/status` | `"stale"` | [samples/41_stale_core_relationships_preserved.ostf](../samples/41_stale_core_relationships_preserved.ostf) `/clipChoices/status` |
| 108 | `#/$defs/clipChoices/properties/status` | `"unverified"` | [samples/40_empty_unverified_core_objects.ostf](../samples/40_empty_unverified_core_objects.ostf) `/clipChoices/status` |
| 109 | `#/$defs/localization/properties/status` | `"current"` | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/status` |
| 110 | `#/$defs/localization/properties/status` | `"stale"` | [samples/41_stale_core_relationships_preserved.ostf](../samples/41_stale_core_relationships_preserved.ostf) `/localization/status` |
| 111 | `#/$defs/localization/properties/status` | `"unverified"` | [samples/40_empty_unverified_core_objects.ostf](../samples/40_empty_unverified_core_objects.ostf) `/localization/status` |
| 112 | `#/$defs/provenanceRecord/properties/action` | `"create"` | [samples/37_resource_kinds_and_provenance_actions.ostf](../samples/37_resource_kinds_and_provenance_actions.ostf) `/provenance/records/0/action` |
| 113 | `#/$defs/provenanceRecord/properties/action` | `"import"` | [samples/37_resource_kinds_and_provenance_actions.ostf](../samples/37_resource_kinds_and_provenance_actions.ostf) `/provenance/records/1/action` |
| 114 | `#/$defs/provenanceRecord/properties/action` | `"conversion"` | [samples/37_resource_kinds_and_provenance_actions.ostf](../samples/37_resource_kinds_and_provenance_actions.ostf) `/provenance/records/2/action` |
| 115 | `#/$defs/provenanceRecord/properties/action` | `"edit"` | [samples/37_resource_kinds_and_provenance_actions.ostf](../samples/37_resource_kinds_and_provenance_actions.ostf) `/provenance/records/3/action` |
| 116 | `#/$defs/provenanceRecord/properties/action` | `"transpose"` | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/action` |
| 117 | `#/$defs/provenanceRecord/properties/action` | `"merge"` | [samples/37_resource_kinds_and_provenance_actions.ostf](../samples/37_resource_kinds_and_provenance_actions.ostf) `/provenance/records/5/action` |
| 118 | `#/$defs/provenanceRecord/properties/action` | `"generation"` | [samples/37_resource_kinds_and_provenance_actions.ostf](../samples/37_resource_kinds_and_provenance_actions.ostf) `/provenance/records/6/action` |
| 119 | `#/$defs/provenanceRecord/properties/action` | `"other"` | [samples/37_resource_kinds_and_provenance_actions.ostf](../samples/37_resource_kinds_and_provenance_actions.ostf) `/provenance/records/7/action` |

## 3. Constants / 定数

| Schema Pointer | Value | Witness |
|---|---|---|
| `#/properties/format` | `"OSTF"` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/format` |
| `#/properties/version` | `"3.4.0"` | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/version` |
| `#/$defs/dependencies/oneOf/1/properties/scope` | `"objects"` | [samples/22_explicit_dependency_scopes.ostf](../samples/22_explicit_dependency_scopes.ostf) `/relativePhrases/dependencies/scope` |
