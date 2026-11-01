# OSTF 3.4.0 — 全パラメーターリファレンス

正式版3.4.0。同梱Schemaから生成した全定義・全条件の一覧です。

**構造の正本:** [JSON Schema](../schema/ostf-3.4.0.schema.json)。**意味の正本:** [正式仕様書](FORMAT_SPECIFICATION.ja.md)。[マニュアル](COMPLETE_MANUAL.ja.md)と[実例対応表](COVERAGE.md)も参照してください。

「親内必須」は親オブジェクトが存在する場合の必須性です。任意の親を必須にしません。条件付き必須・禁止、相互必須、辞書キー、追加項目可否は各節の完全なSchemaブロックも含めて適用します。defaultは読込時に書き込む値ではありません。

現行Core 77定義＋ルート、互換保持用の凍結旧定義 65件を収録。現行の実データ宣言 296件、列挙値の宣言別実例 119件を照合。旧定義を新Core機能として使いません。

## 索引

- [Root](#root)
- [id](#core-id)
- [nonnegative](#core-nonnegative)
- [positive](#core-positive)
- [signed](#core-signed)
- [pitch](#core-pitch)
- [ref](#core-ref)
- [range](#core-range)
- [spelledPitchClass](#core-spelledpitchclass)
- [song](#core-song)
- [section](#core-section)
- [tempo](#core-tempo)
- [meter](#core-meter)
- [timeline](#core-timeline)
- [chord](#core-chord)
- [scale](#core-scale)
- [harmony](#core-harmony)
- [instrument](#core-instrument)
- [note](#core-note)
- [clip](#core-clip)
- [track](#core-track)
- [soundSlot](#core-soundslot)
- [lyricDocument](#core-lyricdocument)
- [lyricPhrase](#core-lyricphrase)
- [lyricUnit](#core-lyricunit)
- [lyricAlignment](#core-lyricalignment)
- [lyrics](#core-lyrics)
- [sha256](#core-sha256)
- [resource](#core-resource)
- [dependencies](#core-dependencies)
- [relativeAssignment](#core-relativeassignment)
- [generator](#core-generator)
- [generationInput](#core-generationinput)
- [generationProcess](#core-generationprocess)
- [color](#core-color)
- [roleDefinition](#core-roledefinition)
- [roleColorMap](#core-rolecolormap)
- [customRoleColorMap](#core-customrolecolormap)
- [objectColor](#core-objectcolor)
- [phraseTemplate](#core-phrasetemplate)
- [phraseNoteMapping](#core-phrasenotemapping)
- [phraseInstance](#core-phraseinstance)
- [clipCandidate](#core-clipcandidate)
- [clipChoiceGroup](#core-clipchoicegroup)
- [midiMapping](#core-midimapping)
- [soundSource](#core-soundsource)
- [localizedNames](#core-localizednames)
- [drumKit](#core-drumkit)
- [voicing](#core-voicing)
- [contributor](#core-contributor)
- [credit](#core-credit)
- [alternateTitle](#core-alternatetitle)
- [languageMap32](#core-languagemap32)
- [localizationTarget](#core-localizationtarget)
- [localizationEntry](#core-localizationentry)
- [genre](#core-genre)
- [opaqueDocumentId](#core-opaquedocumentid)
- [revisionRef](#core-revisionref)
- [software](#core-software)
- [documentInfo](#core-documentinfo)
- [key](#core-key)
- [keyChange](#core-keychange)
- [scaleDefinition](#core-scaledefinition)
- [scaleTarget](#core-scaletarget)
- [mood](#core-mood)
- [rightsStatement](#core-rightsstatement)
- [grooveIntent](#core-grooveintent)
- [generationIntent](#core-generationintent)
- [relativePhrases](#core-relativephrases)
- [generation](#core-generation)
- [presentation](#core-presentation)
- [phraseLibrary](#core-phraselibrary)
- [clipChoices](#core-clipchoices)
- [localization](#core-localization)
- [corePhraseSourceNote](#core-corephrasesourcenote)
- [provenanceSource](#core-provenancesource)
- [provenanceRecord](#core-provenancerecord)
- [provenance](#core-provenance)
- [Frozen legacy compatibility](#frozen-legacy)

<a id="root"></a>
## Root

`#`

Shared composition metadata and editing data are standard typed Core fields. Concrete tracks are the only saved performance. Extensions are optional, never required for standard functions.

親内必須: `format`, `version`, `ppq`, `song`, `timeline`, `harmony`, `tracks`, `soundSlots`, `lyrics`, `resources`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `format` | const "OSTF" | 必須 | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/format` |
| `version` | const "3.4.0" | 必須 | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/version` |
| `ppq` | integer | 必須 | minimum=1; maximum=960000 | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/ppq` |
| `song` | song | 必須 | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/song` |
| `timeline` | timeline | 必須 | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline` |
| `harmony` | harmony | 必須 | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/harmony` |
| `tracks` | array<track> | 必須 | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/tracks` |
| `soundSlots` | array<soundSlot> | 必須 | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/soundSlots` |
| `lyrics` | lyrics | 必須 | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/lyrics` |
| `resources` | array<resource> | 必須 | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/resources` |
| `extensions` | legacy33/$defs/extensions | 任意／条件付き | Optional third-party or verbatim legacy compatibility payloads. Standard Core always remains authoritative. New first-party common information must not be stored only here. | [samples/17_legacy_conflict_core_wins.ostf](../samples/17_legacy_conflict_core_wins.ostf) `/extensions` |
| `drumKits` | array<drumKit> | 任意／条件付き | Optional multiple percussion-kit definitions; absent = no declared kits (3.0 compatible). | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/drumKits` |
| `contributors` | array<contributor> | 任意／条件付き | Optional unordered identity records referenced by song.credits. No contributor limit is imposed by this format. | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/contributors` |
| `document` | documentInfo | 任意／条件付き | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document` |
| `relativePhrases` | relativePhrases | 任意／条件付き | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases` |
| `generation` | generation | 任意／条件付き | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation` |
| `presentation` | presentation | 任意／条件付き | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation` |
| `phraseLibrary` | phraseLibrary | 任意／条件付き | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary` |
| `clipChoices` | clipChoices | 任意／条件付き | — | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices` |
| `localization` | localization | 任意／条件付き | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization` |
| `provenance` | provenance | 任意／条件付き | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://yoh-nak.github.io/ostf/schema/ostf-3.4.0.schema.json",
  "title": "Open Song Timeline Format (OSTF) 3.4.0",
  "description": "Shared composition metadata and editing data are standard typed Core fields. Concrete tracks are the only saved performance. Extensions are optional, never required for standard functions.",
  "$comment": "Authoritative 3.4.0 structural schema. See docs/FORMAT_SPECIFICATION.ja.md for normative semantic rules not expressible in JSON Schema. Schema IDs are identifiers, not a network-fetch requirement.",
  "type": "object",
  "properties": {
    "format": {
      "const": "OSTF"
    },
    "version": {
      "const": "3.4.0"
    },
    "ppq": {
      "type": "integer",
      "minimum": 1,
      "maximum": 960000
    },
    "song": {
      "$ref": "#/$defs/song"
    },
    "timeline": {
      "$ref": "#/$defs/timeline"
    },
    "harmony": {
      "$ref": "#/$defs/harmony"
    },
    "tracks": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/track"
      }
    },
    "soundSlots": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/soundSlot"
      }
    },
    "lyrics": {
      "$ref": "#/$defs/lyrics"
    },
    "resources": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/resource"
      }
    },
    "extensions": {
      "$ref": "#/$defs/legacy33/$defs/extensions",
      "description": "Optional third-party or verbatim legacy compatibility payloads. Standard Core always remains authoritative. New first-party common information must not be stored only here."
    },
    "drumKits": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/drumKit"
      },
      "description": "Optional multiple percussion-kit definitions; absent = no declared kits (3.0 compatible)."
    },
    "contributors": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/contributor"
      },
      "description": "Optional unordered identity records referenced by song.credits. No contributor limit is imposed by this format."
    },
    "document": {
      "$ref": "#/$defs/documentInfo"
    },
    "relativePhrases": {
      "$ref": "#/$defs/relativePhrases"
    },
    "generation": {
      "$ref": "#/$defs/generation"
    },
    "presentation": {
      "$ref": "#/$defs/presentation"
    },
    "phraseLibrary": {
      "$ref": "#/$defs/phraseLibrary"
    },
    "clipChoices": {
      "$ref": "#/$defs/clipChoices"
    },
    "localization": {
      "$ref": "#/$defs/localization"
    },
    "provenance": {
      "$ref": "#/$defs/provenance"
    }
  },
  "required": [
    "format",
    "version",
    "ppq",
    "song",
    "timeline",
    "harmony",
    "tracks",
    "soundSlots",
    "lyrics",
    "resources"
  ],
  "additionalProperties": false
}
```

<a id="core-id"></a>
## id

`#/$defs/id`

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "string",
  "pattern": "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```

<a id="core-nonnegative"></a>
## nonnegative

`#/$defs/nonnegative`

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "integer",
  "minimum": 0,
  "maximum": 9007199254740991
}
```

<a id="core-positive"></a>
## positive

`#/$defs/positive`

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "integer",
  "minimum": 1,
  "maximum": 9007199254740991
}
```

<a id="core-signed"></a>
## signed

`#/$defs/signed`

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "integer",
  "minimum": -9007199254740991,
  "maximum": 9007199254740991
}
```

<a id="core-pitch"></a>
## pitch

`#/$defs/pitch`

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "integer",
  "minimum": 0,
  "maximum": 127
}
```

<a id="core-ref"></a>
## ref

`#/$defs/ref`

親内必須: `type`, `id`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `type` | enum ["section", "track", "clip", "note", "chord", "scale", "soundSlot", "drumKit", "lyricDocument", "lyricPhrase", "lyricUnit", "lyricAlignment", "resource", "genre", "contributor", "credit", "alternateTitle", "mood", "keyChange", "phraseTemplate", "phraseInstance", "clipChoiceGroup", "clipCandidate", "roleDefinition", "generationProcess", "provenanceRecord"] | 必須 | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/appearance/objectColors/0/target/type` |
| `id` | id | 必須 | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/appearance/objectColors/0/target/id` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "type": {
      "enum": [
        "section",
        "track",
        "clip",
        "note",
        "chord",
        "scale",
        "soundSlot",
        "drumKit",
        "lyricDocument",
        "lyricPhrase",
        "lyricUnit",
        "lyricAlignment",
        "resource",
        "genre",
        "contributor",
        "credit",
        "alternateTitle",
        "mood",
        "keyChange",
        "phraseTemplate",
        "phraseInstance",
        "clipChoiceGroup",
        "clipCandidate",
        "roleDefinition",
        "generationProcess",
        "provenanceRecord"
      ]
    },
    "id": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "type",
    "id"
  ],
  "additionalProperties": false
}
```

<a id="core-range"></a>
## range

`#/$defs/range`

親内必須: `start`, `duration`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `start` | nonnegative | 必須 | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/inputs/0/readRange/start` |
| `duration` | positive | 必須 | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/inputs/0/readRange/duration` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    }
  },
  "required": [
    "start",
    "duration"
  ],
  "additionalProperties": false
}
```

<a id="core-spelledpitchclass"></a>
## spelledPitchClass

`#/$defs/spelledPitchClass`

親内必須: `step`, `alter`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `step` | enum ["A", "B", "C", "D", "E", "F", "G"] | 必須 | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/key/tonic/step` |
| `alter` | integer | 必須 | minimum=-2; maximum=2 | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/key/tonic/alter` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "step": {
      "enum": [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G"
      ]
    },
    "alter": {
      "type": "integer",
      "minimum": -2,
      "maximum": 2
    }
  },
  "required": [
    "step",
    "alter"
  ],
  "additionalProperties": false
}
```

<a id="core-song"></a>
## song

`#/$defs/song`

親内必須: `title`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `title` | string | 必須 | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/song/title` |
| `primaryMelodyTrackId` | id | 任意／条件付き | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/primaryMelodyTrackId` |
| `localizedTitles` | localizedNames | 任意／条件付き | Optional localized song-title alternatives. song.title is the stable fallback. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/song/localizedTitles` |
| `subtitle` | string | 任意／条件付き | Optional original-language subtitle. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/song/subtitle` |
| `description` | string | 任意／条件付き | Optional original-language description, including Unicode and line breaks. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/song/description` |
| `alternateTitles` | array<alternateTitle> | 任意／条件付き | Additional stable-ID source-language titles. | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/alternateTitles` |
| `credits` | array<credit> | 任意／条件付き | Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted. | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/credits` |
| `genres` | array<genre> | 任意／条件付き | Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified. | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/genres` |
| `key` | key | 任意／条件付き | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/key` |
| `scale` | scaleDefinition | 任意／条件付き | — | [samples/04_scale_without_key.ostf](../samples/04_scale_without_key.ostf) `/song/scale` |
| `languages` | array<string> | 任意／条件付き | uniqueItems=true | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/languages` |
| `primaryLyricDocumentId` | id | 任意／条件付き | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/song/primaryLyricDocumentId` |
| `moods` | array<mood> | 任意／条件付き | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/moods` |
| `rights` | rightsStatement | 任意／条件付き | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/rights` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    },
    "primaryMelodyTrackId": {
      "$ref": "#/$defs/id"
    },
    "localizedTitles": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized song-title alternatives. song.title is the stable fallback."
    },
    "subtitle": {
      "type": "string",
      "description": "Optional original-language subtitle."
    },
    "description": {
      "type": "string",
      "description": "Optional original-language description, including Unicode and line breaks."
    },
    "alternateTitles": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/alternateTitle"
      },
      "description": "Additional stable-ID source-language titles."
    },
    "credits": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/credit"
      },
      "description": "Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted."
    },
    "genres": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/genre"
      },
      "description": "Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified."
    },
    "key": {
      "$ref": "#/$defs/key"
    },
    "scale": {
      "$ref": "#/$defs/scaleDefinition"
    },
    "languages": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1,
        "description": "Authored language tag, preferably BCP 47. Unknown spelling is retained; case-insensitive duplicate tags forbidden."
      },
      "uniqueItems": true
    },
    "primaryLyricDocumentId": {
      "$ref": "#/$defs/id"
    },
    "moods": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/mood"
      }
    },
    "rights": {
      "$ref": "#/$defs/rightsStatement"
    }
  },
  "required": [
    "title"
  ],
  "additionalProperties": false
}
```

<a id="core-section"></a>
## section

`#/$defs/section`

親内必須: `id`, `name`, `start`, `duration`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/timeline/sections/0/id` |
| `name` | string | 必須 | minLength=1 | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/timeline/sections/0/name` |
| `start` | nonnegative | 必須 | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/timeline/sections/0/start` |
| `duration` | positive | 必須 | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/timeline/sections/0/duration` |
| `role` | string | 任意／条件付き | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/timeline/sections/0/role` |
| `localizedNames` | localizedNames | 任意／条件付き | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/timeline/sections/0/localizedNames` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "role": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "id",
    "name",
    "start",
    "duration"
  ],
  "additionalProperties": false
}
```

<a id="core-tempo"></a>
## tempo

`#/$defs/tempo`

親内必須: `at`, `bpm`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `at` | nonnegative | 必須 | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/tempoChanges/0/at` |
| `bpm` | number | 必須 | maximum=1000; exclusiveMinimum=0 | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/tempoChanges/0/bpm` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/nonnegative"
    },
    "bpm": {
      "type": "number",
      "exclusiveMinimum": 0,
      "maximum": 1000
    }
  },
  "required": [
    "at",
    "bpm"
  ],
  "additionalProperties": false
}
```

<a id="core-meter"></a>
## meter

`#/$defs/meter`

親内必須: `at`, `numerator`, `denominator`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `at` | nonnegative | 必須 | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/meterChanges/0/at` |
| `numerator` | integer | 必須 | minimum=1; maximum=64 | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/meterChanges/0/numerator` |
| `denominator` | enum [1, 2, 4, 8, 16, 32, 64] | 必須 | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/meterChanges/0/denominator` |
| `beatGroups` | array<integer> | 任意／条件付き | minItems=1; maxItems=64; Optional additive grouping in denominator units. Values must sum to numerator. Descriptive only; does not change note timestamps. | [samples/07_pickup_additive_midbar_meter.ostf](../samples/07_pickup_additive_midbar_meter.ostf) `/timeline/meterChanges/0/beatGroups` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/nonnegative"
    },
    "numerator": {
      "type": "integer",
      "minimum": 1,
      "maximum": 64
    },
    "denominator": {
      "enum": [
        1,
        2,
        4,
        8,
        16,
        32,
        64
      ],
      "type": "integer"
    },
    "beatGroups": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 1,
        "maximum": 64
      },
      "minItems": 1,
      "maxItems": 64,
      "description": "Optional additive grouping in denominator units. Values must sum to numerator. Descriptive only; does not change note timestamps."
    }
  },
  "required": [
    "at",
    "numerator",
    "denominator"
  ],
  "additionalProperties": false
}
```

<a id="core-timeline"></a>
## timeline

`#/$defs/timeline`

親内必須: `sections`, `tempoChanges`, `meterChanges`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `sections` | array<section> | 必須 | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/sections` |
| `tempoChanges` | array<tempo> | 必須 | minItems=1 | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/tempoChanges` |
| `meterChanges` | array<meter> | 必須 | minItems=1 | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/meterChanges` |
| `keyChanges` | array<keyChange> | 任意／条件付き | — | [samples/03_modulation_atonal_and_unspecified.ostf](../samples/03_modulation_atonal_and_unspecified.ostf) `/timeline/keyChanges` |
| `duration` | nonnegative | 任意／条件付き | — | [samples/07_pickup_additive_midbar_meter.ostf](../samples/07_pickup_additive_midbar_meter.ostf) `/timeline/duration` |
| `barOrigin` | nonnegative | 任意／条件付き | — | [samples/07_pickup_additive_midbar_meter.ostf](../samples/07_pickup_additive_midbar_meter.ostf) `/timeline/barOrigin` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "sections": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/section"
      }
    },
    "tempoChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/tempo"
      },
      "minItems": 1
    },
    "meterChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/meter"
      },
      "minItems": 1
    },
    "keyChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/keyChange"
      }
    },
    "duration": {
      "$ref": "#/$defs/nonnegative"
    },
    "barOrigin": {
      "$ref": "#/$defs/nonnegative"
    }
  },
  "required": [
    "sections",
    "tempoChanges",
    "meterChanges"
  ],
  "additionalProperties": false
}
```

<a id="core-chord"></a>
## chord

`#/$defs/chord`

親内必須: `id`, `start`, `duration`, `label`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/id` |
| `start` | nonnegative | 必須 | — | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/start` |
| `duration` | positive | 必須 | — | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/duration` |
| `label` | string | 必須 | minLength=1 | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/label` |
| `root` | spelledPitchClass | 任意／条件付き | — | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/root` |
| `intervals` | array<integer> | 任意／条件付き | minItems=1; maxItems=36; uniqueItems=true | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/intervals` |
| `bass` | spelledPitchClass | 任意／条件付き | — | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/harmony/chords/0/bass` |
| `voicing` | voicing | 任意／条件付き | Optional pitch snapshot (not an arrangement note sequence). No automatic playback. | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/voicing` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string",
      "minLength": 1
    },
    "root": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 35
      },
      "minItems": 1,
      "maxItems": 36,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "bass": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "voicing": {
      "$ref": "#/$defs/voicing",
      "description": "Optional pitch snapshot (not an arrangement note sequence). No automatic playback."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "label"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "root": [
      "intervals"
    ],
    "intervals": [
      "root"
    ]
  }
}
```

<a id="core-scale"></a>
## scale

`#/$defs/scale`

親内必須: `id`, `start`, `duration`, `tonic`, `intervals`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/id` |
| `start` | nonnegative | 必須 | — | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/start` |
| `duration` | positive | 必須 | — | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/duration` |
| `label` | string | 任意／条件付き | — | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/label` |
| `tonic` | spelledPitchClass | 必須 | — | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/tonic` |
| `intervals` | array<integer> | 必須 | minItems=1; maxItems=12; uniqueItems=true | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/intervals` |
| `targets` | array<scaleTarget> | 任意／条件付き | minItems=1; uniqueItems=true; Optional explicit scope. Absence means general timed context, not a global key. Overlapping contexts are not resolved by array order. | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/targets` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "tonic": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 11
      },
      "minItems": 1,
      "maxItems": 12,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "targets": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/scaleTarget"
      },
      "minItems": 1,
      "uniqueItems": true,
      "description": "Optional explicit scope. Absence means general timed context, not a global key. Overlapping contexts are not resolved by array order."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "tonic",
    "intervals"
  ],
  "additionalProperties": false
}
```

<a id="core-harmony"></a>
## harmony

`#/$defs/harmony`

親内必須: `chords`, `scales`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `chords` | array<chord> | 必須 | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/harmony/chords` |
| `scales` | array<scale> | 必須 | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/harmony/scales` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "chords": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/chord"
      }
    },
    "scales": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/scale"
      }
    }
  },
  "required": [
    "chords",
    "scales"
  ],
  "additionalProperties": false
}
```

<a id="core-instrument"></a>
## instrument

`#/$defs/instrument`

親内必須: `name`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `name` | string | 必須 | — | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/instrument/name` |
| `family` | string | 任意／条件付き | — | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/instrument/family` |
| `localizedNames` | localizedNames | 任意／条件付き | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/instrument/localizedNames` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "family": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```

<a id="core-note"></a>
## note

`#/$defs/note`

Concrete performed Core note. Native phrase templates use corePhraseSourceNote; legacy source-note schemas remain frozen.

親内必須: `id`, `start`, `duration`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/notes/0/id` |
| `start` | signed | 必須 | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/notes/0/start` |
| `duration` | positive | 必須 | Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample. | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/notes/0/duration` |
| `pitch` | pitch | 任意／条件付き | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/notes/0/pitch` |
| `soundSlotId` | id | 任意／条件付き | Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre. | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/tracks/0/clips/0/notes/1/soundSlotId` |
| `velocity` | integer | 任意／条件付き | minimum=1; maximum=127; Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving. | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/notes/0/velocity` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive",
      "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
    },
    "pitch": {
      "$ref": "#/$defs/pitch"
    },
    "soundSlotId": {
      "$ref": "#/$defs/id",
      "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
    },
    "velocity": {
      "type": "integer",
      "minimum": 1,
      "maximum": 127,
      "description": "Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving."
    }
  },
  "required": [
    "id",
    "start",
    "duration"
  ],
  "additionalProperties": false,
  "oneOf": [
    {
      "required": [
        "pitch"
      ],
      "not": {
        "required": [
          "soundSlotId"
        ]
      }
    },
    {
      "required": [
        "soundSlotId"
      ],
      "not": {
        "required": [
          "pitch"
        ]
      }
    }
  ],
  "description": "Concrete performed Core note. Native phrase templates use corePhraseSourceNote; legacy source-note schemas remain frozen."
}
```

<a id="core-clip"></a>
## clip

`#/$defs/clip`

親内必須: `id`, `start`, `duration`, `notes`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/id` |
| `name` | string | 任意／条件付き | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/name` |
| `start` | nonnegative | 必須 | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/start` |
| `duration` | positive | 必須 | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/duration` |
| `enabled` | boolean | 任意／条件付き | default=true | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/tracks/0/clips/0/enabled` |
| `notes` | array<note> | 必須 | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/notes` |
| `localizedNames` | localizedNames | 任意／条件付き | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/clips/0/localizedNames` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "enabled": {
      "type": "boolean",
      "default": true
    },
    "notes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/note"
      }
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "notes"
  ],
  "additionalProperties": false
}
```

<a id="core-track"></a>
## track

`#/$defs/track`

親内必須: `id`, `name`, `clips`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/id` |
| `name` | string | 必須 | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/name` |
| `role` | string | 任意／条件付き | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/role` |
| `instrument` | instrument | 任意／条件付き | — | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/instrument` |
| `enabled` | boolean | 任意／条件付き | default=true | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/enabled` |
| `clips` | array<clip> | 必須 | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips` |
| `trackType` | enum ["melodic", "drum", "mixed"] | 任意／条件付き | Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class. | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/trackType` |
| `preferredView` | enum ["auto", "pianoRoll", "drumGrid"] | 任意／条件付き | default="auto"; Non-binding presentation preference. Does not change note meaning. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/preferredView` |
| `soundSource` | soundSource | 任意／条件付き | Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/soundSource` |
| `localizedNames` | localizedNames | 任意／条件付き | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/localizedNames` |
| `drumKitId` | id | 任意／条件付き | Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit. | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/tracks/0/drumKitId` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "role": {
      "type": "string"
    },
    "instrument": {
      "$ref": "#/$defs/instrument"
    },
    "enabled": {
      "type": "boolean",
      "default": true
    },
    "clips": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/clip"
      }
    },
    "trackType": {
      "enum": [
        "melodic",
        "drum",
        "mixed"
      ],
      "description": "Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class."
    },
    "preferredView": {
      "enum": [
        "auto",
        "pianoRoll",
        "drumGrid"
      ],
      "default": "auto",
      "description": "Non-binding presentation preference. Does not change note meaning."
    },
    "soundSource": {
      "$ref": "#/$defs/soundSource",
      "description": "Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee."
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    },
    "drumKitId": {
      "$ref": "#/$defs/id",
      "description": "Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit."
    }
  },
  "required": [
    "id",
    "name",
    "clips"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "trackType": {
            "const": "melodic"
          }
        },
        "required": [
          "trackType"
        ]
      },
      "then": {
        "not": {
          "required": [
            "drumKitId"
          ]
        }
      }
    }
  ]
}
```

<a id="core-soundslot"></a>
## soundSlot

`#/$defs/soundSlot`

Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded.

親内必須: `id`, `name`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/soundSlots/0/id` |
| `name` | string | 必須 | — | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/soundSlots/0/name` |
| `role` | string | 任意／条件付き | Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier. | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/soundSlots/0/role` |
| `midiNote` | pitch | 任意／条件付き | Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/soundSlots/0/midiNote` |
| `midiMapping` | midiMapping | 任意／条件付き | Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity. | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/soundSlots/0/midiMapping` |
| `localizedNames` | localizedNames | 任意／条件付き | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/soundSlots/0/localizedNames` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "role": {
      "type": "string",
      "description": "Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier."
    },
    "midiNote": {
      "$ref": "#/$defs/pitch",
      "description": "Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity."
    },
    "midiMapping": {
      "$ref": "#/$defs/midiMapping",
      "description": "Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity."
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false,
  "description": "Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded."
}
```

<a id="core-lyricdocument"></a>
## lyricDocument

`#/$defs/lyricDocument`

親内必須: `id`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/documents/0/id` |
| `title` | string | 任意／条件付き | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/documents/0/title` |
| `language` | string | 任意／条件付き | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/documents/0/language` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "title": {
      "type": "string"
    },
    "language": {
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```

<a id="core-lyricphrase"></a>
## lyricPhrase

`#/$defs/lyricPhrase`

親内必須: `id`, `documentId`, `text`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/phrases/0/id` |
| `documentId` | id | 必須 | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/phrases/0/documentId` |
| `text` | string | 必須 | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/phrases/0/text` |
| `pronunciation` | string | 任意／条件付き | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/phrases/0/pronunciation` |
| `start` | nonnegative | 任意／条件付き | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/phrases/0/start` |
| `duration` | positive | 任意／条件付き | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/phrases/0/duration` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "documentId": {
      "$ref": "#/$defs/id"
    },
    "text": {
      "type": "string"
    },
    "pronunciation": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    }
  },
  "required": [
    "id",
    "documentId",
    "text"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "start": [
      "duration"
    ],
    "duration": [
      "start"
    ]
  }
}
```

<a id="core-lyricunit"></a>
## lyricUnit

`#/$defs/lyricUnit`

親内必須: `id`, `phraseId`, `text`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/units/0/id` |
| `phraseId` | id | 必須 | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/units/0/phraseId` |
| `text` | string | 必須 | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/units/0/text` |
| `pronunciation` | string | 任意／条件付き | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/units/0/pronunciation` |
| `start` | nonnegative | 任意／条件付き | — | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/lyrics/units/0/start` |
| `duration` | positive | 任意／条件付き | — | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/lyrics/units/0/duration` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "phraseId": {
      "$ref": "#/$defs/id"
    },
    "text": {
      "type": "string"
    },
    "pronunciation": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    }
  },
  "required": [
    "id",
    "phraseId",
    "text"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "start": [
      "duration"
    ],
    "duration": [
      "start"
    ]
  }
}
```

<a id="core-lyricalignment"></a>
## lyricAlignment

`#/$defs/lyricAlignment`

親内必須: `id`, `unitIds`, `noteIds`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/alignments/0/id` |
| `unitIds` | array<id> | 必須 | minItems=1; uniqueItems=true | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/alignments/0/unitIds` |
| `noteIds` | array<id> | 必須 | minItems=1; uniqueItems=true | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/alignments/0/noteIds` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "unitIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true,
      "minItems": 1
    },
    "noteIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true,
      "minItems": 1
    }
  },
  "required": [
    "id",
    "unitIds",
    "noteIds"
  ],
  "additionalProperties": false
}
```

<a id="core-lyrics"></a>
## lyrics

`#/$defs/lyrics`

親内必須: `documents`, `phrases`, `units`, `alignments`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `documents` | array<lyricDocument> | 必須 | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/lyrics/documents` |
| `phrases` | array<lyricPhrase> | 必須 | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/lyrics/phrases` |
| `units` | array<lyricUnit> | 必須 | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/lyrics/units` |
| `alignments` | array<lyricAlignment> | 必須 | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/lyrics/alignments` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "documents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricDocument"
      }
    },
    "phrases": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricPhrase"
      }
    },
    "units": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricUnit"
      }
    },
    "alignments": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricAlignment"
      }
    }
  },
  "required": [
    "documents",
    "phrases",
    "units",
    "alignments"
  ],
  "additionalProperties": false
}
```

<a id="core-sha256"></a>
## sha256

`#/$defs/sha256`

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "string",
  "pattern": "^[0-9a-f]{64}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```

<a id="core-resource"></a>
## resource

`#/$defs/resource`

親内必須: `id`, `kind`, `uri`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/resources/0/id` |
| `kind` | enum ["audio", "midi", "text", "other"] | 必須 | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/resources/0/kind` |
| `uri` | string | 必須 | minLength=1 | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/resources/0/uri` |
| `name` | string | 任意／条件付き | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/resources/0/name` |
| `sha256` | sha256 | 任意／条件付き | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/resources/0/sha256` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "kind": {
      "enum": [
        "audio",
        "midi",
        "text",
        "other"
      ]
    },
    "uri": {
      "type": "string",
      "minLength": 1
    },
    "name": {
      "type": "string"
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    }
  },
  "required": [
    "id",
    "kind",
    "uri"
  ],
  "additionalProperties": false
}
```

<a id="core-dependencies"></a>
## dependencies

`#/$defs/dependencies`

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "scope": {
          "enum": [
            "document",
            "none"
          ]
        }
      },
      "required": [
        "scope"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "scope": {
          "const": "objects"
        },
        "refs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/ref"
          },
          "minItems": 1,
          "uniqueItems": true
        }
      },
      "required": [
        "scope",
        "refs"
      ],
      "additionalProperties": false
    }
  ]
}
```

<a id="core-relativeassignment"></a>
## relativeAssignment

`#/$defs/relativeAssignment`

親内必須: `noteId`, `basis`, `contextId`, `anchorPitch`, `index`, `chromaticOffset`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `noteId` | id | 必須 | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments/0/noteId` |
| `basis` | enum ["chordTone", "scaleDegree"] | 必須 | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments/0/basis` |
| `contextId` | id | 必須 | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments/0/contextId` |
| `anchorPitch` | pitch | 必須 | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments/0/anchorPitch` |
| `index` | integer | 必須 | minimum=1; maximum=36 | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments/0/index` |
| `chromaticOffset` | integer | 必須 | minimum=-24; maximum=24 | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments/0/chromaticOffset` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "noteId": {
      "$ref": "#/$defs/id"
    },
    "basis": {
      "enum": [
        "chordTone",
        "scaleDegree"
      ]
    },
    "contextId": {
      "$ref": "#/$defs/id"
    },
    "anchorPitch": {
      "$ref": "#/$defs/pitch"
    },
    "index": {
      "type": "integer",
      "minimum": 1,
      "maximum": 36
    },
    "chromaticOffset": {
      "type": "integer",
      "minimum": -24,
      "maximum": 24
    }
  },
  "required": [
    "noteId",
    "basis",
    "contextId",
    "anchorPitch",
    "index",
    "chromaticOffset"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "basis": {
            "const": "scaleDegree"
          }
        },
        "required": [
          "basis"
        ]
      },
      "then": {
        "properties": {
          "index": {
            "maximum": 12
          }
        }
      }
    }
  ]
}
```

<a id="core-generator"></a>
## generator

`#/$defs/generator`

親内必須: `id`, `version`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | string | 必須 | minLength=1 | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/generator/id` |
| `version` | string | 必須 | minLength=1 | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/generator/version` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "id",
    "version"
  ],
  "additionalProperties": false
}
```

<a id="core-generationinput"></a>
## generationInput

`#/$defs/generationInput`

親内必須: `role`, `ref`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `role` | string | 必須 | minLength=1 | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/inputs/0/role` |
| `ref` | ref | 必須 | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/inputs/0/ref` |
| `readRange` | range | 任意／条件付き | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/inputs/0/readRange` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "role": {
      "type": "string",
      "minLength": 1
    },
    "ref": {
      "$ref": "#/$defs/ref"
    },
    "readRange": {
      "$ref": "#/$defs/range"
    }
  },
  "required": [
    "role",
    "ref"
  ],
  "additionalProperties": false
}
```

<a id="core-generationprocess"></a>
## generationProcess

`#/$defs/generationProcess`

親内必須: `id`, `generator`, `inputs`, `outputs`, `protectedNoteIds`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/id` |
| `generator` | generator | 必須 | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/generator` |
| `inputs` | array<generationInput> | 必須 | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/inputs` |
| `outputs` | array<ref> | 必須 | minItems=1 | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/outputs` |
| `targetRange` | range | 任意／条件付き | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/targetRange` |
| `protectedNoteIds` | array<id> | 必須 | uniqueItems=true | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/protectedNoteIds` |
| `intent` | generationIntent | 任意／条件付き | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "generator": {
      "$ref": "#/$defs/generator"
    },
    "inputs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/generationInput"
      }
    },
    "outputs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/ref"
      },
      "minItems": 1
    },
    "targetRange": {
      "$ref": "#/$defs/range"
    },
    "protectedNoteIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    },
    "intent": {
      "$ref": "#/$defs/generationIntent"
    }
  },
  "required": [
    "id",
    "generator",
    "inputs",
    "outputs",
    "protectedNoteIds"
  ],
  "additionalProperties": false
}
```

<a id="core-color"></a>
## color

`#/$defs/color`

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "string",
  "pattern": "^#[0-9A-Fa-f]{6}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```

<a id="core-roledefinition"></a>
## roleDefinition

`#/$defs/roleDefinition`

親内必須: `id`, `name`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/roleDefinitions/0/id` |
| `name` | string | 必須 | minLength=1 | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/roleDefinitions/0/name` |
| `baseRole` | string | 任意／条件付き | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/roleDefinitions/0/baseRole` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "baseRole": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```

<a id="core-rolecolormap"></a>
## roleColorMap

`#/$defs/roleColorMap`

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "additionalProperties": {
    "$ref": "#/$defs/color"
  }
}
```

<a id="core-customrolecolormap"></a>
## customRoleColorMap

`#/$defs/customRoleColorMap`

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "propertyNames": {
    "$ref": "#/$defs/id"
  },
  "additionalProperties": {
    "$ref": "#/$defs/color"
  }
}
```

<a id="core-objectcolor"></a>
## objectColor

`#/$defs/objectColor`

親内必須: `target`, `color`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `target` | ref | 必須 | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/appearance/objectColors/0/target` |
| `color` | color | 必須 | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/appearance/objectColors/0/color` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "target": {
      "$ref": "#/$defs/ref"
    },
    "color": {
      "$ref": "#/$defs/color"
    }
  },
  "required": [
    "target",
    "color"
  ],
  "additionalProperties": false
}
```

<a id="core-phrasetemplate"></a>
## phraseTemplate

`#/$defs/phraseTemplate`

親内必須: `id`, `duration`, `notes`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/id` |
| `duration` | positive | 必須 | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/duration` |
| `notes` | array<corePhraseSourceNote> | 必須 | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/notes` |
| `name` | string | 任意／条件付き | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/name` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "notes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/corePhraseSourceNote"
      }
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "duration",
    "notes"
  ],
  "additionalProperties": false
}
```

<a id="core-phrasenotemapping"></a>
## phraseNoteMapping

`#/$defs/phraseNoteMapping`

親内必須: `templateNoteId`, `repeatIndex`, `noteId`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `templateNoteId` | id | 必須 | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/noteMap/0/templateNoteId` |
| `repeatIndex` | nonnegative | 必須 | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/noteMap/0/repeatIndex` |
| `noteId` | id | 必須 | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/noteMap/0/noteId` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "templateNoteId": {
      "$ref": "#/$defs/id"
    },
    "repeatIndex": {
      "$ref": "#/$defs/nonnegative"
    },
    "noteId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "templateNoteId",
    "repeatIndex",
    "noteId"
  ],
  "additionalProperties": false
}
```

<a id="core-phraseinstance"></a>
## phraseInstance

`#/$defs/phraseInstance`

親内必須: `id`, `templateId`, `clipId`, `repeatCount`, `transpose`, `noteMap`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/id` |
| `templateId` | id | 必須 | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/templateId` |
| `clipId` | id | 必須 | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/clipId` |
| `repeatCount` | positive | 必須 | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/repeatCount` |
| `transpose` | integer | 必須 | minimum=-127; maximum=127 | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/transpose` |
| `noteMap` | array<phraseNoteMapping> | 必須 | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/noteMap` |
| `velocityMode` | enum ["independent", "linked"] | 任意／条件付き | default="independent"; independent preserves concrete velocities on refresh; linked requires exact presence/value equality with the template. This field does not trigger refresh on load. | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/velocityMode` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "templateId": {
      "$ref": "#/$defs/id"
    },
    "clipId": {
      "$ref": "#/$defs/id"
    },
    "repeatCount": {
      "$ref": "#/$defs/positive"
    },
    "transpose": {
      "type": "integer",
      "minimum": -127,
      "maximum": 127
    },
    "noteMap": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/phraseNoteMapping"
      }
    },
    "velocityMode": {
      "enum": [
        "independent",
        "linked"
      ],
      "default": "independent",
      "description": "independent preserves concrete velocities on refresh; linked requires exact presence/value equality with the template. This field does not trigger refresh on load."
    }
  },
  "required": [
    "id",
    "templateId",
    "clipId",
    "repeatCount",
    "transpose",
    "noteMap"
  ],
  "additionalProperties": false
}
```

<a id="core-clipcandidate"></a>
## clipCandidate

`#/$defs/clipCandidate`

親内必須: `id`, `clipIds`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/candidates/0/id` |
| `clipIds` | array<id> | 必須 | uniqueItems=true | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/candidates/0/clipIds` |
| `name` | string | 任意／条件付き | — | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/candidates/0/name` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "clipIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "clipIds"
  ],
  "additionalProperties": false
}
```

<a id="core-clipchoicegroup"></a>
## clipChoiceGroup

`#/$defs/clipChoiceGroup`

親内必須: `id`, `candidates`, `selectedCandidateId`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/id` |
| `candidates` | array<clipCandidate> | 必須 | minItems=1 | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/candidates` |
| `selectedCandidateId` | oneOf/anyOf | 必須 | — | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/selectedCandidateId` |
| `name` | string | 任意／条件付き | — | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/name` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "candidates": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/clipCandidate"
      },
      "minItems": 1
    },
    "selectedCandidateId": {
      "anyOf": [
        {
          "$ref": "#/$defs/id"
        },
        {
          "type": "null"
        }
      ]
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "candidates",
    "selectedCandidateId"
  ],
  "additionalProperties": false
}
```

<a id="core-midimapping"></a>
## midiMapping

`#/$defs/midiMapping`

親内必須: `standard`, `note`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `standard` | enum ["gm1", "custom"] | 必須 | gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number. | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/soundSlots/0/midiMapping/standard` |
| `note` | pitch | 必須 | MIDI1 note number in 0..127; for gm1 restrict to 35..81. | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/soundSlots/0/midiMapping/note` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "standard": {
      "enum": [
        "gm1",
        "custom"
      ],
      "description": "gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number."
    },
    "note": {
      "$ref": "#/$defs/pitch",
      "description": "MIDI1 note number in 0..127; for gm1 restrict to 35..81."
    }
  },
  "required": [
    "standard",
    "note"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "standard": {
            "const": "gm1"
          }
        },
        "required": [
          "standard"
        ]
      },
      "then": {
        "properties": {
          "note": {
            "type": "integer",
            "minimum": 35,
            "maximum": 81
          }
        }
      }
    }
  ]
}
```

<a id="core-soundsource"></a>
## soundSource

`#/$defs/soundSource`

Optional informational rendering class or opaque destination hint. Program Change, Bank Select and plugin presets are not standardized by Core.

親内必須: `kind`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `kind` | enum ["unassigned", "gm1", "externalMidi", "plugin", "hostManaged"] | 必須 | — | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/soundSource/kind` |
| `identifier` | string | 任意／条件付き | minLength=1; Opaque target identifier, e.g. URI, plug-in identifier or port alias, not a loading command. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/soundSource/identifier` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "description": "Optional informational rendering class or opaque destination hint. Program Change, Bank Select and plugin presets are not standardized by Core.",
  "properties": {
    "kind": {
      "enum": [
        "unassigned",
        "gm1",
        "externalMidi",
        "plugin",
        "hostManaged"
      ]
    },
    "identifier": {
      "type": "string",
      "minLength": 1,
      "description": "Opaque target identifier, e.g. URI, plug-in identifier or port alias, not a loading command."
    }
  },
  "required": [
    "kind"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "kind": {
            "enum": [
              "gm1",
              "unassigned"
            ]
          }
        },
        "required": [
          "kind"
        ]
      },
      "then": {
        "not": {
          "required": [
            "identifier"
          ]
        }
      }
    }
  ]
}
```

<a id="core-localizednames"></a>
## localizedNames

`#/$defs/localizedNames`

Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically.

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "minProperties": 1,
  "propertyNames": {
    "type": "string",
    "pattern": "^(?:[A-Za-z]{2,3}|[A-Za-z]{5,8})(?:-[A-Za-z0-9]{2,8})*$"
  },
  "additionalProperties": {
    "type": "string",
    "minLength": 1
  },
  "description": "Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically."
}
```

<a id="core-drumkit"></a>
## drumKit

`#/$defs/drumKit`

Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.

親内必須: `id`, `name`, `soundSlotIds`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/drumKits/0/id` |
| `name` | string | 必須 | — | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/drumKits/0/name` |
| `localizedNames` | localizedNames | 任意／条件付き | — | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/drumKits/0/localizedNames` |
| `soundSlotIds` | array<id> | 必須 | uniqueItems=true; Ordered, unique references to global soundSlots; may be empty. | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/drumKits/0/soundSlotIds` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "description": "Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames"
    },
    "soundSlotIds": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "$ref": "#/$defs/id"
      },
      "description": "Ordered, unique references to global soundSlots; may be empty."
    }
  },
  "required": [
    "id",
    "name",
    "soundSlotIds"
  ],
  "additionalProperties": false
}
```

<a id="core-voicing"></a>
## voicing

`#/$defs/voicing`

Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.

親内必須: `pitches`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `pitches` | array<pitch> | 必須 | minItems=1; Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed. | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/voicing/pitches` |
| `velocities` | array<oneOf/anyOf> | 任意／条件付き | minItems=1; Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic. | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/voicing/velocities` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.",
  "properties": {
    "pitches": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/pitch"
      },
      "description": "Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed."
    },
    "velocities": {
      "type": "array",
      "minItems": 1,
      "items": {
        "anyOf": [
          {
            "type": "integer",
            "minimum": 1,
            "maximum": 127
          },
          {
            "type": "null"
          }
        ]
      },
      "description": "Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic."
    }
  },
  "required": [
    "pitches"
  ]
}
```

<a id="core-contributor"></a>
## contributor

`#/$defs/contributor`

One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.

親内必須: `id`, `name`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/contributors/0/id` |
| `name` | string | 必須 | minLength=1 | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/contributors/0/name` |
| `kind` | enum ["person", "organization", "other"] | 任意／条件付き | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/contributors/0/kind` |
| `localizedNames` | localizedNames | 任意／条件付き | — | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/contributors/0/localizedNames` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "kind": {
      "enum": [
        "person",
        "organization",
        "other"
      ]
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames"
    }
  },
  "required": [
    "id",
    "name"
  ]
}
```

<a id="core-credit"></a>
## credit

`#/$defs/credit`

Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.

親内必須: `id`, `contributorId`, `role`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/credits/0/id` |
| `contributorId` | id | 必須 | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/credits/0/contributorId` |
| `role` | string | 必須 | pattern="^[a-z][a-z0-9.-]*$" | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/credits/0/role` |
| `label` | string | 任意／条件付き | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/credits/0/label` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "contributorId": {
      "$ref": "#/$defs/id"
    },
    "role": {
      "type": "string",
      "pattern": "^[a-z][a-z0-9.-]*$"
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "contributorId",
    "role"
  ]
}
```

<a id="core-alternatetitle"></a>
## alternateTitle

`#/$defs/alternateTitle`

Stable-ID song title alternative; array position and title text do not identify it.

親内必須: `id`, `title`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/alternateTitles/0/id` |
| `title` | string | 必須 | minLength=1 | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/alternateTitles/0/title` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Stable-ID song title alternative; array position and title text do not identify it.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "title": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "id",
    "title"
  ]
}
```

<a id="core-languagemap32"></a>
## languageMap32

`#/$defs/languageMap32`

Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank.

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "minProperties": 1,
  "propertyNames": {
    "type": "string",
    "pattern": "^[A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})*$"
  },
  "additionalProperties": {
    "type": "string"
  },
  "description": "Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank."
}
```

<a id="core-localizationtarget"></a>
## localizationTarget

`#/$defs/localizationTarget`

Core target; song is ID-less, all others use global Core ID. No namespace/profile selector.

親内必須: `kind`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `kind` | enum ["song", "alternateTitle", "contributor", "credit", "section", "track", "clip", "soundSlot", "drumKit", "lyricDocument", "resource", "phraseTemplate", "clipCandidate", "clipChoiceGroup", "roleDefinition", "genre", "mood", "keyChange", "scale"] | 必須 | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries/0/target/kind` |
| `id` | id | 任意／条件付き | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries/1/target/id` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "kind": {
      "enum": [
        "song",
        "alternateTitle",
        "contributor",
        "credit",
        "section",
        "track",
        "clip",
        "soundSlot",
        "drumKit",
        "lyricDocument",
        "resource",
        "phraseTemplate",
        "clipCandidate",
        "clipChoiceGroup",
        "roleDefinition",
        "genre",
        "mood",
        "keyChange",
        "scale"
      ]
    },
    "id": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "kind"
  ],
  "allOf": [
    {
      "if": {
        "properties": {
          "kind": {
            "const": "song"
          }
        },
        "required": [
          "kind"
        ]
      },
      "then": {
        "not": {
          "required": [
            "id"
          ]
        }
      },
      "else": {
        "required": [
          "id"
        ]
      }
    }
  ],
  "description": "Core target; song is ID-less, all others use global Core ID. No namespace/profile selector."
}
```

<a id="core-localizationentry"></a>
## localizationEntry

`#/$defs/localizationEntry`

Independent translations for one stable source field. Original source text remains authoritative as fallback.

親内必須: `target`, `field`, `values`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `target` | localizationTarget | 必須 | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries/0/target` |
| `field` | string | 必須 | minLength=1; Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields. | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries/0/field` |
| `values` | languageMap32 | 必須 | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries/0/values` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "target": {
      "$ref": "#/$defs/localizationTarget"
    },
    "field": {
      "type": "string",
      "minLength": 1,
      "description": "Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields."
    },
    "values": {
      "$ref": "#/$defs/languageMap32"
    }
  },
  "required": [
    "target",
    "field",
    "values"
  ],
  "description": "Independent translations for one stable source field. Original source text remains authoritative as fallback."
}
```

<a id="core-genre"></a>
## genre

`#/$defs/genre`

One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.

親内必須: `id`, `name`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | Stable song-local ID unique among all Core objects. | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/genres/0/id` |
| `name` | string | 必須 | minLength=1; Original Unicode genre label, never normalized or rewritten during import. | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/genres/0/name` |
| `externalUri` | string | 任意／条件付き | minLength=1; format="uri"; Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced. | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/genres/0/externalUri` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "description": "One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id",
      "description": "Stable song-local ID unique among all Core objects."
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "description": "Original Unicode genre label, never normalized or rewritten during import."
    },
    "externalUri": {
      "type": "string",
      "minLength": 1,
      "format": "uri",
      "description": "Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```

<a id="core-opaquedocumentid"></a>
## opaqueDocumentId

`#/$defs/opaqueDocumentId`

Stable URI or UUID-style identifier for a document lineage. Compared as exact Unicode text; never fetched.

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "string",
  "minLength": 1,
  "description": "Stable URI or UUID-style identifier for a document lineage. Compared as exact Unicode text; never fetched."
}
```

<a id="core-revisionref"></a>
## revisionRef

`#/$defs/revisionRef`

親内必須: `documentId`, `revisionId`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `documentId` | opaqueDocumentId | 必須 | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/parents/0/documentId` |
| `revisionId` | opaqueDocumentId | 必須 | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/parents/0/revisionId` |
| `sha256` | sha256 | 任意／条件付き | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/parents/0/sha256` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "documentId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "revisionId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    }
  },
  "required": [
    "documentId",
    "revisionId"
  ],
  "additionalProperties": false
}
```

<a id="core-software"></a>
## software

`#/$defs/software`

親内必須: `name`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `name` | string | 必須 | minLength=1 | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/createdBy/name` |
| `version` | string | 任意／条件付き | minLength=1 | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/createdBy/version` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```

<a id="core-documentinfo"></a>
## documentInfo

`#/$defs/documentInfo`

親内必須: `id`, `revisionId`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | opaqueDocumentId | 必須 | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/id` |
| `revisionId` | opaqueDocumentId | 必須 | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/revisionId` |
| `parents` | array<revisionRef> | 任意／条件付き | uniqueItems=true | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/parents` |
| `createdBy` | software | 任意／条件付き | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/createdBy` |
| `modifiedBy` | software | 任意／条件付き | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/modifiedBy` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "revisionId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "parents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/revisionRef"
      },
      "uniqueItems": true
    },
    "createdBy": {
      "$ref": "#/$defs/software"
    },
    "modifiedBy": {
      "$ref": "#/$defs/software"
    }
  },
  "required": [
    "id",
    "revisionId"
  ],
  "additionalProperties": false
}
```

<a id="core-key"></a>
## key

`#/$defs/key`

親内必須: `state`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `state` | enum ["tonal", "atonal", "unspecified"] | 必須 | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/key/state` |
| `tonic` | spelledPitchClass | 任意／条件付き | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/key/tonic` |
| `mode` | string | 任意／条件付き | minLength=1; Authored mode identifier. Canonical recognized values include major, minor, dorian, phrygian, lydian, mixolydian, locrian. Unknown values are preserved, never converted to major/minor. | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/key/mode` |
| `label` | string | 任意／条件付き | — | [samples/05_custom_mode_and_scale.ostf](../samples/05_custom_mode_and_scale.ostf) `/song/key/label` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "state": {
      "enum": [
        "tonal",
        "atonal",
        "unspecified"
      ]
    },
    "tonic": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "mode": {
      "type": "string",
      "minLength": 1,
      "description": "Authored mode identifier. Canonical recognized values include major, minor, dorian, phrygian, lydian, mixolydian, locrian. Unknown values are preserved, never converted to major/minor."
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "state"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "state": {
            "const": "tonal"
          }
        },
        "required": [
          "state"
        ]
      },
      "then": {
        "required": [
          "tonic",
          "mode"
        ]
      },
      "else": {
        "not": {
          "anyOf": [
            {
              "required": [
                "tonic"
              ]
            },
            {
              "required": [
                "mode"
              ]
            }
          ]
        }
      }
    }
  ]
}
```

<a id="core-keychange"></a>
## keyChange

`#/$defs/keyChange`

A change after tick zero; initial key is stored only at song.key. Change at tick 0 is forbidden to prevent dual authority.

親内必須: `id`, `at`, `key`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/03_modulation_atonal_and_unspecified.ostf](../samples/03_modulation_atonal_and_unspecified.ostf) `/timeline/keyChanges/0/id` |
| `at` | positive | 必須 | — | [samples/03_modulation_atonal_and_unspecified.ostf](../samples/03_modulation_atonal_and_unspecified.ostf) `/timeline/keyChanges/0/at` |
| `key` | key | 必須 | — | [samples/03_modulation_atonal_and_unspecified.ostf](../samples/03_modulation_atonal_and_unspecified.ostf) `/timeline/keyChanges/0/key` |
| `label` | string | 任意／条件付き | — | [samples/03_modulation_atonal_and_unspecified.ostf](../samples/03_modulation_atonal_and_unspecified.ostf) `/timeline/keyChanges/0/label` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "at": {
      "$ref": "#/$defs/positive"
    },
    "key": {
      "$ref": "#/$defs/key"
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "at",
    "key"
  ],
  "additionalProperties": false,
  "description": "A change after tick zero; initial key is stored only at song.key. Change at tick 0 is forbidden to prevent dual authority."
}
```

<a id="core-scaledefinition"></a>
## scaleDefinition

`#/$defs/scaleDefinition`

親内必須: `id`, `tonic`, `intervals`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/04_scale_without_key.ostf](../samples/04_scale_without_key.ostf) `/song/scale/id` |
| `tonic` | spelledPitchClass | 必須 | — | [samples/04_scale_without_key.ostf](../samples/04_scale_without_key.ostf) `/song/scale/tonic` |
| `intervals` | array<integer> | 必須 | minItems=1; maxItems=12; uniqueItems=true | [samples/04_scale_without_key.ostf](../samples/04_scale_without_key.ostf) `/song/scale/intervals` |
| `label` | string | 任意／条件付き | — | [samples/04_scale_without_key.ostf](../samples/04_scale_without_key.ostf) `/song/scale/label` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "tonic": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 11
      },
      "minItems": 1,
      "maxItems": 12,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "tonic",
    "intervals"
  ],
  "additionalProperties": false
}
```

<a id="core-scaletarget"></a>
## scaleTarget

`#/$defs/scaleTarget`

親内必須: `type`, `id`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `type` | enum ["section", "track", "clip", "chord", "note"] | 必須 | — | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/targets/0/type` |
| `id` | id | 必須 | — | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/targets/0/id` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "type": {
      "enum": [
        "section",
        "track",
        "clip",
        "chord",
        "note"
      ]
    },
    "id": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "type",
    "id"
  ],
  "additionalProperties": false
}
```

<a id="core-mood"></a>
## mood

`#/$defs/mood`

Authored descriptive mood tag; not a generator preset or a probability.

親内必須: `id`, `name`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | Stable song-local ID unique among all Core objects. | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/moods/0/id` |
| `name` | string | 必須 | minLength=1; Original Unicode genre label, never normalized or rewritten during import. | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/moods/0/name` |
| `externalUri` | string | 任意／条件付き | minLength=1; format="uri"; Optional external vocabulary URI hint; never authoritative for the authored mood name and never auto-dereferenced. | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/moods/0/externalUri` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "description": "Authored descriptive mood tag; not a generator preset or a probability.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id",
      "description": "Stable song-local ID unique among all Core objects."
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "description": "Original Unicode genre label, never normalized or rewritten during import."
    },
    "externalUri": {
      "type": "string",
      "minLength": 1,
      "format": "uri",
      "description": "Optional external vocabulary URI hint; never authoritative for the authored mood name and never auto-dereferenced."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```

<a id="core-rightsstatement"></a>
## rightsStatement

`#/$defs/rightsStatement`

Authored rights statement only; no rights or permissions are inferred or granted by the format.

親内必須: —

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `notice` | string | 任意／条件付き | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/rights/notice` |
| `licenseUri` | string | 任意／条件付き | minLength=1 | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/rights/licenseUri` |
| `rightsHolderIds` | array<id> | 任意／条件付き | uniqueItems=true | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/rights/rightsHolderIds` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "notice": {
      "type": "string"
    },
    "licenseUri": {
      "type": "string",
      "minLength": 1
    },
    "rightsHolderIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Authored rights statement only; no rights or permissions are inferred or granted by the format.",
  "minProperties": 1
}
```

<a id="core-grooveintent"></a>
## grooveIntent

`#/$defs/grooveIntent`

Descriptive generation intent only. Never re-apply to already stored notes. unitTicks is one unswung subdivision; two subdivisions form a pair.

親内必須: —

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `name` | string | 任意／条件付き | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/groove/name` |
| `unitTicks` | positive | 任意／条件付き | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/groove/unitTicks` |
| `longWeight` | integer | 任意／条件付き | minimum=1; maximum=1000000 | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/groove/longWeight` |
| `shortWeight` | integer | 任意／条件付き | minimum=1; maximum=1000000 | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/groove/shortWeight` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "unitTicks": {
      "$ref": "#/$defs/positive"
    },
    "longWeight": {
      "type": "integer",
      "minimum": 1,
      "maximum": 1000000
    },
    "shortWeight": {
      "type": "integer",
      "minimum": 1,
      "maximum": 1000000
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Descriptive generation intent only. Never re-apply to already stored notes. unitTicks is one unswung subdivision; two subdivisions form a pair.",
  "minProperties": 1,
  "dependentRequired": {
    "unitTicks": [
      "longWeight",
      "shortWeight"
    ],
    "longWeight": [
      "unitTicks",
      "shortWeight"
    ],
    "shortWeight": [
      "unitTicks",
      "longWeight"
    ]
  }
}
```

<a id="core-generationintent"></a>
## generationIntent

`#/$defs/generationIntent`

Portable description of intent, not a promise to reproduce an algorithm. Does not change song.genres or song.moods.

親内必須: —

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `genreNames` | array<string> | 任意／条件付き | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/genreNames` |
| `moodNames` | array<string> | 任意／条件付き | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/moodNames` |
| `groove` | grooveIntent | 任意／条件付き | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/groove` |
| `prompt` | string | 任意／条件付き | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/prompt` |
| `seed` | string | 任意／条件付き | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/seed` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "genreNames": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      }
    },
    "moodNames": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      }
    },
    "groove": {
      "$ref": "#/$defs/grooveIntent"
    },
    "prompt": {
      "type": "string"
    },
    "seed": {
      "type": "string"
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Portable description of intent, not a promise to reproduce an algorithm. Does not change song.genres or song.moods."
}
```

<a id="core-relativephrases"></a>
## relativePhrases

`#/$defs/relativePhrases`

Standard optional Core object under root version 3.4.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

親内必須: `status`, `dependencies`, `assignments`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `status` | enum ["current", "stale", "unverified"] | 必須 | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/status` |
| `dependencies` | dependencies | 必須 | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/dependencies` |
| `assignments` | array<relativeAssignment> | 必須 | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "assignments": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/relativeAssignment"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "assignments"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 3.4.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="core-generation"></a>
## generation

`#/$defs/generation`

Standard optional Core object under root version 3.4.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

親内必須: `status`, `dependencies`, `processes`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `status` | enum ["current", "stale", "unverified"] | 必須 | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/status` |
| `dependencies` | dependencies | 必須 | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/dependencies` |
| `processes` | array<generationProcess> | 必須 | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "processes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/generationProcess"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "processes"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 3.4.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="core-presentation"></a>
## presentation

`#/$defs/presentation`

Standard optional Core object under root version 3.4.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

親内必須: `status`, `dependencies`, `roleDefinitions`, `sectionRoleAssignments`, `appearance`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `status` | enum ["current", "stale", "unverified"] | 必須 | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/status` |
| `dependencies` | dependencies | 必須 | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/dependencies` |
| `roleDefinitions` | array<roleDefinition> | 必須 | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/roleDefinitions` |
| `sectionRoleAssignments` | object | 必須 | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/sectionRoleAssignments` |
| `appearance` | object | 必須 | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/appearance` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "roleDefinitions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/roleDefinition"
      }
    },
    "sectionRoleAssignments": {
      "type": "object",
      "propertyNames": {
        "$ref": "#/$defs/id"
      },
      "additionalProperties": {
        "$ref": "#/$defs/id"
      }
    },
    "appearance": {
      "type": "object",
      "properties": {
        "roleColors": {
          "$ref": "#/$defs/roleColorMap"
        },
        "customRoleColors": {
          "$ref": "#/$defs/customRoleColorMap"
        },
        "objectColors": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/objectColor"
          }
        }
      },
      "required": [
        "roleColors",
        "customRoleColors",
        "objectColors"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "status",
    "dependencies",
    "roleDefinitions",
    "sectionRoleAssignments",
    "appearance"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 3.4.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="core-phraselibrary"></a>
## phraseLibrary

`#/$defs/phraseLibrary`

Standard optional Core object under root version 3.4.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

親内必須: `status`, `dependencies`, `templates`, `instances`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `status` | enum ["current", "stale", "unverified"] | 必須 | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/status` |
| `dependencies` | dependencies | 必須 | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/dependencies` |
| `templates` | array<phraseTemplate> | 必須 | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates` |
| `instances` | array<phraseInstance> | 必須 | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "templates": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/phraseTemplate"
      }
    },
    "instances": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/phraseInstance"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "templates",
    "instances"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 3.4.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="core-clipchoices"></a>
## clipChoices

`#/$defs/clipChoices`

Standard optional Core object under root version 3.4.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

親内必須: `status`, `dependencies`, `groups`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `status` | enum ["current", "stale", "unverified"] | 必須 | — | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/status` |
| `dependencies` | dependencies | 必須 | — | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/dependencies` |
| `groups` | array<clipChoiceGroup> | 必須 | — | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "groups": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/clipChoiceGroup"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "groups"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 3.4.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="core-localization"></a>
## localization

`#/$defs/localization`

Standard optional Core object under root version 3.4.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

親内必須: `status`, `dependencies`, `entries`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `status` | enum ["current", "stale", "unverified"] | 必須 | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/status` |
| `dependencies` | dependencies | 必須 | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/dependencies` |
| `entries` | array<localizationEntry> | 必須 | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "entries": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/localizationEntry"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "entries"
  ],
  "description": "Standard optional Core object under root version 3.4.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="core-corephrasesourcenote"></a>
## corePhraseSourceNote

`#/$defs/corePhraseSourceNote`

Template-local note ID; not a performed event. Velocity is optional. Only concrete tracks are performed.

親内必須: `id`, `start`, `duration`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/notes/0/id` |
| `start` | signed | 必須 | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/notes/0/start` |
| `duration` | positive | 必須 | Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample. | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/notes/0/duration` |
| `pitch` | pitch | 任意／条件付き | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/notes/0/pitch` |
| `soundSlotId` | id | 任意／条件付き | Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre. | [samples/21_native_drum_template_velocity.ostf](../samples/21_native_drum_template_velocity.ostf) `/phraseLibrary/templates/0/notes/0/soundSlotId` |
| `velocity` | integer | 任意／条件付き | minimum=1; maximum=127; Optional template note-on velocity, 1–127. Applied only by an explicit materialization/update according to instance.velocityMode; never a performed event by itself. | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/notes/0/velocity` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive",
      "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
    },
    "pitch": {
      "$ref": "#/$defs/pitch"
    },
    "soundSlotId": {
      "$ref": "#/$defs/id",
      "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
    },
    "velocity": {
      "type": "integer",
      "minimum": 1,
      "maximum": 127,
      "description": "Optional template note-on velocity, 1–127. Applied only by an explicit materialization/update according to instance.velocityMode; never a performed event by itself."
    }
  },
  "required": [
    "id",
    "start",
    "duration"
  ],
  "additionalProperties": false,
  "oneOf": [
    {
      "required": [
        "pitch"
      ],
      "not": {
        "required": [
          "soundSlotId"
        ]
      }
    },
    {
      "required": [
        "soundSlotId"
      ],
      "not": {
        "required": [
          "pitch"
        ]
      }
    }
  ],
  "description": "Template-local note ID; not a performed event. Velocity is optional. Only concrete tracks are performed."
}
```

<a id="core-provenancesource"></a>
## provenanceSource

`#/$defs/provenanceSource`

Historical source; hashes refer to exact source bytes, not the current document. No automatic retrieval.

親内必須: —

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `format` | string | 任意／条件付き | minLength=1 | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/format` |
| `version` | string | 任意／条件付き | minLength=1 | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/version` |
| `sha256` | sha256 | 任意／条件付き | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/sha256` |
| `uri` | string | 任意／条件付き | minLength=1 | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/uri` |
| `documentId` | opaqueDocumentId | 任意／条件付き | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/documentId` |
| `revisionId` | opaqueDocumentId | 任意／条件付き | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/revisionId` |
| `resourceId` | id | 任意／条件付き | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/resourceId` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "format": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    },
    "uri": {
      "type": "string",
      "minLength": 1
    },
    "documentId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "revisionId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "resourceId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Historical source; hashes refer to exact source bytes, not the current document. No automatic retrieval.",
  "minProperties": 1,
  "dependentRequired": {
    "revisionId": [
      "documentId"
    ]
  }
}
```

<a id="core-provenancerecord"></a>
## provenanceRecord

`#/$defs/provenanceRecord`

親内必須: `id`, `action`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | id | 必須 | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/id` |
| `action` | enum ["create", "import", "conversion", "edit", "transpose", "merge", "generation", "other"] | 必須 | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/action` |
| `description` | string | 任意／条件付き | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/description` |
| `tool` | software | 任意／条件付き | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/tool` |
| `sources` | array<provenanceSource> | 任意／条件付き | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources` |
| `semitones` | integer | 任意／条件付き | minimum=-127; maximum=127 | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/semitones` |
| `beforeKey` | key | 任意／条件付き | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/beforeKey` |
| `afterKey` | key | 任意／条件付き | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/afterKey` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "action": {
      "enum": [
        "create",
        "import",
        "conversion",
        "edit",
        "transpose",
        "merge",
        "generation",
        "other"
      ]
    },
    "description": {
      "type": "string"
    },
    "tool": {
      "$ref": "#/$defs/software"
    },
    "sources": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/provenanceSource"
      }
    },
    "semitones": {
      "type": "integer",
      "minimum": -127,
      "maximum": 127
    },
    "beforeKey": {
      "$ref": "#/$defs/key"
    },
    "afterKey": {
      "$ref": "#/$defs/key"
    }
  },
  "required": [
    "id",
    "action"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "not": {
          "properties": {
            "action": {
              "const": "transpose"
            }
          },
          "required": [
            "action"
          ]
        }
      },
      "then": {
        "not": {
          "required": [
            "semitones"
          ]
        }
      }
    }
  ]
}
```

<a id="core-provenance"></a>
## provenance

`#/$defs/provenance`

Non-executable historical assertions; not composer credits and not a substitute for current metadata. Does not prove authorship or operation correctness.

親内必須: `records`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `records` | array<provenanceRecord> | 必須 | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records` |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "records": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/provenanceRecord"
      }
    }
  },
  "required": [
    "records"
  ],
  "additionalProperties": false,
  "description": "Non-executable historical assertions; not composer credits and not a substitute for current metadata. Does not prove authorship or operation correctness."
}
```

<a id="frozen-legacy"></a>
## 凍結した旧拡張定義（互換保持専用）

次の65定義は原版の構造を維持するための閉じた領域です。現在の296宣言の実例集計には含めません。すべての旧定義が新ルートから到達可能という意味ではありません。3.4のルートに旧songや旧trackを置いてよいという意味でもありません。拡張の版が不明なら既知版と決めつけません。

[Compatibility example](../samples/49_frozen_legacy_profiles_compatibility_only.ostf)

<a id="legacy-id"></a>
## legacy33 / id

`#/$defs/legacy33/$defs/id`

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "string",
  "pattern": "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```

<a id="legacy-nonnegative"></a>
## legacy33 / nonnegative

`#/$defs/legacy33/$defs/nonnegative`

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "integer",
  "minimum": 0,
  "maximum": 9007199254740991
}
```

<a id="legacy-positive"></a>
## legacy33 / positive

`#/$defs/legacy33/$defs/positive`

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "integer",
  "minimum": 1,
  "maximum": 9007199254740991
}
```

<a id="legacy-signed"></a>
## legacy33 / signed

`#/$defs/legacy33/$defs/signed`

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "integer",
  "minimum": -9007199254740991,
  "maximum": 9007199254740991
}
```

<a id="legacy-pitch"></a>
## legacy33 / pitch

`#/$defs/legacy33/$defs/pitch`

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "integer",
  "minimum": 0,
  "maximum": 127
}
```

<a id="legacy-ref"></a>
## legacy33 / ref

`#/$defs/legacy33/$defs/ref`

親内必須: `type`, `id`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `type` | enum ["section", "track", "clip", "note", "chord", "scale", "soundSlot", "drumKit", "lyricDocument", "lyricPhrase", "lyricUnit", "lyricAlignment", "resource", "genre"] | 必須 | — | — |
| `id` | legacy33/$defs/id | 必須 | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "type": {
      "enum": [
        "section",
        "track",
        "clip",
        "note",
        "chord",
        "scale",
        "soundSlot",
        "drumKit",
        "lyricDocument",
        "lyricPhrase",
        "lyricUnit",
        "lyricAlignment",
        "resource",
        "genre"
      ]
    },
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    }
  },
  "required": [
    "type",
    "id"
  ],
  "additionalProperties": false
}
```

<a id="legacy-range"></a>
## legacy33 / range

`#/$defs/legacy33/$defs/range`

親内必須: `start`, `duration`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `start` | legacy33/$defs/nonnegative | 必須 | — | — |
| `duration` | legacy33/$defs/positive | 必須 | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    }
  },
  "required": [
    "start",
    "duration"
  ],
  "additionalProperties": false
}
```

<a id="legacy-spelledpitchclass"></a>
## legacy33 / spelledPitchClass

`#/$defs/legacy33/$defs/spelledPitchClass`

親内必須: `step`, `alter`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `step` | enum ["A", "B", "C", "D", "E", "F", "G"] | 必須 | — | — |
| `alter` | integer | 必須 | minimum=-2; maximum=2 | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "step": {
      "enum": [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G"
      ]
    },
    "alter": {
      "type": "integer",
      "minimum": -2,
      "maximum": 2
    }
  },
  "required": [
    "step",
    "alter"
  ],
  "additionalProperties": false
}
```

<a id="legacy-song"></a>
## legacy33 / song

`#/$defs/legacy33/$defs/song`

親内必須: `title`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `title` | string | 必須 | — | — |
| `primaryMelodyTrackId` | legacy33/$defs/id | 任意／条件付き | — | — |
| `localizedTitles` | legacy33/$defs/localizedNames | 任意／条件付き | Optional localized song-title alternatives. song.title is the stable fallback. | — |
| `subtitle` | string | 任意／条件付き | Optional original-language subtitle. | — |
| `description` | string | 任意／条件付き | Optional original-language description, including Unicode and line breaks. | — |
| `alternateTitles` | array<legacy33/$defs/alternateTitle> | 任意／条件付き | Additional stable-ID source-language titles. | — |
| `credits` | array<legacy33/$defs/credit> | 任意／条件付き | Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted. | — |
| `genres` | array<legacy33/$defs/genre> | 任意／条件付き | Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified. | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    },
    "primaryMelodyTrackId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "localizedTitles": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames",
      "description": "Optional localized song-title alternatives. song.title is the stable fallback."
    },
    "subtitle": {
      "type": "string",
      "description": "Optional original-language subtitle."
    },
    "description": {
      "type": "string",
      "description": "Optional original-language description, including Unicode and line breaks."
    },
    "alternateTitles": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/alternateTitle"
      },
      "description": "Additional stable-ID source-language titles."
    },
    "credits": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/credit"
      },
      "description": "Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted."
    },
    "genres": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/genre"
      },
      "description": "Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified."
    }
  },
  "required": [
    "title"
  ],
  "additionalProperties": false
}
```

<a id="legacy-section"></a>
## legacy33 / section

`#/$defs/legacy33/$defs/section`

親内必須: `id`, `name`, `start`, `duration`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `name` | string | 必須 | minLength=1 | — |
| `start` | legacy33/$defs/nonnegative | 必須 | — | — |
| `duration` | legacy33/$defs/positive | 必須 | — | — |
| `role` | string | 任意／条件付き | — | — |
| `localizedNames` | legacy33/$defs/localizedNames | 任意／条件付き | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "role": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "id",
    "name",
    "start",
    "duration"
  ],
  "additionalProperties": false
}
```

<a id="legacy-tempo"></a>
## legacy33 / tempo

`#/$defs/legacy33/$defs/tempo`

親内必須: `at`, `bpm`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `at` | legacy33/$defs/nonnegative | 必須 | — | — |
| `bpm` | number | 必須 | maximum=1000; exclusiveMinimum=0 | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "bpm": {
      "type": "number",
      "exclusiveMinimum": 0,
      "maximum": 1000
    }
  },
  "required": [
    "at",
    "bpm"
  ],
  "additionalProperties": false
}
```

<a id="legacy-meter"></a>
## legacy33 / meter

`#/$defs/legacy33/$defs/meter`

親内必須: `at`, `numerator`, `denominator`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `at` | legacy33/$defs/nonnegative | 必須 | — | — |
| `numerator` | integer | 必須 | minimum=1; maximum=64 | — |
| `denominator` | enum [1, 2, 4, 8, 16, 32, 64] | 必須 | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "numerator": {
      "type": "integer",
      "minimum": 1,
      "maximum": 64
    },
    "denominator": {
      "enum": [
        1,
        2,
        4,
        8,
        16,
        32,
        64
      ],
      "type": "integer"
    }
  },
  "required": [
    "at",
    "numerator",
    "denominator"
  ],
  "additionalProperties": false
}
```

<a id="legacy-timeline"></a>
## legacy33 / timeline

`#/$defs/legacy33/$defs/timeline`

親内必須: `sections`, `tempoChanges`, `meterChanges`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `sections` | array<legacy33/$defs/section> | 必須 | — | — |
| `tempoChanges` | array<legacy33/$defs/tempo> | 必須 | minItems=1 | — |
| `meterChanges` | array<legacy33/$defs/meter> | 必須 | minItems=1 | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "sections": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/section"
      }
    },
    "tempoChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/tempo"
      },
      "minItems": 1
    },
    "meterChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/meter"
      },
      "minItems": 1
    }
  },
  "required": [
    "sections",
    "tempoChanges",
    "meterChanges"
  ],
  "additionalProperties": false
}
```

<a id="legacy-chord"></a>
## legacy33 / chord

`#/$defs/legacy33/$defs/chord`

親内必須: `id`, `start`, `duration`, `label`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `start` | legacy33/$defs/nonnegative | 必須 | — | — |
| `duration` | legacy33/$defs/positive | 必須 | — | — |
| `label` | string | 必須 | minLength=1 | — |
| `root` | legacy33/$defs/spelledPitchClass | 任意／条件付き | — | — |
| `intervals` | array<integer> | 任意／条件付き | minItems=1; maxItems=36; uniqueItems=true | — |
| `bass` | legacy33/$defs/spelledPitchClass | 任意／条件付き | — | — |
| `voicing` | legacy33/$defs/voicing | 任意／条件付き | Optional pitch snapshot (not an arrangement note sequence). No automatic playback. | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "label": {
      "type": "string",
      "minLength": 1
    },
    "root": {
      "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 35
      },
      "minItems": 1,
      "maxItems": 36,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "bass": {
      "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
    },
    "voicing": {
      "$ref": "#/$defs/legacy33/$defs/voicing",
      "description": "Optional pitch snapshot (not an arrangement note sequence). No automatic playback."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "label"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "root": [
      "intervals"
    ],
    "intervals": [
      "root"
    ]
  }
}
```

<a id="legacy-scale"></a>
## legacy33 / scale

`#/$defs/legacy33/$defs/scale`

親内必須: `id`, `start`, `duration`, `tonic`, `intervals`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `start` | legacy33/$defs/nonnegative | 必須 | — | — |
| `duration` | legacy33/$defs/positive | 必須 | — | — |
| `label` | string | 任意／条件付き | — | — |
| `tonic` | legacy33/$defs/spelledPitchClass | 必須 | — | — |
| `intervals` | array<integer> | 必須 | minItems=1; maxItems=12; uniqueItems=true | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "tonic": {
      "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 11
      },
      "minItems": 1,
      "maxItems": 12,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "tonic",
    "intervals"
  ],
  "additionalProperties": false
}
```

<a id="legacy-harmony"></a>
## legacy33 / harmony

`#/$defs/legacy33/$defs/harmony`

親内必須: `chords`, `scales`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `chords` | array<legacy33/$defs/chord> | 必須 | — | — |
| `scales` | array<legacy33/$defs/scale> | 必須 | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "chords": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/chord"
      }
    },
    "scales": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/scale"
      }
    }
  },
  "required": [
    "chords",
    "scales"
  ],
  "additionalProperties": false
}
```

<a id="legacy-instrument"></a>
## legacy33 / instrument

`#/$defs/legacy33/$defs/instrument`

親内必須: `name`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `name` | string | 必須 | — | — |
| `family` | string | 任意／条件付き | — | — |
| `localizedNames` | legacy33/$defs/localizedNames | 任意／条件付き | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "family": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```

<a id="legacy-note"></a>
## legacy33 / note

`#/$defs/legacy33/$defs/note`

Concrete Core note; optional velocity is a note-on attribute. Phrase templates use a separate version-frozen sourceNote shape.

親内必須: `id`, `start`, `duration`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `start` | legacy33/$defs/signed | 必須 | — | — |
| `duration` | legacy33/$defs/positive | 必須 | Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample. | — |
| `pitch` | legacy33/$defs/pitch | 任意／条件付き | — | — |
| `soundSlotId` | legacy33/$defs/id | 任意／条件付き | Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre. | — |
| `velocity` | integer | 任意／条件付き | minimum=1; maximum=127; Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving. | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive",
      "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
    },
    "pitch": {
      "$ref": "#/$defs/legacy33/$defs/pitch"
    },
    "soundSlotId": {
      "$ref": "#/$defs/legacy33/$defs/id",
      "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
    },
    "velocity": {
      "type": "integer",
      "minimum": 1,
      "maximum": 127,
      "description": "Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving."
    }
  },
  "required": [
    "id",
    "start",
    "duration"
  ],
  "additionalProperties": false,
  "oneOf": [
    {
      "required": [
        "pitch"
      ],
      "not": {
        "required": [
          "soundSlotId"
        ]
      }
    },
    {
      "required": [
        "soundSlotId"
      ],
      "not": {
        "required": [
          "pitch"
        ]
      }
    }
  ],
  "description": "Concrete Core note; optional velocity is a note-on attribute. Phrase templates use a separate version-frozen sourceNote shape."
}
```

<a id="legacy-clip"></a>
## legacy33 / clip

`#/$defs/legacy33/$defs/clip`

親内必須: `id`, `start`, `duration`, `notes`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `name` | string | 任意／条件付き | — | — |
| `start` | legacy33/$defs/nonnegative | 必須 | — | — |
| `duration` | legacy33/$defs/positive | 必須 | — | — |
| `enabled` | boolean | 任意／条件付き | default=true | — |
| `notes` | array<legacy33/$defs/note> | 必須 | — | — |
| `localizedNames` | legacy33/$defs/localizedNames | 任意／条件付き | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "enabled": {
      "type": "boolean",
      "default": true
    },
    "notes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/note"
      }
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "notes"
  ],
  "additionalProperties": false
}
```

<a id="legacy-track"></a>
## legacy33 / track

`#/$defs/legacy33/$defs/track`

親内必須: `id`, `name`, `clips`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `name` | string | 必須 | — | — |
| `role` | string | 任意／条件付き | — | — |
| `instrument` | legacy33/$defs/instrument | 任意／条件付き | — | — |
| `enabled` | boolean | 任意／条件付き | default=true | — |
| `clips` | array<legacy33/$defs/clip> | 必須 | — | — |
| `trackType` | enum ["melodic", "drum", "mixed"] | 任意／条件付き | Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class. | — |
| `preferredView` | enum ["auto", "pianoRoll", "drumGrid"] | 任意／条件付き | default="auto"; Non-binding presentation preference. Does not change note meaning. | — |
| `soundSource` | legacy33/$defs/soundSource | 任意／条件付き | Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee. | — |
| `localizedNames` | legacy33/$defs/localizedNames | 任意／条件付き | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | — |
| `drumKitId` | legacy33/$defs/id | 任意／条件付き | Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit. | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "role": {
      "type": "string"
    },
    "instrument": {
      "$ref": "#/$defs/legacy33/$defs/instrument"
    },
    "enabled": {
      "type": "boolean",
      "default": true
    },
    "clips": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/clip"
      }
    },
    "trackType": {
      "enum": [
        "melodic",
        "drum",
        "mixed"
      ],
      "description": "Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class."
    },
    "preferredView": {
      "enum": [
        "auto",
        "pianoRoll",
        "drumGrid"
      ],
      "default": "auto",
      "description": "Non-binding presentation preference. Does not change note meaning."
    },
    "soundSource": {
      "$ref": "#/$defs/legacy33/$defs/soundSource",
      "description": "Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee."
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    },
    "drumKitId": {
      "$ref": "#/$defs/legacy33/$defs/id",
      "description": "Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit."
    }
  },
  "required": [
    "id",
    "name",
    "clips"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "trackType": {
            "const": "melodic"
          }
        },
        "required": [
          "trackType"
        ]
      },
      "then": {
        "not": {
          "required": [
            "drumKitId"
          ]
        }
      }
    }
  ]
}
```

<a id="legacy-soundslot"></a>
## legacy33 / soundSlot

`#/$defs/legacy33/$defs/soundSlot`

Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded.

親内必須: `id`, `name`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `name` | string | 必須 | — | — |
| `role` | string | 任意／条件付き | Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier. | — |
| `midiNote` | legacy33/$defs/pitch | 任意／条件付き | Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity. | — |
| `midiMapping` | legacy33/$defs/midiMapping | 任意／条件付き | Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity. | — |
| `localizedNames` | legacy33/$defs/localizedNames | 任意／条件付き | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "role": {
      "type": "string",
      "description": "Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier."
    },
    "midiNote": {
      "$ref": "#/$defs/legacy33/$defs/pitch",
      "description": "Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity."
    },
    "midiMapping": {
      "$ref": "#/$defs/legacy33/$defs/midiMapping",
      "description": "Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity."
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false,
  "description": "Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded."
}
```

<a id="legacy-lyricdocument"></a>
## legacy33 / lyricDocument

`#/$defs/legacy33/$defs/lyricDocument`

親内必須: `id`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `title` | string | 任意／条件付き | — | — |
| `language` | string | 任意／条件付き | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "title": {
      "type": "string"
    },
    "language": {
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```

<a id="legacy-lyricphrase"></a>
## legacy33 / lyricPhrase

`#/$defs/legacy33/$defs/lyricPhrase`

親内必須: `id`, `documentId`, `text`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `documentId` | legacy33/$defs/id | 必須 | — | — |
| `text` | string | 必須 | — | — |
| `pronunciation` | string | 任意／条件付き | — | — |
| `start` | legacy33/$defs/nonnegative | 任意／条件付き | — | — |
| `duration` | legacy33/$defs/positive | 任意／条件付き | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "documentId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "text": {
      "type": "string"
    },
    "pronunciation": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    }
  },
  "required": [
    "id",
    "documentId",
    "text"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "start": [
      "duration"
    ],
    "duration": [
      "start"
    ]
  }
}
```

<a id="legacy-lyricunit"></a>
## legacy33 / lyricUnit

`#/$defs/legacy33/$defs/lyricUnit`

親内必須: `id`, `phraseId`, `text`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `phraseId` | legacy33/$defs/id | 必須 | — | — |
| `text` | string | 必須 | — | — |
| `pronunciation` | string | 任意／条件付き | — | — |
| `start` | legacy33/$defs/nonnegative | 任意／条件付き | — | — |
| `duration` | legacy33/$defs/positive | 任意／条件付き | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "phraseId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "text": {
      "type": "string"
    },
    "pronunciation": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    }
  },
  "required": [
    "id",
    "phraseId",
    "text"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "start": [
      "duration"
    ],
    "duration": [
      "start"
    ]
  }
}
```

<a id="legacy-lyricalignment"></a>
## legacy33 / lyricAlignment

`#/$defs/legacy33/$defs/lyricAlignment`

親内必須: `id`, `unitIds`, `noteIds`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `unitIds` | array<legacy33/$defs/id> | 必須 | minItems=1; uniqueItems=true | — |
| `noteIds` | array<legacy33/$defs/id> | 必須 | minItems=1; uniqueItems=true | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "unitIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/id"
      },
      "uniqueItems": true,
      "minItems": 1
    },
    "noteIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/id"
      },
      "uniqueItems": true,
      "minItems": 1
    }
  },
  "required": [
    "id",
    "unitIds",
    "noteIds"
  ],
  "additionalProperties": false
}
```

<a id="legacy-lyrics"></a>
## legacy33 / lyrics

`#/$defs/legacy33/$defs/lyrics`

親内必須: `documents`, `phrases`, `units`, `alignments`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `documents` | array<legacy33/$defs/lyricDocument> | 必須 | — | — |
| `phrases` | array<legacy33/$defs/lyricPhrase> | 必須 | — | — |
| `units` | array<legacy33/$defs/lyricUnit> | 必須 | — | — |
| `alignments` | array<legacy33/$defs/lyricAlignment> | 必須 | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "documents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/lyricDocument"
      }
    },
    "phrases": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/lyricPhrase"
      }
    },
    "units": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/lyricUnit"
      }
    },
    "alignments": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/lyricAlignment"
      }
    }
  },
  "required": [
    "documents",
    "phrases",
    "units",
    "alignments"
  ],
  "additionalProperties": false
}
```

<a id="legacy-sha256"></a>
## legacy33 / sha256

`#/$defs/legacy33/$defs/sha256`

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "string",
  "pattern": "^[0-9a-f]{64}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```

<a id="legacy-resource"></a>
## legacy33 / resource

`#/$defs/legacy33/$defs/resource`

親内必須: `id`, `kind`, `uri`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `kind` | enum ["audio", "midi", "text", "other"] | 必須 | — | — |
| `uri` | string | 必須 | minLength=1 | — |
| `name` | string | 任意／条件付き | — | — |
| `sha256` | legacy33/$defs/sha256 | 任意／条件付き | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "kind": {
      "enum": [
        "audio",
        "midi",
        "text",
        "other"
      ]
    },
    "uri": {
      "type": "string",
      "minLength": 1
    },
    "name": {
      "type": "string"
    },
    "sha256": {
      "$ref": "#/$defs/legacy33/$defs/sha256"
    }
  },
  "required": [
    "id",
    "kind",
    "uri"
  ],
  "additionalProperties": false
}
```

<a id="legacy-dependencies"></a>
## legacy33 / dependencies

`#/$defs/legacy33/$defs/dependencies`

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "scope": {
          "enum": [
            "document",
            "none"
          ]
        }
      },
      "required": [
        "scope"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "scope": {
          "const": "objects"
        },
        "refs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/ref"
          },
          "minItems": 1,
          "uniqueItems": true
        }
      },
      "required": [
        "scope",
        "refs"
      ],
      "additionalProperties": false
    }
  ]
}
```

<a id="legacy-extension"></a>
## legacy33 / extension

`#/$defs/legacy33/$defs/extension`

親内必須: `version`, `status`, `dependencies`, `data`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `version` | string | 必須 | minLength=1 | — |
| `status` | enum ["current", "stale", "unverified"] | 必須 | — | — |
| `dependencies` | legacy33/$defs/dependencies | 必須 | — | — |
| `data` | schema | 必須 | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "version": {
      "type": "string",
      "minLength": 1
    },
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/legacy33/$defs/dependencies"
    },
    "data": {}
  },
  "required": [
    "version",
    "status",
    "dependencies",
    "data"
  ],
  "additionalProperties": false
}
```

<a id="legacy-relativeassignment"></a>
## legacy33 / relativeAssignment

`#/$defs/legacy33/$defs/relativeAssignment`

親内必須: `noteId`, `basis`, `contextId`, `anchorPitch`, `index`, `chromaticOffset`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `noteId` | legacy33/$defs/id | 必須 | — | — |
| `basis` | enum ["chordTone", "scaleDegree"] | 必須 | — | — |
| `contextId` | legacy33/$defs/id | 必須 | — | — |
| `anchorPitch` | legacy33/$defs/pitch | 必須 | — | — |
| `index` | integer | 必須 | minimum=1; maximum=36 | — |
| `chromaticOffset` | integer | 必須 | minimum=-24; maximum=24 | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "noteId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "basis": {
      "enum": [
        "chordTone",
        "scaleDegree"
      ]
    },
    "contextId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "anchorPitch": {
      "$ref": "#/$defs/legacy33/$defs/pitch"
    },
    "index": {
      "type": "integer",
      "minimum": 1,
      "maximum": 36
    },
    "chromaticOffset": {
      "type": "integer",
      "minimum": -24,
      "maximum": 24
    }
  },
  "required": [
    "noteId",
    "basis",
    "contextId",
    "anchorPitch",
    "index",
    "chromaticOffset"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "basis": {
            "const": "scaleDegree"
          }
        },
        "required": [
          "basis"
        ]
      },
      "then": {
        "properties": {
          "index": {
            "maximum": 12
          }
        }
      }
    }
  ]
}
```

<a id="legacy-relativedata"></a>
## legacy33 / relativeData

`#/$defs/legacy33/$defs/relativeData`

親内必須: `assignments`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `assignments` | array<legacy33/$defs/relativeAssignment> | 必須 | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "assignments": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/relativeAssignment"
      }
    }
  },
  "required": [
    "assignments"
  ],
  "additionalProperties": false
}
```

<a id="legacy-generator"></a>
## legacy33 / generator

`#/$defs/legacy33/$defs/generator`

親内必須: `id`, `version`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | string | 必須 | minLength=1 | — |
| `version` | string | 必須 | minLength=1 | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "id",
    "version"
  ],
  "additionalProperties": false
}
```

<a id="legacy-generationinput"></a>
## legacy33 / generationInput

`#/$defs/legacy33/$defs/generationInput`

親内必須: `role`, `ref`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `role` | string | 必須 | minLength=1 | — |
| `ref` | legacy33/$defs/ref | 必須 | — | — |
| `readRange` | legacy33/$defs/range | 任意／条件付き | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "role": {
      "type": "string",
      "minLength": 1
    },
    "ref": {
      "$ref": "#/$defs/legacy33/$defs/ref"
    },
    "readRange": {
      "$ref": "#/$defs/legacy33/$defs/range"
    }
  },
  "required": [
    "role",
    "ref"
  ],
  "additionalProperties": false
}
```

<a id="legacy-generationprocess"></a>
## legacy33 / generationProcess

`#/$defs/legacy33/$defs/generationProcess`

親内必須: `id`, `generator`, `inputs`, `outputs`, `protectedNoteIds`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `generator` | legacy33/$defs/generator | 必須 | — | — |
| `inputs` | array<legacy33/$defs/generationInput> | 必須 | — | — |
| `outputs` | array<legacy33/$defs/ref> | 必須 | minItems=1 | — |
| `targetRange` | legacy33/$defs/range | 任意／条件付き | — | — |
| `protectedNoteIds` | array<legacy33/$defs/id> | 必須 | uniqueItems=true | — |
| `vendorExtension` | string | 任意／条件付き | minLength=1 | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "generator": {
      "$ref": "#/$defs/legacy33/$defs/generator"
    },
    "inputs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/generationInput"
      }
    },
    "outputs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/ref"
      },
      "minItems": 1
    },
    "targetRange": {
      "$ref": "#/$defs/legacy33/$defs/range"
    },
    "protectedNoteIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/id"
      },
      "uniqueItems": true
    },
    "vendorExtension": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "id",
    "generator",
    "inputs",
    "outputs",
    "protectedNoteIds"
  ],
  "additionalProperties": false
}
```

<a id="legacy-generationdata"></a>
## legacy33 / generationData

`#/$defs/legacy33/$defs/generationData`

親内必須: `processes`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `processes` | array<legacy33/$defs/generationProcess> | 必須 | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "processes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/generationProcess"
      }
    }
  },
  "required": [
    "processes"
  ],
  "additionalProperties": false
}
```

<a id="legacy-color"></a>
## legacy33 / color

`#/$defs/legacy33/$defs/color`

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "string",
  "pattern": "^#[0-9A-Fa-f]{6}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```

<a id="legacy-roledefinition"></a>
## legacy33 / roleDefinition

`#/$defs/legacy33/$defs/roleDefinition`

親内必須: `id`, `name`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `name` | string | 必須 | minLength=1 | — |
| `baseRole` | string | 任意／条件付き | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "baseRole": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```

<a id="legacy-rolecolormap"></a>
## legacy33 / roleColorMap

`#/$defs/legacy33/$defs/roleColorMap`

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "additionalProperties": {
    "$ref": "#/$defs/legacy33/$defs/color"
  }
}
```

<a id="legacy-customrolecolormap"></a>
## legacy33 / customRoleColorMap

`#/$defs/legacy33/$defs/customRoleColorMap`

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "propertyNames": {
    "$ref": "#/$defs/legacy33/$defs/id"
  },
  "additionalProperties": {
    "$ref": "#/$defs/legacy33/$defs/color"
  }
}
```

<a id="legacy-objectcolor"></a>
## legacy33 / objectColor

`#/$defs/legacy33/$defs/objectColor`

親内必須: `target`, `color`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `target` | legacy33/$defs/ref | 必須 | — | — |
| `color` | legacy33/$defs/color | 必須 | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "target": {
      "$ref": "#/$defs/legacy33/$defs/ref"
    },
    "color": {
      "$ref": "#/$defs/legacy33/$defs/color"
    }
  },
  "required": [
    "target",
    "color"
  ],
  "additionalProperties": false
}
```

<a id="legacy-appearancedata"></a>
## legacy33 / appearanceData

`#/$defs/legacy33/$defs/appearanceData`

親内必須: `roleDefinitions`, `sectionRoleAssignments`, `appearance`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `roleDefinitions` | array<legacy33/$defs/roleDefinition> | 必須 | — | — |
| `sectionRoleAssignments` | object | 必須 | — | — |
| `appearance` | object | 必須 | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "roleDefinitions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/roleDefinition"
      }
    },
    "sectionRoleAssignments": {
      "type": "object",
      "propertyNames": {
        "$ref": "#/$defs/legacy33/$defs/id"
      },
      "additionalProperties": {
        "$ref": "#/$defs/legacy33/$defs/id"
      }
    },
    "appearance": {
      "type": "object",
      "properties": {
        "roleColors": {
          "$ref": "#/$defs/legacy33/$defs/roleColorMap"
        },
        "customRoleColors": {
          "$ref": "#/$defs/legacy33/$defs/customRoleColorMap"
        },
        "objectColors": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/objectColor"
          }
        }
      },
      "required": [
        "roleColors",
        "customRoleColors",
        "objectColors"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "roleDefinitions",
    "sectionRoleAssignments",
    "appearance"
  ],
  "additionalProperties": false
}
```

<a id="legacy-legacydata"></a>
## legacy33 / legacyData

`#/$defs/legacy33/$defs/legacyData`

親内必須: `sourceVersion`, `sourceSha256`, `sourceText`, `conversionReport`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `sourceVersion` | const "2.3.0" | 必須 | — | — |
| `sourceSha256` | legacy33/$defs/sha256 | 必須 | — | — |
| `sourceText` | string | 必須 | minLength=1 | — |
| `conversionReport` | object | 必須 | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "sourceVersion": {
      "const": "2.3.0"
    },
    "sourceSha256": {
      "$ref": "#/$defs/legacy33/$defs/sha256"
    },
    "sourceText": {
      "type": "string",
      "minLength": 1
    },
    "conversionReport": {
      "type": "object"
    }
  },
  "required": [
    "sourceVersion",
    "sourceSha256",
    "sourceText",
    "conversionReport"
  ],
  "additionalProperties": false
}
```

<a id="legacy-extensions"></a>
## legacy33 / extensions

`#/$defs/legacy33/$defs/extensions`

親内必須: —

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `org.ostf.relative-phrase.v1` | schema | 任意／条件付き | — | — |
| `org.ostf.generation-context.v1` | schema | 任意／条件付き | — | — |
| `org.ostf.appearance.v1` | schema | 任意／条件付き | — | — |
| `org.ostf.legacy-import.v1` | schema | 任意／条件付き | — | — |
| `org.ostf.phrase-library.v1` | schema | 任意／条件付き | — | — |
| `org.ostf.clip-choices.v1` | schema | 任意／条件付き | — | — |
| `org.ostf.localization.v1` | schema | 任意／条件付き | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "propertyNames": {
    "pattern": "^[a-z][a-z0-9-]*(?:\\.[a-z][a-z0-9-]*){2,}$",
    "not": {
      "pattern": "[\\r\\n\\u2028\\u2029]"
    }
  },
  "properties": {
    "org.ostf.relative-phrase.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0-draft.1"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/relativeData"
              }
            }
          }
        }
      ]
    },
    "org.ostf.generation-context.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0-draft.1"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/generationData"
              }
            }
          }
        }
      ]
    },
    "org.ostf.appearance.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0-draft.1"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/appearanceData"
              }
            }
          }
        }
      ]
    },
    "org.ostf.legacy-import.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0-draft.1"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/legacyData"
              }
            }
          }
        }
      ]
    },
    "org.ostf.phrase-library.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0-draft.1"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/phraseLibraryData"
              }
            }
          }
        }
      ]
    },
    "org.ostf.clip-choices.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0-draft.1"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/clipChoicesData"
              }
            }
          }
        }
      ]
    },
    "org.ostf.localization.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/localizationData"
              }
            }
          }
        }
      ]
    }
  },
  "additionalProperties": {
    "$ref": "#/$defs/legacy33/$defs/extension"
  }
}
```

<a id="legacy-phrasetemplate"></a>
## legacy33 / phraseTemplate

`#/$defs/legacy33/$defs/phraseTemplate`

親内必須: `id`, `duration`, `notes`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `duration` | legacy33/$defs/positive | 必須 | — | — |
| `notes` | array<legacy33/$defs/phraseSourceNote> | 必須 | — | — |
| `name` | string | 任意／条件付き | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "notes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/phraseSourceNote"
      }
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "duration",
    "notes"
  ],
  "additionalProperties": false
}
```

<a id="legacy-phrasenotemapping"></a>
## legacy33 / phraseNoteMapping

`#/$defs/legacy33/$defs/phraseNoteMapping`

親内必須: `templateNoteId`, `repeatIndex`, `noteId`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `templateNoteId` | legacy33/$defs/id | 必須 | — | — |
| `repeatIndex` | legacy33/$defs/nonnegative | 必須 | — | — |
| `noteId` | legacy33/$defs/id | 必須 | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "templateNoteId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "repeatIndex": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "noteId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    }
  },
  "required": [
    "templateNoteId",
    "repeatIndex",
    "noteId"
  ],
  "additionalProperties": false
}
```

<a id="legacy-phraseinstance"></a>
## legacy33 / phraseInstance

`#/$defs/legacy33/$defs/phraseInstance`

親内必須: `id`, `templateId`, `clipId`, `repeatCount`, `transpose`, `noteMap`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `templateId` | legacy33/$defs/id | 必須 | — | — |
| `clipId` | legacy33/$defs/id | 必須 | — | — |
| `repeatCount` | legacy33/$defs/positive | 必須 | — | — |
| `transpose` | integer | 必須 | minimum=-127; maximum=127 | — |
| `noteMap` | array<legacy33/$defs/phraseNoteMapping> | 必須 | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "templateId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "clipId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "repeatCount": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "transpose": {
      "type": "integer",
      "minimum": -127,
      "maximum": 127
    },
    "noteMap": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/phraseNoteMapping"
      }
    }
  },
  "required": [
    "id",
    "templateId",
    "clipId",
    "repeatCount",
    "transpose",
    "noteMap"
  ],
  "additionalProperties": false
}
```

<a id="legacy-phraselibrarydata"></a>
## legacy33 / phraseLibraryData

`#/$defs/legacy33/$defs/phraseLibraryData`

親内必須: `templates`, `instances`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `templates` | array<legacy33/$defs/phraseTemplate> | 必須 | — | — |
| `instances` | array<legacy33/$defs/phraseInstance> | 必須 | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "templates": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/phraseTemplate"
      }
    },
    "instances": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/phraseInstance"
      }
    }
  },
  "required": [
    "templates",
    "instances"
  ],
  "additionalProperties": false
}
```

<a id="legacy-clipcandidate"></a>
## legacy33 / clipCandidate

`#/$defs/legacy33/$defs/clipCandidate`

親内必須: `id`, `clipIds`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `clipIds` | array<legacy33/$defs/id> | 必須 | uniqueItems=true | — |
| `name` | string | 任意／条件付き | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "clipIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/id"
      },
      "uniqueItems": true
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "clipIds"
  ],
  "additionalProperties": false
}
```

<a id="legacy-clipchoicegroup"></a>
## legacy33 / clipChoiceGroup

`#/$defs/legacy33/$defs/clipChoiceGroup`

親内必須: `id`, `candidates`, `selectedCandidateId`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `candidates` | array<legacy33/$defs/clipCandidate> | 必須 | minItems=1 | — |
| `selectedCandidateId` | oneOf/anyOf | 必須 | — | — |
| `name` | string | 任意／条件付き | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "candidates": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/clipCandidate"
      },
      "minItems": 1
    },
    "selectedCandidateId": {
      "anyOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        {
          "type": "null"
        }
      ]
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "candidates",
    "selectedCandidateId"
  ],
  "additionalProperties": false
}
```

<a id="legacy-clipchoicesdata"></a>
## legacy33 / clipChoicesData

`#/$defs/legacy33/$defs/clipChoicesData`

親内必須: `groups`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `groups` | array<legacy33/$defs/clipChoiceGroup> | 必須 | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "groups": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/clipChoiceGroup"
      }
    }
  },
  "required": [
    "groups"
  ],
  "additionalProperties": false
}
```

<a id="legacy-midimapping"></a>
## legacy33 / midiMapping

`#/$defs/legacy33/$defs/midiMapping`

親内必須: `standard`, `note`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `standard` | enum ["gm1", "custom"] | 必須 | gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number. | — |
| `note` | legacy33/$defs/pitch | 必須 | MIDI1 note number in 0..127; for gm1 restrict to 35..81. | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "standard": {
      "enum": [
        "gm1",
        "custom"
      ],
      "description": "gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number."
    },
    "note": {
      "$ref": "#/$defs/legacy33/$defs/pitch",
      "description": "MIDI1 note number in 0..127; for gm1 restrict to 35..81."
    }
  },
  "required": [
    "standard",
    "note"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "standard": {
            "const": "gm1"
          }
        },
        "required": [
          "standard"
        ]
      },
      "then": {
        "properties": {
          "note": {
            "type": "integer",
            "minimum": 35,
            "maximum": 81
          }
        }
      }
    }
  ]
}
```

<a id="legacy-soundsource"></a>
## legacy33 / soundSource

`#/$defs/legacy33/$defs/soundSource`

Optional informational rendering class or opaque destination hint. Program Change, Bank Select and plugin presets are not standardized by Core.

親内必須: `kind`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `kind` | enum ["unassigned", "gm1", "externalMidi", "plugin", "hostManaged"] | 必須 | — | — |
| `identifier` | string | 任意／条件付き | minLength=1; Opaque target identifier, e.g. URI, plug-in identifier or port alias, not a loading command. | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "description": "Optional informational rendering class or opaque destination hint. Program Change, Bank Select and plugin presets are not standardized by Core.",
  "properties": {
    "kind": {
      "enum": [
        "unassigned",
        "gm1",
        "externalMidi",
        "plugin",
        "hostManaged"
      ]
    },
    "identifier": {
      "type": "string",
      "minLength": 1,
      "description": "Opaque target identifier, e.g. URI, plug-in identifier or port alias, not a loading command."
    }
  },
  "required": [
    "kind"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "kind": {
            "enum": [
              "gm1",
              "unassigned"
            ]
          }
        },
        "required": [
          "kind"
        ]
      },
      "then": {
        "not": {
          "required": [
            "identifier"
          ]
        }
      }
    }
  ]
}
```

<a id="legacy-localizednames"></a>
## legacy33 / localizedNames

`#/$defs/legacy33/$defs/localizedNames`

Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically.

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "minProperties": 1,
  "propertyNames": {
    "type": "string",
    "pattern": "^(?:[A-Za-z]{2,3}|[A-Za-z]{5,8})(?:-[A-Za-z0-9]{2,8})*$"
  },
  "additionalProperties": {
    "type": "string",
    "minLength": 1
  },
  "description": "Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically."
}
```

<a id="legacy-drumkit"></a>
## legacy33 / drumKit

`#/$defs/legacy33/$defs/drumKit`

Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.

親内必須: `id`, `name`, `soundSlotIds`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `name` | string | 必須 | — | — |
| `localizedNames` | legacy33/$defs/localizedNames | 任意／条件付き | — | — |
| `soundSlotIds` | array<legacy33/$defs/id> | 必須 | uniqueItems=true; Ordered, unique references to global soundSlots; may be empty. | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "description": "Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames"
    },
    "soundSlotIds": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "$ref": "#/$defs/legacy33/$defs/id"
      },
      "description": "Ordered, unique references to global soundSlots; may be empty."
    }
  },
  "required": [
    "id",
    "name",
    "soundSlotIds"
  ],
  "additionalProperties": false
}
```

<a id="legacy-phrasesourcenote"></a>
## legacy33 / phraseSourceNote

`#/$defs/legacy33/$defs/phraseSourceNote`

Version-frozen 1.0.0-draft.1 phrase source note. Does NOT admit velocity; a linked Core instance may independently set velocity.

親内必須: `id`, `start`, `duration`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `start` | legacy33/$defs/signed | 必須 | — | — |
| `duration` | legacy33/$defs/positive | 必須 | — | — |
| `pitch` | legacy33/$defs/pitch | 任意／条件付き | — | — |
| `soundSlotId` | legacy33/$defs/id | 任意／条件付き | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "pitch": {
      "$ref": "#/$defs/legacy33/$defs/pitch"
    },
    "soundSlotId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    }
  },
  "required": [
    "id",
    "start",
    "duration"
  ],
  "additionalProperties": false,
  "oneOf": [
    {
      "required": [
        "pitch"
      ],
      "not": {
        "required": [
          "soundSlotId"
        ]
      }
    },
    {
      "required": [
        "soundSlotId"
      ],
      "not": {
        "required": [
          "pitch"
        ]
      }
    }
  ],
  "description": "Version-frozen 1.0.0-draft.1 phrase source note. Does NOT admit velocity; a linked Core instance may independently set velocity."
}
```

<a id="legacy-voicing"></a>
## legacy33 / voicing

`#/$defs/legacy33/$defs/voicing`

Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.

親内必須: `pitches`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `pitches` | array<legacy33/$defs/pitch> | 必須 | minItems=1; Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed. | — |
| `velocities` | array<oneOf/anyOf> | 任意／条件付き | minItems=1; Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic. | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.",
  "properties": {
    "pitches": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/legacy33/$defs/pitch"
      },
      "description": "Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed."
    },
    "velocities": {
      "type": "array",
      "minItems": 1,
      "items": {
        "anyOf": [
          {
            "type": "integer",
            "minimum": 1,
            "maximum": 127
          },
          {
            "type": "null"
          }
        ]
      },
      "description": "Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic."
    }
  },
  "required": [
    "pitches"
  ]
}
```

<a id="legacy-contributor"></a>
## legacy33 / contributor

`#/$defs/legacy33/$defs/contributor`

One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.

親内必須: `id`, `name`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `name` | string | 必須 | minLength=1 | — |
| `kind` | enum ["person", "organization", "other"] | 任意／条件付き | — | — |
| `localizedNames` | legacy33/$defs/localizedNames | 任意／条件付き | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "kind": {
      "enum": [
        "person",
        "organization",
        "other"
      ]
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames"
    }
  },
  "required": [
    "id",
    "name"
  ]
}
```

<a id="legacy-credit"></a>
## legacy33 / credit

`#/$defs/legacy33/$defs/credit`

Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.

親内必須: `id`, `contributorId`, `role`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `contributorId` | legacy33/$defs/id | 必須 | — | — |
| `role` | string | 必須 | pattern="^[a-z][a-z0-9.-]*$" | — |
| `label` | string | 任意／条件付き | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "contributorId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "role": {
      "type": "string",
      "pattern": "^[a-z][a-z0-9.-]*$"
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "contributorId",
    "role"
  ]
}
```

<a id="legacy-alternatetitle"></a>
## legacy33 / alternateTitle

`#/$defs/legacy33/$defs/alternateTitle`

Stable-ID song title alternative; array position and title text do not identify it.

親内必須: `id`, `title`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | — | — |
| `title` | string | 必須 | minLength=1 | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Stable-ID song title alternative; array position and title text do not identify it.",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "title": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "id",
    "title"
  ]
}
```

<a id="legacy-languagemap32"></a>
## legacy33 / languageMap32

`#/$defs/legacy33/$defs/languageMap32`

Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank.

親内必須: —

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "minProperties": 1,
  "propertyNames": {
    "type": "string",
    "pattern": "^[A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})*$"
  },
  "additionalProperties": {
    "type": "string"
  },
  "description": "Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank."
}
```

<a id="legacy-localizationtarget"></a>
## legacy33 / localizationTarget

`#/$defs/legacy33/$defs/localizationTarget`

Stable target by Core ID or profile-local scoped ID; song is the only ID-less target. No array indexes or mutable names as locators.

親内必須: `kind`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `kind` | enum ["song", "alternateTitle", "contributor", "credit", "section", "track", "clip", "soundSlot", "drumKit", "lyricDocument", "resource", "phraseTemplate", "clipCandidate", "clipChoiceGroup", "roleDefinition", "genre"] | 必須 | — | — |
| `id` | legacy33/$defs/id | 任意／条件付き | — | — |
| `profile` | enum ["org.ostf.phrase-library.v1", "org.ostf.clip-choices.v1", "org.ostf.appearance.v1"] | 任意／条件付き | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "kind": {
      "enum": [
        "song",
        "alternateTitle",
        "contributor",
        "credit",
        "section",
        "track",
        "clip",
        "soundSlot",
        "drumKit",
        "lyricDocument",
        "resource",
        "phraseTemplate",
        "clipCandidate",
        "clipChoiceGroup",
        "roleDefinition",
        "genre"
      ]
    },
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "profile": {
      "type": "string",
      "enum": [
        "org.ostf.phrase-library.v1",
        "org.ostf.clip-choices.v1",
        "org.ostf.appearance.v1"
      ]
    }
  },
  "required": [
    "kind"
  ],
  "allOf": [
    {
      "if": {
        "properties": {
          "kind": {
            "const": "song"
          }
        },
        "required": [
          "kind"
        ]
      },
      "then": {
        "not": {
          "anyOf": [
            {
              "required": [
                "id"
              ]
            },
            {
              "required": [
                "profile"
              ]
            }
          ]
        }
      },
      "else": {
        "required": [
          "id"
        ]
      }
    },
    {
      "if": {
        "properties": {
          "kind": {
            "enum": [
              "phraseTemplate",
              "clipCandidate",
              "clipChoiceGroup",
              "roleDefinition"
            ]
          }
        },
        "required": [
          "kind"
        ]
      },
      "then": {
        "required": [
          "profile"
        ]
      },
      "else": {
        "not": {
          "required": [
            "profile"
          ]
        }
      }
    }
  ],
  "description": "Stable target by Core ID or profile-local scoped ID; song is the only ID-less target. No array indexes or mutable names as locators."
}
```

<a id="legacy-localizationentry"></a>
## legacy33 / localizationEntry

`#/$defs/legacy33/$defs/localizationEntry`

Independent translations for one stable source field. Original source text remains authoritative as fallback.

親内必須: `target`, `field`, `values`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `target` | legacy33/$defs/localizationTarget | 必須 | — | — |
| `field` | string | 必須 | minLength=1; Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields. | — |
| `values` | legacy33/$defs/languageMap32 | 必須 | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "target": {
      "$ref": "#/$defs/legacy33/$defs/localizationTarget"
    },
    "field": {
      "type": "string",
      "minLength": 1,
      "description": "Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields."
    },
    "values": {
      "$ref": "#/$defs/legacy33/$defs/languageMap32"
    }
  },
  "required": [
    "target",
    "field",
    "values"
  ],
  "description": "Independent translations for one stable source field. Original source text remains authoritative as fallback."
}
```

<a id="legacy-localizationdata"></a>
## legacy33 / localizationData

`#/$defs/legacy33/$defs/localizationData`

Language-map translations indexed by stable kind/id/field, never by names or array positions.

親内必須: `entries`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `entries` | array<legacy33/$defs/localizationEntry> | 必須 | — | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "entries": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/localizationEntry"
      }
    }
  },
  "required": [
    "entries"
  ],
  "description": "Language-map translations indexed by stable kind/id/field, never by names or array positions."
}
```

<a id="legacy-genre"></a>
## legacy33 / genre

`#/$defs/legacy33/$defs/genre`

One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.

親内必須: `id`, `name`

| 項目 | 型 | 親内必須 | 明示制約・説明 | 実例 |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | 必須 | Stable song-local ID unique among all Core objects. | — |
| `name` | string | 必須 | minLength=1; Original Unicode genre label, never normalized or rewritten during import. | — |
| `externalUri` | string | 任意／条件付き | minLength=1; format="uri"; Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced. | — |

完全な構造定義（参照は同梱Schema内のJSON Pointer）:

```json
{
  "type": "object",
  "description": "One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id",
      "description": "Stable song-local ID unique among all Core objects."
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "description": "Original Unicode genre label, never normalized or rewritten during import."
    },
    "externalUri": {
      "type": "string",
      "minLength": 1,
      "format": "uri",
      "description": "Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```

## Schemaだけでは判定できない規則

IDの種別横断一意性、参照解決、開始順・拍子合計、絶対時間と演算後範囲、voicingの配列同長、候補所有、原型対応、相対音の等式、依存範囲、翻訳対象field・原文存在・重複、数値トークン保持、編集の原子性は正式仕様を併読します。構造上許された値でも意味規則を満たさなければ適合しません。

`languageMap32`は継承された汎用構造として空文字を許しますが、3.4のlocalization本文では非空翻訳を要求しています。新Coreでは両方を満たす非空の値を使います。これはSchemaの許容範囲と意味要件の区別であり、今回Schemaを書き換えたものではありません。

動作・再生・全組合せの網羅や実装認証を意味しません。
