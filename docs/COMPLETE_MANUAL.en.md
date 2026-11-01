# OSTF 3.4.0 — Complete Manual

**Official release / Open Song Timeline Format 3.4.0**  
For composers, arrangers, file authors and Reader/Writer implementers. A `.ostf` file contains UTF-8 JSON.

This manual combines a practical authoring workflow with the complete semantic feature rules. Use the [complete parameter reference](PARAMETER_REFERENCE.en.md) for exact types, ranges and conditional constraints. The [schema](../schema/ostf-3.4.0.schema.json) is the structural authority; the [Japanese specification](FORMAT_SPECIFICATION.ja.md) is the semantic authority. Part II includes all fourteen sections of the English specification translation; it does not mix historical-version chapters into current rules.

[日本語マニュアル](COMPLETE_MANUAL.ja.md) · [Coverage](COVERAGE.md) · [54 sample index](../samples/INDEX.md) · [11 complete demos](../demos/README.md)

## Part I — Practical authoring, reading and editing

### 1. Reading paths

| Goal | Read / open |
|---|---|
| Write a first valid document | Section 2 and sample 01 |
| Avoid key/genre ambiguity | Section 3, detailed rules 4–5, samples 02–06/24/39 |
| Store performance, drums and lyrics | Sections 4–6, detailed rules 7–10, samples 29–36 |
| Preserve relative/phrase/generation/choice/localization relationships | Section 7, detailed rules 11, samples 11–15/38/40–46 |
| Implement merging and migration | Sections 8–9, detailed rules 12–13, sample 47 |
| Find every field and condition | Complete parameter reference and coverage index |
| Inspect the distributable | Section 11, release readiness and check_release.py |

Optional Core is not an extension. A phrase library, for example, is optional song content whose type and meaning are fully defined by OSTF 3.4; it does not depend on a separate developer's protocol. An application that cannot execute a feature still must not delete its saved information.

### 2. Start with the minimal document

This is the complete sample 01. It is valid without a key, genre or notes. Extensions are unnecessary. Tempo and meter maps are required and cannot be empty.

```json
{
  "format": "OSTF",
  "version": "3.4.0",
  "ppq": 960,
  "song": {
    "title": ""
  },
  "timeline": {
    "sections": [],
    "tempoChanges": [
      {
        "at": 0,
        "bpm": 120
      }
    ],
    "meterChanges": [
      {
        "at": 0,
        "numerator": 4,
        "denominator": 4
      }
    ]
  },
  "harmony": {
    "chords": [],
    "scales": []
  },
  "tracks": [],
  "soundSlots": [],
  "lyrics": {
    "documents": [],
    "phrases": [],
    "units": [],
    "alignments": []
  },
  "resources": []
}
```


For a new composition, enter intentionally chosen values. The example's 120 BPM and 4/4 are not silent repair defaults for someone else's invalid input. In particular, do not turn an absent key into C major.

An authoring sequence is: supply title and intended metadata; place sections; create harmony annotations and performance tracks separately; add lyrics and shared editing relationships as needed; verify identity/time/reference consistency; save. Unused required arrays may remain empty.

### 3. Read keys, scales and genres from their own authorities

The song portion of sample 02 follows. This is an illustrative **JSON fragment**, not a complete standalone file.

```json
{
  "song": {
    "title": "Standard E minor",
    "key": {
      "state": "tonal",
      "tonic": {
        "step": "E",
        "alter": 0
      },
      "mode": "minor"
    },
    "genres": [
      {
        "id": "genre-trance",
        "name": "Trance"
      }
    ],
    "primaryMelodyTrackId": "lead"
  }
}
```


The initial key is song.key, modulation is timeline.keyChanges, a default scale is song.scale, and timed/targeted scale context is harmony.scales. These locations are not interchangeable. E minor does not automatically insert a natural-minor scale, and an existing scale does not establish the global key by inference.

At position t, choose the last key change at or before t; otherwise use song.key; otherwise display unspecified. Do not add an at:0 key change. Returning modulation requires an explicit event. Borrowed chords or chord-scale substitutions are not automatic modulation.

Genres and moods are open authored metadata. Generator genres, moods and groove belong in generation.intent and do not overwrite song metadata. Preserve multiple tags, original text, IDs and order. Unknown names do not become Pop. Key modes are also open strings rather than a fixed major/minor selector.

Player “Original” is the loaded document baseline. Preview or print transposition does not mutate it. Committed transpose is a separate atomic edit of affected pitches, harmony, key, scales and relationships. Drum slots and drum mappings do not transpose.

### 4. Store structure, timing and performance safely

PPQ is integer ticks per quarter note and is unchanged by meter. Clip start is absolute; note start is clip-local; note duration is a gate. This track fragment from sample 08 includes a local pickup and a long tail.

```json
{
  "id": "lead",
  "name": "Lead",
  "trackType": "melodic",
  "role": "melody",
  "clips": [
    {
      "id": "lead-clip",
      "name": "Phrase",
      "start": 120,
      "duration": 3600,
      "notes": [
        {
          "id": "note-a",
          "start": -120,
          "duration": 5000,
          "pitch": 64,
          "velocity": 90
        }
      ]
    }
  ]
}
```


Onset equals clip.start+note.start; gateEnd adds duration. Local starts may be negative, but absolute onsets may not. Clip, section and nominal timeline boundaries do not truncate notes. Same-pitch overlaps remain separate identified events.

Nominal timeline.duration and the largest enabled gateEnd are different lengths. BarOrigin locates the first complete bar after a pickup. Preserve mid-bar meter changes rather than rounding them. BeatGroups can describe 7/8 as 2+2+3 without automatically changing accents or note timing.

Chord labels, intervals and voicing are annotations or inputs to an explicit preview/materialization operation. Saved performance is notes. A Player must not silently double-play chord-derived sound over tracks. Voicing preserves pitch order, duplicates and positional null velocities.

### 5. Keep drums, kits and instruments distinct

A pitched note has pitch; a percussion note has soundSlotId; exactly one is present. TrackType is melodic/drum/mixed, separate from pianoRoll/drumGrid display preference. Do not change note target kind from its track name, view or preview instrument.

Sound Slots register logical sound targets, Drum Kits record membership/order, and midiMapping specifies external MIDI numbers. Two IDs with one MIDI key remain distinct. A mixed-track pitched 36 is not a slot mapped to GM36. Sample 32 covers every GM1 number; sample 33 covers shared numbers, unmapped slots, legacy hints and custom boundaries.

The five soundSource kinds are informational. Identifier does not execute a plug-in or restore a preset. Choosing an internal preview does not rewrite Core instruments/slots. Do not silently infer a GM mapping for formal external MIDI export.

### 6. Separate lyrics, display translations and authorship

Lyric documents, phrases and units form one structure; alignment relates units to notes separately. Unit concatenation need not equal the original phrase text. Pronunciation annotates rather than replaces text. Sample 36 demonstrates parallel languages and many-to-many alignment.

Song languages describe the whole work; each lyric document has its own optional language. An absent primaryLyricDocumentId does not select the first document. Primary melody is likewise an explicit track reference.

Localization supplies display translations, not replacement lyric text or changes to mode, role, URI, IDs or pitches. Existing localizedNames/localizedTitles remain valid inherited fields, but overlapping same-language values must agree exactly with current localization.

Contributors identify people/organizations; credits relate an identity to a role. A software developer or data editor is not thereby a composer. Rights statements neither grant nor authenticate rights. Do not invent omitted authors or licenses.

### 7. Use six common editing features as Core

| Core object | Purpose | Never do automatically on load |
|---|---|---|
| relativePhrases | Links between notes and chord/scale positions | Recalculate or overwrite pitch |
| generation | Inputs/outputs/protection/range/intent | Regenerate, transmit prompts or reapply swing |
| presentation | Roles and display colors | Infer sound from a name/color |
| phraseLibrary | Templates, occurrences and mappings | Expand or refresh automatically |
| clipChoices | Combinations of materialized clips | Apply the selection again |
| localization | Original-preserving display translations | Replace original or musical values |

All six have status and dependencies. Current means consistent now, stale means known disagreement, unverified means not checked. These are neither maturity labels nor quality judgments. After an edit, recalculate a relationship or update its status. Stale does not excuse invalid references in concrete Core performance, lyrics or kits.

Here is the phrase-library fragment from sample 42. Concrete notes separately exist in tracks; noteMap connects the two layers.

```json
{
  "phraseLibrary": {
    "status": "current",
    "dependencies": {
      "scope": "document"
    },
    "templates": [
      {
        "id": "tpl",
        "duration": 960,
        "name": "Two notes",
        "notes": [
          {
            "id": "src-a",
            "start": 0,
            "duration": 240,
            "pitch": 60,
            "velocity": 80
          },
          {
            "id": "src-b",
            "start": 480,
            "duration": 240,
            "pitch": 64,
            "velocity": 90
          }
        ]
      }
    ],
    "instances": [
      {
        "id": "inst",
        "templateId": "tpl",
        "clipId": "c",
        "repeatCount": 2,
        "transpose": 0,
        "velocityMode": "linked",
        "noteMap": [
          {
            "templateNoteId": "src-a",
            "repeatIndex": 0,
            "noteId": "n-0-0"
          },
          {
            "templateNoteId": "src-b",
            "repeatIndex": 0,
            "noteId": "n-0-1"
          },
          {
            "templateNoteId": "src-a",
            "repeatIndex": 1,
            "noteId": "n-1-0"
          },
          {
            "templateNoteId": "src-b",
            "repeatIndex": 1,
            "noteId": "n-1-1"
          }
        ]
      }
    ]
  }
}
```


Only source-note IDs inside each template are local. Templates, instances, choices and other Core IDs are document-global. Linked velocity requires exact presence/value agreement between source and performed note. Independent preserves existing concrete velocities. Absence is interpreted as independent but is not automatically written into the file.

Samples 42 and 43 are independent before/after data descriptions, not logs of an executed editor. Sample 44 describes detachment. Template replacement is atomic across affected instances/notes; surviving occurrences retain note IDs. Detachment does not delete performance or unused templates.

A choice update changes selectedCandidateId and all managed clip.enabled states together. Null means no managed clip selected; an empty clipIds candidate represents silence. Parent track mute is independent. Sharing clips within one group is allowed, but separate groups must have disjoint managed sets. See samples 14 and 45.

### 8. Device hand-off and merging

A useful workflow has Composer/Chord Arranger author structure and harmony, Song Writer and Drum Arranger author explicitly selected content, Editor merge approved differences, and Player read authoritative Core. This is not exclusive ownership by a named application. It is a contract separating selected targets from shared metadata.

Merging notes does not authorize replacing the master's key, tempo, meter, sections, genres or lyrics. Compare and approve those separately. Track names and array positions do not establish identity. Equal ID strings from independent documents may collide.

Document id/revisionId/parents describe lineage, not authentication or automatic merge correctness. Without a base, do not claim safe three-way merging. Compare time as exact tick/ppq rational values and convert every time field together. If limits or rounding prevent exact conversion, refuse or obtain explicit loss approval.

Validate references, protected targets, relationship status and ownership before an all-or-nothing save. Full contracts are in detailed section 12 and the [device contract](DEVICE_CONTRACT.ja.md).

### 9. Explicit migration from 3.0–3.3

Read old files as their original versions. Changing only the version string is not a migration. Do not silently make old Player metadata authoritative during ordinary import. Migrate only known exact namespace/version contracts, with preview and approval.

Moving old profiles into Core requires a scoped old-ID to new-global-ID map. Update collisions, localization profile targets, dependencies, noteMap and selected candidates together. Old templates lacked velocity; this must not erase existing performed velocities.

Downgrades require path-level loss reporting and approval. Hiding new Core back in private Player extensions is not the standard inverse transformation. The [migration guide](MIGRATION_3_3_TO_3_4.ja.md) provides precise field mappings and conflict rules.

### 10. Sample selection and coverage limits

All 54 small samples and 11 complete demos use root version 3.4.0 and `.ostf`. Samples 01–22 preserve the previously established package; 23–54 add inherited-field coverage, every explicit enum value, boundaries and before/after states.

There are witnesses for all 296 current storage declarations, 119 per-declaration enum values and three const declarations. This is not all values, all strings, all combinations or all device behavior. Stale positive examples intentionally preserve warning states; they do not silently permit malformed Core.

Only samples 17, 49 and 50 use extensions for compatibility-preservation demonstrations. The other 51 samples and all eleven demos require none. Sample 28 is an extreme-duration static boundary example, and 50 demonstrates opaque numeric precision; neither is a recommended playback demo. Sample 49's frozen profiles are unverified; their legacy relationships were not executed or fully semantically certified.

### 11. Static local checks

With Python and the declared dependencies installed, run from the repository root:

```sh
python -m pip install -r requirements.txt
python tools/check_release.py
```

After dependency installation, the checks themselves retrieve no remote schemas or assets. They inspect bundled structures, selected semantic invariants, references, documentation links, witnesses and manifest entries. Installing a documentation checker is not an extension dependency of the musical format.

```sh
python tools/check_package.py
python tools/build_catalogue.py
```

The latter regenerates the reference and coverage files for development. After editing release files, regenerate reports and the manifest before publishing. The checker is for this distribution, not a certified general-purpose validator for every semantic requirement. Device execution, audio, Live save/restore, hardware MIDI and UI behavior are not tested.

### 12. Common mistakes

| Mistake | Correct handling |
|---|---|
| Save an absent key as C major | Preserve absence; label estimates separately |
| Normalize an unknown genre to Pop | Preserve authored name, ID and order |
| Duplicate the initial key at keyChanges[0] | song.key is the only tick-0 authority |
| Generate notes from harmony/templates on load | Saved notes are the performance |
| Cut gates at clip boundaries | Preserve authored gateEnd |
| Infer GM mapping from slot names | Keep unmapped; require explicit output assignment |
| Rerun a seed as the restoration authority | Restore concrete saved notes |
| Translate Japanese content when changing UI language | Separate interface text from authored data |
| Drop unsupported Core when resaving | Preserve it or refuse editing/saving |
| Treat schema success as audio/runtime certification | Separate structure, semantics, editing and runtime |

## Part II — Complete semantic feature rules

The following reproduces all fourteen sections of the bundled English specification translation, with heading levels shifted for this manual. Apply the full structural blocks in the parameter reference as well. The Japanese normative text remains authoritative for translation discrepancies.

### 1. Purpose, scope and independence from extensions

OSTF exchanges song information, structure, harmony, concrete performance, lyrics and portable editing relationships. It is not a replacement for a DAW session or instrument state.

Keys, modulation, global scales, languages, provenance, localization, display colors, relative notes, phrase templates, clip choices and shared generation intent are defined as named, typed Core fields. Reading or preserving this information must not depend on an extension namespace, additional plug-in, external server or another developer implementing an extension.

`extensions` is optional. Every standard feature can be expressed without it. Retain the ability to preserve old or third-party payloads, but do not make them the authority for current information standardized by 3.4. Removing unknown extensions is not required. When an old extension cannot be migrated, preserve the source; do not guess its meaning into new Core fields.

Instrument presets, DSP state, internal generation models and temporary Live window positions belong in the application or Live Set. Common standardized information must not be hidden in an arbitrary `appData` or `settings` JSON object. Future shared information requires a versioned specification with defined types and semantics.

CC, Pitch Bend, Aftertouch, MPE, audio clips, singing engines, executable choke behavior, complete plug-in restoration, continuous tempo curves and complete notation engraving are outside 3.4. Do not claim support or silently discard such information while claiming lossless conversion.

### 2. Serialization, versions and numbers

A file is one UTF-8 JSON object. UTF-8 BOM, duplicate members in one object, lone Unicode surrogates, invalid UTF-8, NaN/Infinity and trailing non-whitespace are forbidden. Core integers must use JSON integer tokens: `1.0`, `1e0` and `true` cannot stand in for `1`. The maximum absolute Core integer is `9007199254740991`; arithmetic results must also remain in range.

A mathematically finite decimal JSON number is not invalid merely because binary64 cannot represent it. An implementation claiming lossless preservation must retain original numeric tokens or equivalent precision. Otherwise it must use read-only mode, refuse saving or explicitly report and obtain approval for loss. Key order and whitespace byte identity are different from semantic preservation.

The ten required root members are `format`, `version`, `ppq`, `song`, `timeline`, `harmony`, `tracks`, `soundSlots`, `lyrics`, and `resources`. `format` is `OSTF`; `version` is `3.4.0`. An empty `extensions`, required through 3.3, may be omitted in 3.4.

Optional root members are `extensions`, `drumKits`, `contributors`, `document`, `relativePhrases`, `generation`, `presentation`, `phraseLibrary`, `clipChoices`, `localization`, and `provenance`. Undefined Core members are forbidden. A schema URL is an identifier, not a requirement to retrieve it on import.

Read 3.0.0, 3.1.0, 3.2.0 and 3.3.0 using their respective schemas and meanings. Loading does not upgrade a file. Identify an unknown future version as unsupported; refuse editing or preserve the untouched original in a limited mode. Do not modify future fields by assuming they mean the same thing as a 3.4 field.

### 3. Time, identity and references

`ppq` is integer ticks per quarter note, from 1 through 960000; 960 is recommended. All tracks and standardized editing information share this value. Meter changes do not change tick units. Core absolute times are nonnegative and gate lengths are positive. A performed note's clip-local start may be negative, but its absolute onset must remain nonnegative. Phrase-source local starts also follow their signed schema definition.

Intervals are half-open: `[start, start + duration)`. A change applies from its `at`. At equal times, process Note Off before Note On, using lexical note-ID order within each group. Display bars/beats, seconds, MIDI numbers and array indexes do not replace time coordinates or IDs.

IDs match `^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$`. Core object IDs are unique across object kinds within a document. This includes templates, instances, choice groups/candidates, role definitions, generation processes, provenance records, global scales and key changes. A source note ID inside a phrase template is the exception: it is local to that template. `document.id` and `revisionId` use a separate document identity space. Do not recursively register IDs from unknown extensions or historical local scopes as current Core IDs.

A typed reference is `{type, id}` and must resolve to the declared kind. Do not substitute a same-named object, a same-string ID of the wrong kind, or an object at the same array position. Moves retain IDs; independent copies receive new IDs. Refuse operations whose references cannot be updated, or update the status of affected standardized editing relationships as specified below.

### 4. Authoritative song information

| Information | Authoritative location | Forbidden shortcut |
|---|---|---|
| Original title, subtitle and description | `song.title`, `subtitle`, `description` | Replacing original text with the UI language |
| Initial key | `song.key` | Inferring from the first chord/scale or silently promoting old metadata |
| Key changes | `timeline.keyChanges` | Transposing notes on import |
| Default scale | `song.scale` | Equating a scale with a key |
| Timed scale contexts | `harmony.scales` | Changing the global key for each local scale |
| Initial tempo/meter | First tempo/meter event at tick 0 | Creating a second authority such as `song.bpm` |
| Genres/moods | `song.genres`, `song.moods` | Replacing unknown labels with a preset |
| Credits | `contributors` and `song.credits` | Treating a developer or data editor as composer |
| Primary melody/lyrics | `primaryMelodyTrackId`, `primaryLyricDocumentId` | Treating absence as “first item” |
| Chord voicing | `harmony.chords[].voicing` | Generating notes or double-playing automatically |
| Performance | `tracks[].clips[].notes` | Reconstructing saved performance by rerunning a generator |

Only `song.title` is required within `song`; the empty string is permitted for an untitled work. Missing optional metadata is a valid unfinished state. Do not replace absence with C major, Pop, English or other guesses. Tempo and meter are exceptions because their maps are required: missing required events make a document invalid rather than eligible for silent repair.

Primary melody and lyric references must resolve to existing tracks/documents. Neither reference produces additional sound or removes other content.

### 5. Keys, modulation and scales

#### 5.1 Key values

`key.state` is `tonal`, `atonal` or `unspecified`. A tonal key requires `tonic` and `mode`; both are forbidden in the other states. `label` is an optional original display annotation. Preserve absence separately from explicit `unspecified`; neither authorizes estimated key metadata. An atonal work must not be displayed as C major.

`tonic` is `{step, alter}`: step A–G and integer alteration −2 through 2. Natural pitch classes are C=0, D=2, E=4, F=5, G=7, A=9, B=11; add alter and normalize modulo 12. Preserve C-sharp versus D-flat spelling.

`mode` is a nonempty authored identifier. The exact commonly recognized identifiers are `major`, `minor`, `dorian`, `phrygian`, `lydian`, `mixolydian`, and `locrian`. Major/minor describe tonal interpretation, not a closed set of permitted notes. Minor does not force natural-minor-only notes. Preserve unknown modes, including labels such as `blues`, without converting them to major/minor. An implementation may preserve/display an unsupported mode without interpreting it.

`label` does not override tonic or mode. Suspected label disagreement may be diagnosed but not silently repaired. Camelot numbers, circle-of-fifths positions and key signatures are derived displays, not additional authorities. Do not falsely present an unsupported mode as an exact major/minor mapping.

#### 5.2 Initial key and changes

The initial key is stored only in `song.key`. A `timeline.keyChanges` entry requires `id`, `at`, and `key`, with optional `label`. `at` must be at least 1, strictly increasing, with no duplicate change time. Do not define a second initial key at tick 0.

At time t, use the last change with `at <= t`; otherwise use `song.key`; otherwise the key is unspecified. Returning to an earlier key requires another explicit change. Borrowed chords and per-chord scales are not automatic evidence of modulation. A change persists until the next one, including across section boundaries. Changes to atonal and unspecified states use the same map.

The map is one shared tonal description, not an automatic synthesis of simultaneous tonalities. Multiple scale contexts may preserve polytonal analysis, but must not be silently compressed into one key.

#### 5.3 Default scale and local contexts

Optional `song.scale` requires `id`, `tonic`, and `intervals`, with optional `label`. Intervals are strictly increasing unique integers 0–11 including 0. Do not construct it automatically from the key mode or shift it automatically following key changes.

Timed scales retain `id`, `start`, `duration`, `tonic`, `intervals`, and optional `label`. Optional 3.4 `targets` is an array of references to sections, tracks, clips, chords or notes. All must exist. The context may apply to any matching target: a track includes its clips/notes; a clip includes its notes; a section contributes its overlapping time range; chord/note targets annotate that object. No target means a general timed context, not track ownership.

Use an explicitly referenced context ID when present. One matching timed context may be offered as a candidate; multiple matches remain multiple candidates. Array order alone must not decide correctness. If no timed context matches, `song.scale`, when present, supplies the default candidate. Application-specific choices are explicit operations and do not delete alternative contexts.

A different tonic or pitch collection between key and scale is not by itself invalid. Analysis does not restrict performed notes. Changing the global key does not automatically rewrite melody, voicing, scales or drums.

#### 5.4 Loaded key, temporary transpose and committed transpose

Player “Original” means the baseline of the loaded document, not necessarily the historical composer's original key. Initial display uses `song.key`; position-aware display uses the effective key. The UI must distinguish them.

Playback transpose, print-only transpose and preview tempo ratios are temporary application state, not current OSTF music metadata. Do not save a temporary transpose to be reapplied on the next import.

Committed transpose is an explicit atomic edit. Update selected pitched notes, chord roots/basses/voicings, keys, scales and their relationships consistently, or mark relationships stale/unverified when they cannot be updated. Do not transpose Sound Slot IDs or drum MIDI mappings. Do not silently clip or wrap out-of-range pitches. Do not hide unsafe or inconsistent label updates. Chord and scale intervals remain invariant under semitone transposition.

Avoid transposing templates and their materialized notes twice. Recalculate links or mark them stale. Provenance may describe earlier keys but never overrides the current key.

### 6. Tempo, meter, sections, duration and pickup bars

`tempoChanges` is nonempty, starts at tick 0 and is strictly increasing. BPM is finite, greater than zero and at most 1000. It always means quarter notes per minute, not dotted-quarter BPM in 6/8. Changes are stepwise. A constant interval lasts `tickDifference * 60 / ppq / bpm` seconds; split at changes to integrate a longer interval.

`meterChanges` also starts at tick 0 and is strictly increasing. Numerator is 1–64; denominator is one of 1,2,4,8,16,32,64. Do not move mid-bar changes to estimated bar lines. Optional positive `beatGroups` are counted in denominator-note units and must sum to the numerator. A 7/8 grouping `[2,2,3]` does not command new accents or note timing.

Sections are sorted by start, with nonoverlapping intervals; gaps and an empty array are allowed. Required fields are `id,name,start,duration`; role is an open string and localizedNames is optional. A display name is not an identity or reliable Verse/Chorus classifier. Unknown roles and sections are preserved. Section boundaries do not cut notes.

Optional `timeline.duration` is a nominal placement length in ticks, including zero. It can preserve intended silence before/after content. It is not a crop instruction. Preserve events and gates beyond it. Distinguish nominal length, content extent and the end of enabled performance. Missing duration is not equivalent to a known computed length. The performance endpoint is the maximum enabled note gate end, or zero if there are no enabled notes.

Optional `barOrigin` locates the first complete bar. When absent, use 0 for bar calculation without inserting it into the file. A positive value must be less than the initial bar length `ppq*4*numerator/denominator`; no meter change may lie strictly between 0 and barOrigin. `[0,barOrigin)` is the pickup display, and barOrigin begins bar 1. Do not introduce negative absolute time.

After barOrigin, accumulate bars under the current meter. A mid-bar change terminates the preceding partial bar and begins the next bar number at the change. A change already on a boundary does not add an empty bar. Keep rational bar lengths when they are fractional ticks; event times remain integers.

### 7. Harmony, voicing and performance are separate

Chords and scales may be empty, are sorted by nondecreasing start and may overlap. A chord requires `id,start,duration` and a nonempty label. Root and intervals must either both exist or both be absent. Bass is optional. Intervals are strictly increasing unique integers 0–35 including 0; do not reduce 14 to 2.

Symbol-only chords are valid. A reader's own label parser is not a portable structured interpretation. Diagnose discrepancies between labels, root/intervals/bass and voicing without rewriting authored values.

`voicing.pitches` is a nonempty ordered multiset of integer pitches 0–127: retain order and duplicates. Optional velocities must have exactly the same length and positional alignment, each element 1–127 or null. Null means unspecified, not zero. If sorting, move pitch and velocity together.

A voicing snapshot has no gate or track. It is not a replacement for performance notes. Chord preview or accompaniment materialization requires an explicit action; do not automatically double it with saved tracks. Voicing velocity and performed-note velocity are different fields.

### 8. Tracks, clips, notes and percussion

A track requires `id,name,clips`. Optional fields are role, instrument, enabled, trackType, preferredView, soundSource, localizedNames and drumKitId. Instrument requires name and may include family/localizedNames. Enabled defaults to true for interpretation. trackType is melodic/drum/mixed: pitched notes, Sound Slot notes, or both respectively. Do not infer drum type for an undeclared empty track. This category is not the DAW's track class.

A clip requires `id,start,duration,notes`, with optional name/enabled/localizedNames. Clip start is absolute and note start is clip-local. Preserve nondecreasing start order, retaining original order at equal starts. `onset = clip.start + note.start`; `gateEnd = onset + duration`. Onset must be nonnegative and both results within the Core integer maximum. Retain pickups, notes beyond a nominal clip boundary, tails crossing clips and same-pitch overlaps.

A note requires `id,start,duration` and exactly one of pitch or soundSlotId. Pitch is 0–127, with 60=C4 and 69=A4. Optional velocity is 1–127; do not fill it when absent. Gate is not instrument release duration, one-shot sample length or notated duration. A note performs only when both its track and clip are enabled. Disabled data is still preserved and validated.

A Sound Slot requires id/name; role, midiNote, midiMapping and localizedNames are optional. The ID names the logical sound target; midiMapping describes external MIDI mapping. gm1 permits keys 35–81, custom permits 0–127. Custom key 36 is not automatically a GM kick. If midiNote and midiMapping coexist, their numbers must agree. Different IDs with equal MIDI numbers stay distinct.

A Drum Kit requires id,name,soundSlotIds, with optional localizedNames. It is ordered membership, not a sound preset. A track's drumKitId must resolve and all stored slot notes in that track must belong to that kit. Slots may be shared across kits.

Sound-source kinds are unassigned, gm1, externalMidi, plugin and hostManaged; identifier restrictions follow the schema. They are informational hints, not executable loading/restoration/routing commands. Choosing preview sounds must not rewrite Core instruments or slots.

Mixed pitched 36 and a slot mapped to GM36 remain different targets. External MIDI may require separate routes or explicit loss approval. Never silently remove same-pitch overlaps, slot identity, precision or unsupported mappings. Do not guess GM numbers for unmapped slots during formal export. Approximate internal preview is not proof of MIDI compatibility.

### 9. Lyrics, languages and primary lyrics

`lyrics` requires four arrays: documents, phrases, units and alignments. All may be empty. A lyric document requires id; title/language are optional. A phrase requires id,documentId,text; a unit requires id,phraseId,text. Phrase and unit may include pronunciation and a paired start/duration. Their timing is absolute, and arithmetic endpoints must remain in range.

Text is original display content; pronunciation is an annotation, not an instruction to segment, transliterate or synthesize. Concatenated units need not equal the phrase string. Alignment unitIds and noteIds are nonempty, unique within each ordered list, and must resolve. Many-to-many relationships are allowed. Alignment does not generate notes.

`song.languages` is song-level metadata; document.language describes that lyric document. They may differ or mix; do not copy between them automatically. An absent language array is unknown; an empty one means no registered language, not an inferred instrumental or English work. BCP 47 notation is recommended; preserve unrecognized original labels. Case-only duplicate entries in song.languages are invalid.

Only an explicit primaryLyricDocumentId selects primary lyrics. Do not combine parallel languages/versions into one document. Translated lyrics are separate documents/alignment, not replacement text through name localization. Moving/deleting notes must update alignment explicitly, report/approve loss or fail. A stale flag cannot excuse an invalid Core alignment.

### 10. Genres, moods, credits, rights and resources

Genres and moods are optional ordered arrays of id,name,externalUri?. Neither uses a fixed dictionary. Order reflects author preference; same names with different IDs are preserved. Do not replace absent, empty or unknown labels with defaults. An absolute externalUri does not authorize fetching or replacing the name; existence of the URI is not conformance validation.

Contributors have id,name,kind?,localizedNames?; credits have id,contributorId,role,label?. Role is the existing open ASCII semantic token. Resolve the contributor ID. Do not equate data-editor, software-developer and composer, or merge people merely because their names match.

`song.rights` contains at least one of notice,licenseUri,rightsHolderIds. Holder IDs are unique references to contributors; licenseUri is an authored absolute URI. Recording a statement neither authenticates nor grants rights. Do not infer missing licenses or authors.

A resource requires id,kind,uri, with optional name/sha256. Kind is audio/midi/text/other. A URI is a reference, not an audio-playback or download command. Resolve relative URIs against the OSTF file only under an explicit user action. Loading must not fetch external resources or execute plug-ins/scripts. An unavailable asset does not invalidate otherwise saved note content.

### 11. Standard editing objects and status

The old shared profiles become named root Core objects without a namespace/version/data envelope:

| Core object | Data | Historical migration source only |
|---|---|---|
| relativePhrases | assignments | org.ostf.relative-phrase.v1 |
| generation | processes | org.ostf.generation-context.v1 |
| presentation | roles, assignments, appearance | org.ostf.appearance.v1 |
| phraseLibrary | templates, instances | org.ostf.phrase-library.v1 |
| clipChoices | groups | org.ostf.clip-choices.v1 |
| localization | entries | org.ostf.localization.v1 |

Each requires status and dependencies. Current means agreement with current Core; stale means known disagreement; unverified means not checked. These are not maturity or execution-success claims. Dependencies is none, document, or objects with nonempty unique typed refs.

Current relationships must resolve and satisfy semantic consistency. Object scope must enumerate all directly referenced Core targets; use document scope when that cannot be done. Moving a parent track/clip or changing enabled state can affect descendants' absolute timing/effective state. Referencing content while claiming scope=none is invalid. Song translations, without a song Ref type, require document scope.

When related Core is edited, recalculate and verify the relationship or mark it stale/unverified. Do not leave unhandled relations current. Status updates alone do not recursively trigger another music edit. Stale/unverified reference and relationship mismatches are retained with warnings, but do not permit wrong types, duplicate IDs or overlapping ownership. The relaxation does not excuse invalid performance/lyric/kit Core references.

Loading never generates, rerolls, applies choices or refreshes templates. Concrete tracks remain the saved performance.

#### 11.1 Relative notes

Assignments contain noteId,basis,contextId,anchorPitch,index,chromaticOffset; no duplicate assignment to a note. Basis is chordTone or scaleDegree; the context resolves to a chord or scale, including song.scale. Anchor pitch class must agree with root/tonic.

`note.pitch = anchorPitch + context.intervals[index - 1] + chromaticOffset`.

Index is one-based within the actual interval array; chromatic offset is −24 through 24 and the result 0–127. Array position is not the same as a symbol's “fifth.” An explicit context relationship is not rejected solely because a pickup note falls outside the context's timed interval.

Stale relationships must not overwrite concrete notes. Automatic voice leading or reharmonization is not defined as a load-time operation.

#### 11.2 Generation records and intent

Each process requires id,generator,inputs,outputs,protectedNoteIds; targetRange/intent are optional. Generator requires nonempty id/version. Inputs contain role,ref,readRange? and may be empty or multiple. Outputs are nonempty typed references; protected IDs are unique.

Intent permits only genreNames,moodNames,groove,prompt,seed. Seed is a string to preserve precision. Intent does not guarantee identical output across engines. Do not execute or transmit prompts on import. No arbitrary vendor/internal parameter dictionary is added to the 3.4 generation object.

Groove may have a name and/or the complete trio unitTicks,longWeight,shortWeight. UnitTicks is one straight subdivision. In a pair of length `2*unitTicks`, an L:S intention places the second onset at `2*unitTicks*L/(L+S)`. Never reapply this to saved notes. Explicit generation needing fractional event ticks must change PPQ exactly or report/approve loss. A groove name alone does not define a portable algorithm.

Generation genres/moods are not song genres/moods. Inputs, targetRange and outputs define scope; section names do not.

Freeze protected notes before an operation. Compare IDs, target kinds, absolute onset, duration, velocity presence/value and combined track/clip enabled state. Do not delete the protection list after an operation to evade protection. PPQ conversions require exact rational comparison or refusal. Actual seconds under changed tempo and sound timbre are separate guarantees from tick protection.

#### 11.3 Presentation and roles

Role definitions have id/name/baseRole?; sectionRoleAssignments maps section IDs to role-definition IDs. Appearance contains roleColors/customRoleColors/objectColors. Colors are #RRGGBB. Object colors have target/color, with no duplicate target.

For sections, priority is own objectColor, assigned custom role color, that role's baseRole color, section.role color, then host default. Tracks/slots use own color, role color, then default. Clips inherit from tracks; notes inherit from clips unless their own color exists. Other objects use own color or default. Names/colors do not define musical roles or sound. Unresolved references must not be redirected by name.

#### 11.4 Reusable phrases and velocity

A template requires id,duration,notes; name is optional. Duration is the repetition period. Source notes have local id/start/duration and pitch XOR soundSlotId, with optional velocity. Source notes are not performed themselves.

An instance requires id,templateId,clipId,repeatCount,transpose,noteMap; velocityMode is optional. Template/instance IDs are globally unique Core IDs. A clip cannot be owned by multiple instances. Each mapping has templateNoteId,repeatIndex,noteId. Every source-note occurrence and every Core note in the owned clip must correspond exactly once.

```
clip.duration = template.duration * repeatCount
note.start = repeatIndex * template.duration + sourceNote.start
note.duration = sourceNote.duration
note.pitch = sourceNote.pitch + instance.transpose       # pitched only
note.soundSlotId = sourceNote.soundSlotId                 # percussion only
```

Repeat index is 0 through repeatCount−1. Duplicate occurrences, shared ownership of a mapped note or clip, out-of-range pitches and arithmetic overflow are forbidden. Preserve pickups/tails. Current consistency can be checked by cardinality and mappings without expanding a huge Cartesian product.

VelocityMode defaults to independent for interpretation. Existing concrete velocities survive explicit template refresh independently; an explicit new materialization may copy initial source velocity. Linked requires exact equality of both presence and value between mapped and source notes. A mode change alone does not silently rewrite performance; present necessary updates as one operation.

Template replacement updates all affected instances, notes and dependencies atomically or fails. Surviving `(repeatIndex,templateNoteId)` pairs retain note IDs. Detaching removes only that instance and preserves the clip/notes. Do not automatically remove unused templates. Infinite repetition and probabilistic expansion on import are outside scope.

#### 11.5 Clip choices

A group requires id,candidates,selectedCandidateId; name is optional. Candidates require id,clipIds, with optional name. At least one candidate is required per group. Clip IDs are unique within a candidate; an empty candidate can represent silence. Selection is a candidate ID from that group or null. Group/candidate IDs are globally unique Core IDs.

Candidates in one group may share clips; separate groups cannot share managed clips. In current state, each managed clip's own enabled value must match membership in the selected candidate; null disables all managed clips. Parent track enabled remains a separate mute.

Changing selection updates the selected ID and all managed clip states atomically. Loading diagnoses disagreement but does not apply selection. Choices combine already materialized performance clips; they are not whole-song scenes including structure, harmony and lyrics.

#### 11.6 Localization

Entries contain target,field,values. Target has kind and, except for song, a global Core ID. There is no old profile selector. Values maps language tags to nonempty translations. Case-only duplicate tags are forbidden. The schema alone does not validate all BCP 47 rules. Preserve original text and fall back to it when translation is absent.

| Target kind | Permitted field |
|---|---|
| song | title, subtitle, description, key.label, rights.notice |
| alternateTitle | title |
| contributor, section, track, clip, soundSlot, drumKit, resource, phraseTemplate, clipCandidate, clipChoiceGroup, roleDefinition, genre, mood | name |
| track, additionally | instrument.name |
| credit | label |
| lyricDocument | title |
| keyChange | label, key.label |
| scale | label |

Current entries require the source field to exist. Duplicate target/field/language combinations are forbidden. Overlapping old localizedNames/localizedTitles and current translations must have exactly equal strings. New authoring should consolidate into localization, but preserve inherited dictionaries. Localization must not change lyric text, pitch spelling, chord values, IDs, URIs, role or mode meaning.

### 12. Document identity, provenance and merging

Optional document requires id/revisionId; parents/createdBy/modifiedBy are optional. ID identifies one working lineage; revisionId is a fresh opaque identity whenever semantic content changes. A no-change save may retain it. Independent copies use a new document ID; derivations may retain source pairs in parents. Branches with one ID have distinct revisions. A new save after edits or Undo receives a new revision, not a reused historical pair.

Parents require documentId/revisionId and optionally sha256. No self-parent pair, repeated pair or conflicting hashes for one pair is allowed. These declarations do not prove tamper resistance, authentication or safe automatic merging. A full graph can only be checked when relevant history is available.

Provenance records require id/action; optional fields are description,tool,sources,semitones,beforeKey,afterKey. Actions are create/import/conversion/edit/transpose/merge/generation/other. Semitones is allowed only for transpose. History is non-executable and self-reported. Historical document identities do not resolve in the current Core registry; resourceId does. Hashes describe exact input bytes, never a self-referential current output hash.

Merge contracts:

1. Default to explicitly selected owned targets. A drum tool edits selected drum/mixed material; a melody tool edits the explicitly selected melody. Names/array positions do not establish ownership. Do not silently reassign an absent primaryMelodyTrackId.
2. Compare shared structure, tempo, meter, key, scales, genres, credits and lyrics separately. A note merge does not authorize overwriting them. Without a base, do not claim safe three-way merging.
3. Do not trust same IDs across independent documents. Create collision mappings and update all known references together. Do not rewrite unknown internal references by guessing. Refuse a merge that cannot safely preserve required references.
4. Reconcile PPQ using exact rational `tick/ppq`. Choose an exact common PPQ within 960000 and integer limits. Otherwise refuse or obtain explicit loss approval. Convert all time fields, ranges, phrase periods and groove units, not just notes.
5. Separate movement from tempo/key/meter edits. Show which objects move, remain or change boundary before atomically committing.
6. Save atomically. Check references, protection and dependencies before replacing the authority or writing a separate result. A writer unable to preserve unsupported Core must refuse that edit.

Preserving unsupported data is distinct from implementing every generation/editing operation. Lack of an operation does not authorize deleting its data.

### 13. Legacy and private-extension migration boundaries

Do not treat a 3.3-or-earlier document as 3.4 directly. Keep original-version reading, explicit migration preview and 3.4 output as separate steps.

In 3.4, Core takes priority. Warn on disagreement with old extensions. An absent Core field does not authorize silently promoting old Player metadata. Display retained legacy information as unmigrated. Preserve unknown payloads and mark their status stale/unverified if a dependent edit affects them.

Interpret a known old extension only under its exact namespace/version/structure. The 3.4 schema includes frozen old definitions; do not add new source-note velocity or current-Core reference kinds to an unchanged old extension version. Unknown extension versions are not validated as known versions.

Downgrading may be lossy. Report removed fields, IDs, references, translations and relationships by path, and require approval. Pushing new Core into Player-specific extensions is not the standard inverse migration. See the [migration rules](MIGRATION_3_3_TO_3_4.ja.md).

### 14. Conformance and release boundary

Structure is governed by the schema; semantics by identity/reference/time/relationship rules; editing conformance by preservation, non-destructive operations and loss reporting. A reader can declare that it cannot display a feature. A writer that cannot preserve it must refuse saving. Sound identity, generation quality and successful DAW connections are different from format conformance.

Bundled checks are static documentation/data checks: schema, references, examples, field witnesses and preservation comparisons. They are not execution tests of Player, Composer, Editor, Song Writer, Drum Arranger, Live, MIDI hardware, UI or audio quality.

See [release readiness](../RELEASE_READINESS.ja.md). The specification supplies authoritative storage and preservation contracts for the identified common information; it does not guarantee every future requirement or defect-free existing devices.
