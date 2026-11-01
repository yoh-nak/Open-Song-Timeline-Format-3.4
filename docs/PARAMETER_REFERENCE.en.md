# OSTF 3.4.0 — Complete Parameter Reference

Official version 3.4.0. All definitions and constraints below are generated from the bundled schema.

**Structural authority:** [JSON Schema](../schema/ostf-3.4.0.schema.json). **Semantic authority:** [normative Japanese specification](FORMAT_SPECIFICATION.ja.md), with an [English translation](FORMAT_SPECIFICATION.en.md). See the [manual](COMPLETE_MANUAL.en.md) and [witness index](COVERAGE.md).

Required means required within a present parent object. An optional parent remains optional. Apply the full schema blocks, including conditional requirements/prohibitions, dependentRequired, dictionary key constraints and additionalProperties. A default is not an instruction to insert a value.

Includes 77 current definitions plus the root and 65 frozen compatibility definitions. Covers 296 current storage declarations and 119 per-declaration enum values. Legacy definitions do not define alternative current-Core authorities.

## Index

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

Required within this object: `format`, `version`, `ppq`, `song`, `timeline`, `harmony`, `tracks`, `soundSlots`, `lyrics`, `resources`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `format` | const "OSTF" | yes | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/format` |
| `version` | const "3.4.0" | yes | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/version` |
| `ppq` | integer | yes | minimum=1; maximum=960000 | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/ppq` |
| `song` | song | yes | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/song` |
| `timeline` | timeline | yes | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline` |
| `harmony` | harmony | yes | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/harmony` |
| `tracks` | array<track> | yes | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/tracks` |
| `soundSlots` | array<soundSlot> | yes | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/soundSlots` |
| `lyrics` | lyrics | yes | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/lyrics` |
| `resources` | array<resource> | yes | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/resources` |
| `extensions` | legacy33/$defs/extensions | optional / conditional | Optional third-party or verbatim legacy compatibility payloads. Standard Core always remains authoritative. New first-party common information must not be stored only here. | [samples/17_legacy_conflict_core_wins.ostf](../samples/17_legacy_conflict_core_wins.ostf) `/extensions` |
| `drumKits` | array<drumKit> | optional / conditional | Optional multiple percussion-kit definitions; absent = no declared kits (3.0 compatible). | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/drumKits` |
| `contributors` | array<contributor> | optional / conditional | Optional unordered identity records referenced by song.credits. No contributor limit is imposed by this format. | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/contributors` |
| `document` | documentInfo | optional / conditional | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document` |
| `relativePhrases` | relativePhrases | optional / conditional | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases` |
| `generation` | generation | optional / conditional | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation` |
| `presentation` | presentation | optional / conditional | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation` |
| `phraseLibrary` | phraseLibrary | optional / conditional | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary` |
| `clipChoices` | clipChoices | optional / conditional | — | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices` |
| `localization` | localization | optional / conditional | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization` |
| `provenance` | provenance | optional / conditional | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `type`, `id`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `type` | enum ["section", "track", "clip", "note", "chord", "scale", "soundSlot", "drumKit", "lyricDocument", "lyricPhrase", "lyricUnit", "lyricAlignment", "resource", "genre", "contributor", "credit", "alternateTitle", "mood", "keyChange", "phraseTemplate", "phraseInstance", "clipChoiceGroup", "clipCandidate", "roleDefinition", "generationProcess", "provenanceRecord"] | yes | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/appearance/objectColors/0/target/type` |
| `id` | id | yes | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/appearance/objectColors/0/target/id` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `start`, `duration`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `start` | nonnegative | yes | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/inputs/0/readRange/start` |
| `duration` | positive | yes | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/inputs/0/readRange/duration` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `step`, `alter`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `step` | enum ["A", "B", "C", "D", "E", "F", "G"] | yes | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/key/tonic/step` |
| `alter` | integer | yes | minimum=-2; maximum=2 | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/key/tonic/alter` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `title`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `title` | string | yes | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/song/title` |
| `primaryMelodyTrackId` | id | optional / conditional | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/primaryMelodyTrackId` |
| `localizedTitles` | localizedNames | optional / conditional | Optional localized song-title alternatives. song.title is the stable fallback. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/song/localizedTitles` |
| `subtitle` | string | optional / conditional | Optional original-language subtitle. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/song/subtitle` |
| `description` | string | optional / conditional | Optional original-language description, including Unicode and line breaks. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/song/description` |
| `alternateTitles` | array<alternateTitle> | optional / conditional | Additional stable-ID source-language titles. | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/alternateTitles` |
| `credits` | array<credit> | optional / conditional | Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted. | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/credits` |
| `genres` | array<genre> | optional / conditional | Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified. | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/genres` |
| `key` | key | optional / conditional | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/key` |
| `scale` | scaleDefinition | optional / conditional | — | [samples/04_scale_without_key.ostf](../samples/04_scale_without_key.ostf) `/song/scale` |
| `languages` | array<string> | optional / conditional | uniqueItems=true | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/languages` |
| `primaryLyricDocumentId` | id | optional / conditional | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/song/primaryLyricDocumentId` |
| `moods` | array<mood> | optional / conditional | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/moods` |
| `rights` | rightsStatement | optional / conditional | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/rights` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `name`, `start`, `duration`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/timeline/sections/0/id` |
| `name` | string | yes | minLength=1 | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/timeline/sections/0/name` |
| `start` | nonnegative | yes | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/timeline/sections/0/start` |
| `duration` | positive | yes | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/timeline/sections/0/duration` |
| `role` | string | optional / conditional | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/timeline/sections/0/role` |
| `localizedNames` | localizedNames | optional / conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/timeline/sections/0/localizedNames` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `at`, `bpm`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `at` | nonnegative | yes | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/tempoChanges/0/at` |
| `bpm` | number | yes | maximum=1000; exclusiveMinimum=0 | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/tempoChanges/0/bpm` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `at`, `numerator`, `denominator`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `at` | nonnegative | yes | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/meterChanges/0/at` |
| `numerator` | integer | yes | minimum=1; maximum=64 | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/meterChanges/0/numerator` |
| `denominator` | enum [1, 2, 4, 8, 16, 32, 64] | yes | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/meterChanges/0/denominator` |
| `beatGroups` | array<integer> | optional / conditional | minItems=1; maxItems=64; Optional additive grouping in denominator units. Values must sum to numerator. Descriptive only; does not change note timestamps. | [samples/07_pickup_additive_midbar_meter.ostf](../samples/07_pickup_additive_midbar_meter.ostf) `/timeline/meterChanges/0/beatGroups` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `sections`, `tempoChanges`, `meterChanges`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `sections` | array<section> | yes | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/sections` |
| `tempoChanges` | array<tempo> | yes | minItems=1 | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/tempoChanges` |
| `meterChanges` | array<meter> | yes | minItems=1 | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/timeline/meterChanges` |
| `keyChanges` | array<keyChange> | optional / conditional | — | [samples/03_modulation_atonal_and_unspecified.ostf](../samples/03_modulation_atonal_and_unspecified.ostf) `/timeline/keyChanges` |
| `duration` | nonnegative | optional / conditional | — | [samples/07_pickup_additive_midbar_meter.ostf](../samples/07_pickup_additive_midbar_meter.ostf) `/timeline/duration` |
| `barOrigin` | nonnegative | optional / conditional | — | [samples/07_pickup_additive_midbar_meter.ostf](../samples/07_pickup_additive_midbar_meter.ostf) `/timeline/barOrigin` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `start`, `duration`, `label`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/id` |
| `start` | nonnegative | yes | — | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/start` |
| `duration` | positive | yes | — | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/duration` |
| `label` | string | yes | minLength=1 | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/label` |
| `root` | spelledPitchClass | optional / conditional | — | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/root` |
| `intervals` | array<integer> | optional / conditional | minItems=1; maxItems=36; uniqueItems=true | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/intervals` |
| `bass` | spelledPitchClass | optional / conditional | — | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/harmony/chords/0/bass` |
| `voicing` | voicing | optional / conditional | Optional pitch snapshot (not an arrangement note sequence). No automatic playback. | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/voicing` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `start`, `duration`, `tonic`, `intervals`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/id` |
| `start` | nonnegative | yes | — | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/start` |
| `duration` | positive | yes | — | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/duration` |
| `label` | string | optional / conditional | — | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/label` |
| `tonic` | spelledPitchClass | yes | — | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/tonic` |
| `intervals` | array<integer> | yes | minItems=1; maxItems=12; uniqueItems=true | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/intervals` |
| `targets` | array<scaleTarget> | optional / conditional | minItems=1; uniqueItems=true; Optional explicit scope. Absence means general timed context, not a global key. Overlapping contexts are not resolved by array order. | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/targets` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `chords`, `scales`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `chords` | array<chord> | yes | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/harmony/chords` |
| `scales` | array<scale> | yes | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/harmony/scales` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `name`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `name` | string | yes | — | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/instrument/name` |
| `family` | string | optional / conditional | — | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/instrument/family` |
| `localizedNames` | localizedNames | optional / conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/instrument/localizedNames` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `start`, `duration`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/notes/0/id` |
| `start` | signed | yes | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/notes/0/start` |
| `duration` | positive | yes | Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample. | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/notes/0/duration` |
| `pitch` | pitch | optional / conditional | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/notes/0/pitch` |
| `soundSlotId` | id | optional / conditional | Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre. | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/tracks/0/clips/0/notes/1/soundSlotId` |
| `velocity` | integer | optional / conditional | minimum=1; maximum=127; Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving. | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/notes/0/velocity` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `start`, `duration`, `notes`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/id` |
| `name` | string | optional / conditional | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/name` |
| `start` | nonnegative | yes | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/start` |
| `duration` | positive | yes | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/duration` |
| `enabled` | boolean | optional / conditional | default=true | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/tracks/0/clips/0/enabled` |
| `notes` | array<note> | yes | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips/0/notes` |
| `localizedNames` | localizedNames | optional / conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/clips/0/localizedNames` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `name`, `clips`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/id` |
| `name` | string | yes | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/name` |
| `role` | string | optional / conditional | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/role` |
| `instrument` | instrument | optional / conditional | — | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/instrument` |
| `enabled` | boolean | optional / conditional | default=true | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/enabled` |
| `clips` | array<clip> | yes | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/clips` |
| `trackType` | enum ["melodic", "drum", "mixed"] | optional / conditional | Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class. | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/tracks/0/trackType` |
| `preferredView` | enum ["auto", "pianoRoll", "drumGrid"] | optional / conditional | default="auto"; Non-binding presentation preference. Does not change note meaning. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/preferredView` |
| `soundSource` | soundSource | optional / conditional | Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/soundSource` |
| `localizedNames` | localizedNames | optional / conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/localizedNames` |
| `drumKitId` | id | optional / conditional | Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit. | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/tracks/0/drumKitId` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `name`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/soundSlots/0/id` |
| `name` | string | yes | — | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/soundSlots/0/name` |
| `role` | string | optional / conditional | Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier. | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/soundSlots/0/role` |
| `midiNote` | pitch | optional / conditional | Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/soundSlots/0/midiNote` |
| `midiMapping` | midiMapping | optional / conditional | Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity. | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/soundSlots/0/midiMapping` |
| `localizedNames` | localizedNames | optional / conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/soundSlots/0/localizedNames` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/documents/0/id` |
| `title` | string | optional / conditional | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/documents/0/title` |
| `language` | string | optional / conditional | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/documents/0/language` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `documentId`, `text`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/phrases/0/id` |
| `documentId` | id | yes | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/phrases/0/documentId` |
| `text` | string | yes | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/phrases/0/text` |
| `pronunciation` | string | optional / conditional | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/phrases/0/pronunciation` |
| `start` | nonnegative | optional / conditional | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/phrases/0/start` |
| `duration` | positive | optional / conditional | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/phrases/0/duration` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `phraseId`, `text`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/units/0/id` |
| `phraseId` | id | yes | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/units/0/phraseId` |
| `text` | string | yes | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/units/0/text` |
| `pronunciation` | string | optional / conditional | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/units/0/pronunciation` |
| `start` | nonnegative | optional / conditional | — | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/lyrics/units/0/start` |
| `duration` | positive | optional / conditional | — | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/lyrics/units/0/duration` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `unitIds`, `noteIds`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/alignments/0/id` |
| `unitIds` | array<id> | yes | minItems=1; uniqueItems=true | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/alignments/0/unitIds` |
| `noteIds` | array<id> | yes | minItems=1; uniqueItems=true | [samples/10_primary_lyrics_and_alignment.ostf](../samples/10_primary_lyrics_and_alignment.ostf) `/lyrics/alignments/0/noteIds` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `documents`, `phrases`, `units`, `alignments`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `documents` | array<lyricDocument> | yes | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/lyrics/documents` |
| `phrases` | array<lyricPhrase> | yes | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/lyrics/phrases` |
| `units` | array<lyricUnit> | yes | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/lyrics/units` |
| `alignments` | array<lyricAlignment> | yes | — | [samples/01_empty_without_extensions.ostf](../samples/01_empty_without_extensions.ostf) `/lyrics/alignments` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `kind`, `uri`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/resources/0/id` |
| `kind` | enum ["audio", "midi", "text", "other"] | yes | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/resources/0/kind` |
| `uri` | string | yes | minLength=1 | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/resources/0/uri` |
| `name` | string | optional / conditional | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/resources/0/name` |
| `sha256` | sha256 | optional / conditional | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/resources/0/sha256` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `noteId`, `basis`, `contextId`, `anchorPitch`, `index`, `chromaticOffset`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `noteId` | id | yes | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments/0/noteId` |
| `basis` | enum ["chordTone", "scaleDegree"] | yes | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments/0/basis` |
| `contextId` | id | yes | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments/0/contextId` |
| `anchorPitch` | pitch | yes | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments/0/anchorPitch` |
| `index` | integer | yes | minimum=1; maximum=36 | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments/0/index` |
| `chromaticOffset` | integer | yes | minimum=-24; maximum=24 | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments/0/chromaticOffset` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `version`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | string | yes | minLength=1 | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/generator/id` |
| `version` | string | yes | minLength=1 | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/generator/version` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `role`, `ref`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `role` | string | yes | minLength=1 | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/inputs/0/role` |
| `ref` | ref | yes | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/inputs/0/ref` |
| `readRange` | range | optional / conditional | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/inputs/0/readRange` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `generator`, `inputs`, `outputs`, `protectedNoteIds`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/id` |
| `generator` | generator | yes | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/generator` |
| `inputs` | array<generationInput> | yes | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/inputs` |
| `outputs` | array<ref> | yes | minItems=1 | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/outputs` |
| `targetRange` | range | optional / conditional | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/targetRange` |
| `protectedNoteIds` | array<id> | yes | uniqueItems=true | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/protectedNoteIds` |
| `intent` | generationIntent | optional / conditional | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `name`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/roleDefinitions/0/id` |
| `name` | string | yes | minLength=1 | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/roleDefinitions/0/name` |
| `baseRole` | string | optional / conditional | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/roleDefinitions/0/baseRole` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `target`, `color`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `target` | ref | yes | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/appearance/objectColors/0/target` |
| `color` | color | yes | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/appearance/objectColors/0/color` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `duration`, `notes`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/id` |
| `duration` | positive | yes | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/duration` |
| `notes` | array<corePhraseSourceNote> | yes | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/notes` |
| `name` | string | optional / conditional | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/name` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `templateNoteId`, `repeatIndex`, `noteId`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `templateNoteId` | id | yes | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/noteMap/0/templateNoteId` |
| `repeatIndex` | nonnegative | yes | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/noteMap/0/repeatIndex` |
| `noteId` | id | yes | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/noteMap/0/noteId` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `templateId`, `clipId`, `repeatCount`, `transpose`, `noteMap`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/id` |
| `templateId` | id | yes | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/templateId` |
| `clipId` | id | yes | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/clipId` |
| `repeatCount` | positive | yes | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/repeatCount` |
| `transpose` | integer | yes | minimum=-127; maximum=127 | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/transpose` |
| `noteMap` | array<phraseNoteMapping> | yes | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/noteMap` |
| `velocityMode` | enum ["independent", "linked"] | optional / conditional | default="independent"; independent preserves concrete velocities on refresh; linked requires exact presence/value equality with the template. This field does not trigger refresh on load. | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances/0/velocityMode` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `clipIds`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/candidates/0/id` |
| `clipIds` | array<id> | yes | uniqueItems=true | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/candidates/0/clipIds` |
| `name` | string | optional / conditional | — | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/candidates/0/name` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `candidates`, `selectedCandidateId`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/id` |
| `candidates` | array<clipCandidate> | yes | minItems=1 | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/candidates` |
| `selectedCandidateId` | oneOf/anyOf | yes | — | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/selectedCandidateId` |
| `name` | string | optional / conditional | — | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups/0/name` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `standard`, `note`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `standard` | enum ["gm1", "custom"] | yes | gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number. | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/soundSlots/0/midiMapping/standard` |
| `note` | pitch | yes | MIDI1 note number in 0..127; for gm1 restrict to 35..81. | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/soundSlots/0/midiMapping/note` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `kind`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `kind` | enum ["unassigned", "gm1", "externalMidi", "plugin", "hostManaged"] | yes | — | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/soundSource/kind` |
| `identifier` | string | optional / conditional | minLength=1; Opaque target identifier, e.g. URI, plug-in identifier or port alias, not a loading command. | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/tracks/0/soundSource/identifier` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `name`, `soundSlotIds`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/drumKits/0/id` |
| `name` | string | yes | — | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/drumKits/0/name` |
| `localizedNames` | localizedNames | optional / conditional | — | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/drumKits/0/localizedNames` |
| `soundSlotIds` | array<id> | yes | uniqueItems=true; Ordered, unique references to global soundSlots; may be empty. | [samples/19_mixed_identity_no_drum_transpose.ostf](../samples/19_mixed_identity_no_drum_transpose.ostf) `/drumKits/0/soundSlotIds` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `pitches`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `pitches` | array<pitch> | yes | minItems=1; Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed. | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/voicing/pitches` |
| `velocities` | array<oneOf/anyOf> | optional / conditional | minItems=1; Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic. | [samples/20_voicing_snapshot_not_double_playback.ostf](../samples/20_voicing_snapshot_not_double_playback.ostf) `/harmony/chords/0/voicing/velocities` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `name`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/contributors/0/id` |
| `name` | string | yes | minLength=1 | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/contributors/0/name` |
| `kind` | enum ["person", "organization", "other"] | optional / conditional | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/contributors/0/kind` |
| `localizedNames` | localizedNames | optional / conditional | — | [samples/23_complete_core_metadata_and_localization.ostf](../samples/23_complete_core_metadata_and_localization.ostf) `/contributors/0/localizedNames` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `contributorId`, `role`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/credits/0/id` |
| `contributorId` | id | yes | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/credits/0/contributorId` |
| `role` | string | yes | pattern="^[a-z][a-z0-9.-]*$" | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/credits/0/role` |
| `label` | string | optional / conditional | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/credits/0/label` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `title`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/alternateTitles/0/id` |
| `title` | string | yes | minLength=1 | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/alternateTitles/0/title` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `kind`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `kind` | enum ["song", "alternateTitle", "contributor", "credit", "section", "track", "clip", "soundSlot", "drumKit", "lyricDocument", "resource", "phraseTemplate", "clipCandidate", "clipChoiceGroup", "roleDefinition", "genre", "mood", "keyChange", "scale"] | yes | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries/0/target/kind` |
| `id` | id | optional / conditional | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries/1/target/id` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `target`, `field`, `values`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `target` | localizationTarget | yes | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries/0/target` |
| `field` | string | yes | minLength=1; Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields. | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries/0/field` |
| `values` | languageMap32 | yes | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries/0/values` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `name`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | Stable song-local ID unique among all Core objects. | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/genres/0/id` |
| `name` | string | yes | minLength=1; Original Unicode genre label, never normalized or rewritten during import. | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/genres/0/name` |
| `externalUri` | string | optional / conditional | minLength=1; format="uri"; Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced. | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/genres/0/externalUri` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `documentId`, `revisionId`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `documentId` | opaqueDocumentId | yes | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/parents/0/documentId` |
| `revisionId` | opaqueDocumentId | yes | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/parents/0/revisionId` |
| `sha256` | sha256 | optional / conditional | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/parents/0/sha256` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `name`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `name` | string | yes | minLength=1 | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/createdBy/name` |
| `version` | string | optional / conditional | minLength=1 | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/createdBy/version` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `revisionId`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | opaqueDocumentId | yes | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/id` |
| `revisionId` | opaqueDocumentId | yes | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/revisionId` |
| `parents` | array<revisionRef> | optional / conditional | uniqueItems=true | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/parents` |
| `createdBy` | software | optional / conditional | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/createdBy` |
| `modifiedBy` | software | optional / conditional | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/document/modifiedBy` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `state`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `state` | enum ["tonal", "atonal", "unspecified"] | yes | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/key/state` |
| `tonic` | spelledPitchClass | optional / conditional | — | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/key/tonic` |
| `mode` | string | optional / conditional | minLength=1; Authored mode identifier. Canonical recognized values include major, minor, dorian, phrygian, lydian, mixolydian, locrian. Unknown values are preserved, never converted to major/minor. | [samples/02_trance_metadata_core_only.ostf](../samples/02_trance_metadata_core_only.ostf) `/song/key/mode` |
| `label` | string | optional / conditional | — | [samples/05_custom_mode_and_scale.ostf](../samples/05_custom_mode_and_scale.ostf) `/song/key/label` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `at`, `key`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/03_modulation_atonal_and_unspecified.ostf](../samples/03_modulation_atonal_and_unspecified.ostf) `/timeline/keyChanges/0/id` |
| `at` | positive | yes | — | [samples/03_modulation_atonal_and_unspecified.ostf](../samples/03_modulation_atonal_and_unspecified.ostf) `/timeline/keyChanges/0/at` |
| `key` | key | yes | — | [samples/03_modulation_atonal_and_unspecified.ostf](../samples/03_modulation_atonal_and_unspecified.ostf) `/timeline/keyChanges/0/key` |
| `label` | string | optional / conditional | — | [samples/03_modulation_atonal_and_unspecified.ostf](../samples/03_modulation_atonal_and_unspecified.ostf) `/timeline/keyChanges/0/label` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `tonic`, `intervals`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/04_scale_without_key.ostf](../samples/04_scale_without_key.ostf) `/song/scale/id` |
| `tonic` | spelledPitchClass | yes | — | [samples/04_scale_without_key.ostf](../samples/04_scale_without_key.ostf) `/song/scale/tonic` |
| `intervals` | array<integer> | yes | minItems=1; maxItems=12; uniqueItems=true | [samples/04_scale_without_key.ostf](../samples/04_scale_without_key.ostf) `/song/scale/intervals` |
| `label` | string | optional / conditional | — | [samples/04_scale_without_key.ostf](../samples/04_scale_without_key.ostf) `/song/scale/label` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `type`, `id`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `type` | enum ["section", "track", "clip", "chord", "note"] | yes | — | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/targets/0/type` |
| `id` | id | yes | — | [samples/06_overlapping_scale_contexts.ostf](../samples/06_overlapping_scale_contexts.ostf) `/harmony/scales/0/targets/0/id` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `name`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | Stable song-local ID unique among all Core objects. | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/moods/0/id` |
| `name` | string | yes | minLength=1; Original Unicode genre label, never normalized or rewritten during import. | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/moods/0/name` |
| `externalUri` | string | optional / conditional | minLength=1; format="uri"; Optional external vocabulary URI hint; never authoritative for the authored mood name and never auto-dereferenced. | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/moods/0/externalUri` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `notice` | string | optional / conditional | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/rights/notice` |
| `licenseUri` | string | optional / conditional | minLength=1 | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/rights/licenseUri` |
| `rightsHolderIds` | array<id> | optional / conditional | uniqueItems=true | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/song/rights/rightsHolderIds` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `name` | string | optional / conditional | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/groove/name` |
| `unitTicks` | positive | optional / conditional | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/groove/unitTicks` |
| `longWeight` | integer | optional / conditional | minimum=1; maximum=1000000 | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/groove/longWeight` |
| `shortWeight` | integer | optional / conditional | minimum=1; maximum=1000000 | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/groove/shortWeight` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `genreNames` | array<string> | optional / conditional | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/genreNames` |
| `moodNames` | array<string> | optional / conditional | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/moodNames` |
| `groove` | grooveIntent | optional / conditional | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/groove` |
| `prompt` | string | optional / conditional | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/prompt` |
| `seed` | string | optional / conditional | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes/0/intent/seed` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `status`, `dependencies`, `assignments`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `status` | enum ["current", "stale", "unverified"] | yes | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/status` |
| `dependencies` | dependencies | yes | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/dependencies` |
| `assignments` | array<relativeAssignment> | yes | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/relativePhrases/assignments` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `status`, `dependencies`, `processes`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `status` | enum ["current", "stale", "unverified"] | yes | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/status` |
| `dependencies` | dependencies | yes | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/dependencies` |
| `processes` | array<generationProcess> | yes | — | [samples/15_relative_and_generation_intent.ostf](../samples/15_relative_and_generation_intent.ostf) `/generation/processes` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `status`, `dependencies`, `roleDefinitions`, `sectionRoleAssignments`, `appearance`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `status` | enum ["current", "stale", "unverified"] | yes | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/status` |
| `dependencies` | dependencies | yes | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/dependencies` |
| `roleDefinitions` | array<roleDefinition> | yes | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/roleDefinitions` |
| `sectionRoleAssignments` | object | yes | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/sectionRoleAssignments` |
| `appearance` | object | yes | — | [samples/11_presentation_no_extension.ostf](../samples/11_presentation_no_extension.ostf) `/presentation/appearance` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `status`, `dependencies`, `templates`, `instances`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `status` | enum ["current", "stale", "unverified"] | yes | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/status` |
| `dependencies` | dependencies | yes | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/dependencies` |
| `templates` | array<phraseTemplate> | yes | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates` |
| `instances` | array<phraseInstance> | yes | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/instances` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `status`, `dependencies`, `groups`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `status` | enum ["current", "stale", "unverified"] | yes | — | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/status` |
| `dependencies` | dependencies | yes | — | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/dependencies` |
| `groups` | array<clipChoiceGroup> | yes | — | [samples/14_clip_choices_no_selection.ostf](../samples/14_clip_choices_no_selection.ostf) `/clipChoices/groups` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `status`, `dependencies`, `entries`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `status` | enum ["current", "stale", "unverified"] | yes | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/status` |
| `dependencies` | dependencies | yes | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/dependencies` |
| `entries` | array<localizationEntry> | yes | — | [samples/09_languages_genres_moods_credits.ostf](../samples/09_languages_genres_moods_credits.ostf) `/localization/entries` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `start`, `duration`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/notes/0/id` |
| `start` | signed | yes | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/notes/0/start` |
| `duration` | positive | yes | Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample. | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/notes/0/duration` |
| `pitch` | pitch | optional / conditional | — | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/notes/0/pitch` |
| `soundSlotId` | id | optional / conditional | Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre. | [samples/21_native_drum_template_velocity.ostf](../samples/21_native_drum_template_velocity.ostf) `/phraseLibrary/templates/0/notes/0/soundSlotId` |
| `velocity` | integer | optional / conditional | minimum=1; maximum=127; Optional template note-on velocity, 1–127. Applied only by an explicit materialization/update according to instance.velocityMode; never a performed event by itself. | [samples/12_phrase_velocity_linked.ostf](../samples/12_phrase_velocity_linked.ostf) `/phraseLibrary/templates/0/notes/0/velocity` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `format` | string | optional / conditional | minLength=1 | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/format` |
| `version` | string | optional / conditional | minLength=1 | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/version` |
| `sha256` | sha256 | optional / conditional | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/sha256` |
| `uri` | string | optional / conditional | minLength=1 | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/uri` |
| `documentId` | opaqueDocumentId | optional / conditional | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/documentId` |
| `revisionId` | opaqueDocumentId | optional / conditional | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/revisionId` |
| `resourceId` | id | optional / conditional | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources/0/resourceId` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `action`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | id | yes | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/id` |
| `action` | enum ["create", "import", "conversion", "edit", "transpose", "merge", "generation", "other"] | yes | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/action` |
| `description` | string | optional / conditional | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/description` |
| `tool` | software | optional / conditional | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/tool` |
| `sources` | array<provenanceSource> | optional / conditional | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/sources` |
| `semitones` | integer | optional / conditional | minimum=-127; maximum=127 | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/semitones` |
| `beforeKey` | key | optional / conditional | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/beforeKey` |
| `afterKey` | key | optional / conditional | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records/0/afterKey` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `records`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `records` | array<provenanceRecord> | yes | — | [samples/16_identity_provenance_and_transpose.ostf](../samples/16_identity_provenance_and_transpose.ostf) `/provenance/records` |

Complete structural definition (references are JSON Pointers in the bundled schema):

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
## Frozen legacy definitions — compatibility only

The following 65 definitions preserve the old structural contract. They are excluded from the 296 current-field witness denominator. Not every frozen definition is reachable from the current root, and an old song or track definition cannot substitute for its current version. Do not treat an unknown extension version as a known version.

[Compatibility example](../samples/49_frozen_legacy_profiles_compatibility_only.ostf)

<a id="legacy-id"></a>
## legacy33 / id

`#/$defs/legacy33/$defs/id`

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `type`, `id`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `type` | enum ["section", "track", "clip", "note", "chord", "scale", "soundSlot", "drumKit", "lyricDocument", "lyricPhrase", "lyricUnit", "lyricAlignment", "resource", "genre"] | yes | — | — |
| `id` | legacy33/$defs/id | yes | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `start`, `duration`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `start` | legacy33/$defs/nonnegative | yes | — | — |
| `duration` | legacy33/$defs/positive | yes | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `step`, `alter`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `step` | enum ["A", "B", "C", "D", "E", "F", "G"] | yes | — | — |
| `alter` | integer | yes | minimum=-2; maximum=2 | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `title`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `title` | string | yes | — | — |
| `primaryMelodyTrackId` | legacy33/$defs/id | optional / conditional | — | — |
| `localizedTitles` | legacy33/$defs/localizedNames | optional / conditional | Optional localized song-title alternatives. song.title is the stable fallback. | — |
| `subtitle` | string | optional / conditional | Optional original-language subtitle. | — |
| `description` | string | optional / conditional | Optional original-language description, including Unicode and line breaks. | — |
| `alternateTitles` | array<legacy33/$defs/alternateTitle> | optional / conditional | Additional stable-ID source-language titles. | — |
| `credits` | array<legacy33/$defs/credit> | optional / conditional | Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted. | — |
| `genres` | array<legacy33/$defs/genre> | optional / conditional | Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified. | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `name`, `start`, `duration`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `name` | string | yes | minLength=1 | — |
| `start` | legacy33/$defs/nonnegative | yes | — | — |
| `duration` | legacy33/$defs/positive | yes | — | — |
| `role` | string | optional / conditional | — | — |
| `localizedNames` | legacy33/$defs/localizedNames | optional / conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `at`, `bpm`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `at` | legacy33/$defs/nonnegative | yes | — | — |
| `bpm` | number | yes | maximum=1000; exclusiveMinimum=0 | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `at`, `numerator`, `denominator`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `at` | legacy33/$defs/nonnegative | yes | — | — |
| `numerator` | integer | yes | minimum=1; maximum=64 | — |
| `denominator` | enum [1, 2, 4, 8, 16, 32, 64] | yes | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `sections`, `tempoChanges`, `meterChanges`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `sections` | array<legacy33/$defs/section> | yes | — | — |
| `tempoChanges` | array<legacy33/$defs/tempo> | yes | minItems=1 | — |
| `meterChanges` | array<legacy33/$defs/meter> | yes | minItems=1 | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `start`, `duration`, `label`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `start` | legacy33/$defs/nonnegative | yes | — | — |
| `duration` | legacy33/$defs/positive | yes | — | — |
| `label` | string | yes | minLength=1 | — |
| `root` | legacy33/$defs/spelledPitchClass | optional / conditional | — | — |
| `intervals` | array<integer> | optional / conditional | minItems=1; maxItems=36; uniqueItems=true | — |
| `bass` | legacy33/$defs/spelledPitchClass | optional / conditional | — | — |
| `voicing` | legacy33/$defs/voicing | optional / conditional | Optional pitch snapshot (not an arrangement note sequence). No automatic playback. | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `start`, `duration`, `tonic`, `intervals`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `start` | legacy33/$defs/nonnegative | yes | — | — |
| `duration` | legacy33/$defs/positive | yes | — | — |
| `label` | string | optional / conditional | — | — |
| `tonic` | legacy33/$defs/spelledPitchClass | yes | — | — |
| `intervals` | array<integer> | yes | minItems=1; maxItems=12; uniqueItems=true | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `chords`, `scales`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `chords` | array<legacy33/$defs/chord> | yes | — | — |
| `scales` | array<legacy33/$defs/scale> | yes | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `name`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `name` | string | yes | — | — |
| `family` | string | optional / conditional | — | — |
| `localizedNames` | legacy33/$defs/localizedNames | optional / conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `start`, `duration`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `start` | legacy33/$defs/signed | yes | — | — |
| `duration` | legacy33/$defs/positive | yes | Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample. | — |
| `pitch` | legacy33/$defs/pitch | optional / conditional | — | — |
| `soundSlotId` | legacy33/$defs/id | optional / conditional | Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre. | — |
| `velocity` | integer | optional / conditional | minimum=1; maximum=127; Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving. | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `start`, `duration`, `notes`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `name` | string | optional / conditional | — | — |
| `start` | legacy33/$defs/nonnegative | yes | — | — |
| `duration` | legacy33/$defs/positive | yes | — | — |
| `enabled` | boolean | optional / conditional | default=true | — |
| `notes` | array<legacy33/$defs/note> | yes | — | — |
| `localizedNames` | legacy33/$defs/localizedNames | optional / conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `name`, `clips`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `name` | string | yes | — | — |
| `role` | string | optional / conditional | — | — |
| `instrument` | legacy33/$defs/instrument | optional / conditional | — | — |
| `enabled` | boolean | optional / conditional | default=true | — |
| `clips` | array<legacy33/$defs/clip> | yes | — | — |
| `trackType` | enum ["melodic", "drum", "mixed"] | optional / conditional | Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class. | — |
| `preferredView` | enum ["auto", "pianoRoll", "drumGrid"] | optional / conditional | default="auto"; Non-binding presentation preference. Does not change note meaning. | — |
| `soundSource` | legacy33/$defs/soundSource | optional / conditional | Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee. | — |
| `localizedNames` | legacy33/$defs/localizedNames | optional / conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | — |
| `drumKitId` | legacy33/$defs/id | optional / conditional | Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit. | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `name`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `name` | string | yes | — | — |
| `role` | string | optional / conditional | Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier. | — |
| `midiNote` | legacy33/$defs/pitch | optional / conditional | Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity. | — |
| `midiMapping` | legacy33/$defs/midiMapping | optional / conditional | Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity. | — |
| `localizedNames` | legacy33/$defs/localizedNames | optional / conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `title` | string | optional / conditional | — | — |
| `language` | string | optional / conditional | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `documentId`, `text`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `documentId` | legacy33/$defs/id | yes | — | — |
| `text` | string | yes | — | — |
| `pronunciation` | string | optional / conditional | — | — |
| `start` | legacy33/$defs/nonnegative | optional / conditional | — | — |
| `duration` | legacy33/$defs/positive | optional / conditional | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `phraseId`, `text`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `phraseId` | legacy33/$defs/id | yes | — | — |
| `text` | string | yes | — | — |
| `pronunciation` | string | optional / conditional | — | — |
| `start` | legacy33/$defs/nonnegative | optional / conditional | — | — |
| `duration` | legacy33/$defs/positive | optional / conditional | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `unitIds`, `noteIds`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `unitIds` | array<legacy33/$defs/id> | yes | minItems=1; uniqueItems=true | — |
| `noteIds` | array<legacy33/$defs/id> | yes | minItems=1; uniqueItems=true | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `documents`, `phrases`, `units`, `alignments`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `documents` | array<legacy33/$defs/lyricDocument> | yes | — | — |
| `phrases` | array<legacy33/$defs/lyricPhrase> | yes | — | — |
| `units` | array<legacy33/$defs/lyricUnit> | yes | — | — |
| `alignments` | array<legacy33/$defs/lyricAlignment> | yes | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `kind`, `uri`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `kind` | enum ["audio", "midi", "text", "other"] | yes | — | — |
| `uri` | string | yes | minLength=1 | — |
| `name` | string | optional / conditional | — | — |
| `sha256` | legacy33/$defs/sha256 | optional / conditional | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `version`, `status`, `dependencies`, `data`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `version` | string | yes | minLength=1 | — |
| `status` | enum ["current", "stale", "unverified"] | yes | — | — |
| `dependencies` | legacy33/$defs/dependencies | yes | — | — |
| `data` | schema | yes | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `noteId`, `basis`, `contextId`, `anchorPitch`, `index`, `chromaticOffset`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `noteId` | legacy33/$defs/id | yes | — | — |
| `basis` | enum ["chordTone", "scaleDegree"] | yes | — | — |
| `contextId` | legacy33/$defs/id | yes | — | — |
| `anchorPitch` | legacy33/$defs/pitch | yes | — | — |
| `index` | integer | yes | minimum=1; maximum=36 | — |
| `chromaticOffset` | integer | yes | minimum=-24; maximum=24 | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `assignments`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `assignments` | array<legacy33/$defs/relativeAssignment> | yes | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `version`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | string | yes | minLength=1 | — |
| `version` | string | yes | minLength=1 | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `role`, `ref`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `role` | string | yes | minLength=1 | — |
| `ref` | legacy33/$defs/ref | yes | — | — |
| `readRange` | legacy33/$defs/range | optional / conditional | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `generator`, `inputs`, `outputs`, `protectedNoteIds`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `generator` | legacy33/$defs/generator | yes | — | — |
| `inputs` | array<legacy33/$defs/generationInput> | yes | — | — |
| `outputs` | array<legacy33/$defs/ref> | yes | minItems=1 | — |
| `targetRange` | legacy33/$defs/range | optional / conditional | — | — |
| `protectedNoteIds` | array<legacy33/$defs/id> | yes | uniqueItems=true | — |
| `vendorExtension` | string | optional / conditional | minLength=1 | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `processes`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `processes` | array<legacy33/$defs/generationProcess> | yes | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `name`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `name` | string | yes | minLength=1 | — |
| `baseRole` | string | optional / conditional | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `target`, `color`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `target` | legacy33/$defs/ref | yes | — | — |
| `color` | legacy33/$defs/color | yes | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `roleDefinitions`, `sectionRoleAssignments`, `appearance`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `roleDefinitions` | array<legacy33/$defs/roleDefinition> | yes | — | — |
| `sectionRoleAssignments` | object | yes | — | — |
| `appearance` | object | yes | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `sourceVersion`, `sourceSha256`, `sourceText`, `conversionReport`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `sourceVersion` | const "2.3.0" | yes | — | — |
| `sourceSha256` | legacy33/$defs/sha256 | yes | — | — |
| `sourceText` | string | yes | minLength=1 | — |
| `conversionReport` | object | yes | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `org.ostf.relative-phrase.v1` | schema | optional / conditional | — | — |
| `org.ostf.generation-context.v1` | schema | optional / conditional | — | — |
| `org.ostf.appearance.v1` | schema | optional / conditional | — | — |
| `org.ostf.legacy-import.v1` | schema | optional / conditional | — | — |
| `org.ostf.phrase-library.v1` | schema | optional / conditional | — | — |
| `org.ostf.clip-choices.v1` | schema | optional / conditional | — | — |
| `org.ostf.localization.v1` | schema | optional / conditional | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `duration`, `notes`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `duration` | legacy33/$defs/positive | yes | — | — |
| `notes` | array<legacy33/$defs/phraseSourceNote> | yes | — | — |
| `name` | string | optional / conditional | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `templateNoteId`, `repeatIndex`, `noteId`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `templateNoteId` | legacy33/$defs/id | yes | — | — |
| `repeatIndex` | legacy33/$defs/nonnegative | yes | — | — |
| `noteId` | legacy33/$defs/id | yes | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `templateId`, `clipId`, `repeatCount`, `transpose`, `noteMap`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `templateId` | legacy33/$defs/id | yes | — | — |
| `clipId` | legacy33/$defs/id | yes | — | — |
| `repeatCount` | legacy33/$defs/positive | yes | — | — |
| `transpose` | integer | yes | minimum=-127; maximum=127 | — |
| `noteMap` | array<legacy33/$defs/phraseNoteMapping> | yes | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `templates`, `instances`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `templates` | array<legacy33/$defs/phraseTemplate> | yes | — | — |
| `instances` | array<legacy33/$defs/phraseInstance> | yes | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `clipIds`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `clipIds` | array<legacy33/$defs/id> | yes | uniqueItems=true | — |
| `name` | string | optional / conditional | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `candidates`, `selectedCandidateId`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `candidates` | array<legacy33/$defs/clipCandidate> | yes | minItems=1 | — |
| `selectedCandidateId` | oneOf/anyOf | yes | — | — |
| `name` | string | optional / conditional | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `groups`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `groups` | array<legacy33/$defs/clipChoiceGroup> | yes | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `standard`, `note`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `standard` | enum ["gm1", "custom"] | yes | gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number. | — |
| `note` | legacy33/$defs/pitch | yes | MIDI1 note number in 0..127; for gm1 restrict to 35..81. | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `kind`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `kind` | enum ["unassigned", "gm1", "externalMidi", "plugin", "hostManaged"] | yes | — | — |
| `identifier` | string | optional / conditional | minLength=1; Opaque target identifier, e.g. URI, plug-in identifier or port alias, not a loading command. | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `name`, `soundSlotIds`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `name` | string | yes | — | — |
| `localizedNames` | legacy33/$defs/localizedNames | optional / conditional | — | — |
| `soundSlotIds` | array<legacy33/$defs/id> | yes | uniqueItems=true; Ordered, unique references to global soundSlots; may be empty. | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `start`, `duration`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `start` | legacy33/$defs/signed | yes | — | — |
| `duration` | legacy33/$defs/positive | yes | — | — |
| `pitch` | legacy33/$defs/pitch | optional / conditional | — | — |
| `soundSlotId` | legacy33/$defs/id | optional / conditional | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `pitches`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `pitches` | array<legacy33/$defs/pitch> | yes | minItems=1; Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed. | — |
| `velocities` | array<oneOf/anyOf> | optional / conditional | minItems=1; Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic. | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `name`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `name` | string | yes | minLength=1 | — |
| `kind` | enum ["person", "organization", "other"] | optional / conditional | — | — |
| `localizedNames` | legacy33/$defs/localizedNames | optional / conditional | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `contributorId`, `role`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `contributorId` | legacy33/$defs/id | yes | — | — |
| `role` | string | yes | pattern="^[a-z][a-z0-9.-]*$" | — |
| `label` | string | optional / conditional | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `title`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | — | — |
| `title` | string | yes | minLength=1 | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: —

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `kind`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `kind` | enum ["song", "alternateTitle", "contributor", "credit", "section", "track", "clip", "soundSlot", "drumKit", "lyricDocument", "resource", "phraseTemplate", "clipCandidate", "clipChoiceGroup", "roleDefinition", "genre"] | yes | — | — |
| `id` | legacy33/$defs/id | optional / conditional | — | — |
| `profile` | enum ["org.ostf.phrase-library.v1", "org.ostf.clip-choices.v1", "org.ostf.appearance.v1"] | optional / conditional | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `target`, `field`, `values`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `target` | legacy33/$defs/localizationTarget | yes | — | — |
| `field` | string | yes | minLength=1; Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields. | — |
| `values` | legacy33/$defs/languageMap32 | yes | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `entries`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `entries` | array<legacy33/$defs/localizationEntry> | yes | — | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

Required within this object: `id`, `name`

| Property | Type | Required | Explicit constraints / description | Witness |
|---|---|---|---|---|
| `id` | legacy33/$defs/id | yes | Stable song-local ID unique among all Core objects. | — |
| `name` | string | yes | minLength=1; Original Unicode genre label, never normalized or rewritten during import. | — |
| `externalUri` | string | optional / conditional | minLength=1; format="uri"; Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced. | — |

Complete structural definition (references are JSON Pointers in the bundled schema):

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

## Rules not fully expressible in JSON Schema

Also apply the normative rules for global identity, typed references, ordering, beat-group sums, arithmetic bounds, equal voicing lengths, ownership, phrase mappings, relative-pitch equations, dependencies, localization source fields/existence/uniqueness, numeric-token preservation and atomic edits. Structural acceptance alone is not full conformance.

The inherited languageMap32 shape permits empty strings, while the 3.4 normative localization rule requires nonempty translations. New Core entries must satisfy both by using nonempty values. This records the distinction between structural permissiveness and semantic requirements; the schema has not been silently altered.

This is not runtime, playback, all-combination coverage or implementation certification.
