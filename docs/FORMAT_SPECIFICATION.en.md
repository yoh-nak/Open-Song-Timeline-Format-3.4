# OSTF 3.4.0 — Format Specification

Specification date: 2026-10-31. Format: Open Song Timeline Format. File extension: `.ostf`.

This is an English translation of the supplied [Japanese normative specification](FORMAT_SPECIFICATION.ja.md), organized in the same sections. The Japanese text is the semantic authority if translation wording differs. The [3.4 JSON Schema](../schema/ostf-3.4.0.schema.json) is the structural authority. Conformance requires both. The 3.3 specification and schemas are not retroactively redefined. The new 3.4 fields were not already fields of 3.3.

“Required” and “must not” express conformance requirements; recommendations permit a reasoned alternative. Preserve the distinction between absence and an explicitly empty value. A schema `default` specifies an interpretation, not a command to add a member when loading.

## 1. Purpose, scope and independence from extensions

OSTF exchanges song information, structure, harmony, concrete performance, lyrics and portable editing relationships. It is not a replacement for a DAW session or instrument state.

Keys, modulation, global scales, languages, provenance, localization, display colors, relative notes, phrase templates, clip choices and shared generation intent are defined as named, typed Core fields. Reading or preserving this information must not depend on an extension namespace, additional plug-in, external server or another developer implementing an extension.

`extensions` is optional. Every standard feature can be expressed without it. Retain the ability to preserve old or third-party payloads, but do not make them the authority for current information standardized by 3.4. Removing unknown extensions is not required. When an old extension cannot be migrated, preserve the source; do not guess its meaning into new Core fields.

Instrument presets, DSP state, internal generation models and temporary Live window positions belong in the application or Live Set. Common standardized information must not be hidden in an arbitrary `appData` or `settings` JSON object. Future shared information requires a versioned specification with defined types and semantics.

CC, Pitch Bend, Aftertouch, MPE, audio clips, singing engines, executable choke behavior, complete plug-in restoration, continuous tempo curves and complete notation engraving are outside 3.4. Do not claim support or silently discard such information while claiming lossless conversion.

## 2. Serialization, versions and numbers

A file is one UTF-8 JSON object. UTF-8 BOM, duplicate members in one object, lone Unicode surrogates, invalid UTF-8, NaN/Infinity and trailing non-whitespace are forbidden. Core integers must use JSON integer tokens: `1.0`, `1e0` and `true` cannot stand in for `1`. The maximum absolute Core integer is `9007199254740991`; arithmetic results must also remain in range.

A mathematically finite decimal JSON number is not invalid merely because binary64 cannot represent it. An implementation claiming lossless preservation must retain original numeric tokens or equivalent precision. Otherwise it must use read-only mode, refuse saving or explicitly report and obtain approval for loss. Key order and whitespace byte identity are different from semantic preservation.

The ten required root members are `format`, `version`, `ppq`, `song`, `timeline`, `harmony`, `tracks`, `soundSlots`, `lyrics`, and `resources`. `format` is `OSTF`; `version` is `3.4.0`. An empty `extensions`, required through 3.3, may be omitted in 3.4.

Optional root members are `extensions`, `drumKits`, `contributors`, `document`, `relativePhrases`, `generation`, `presentation`, `phraseLibrary`, `clipChoices`, `localization`, and `provenance`. Undefined Core members are forbidden. A schema URL is an identifier, not a requirement to retrieve it on import.

Read 3.0.0, 3.1.0, 3.2.0 and 3.3.0 using their respective schemas and meanings. Loading does not upgrade a file. Identify an unknown future version as unsupported; refuse editing or preserve the untouched original in a limited mode. Do not modify future fields by assuming they mean the same thing as a 3.4 field.

## 3. Time, identity and references

`ppq` is integer ticks per quarter note, from 1 through 960000; 960 is recommended. All tracks and standardized editing information share this value. Meter changes do not change tick units. Core absolute times are nonnegative and gate lengths are positive. A performed note's clip-local start may be negative, but its absolute onset must remain nonnegative. Phrase-source local starts also follow their signed schema definition.

Intervals are half-open: `[start, start + duration)`. A change applies from its `at`. At equal times, process Note Off before Note On, using lexical note-ID order within each group. Display bars/beats, seconds, MIDI numbers and array indexes do not replace time coordinates or IDs.

IDs match `^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$`. Core object IDs are unique across object kinds within a document. This includes templates, instances, choice groups/candidates, role definitions, generation processes, provenance records, global scales and key changes. A source note ID inside a phrase template is the exception: it is local to that template. `document.id` and `revisionId` use a separate document identity space. Do not recursively register IDs from unknown extensions or historical local scopes as current Core IDs.

A typed reference is `{type, id}` and must resolve to the declared kind. Do not substitute a same-named object, a same-string ID of the wrong kind, or an object at the same array position. Moves retain IDs; independent copies receive new IDs. Refuse operations whose references cannot be updated, or update the status of affected standardized editing relationships as specified below.

## 4. Authoritative song information

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

## 5. Keys, modulation and scales

### 5.1 Key values

`key.state` is `tonal`, `atonal` or `unspecified`. A tonal key requires `tonic` and `mode`; both are forbidden in the other states. `label` is an optional original display annotation. Preserve absence separately from explicit `unspecified`; neither authorizes estimated key metadata. An atonal work must not be displayed as C major.

`tonic` is `{step, alter}`: step A–G and integer alteration −2 through 2. Natural pitch classes are C=0, D=2, E=4, F=5, G=7, A=9, B=11; add alter and normalize modulo 12. Preserve C-sharp versus D-flat spelling.

`mode` is a nonempty authored identifier. The exact commonly recognized identifiers are `major`, `minor`, `dorian`, `phrygian`, `lydian`, `mixolydian`, and `locrian`. Major/minor describe tonal interpretation, not a closed set of permitted notes. Minor does not force natural-minor-only notes. Preserve unknown modes, including labels such as `blues`, without converting them to major/minor. An implementation may preserve/display an unsupported mode without interpreting it.

`label` does not override tonic or mode. Suspected label disagreement may be diagnosed but not silently repaired. Camelot numbers, circle-of-fifths positions and key signatures are derived displays, not additional authorities. Do not falsely present an unsupported mode as an exact major/minor mapping.

### 5.2 Initial key and changes

The initial key is stored only in `song.key`. A `timeline.keyChanges` entry requires `id`, `at`, and `key`, with optional `label`. `at` must be at least 1, strictly increasing, with no duplicate change time. Do not define a second initial key at tick 0.

At time t, use the last change with `at <= t`; otherwise use `song.key`; otherwise the key is unspecified. Returning to an earlier key requires another explicit change. Borrowed chords and per-chord scales are not automatic evidence of modulation. A change persists until the next one, including across section boundaries. Changes to atonal and unspecified states use the same map.

The map is one shared tonal description, not an automatic synthesis of simultaneous tonalities. Multiple scale contexts may preserve polytonal analysis, but must not be silently compressed into one key.

### 5.3 Default scale and local contexts

Optional `song.scale` requires `id`, `tonic`, and `intervals`, with optional `label`. Intervals are strictly increasing unique integers 0–11 including 0. Do not construct it automatically from the key mode or shift it automatically following key changes.

Timed scales retain `id`, `start`, `duration`, `tonic`, `intervals`, and optional `label`. Optional 3.4 `targets` is an array of references to sections, tracks, clips, chords or notes. All must exist. The context may apply to any matching target: a track includes its clips/notes; a clip includes its notes; a section contributes its overlapping time range; chord/note targets annotate that object. No target means a general timed context, not track ownership.

Use an explicitly referenced context ID when present. One matching timed context may be offered as a candidate; multiple matches remain multiple candidates. Array order alone must not decide correctness. If no timed context matches, `song.scale`, when present, supplies the default candidate. Application-specific choices are explicit operations and do not delete alternative contexts.

A different tonic or pitch collection between key and scale is not by itself invalid. Analysis does not restrict performed notes. Changing the global key does not automatically rewrite melody, voicing, scales or drums.

### 5.4 Loaded key, temporary transpose and committed transpose

Player “Original” means the baseline of the loaded document, not necessarily the historical composer's original key. Initial display uses `song.key`; position-aware display uses the effective key. The UI must distinguish them.

Playback transpose, print-only transpose and preview tempo ratios are temporary application state, not current OSTF music metadata. Do not save a temporary transpose to be reapplied on the next import.

Committed transpose is an explicit atomic edit. Update selected pitched notes, chord roots/basses/voicings, keys, scales and their relationships consistently, or mark relationships stale/unverified when they cannot be updated. Do not transpose Sound Slot IDs or drum MIDI mappings. Do not silently clip or wrap out-of-range pitches. Do not hide unsafe or inconsistent label updates. Chord and scale intervals remain invariant under semitone transposition.

Avoid transposing templates and their materialized notes twice. Recalculate links or mark them stale. Provenance may describe earlier keys but never overrides the current key.

## 6. Tempo, meter, sections, duration and pickup bars

`tempoChanges` is nonempty, starts at tick 0 and is strictly increasing. BPM is finite, greater than zero and at most 1000. It always means quarter notes per minute, not dotted-quarter BPM in 6/8. Changes are stepwise. A constant interval lasts `tickDifference * 60 / ppq / bpm` seconds; split at changes to integrate a longer interval.

`meterChanges` also starts at tick 0 and is strictly increasing. Numerator is 1–64; denominator is one of 1,2,4,8,16,32,64. Do not move mid-bar changes to estimated bar lines. Optional positive `beatGroups` are counted in denominator-note units and must sum to the numerator. A 7/8 grouping `[2,2,3]` does not command new accents or note timing.

Sections are sorted by start, with nonoverlapping intervals; gaps and an empty array are allowed. Required fields are `id,name,start,duration`; role is an open string and localizedNames is optional. A display name is not an identity or reliable Verse/Chorus classifier. Unknown roles and sections are preserved. Section boundaries do not cut notes.

Optional `timeline.duration` is a nominal placement length in ticks, including zero. It can preserve intended silence before/after content. It is not a crop instruction. Preserve events and gates beyond it. Distinguish nominal length, content extent and the end of enabled performance. Missing duration is not equivalent to a known computed length. The performance endpoint is the maximum enabled note gate end, or zero if there are no enabled notes.

Optional `barOrigin` locates the first complete bar. When absent, use 0 for bar calculation without inserting it into the file. A positive value must be less than the initial bar length `ppq*4*numerator/denominator`; no meter change may lie strictly between 0 and barOrigin. `[0,barOrigin)` is the pickup display, and barOrigin begins bar 1. Do not introduce negative absolute time.

After barOrigin, accumulate bars under the current meter. A mid-bar change terminates the preceding partial bar and begins the next bar number at the change. A change already on a boundary does not add an empty bar. Keep rational bar lengths when they are fractional ticks; event times remain integers.

## 7. Harmony, voicing and performance are separate

Chords and scales may be empty, are sorted by nondecreasing start and may overlap. A chord requires `id,start,duration` and a nonempty label. Root and intervals must either both exist or both be absent. Bass is optional. Intervals are strictly increasing unique integers 0–35 including 0; do not reduce 14 to 2.

Symbol-only chords are valid. A reader's own label parser is not a portable structured interpretation. Diagnose discrepancies between labels, root/intervals/bass and voicing without rewriting authored values.

`voicing.pitches` is a nonempty ordered multiset of integer pitches 0–127: retain order and duplicates. Optional velocities must have exactly the same length and positional alignment, each element 1–127 or null. Null means unspecified, not zero. If sorting, move pitch and velocity together.

A voicing snapshot has no gate or track. It is not a replacement for performance notes. Chord preview or accompaniment materialization requires an explicit action; do not automatically double it with saved tracks. Voicing velocity and performed-note velocity are different fields.

## 8. Tracks, clips, notes and percussion

A track requires `id,name,clips`. Optional fields are role, instrument, enabled, trackType, preferredView, soundSource, localizedNames and drumKitId. Instrument requires name and may include family/localizedNames. Enabled defaults to true for interpretation. trackType is melodic/drum/mixed: pitched notes, Sound Slot notes, or both respectively. Do not infer drum type for an undeclared empty track. This category is not the DAW's track class.

A clip requires `id,start,duration,notes`, with optional name/enabled/localizedNames. Clip start is absolute and note start is clip-local. Preserve nondecreasing start order, retaining original order at equal starts. `onset = clip.start + note.start`; `gateEnd = onset + duration`. Onset must be nonnegative and both results within the Core integer maximum. Retain pickups, notes beyond a nominal clip boundary, tails crossing clips and same-pitch overlaps.

A note requires `id,start,duration` and exactly one of pitch or soundSlotId. Pitch is 0–127, with 60=C4 and 69=A4. Optional velocity is 1–127; do not fill it when absent. Gate is not instrument release duration, one-shot sample length or notated duration. A note performs only when both its track and clip are enabled. Disabled data is still preserved and validated.

A Sound Slot requires id/name; role, midiNote, midiMapping and localizedNames are optional. The ID names the logical sound target; midiMapping describes external MIDI mapping. gm1 permits keys 35–81, custom permits 0–127. Custom key 36 is not automatically a GM kick. If midiNote and midiMapping coexist, their numbers must agree. Different IDs with equal MIDI numbers stay distinct.

A Drum Kit requires id,name,soundSlotIds, with optional localizedNames. It is ordered membership, not a sound preset. A track's drumKitId must resolve and all stored slot notes in that track must belong to that kit. Slots may be shared across kits.

Sound-source kinds are unassigned, gm1, externalMidi, plugin and hostManaged; identifier restrictions follow the schema. They are informational hints, not executable loading/restoration/routing commands. Choosing preview sounds must not rewrite Core instruments or slots.

Mixed pitched 36 and a slot mapped to GM36 remain different targets. External MIDI may require separate routes or explicit loss approval. Never silently remove same-pitch overlaps, slot identity, precision or unsupported mappings. Do not guess GM numbers for unmapped slots during formal export. Approximate internal preview is not proof of MIDI compatibility.

## 9. Lyrics, languages and primary lyrics

`lyrics` requires four arrays: documents, phrases, units and alignments. All may be empty. A lyric document requires id; title/language are optional. A phrase requires id,documentId,text; a unit requires id,phraseId,text. Phrase and unit may include pronunciation and a paired start/duration. Their timing is absolute, and arithmetic endpoints must remain in range.

Text is original display content; pronunciation is an annotation, not an instruction to segment, transliterate or synthesize. Concatenated units need not equal the phrase string. Alignment unitIds and noteIds are nonempty, unique within each ordered list, and must resolve. Many-to-many relationships are allowed. Alignment does not generate notes.

`song.languages` is song-level metadata; document.language describes that lyric document. They may differ or mix; do not copy between them automatically. An absent language array is unknown; an empty one means no registered language, not an inferred instrumental or English work. BCP 47 notation is recommended; preserve unrecognized original labels. Case-only duplicate entries in song.languages are invalid.

Only an explicit primaryLyricDocumentId selects primary lyrics. Do not combine parallel languages/versions into one document. Translated lyrics are separate documents/alignment, not replacement text through name localization. Moving/deleting notes must update alignment explicitly, report/approve loss or fail. A stale flag cannot excuse an invalid Core alignment.

## 10. Genres, moods, credits, rights and resources

Genres and moods are optional ordered arrays of id,name,externalUri?. Neither uses a fixed dictionary. Order reflects author preference; same names with different IDs are preserved. Do not replace absent, empty or unknown labels with defaults. An absolute externalUri does not authorize fetching or replacing the name; existence of the URI is not conformance validation.

Contributors have id,name,kind?,localizedNames?; credits have id,contributorId,role,label?. Role is the existing open ASCII semantic token. Resolve the contributor ID. Do not equate data-editor, software-developer and composer, or merge people merely because their names match.

`song.rights` contains at least one of notice,licenseUri,rightsHolderIds. Holder IDs are unique references to contributors; licenseUri is an authored absolute URI. Recording a statement neither authenticates nor grants rights. Do not infer missing licenses or authors.

A resource requires id,kind,uri, with optional name/sha256. Kind is audio/midi/text/other. A URI is a reference, not an audio-playback or download command. Resolve relative URIs against the OSTF file only under an explicit user action. Loading must not fetch external resources or execute plug-ins/scripts. An unavailable asset does not invalidate otherwise saved note content.

## 11. Standard editing objects and status

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

### 11.1 Relative notes

Assignments contain noteId,basis,contextId,anchorPitch,index,chromaticOffset; no duplicate assignment to a note. Basis is chordTone or scaleDegree; the context resolves to a chord or scale, including song.scale. Anchor pitch class must agree with root/tonic.

`note.pitch = anchorPitch + context.intervals[index - 1] + chromaticOffset`.

Index is one-based within the actual interval array; chromatic offset is −24 through 24 and the result 0–127. Array position is not the same as a symbol's “fifth.” An explicit context relationship is not rejected solely because a pickup note falls outside the context's timed interval.

Stale relationships must not overwrite concrete notes. Automatic voice leading or reharmonization is not defined as a load-time operation.

### 11.2 Generation records and intent

Each process requires id,generator,inputs,outputs,protectedNoteIds; targetRange/intent are optional. Generator requires nonempty id/version. Inputs contain role,ref,readRange? and may be empty or multiple. Outputs are nonempty typed references; protected IDs are unique.

Intent permits only genreNames,moodNames,groove,prompt,seed. Seed is a string to preserve precision. Intent does not guarantee identical output across engines. Do not execute or transmit prompts on import. No arbitrary vendor/internal parameter dictionary is added to the 3.4 generation object.

Groove may have a name and/or the complete trio unitTicks,longWeight,shortWeight. UnitTicks is one straight subdivision. In a pair of length `2*unitTicks`, an L:S intention places the second onset at `2*unitTicks*L/(L+S)`. Never reapply this to saved notes. Explicit generation needing fractional event ticks must change PPQ exactly or report/approve loss. A groove name alone does not define a portable algorithm.

Generation genres/moods are not song genres/moods. Inputs, targetRange and outputs define scope; section names do not.

Freeze protected notes before an operation. Compare IDs, target kinds, absolute onset, duration, velocity presence/value and combined track/clip enabled state. Do not delete the protection list after an operation to evade protection. PPQ conversions require exact rational comparison or refusal. Actual seconds under changed tempo and sound timbre are separate guarantees from tick protection.

### 11.3 Presentation and roles

Role definitions have id/name/baseRole?; sectionRoleAssignments maps section IDs to role-definition IDs. Appearance contains roleColors/customRoleColors/objectColors. Colors are #RRGGBB. Object colors have target/color, with no duplicate target.

For sections, priority is own objectColor, assigned custom role color, that role's baseRole color, section.role color, then host default. Tracks/slots use own color, role color, then default. Clips inherit from tracks; notes inherit from clips unless their own color exists. Other objects use own color or default. Names/colors do not define musical roles or sound. Unresolved references must not be redirected by name.

### 11.4 Reusable phrases and velocity

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

### 11.5 Clip choices

A group requires id,candidates,selectedCandidateId; name is optional. Candidates require id,clipIds, with optional name. At least one candidate is required per group. Clip IDs are unique within a candidate; an empty candidate can represent silence. Selection is a candidate ID from that group or null. Group/candidate IDs are globally unique Core IDs.

Candidates in one group may share clips; separate groups cannot share managed clips. In current state, each managed clip's own enabled value must match membership in the selected candidate; null disables all managed clips. Parent track enabled remains a separate mute.

Changing selection updates the selected ID and all managed clip states atomically. Loading diagnoses disagreement but does not apply selection. Choices combine already materialized performance clips; they are not whole-song scenes including structure, harmony and lyrics.

### 11.6 Localization

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

## 12. Document identity, provenance and merging

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

## 13. Legacy and private-extension migration boundaries

Do not treat a 3.3-or-earlier document as 3.4 directly. Keep original-version reading, explicit migration preview and 3.4 output as separate steps.

In 3.4, Core takes priority. Warn on disagreement with old extensions. An absent Core field does not authorize silently promoting old Player metadata. Display retained legacy information as unmigrated. Preserve unknown payloads and mark their status stale/unverified if a dependent edit affects them.

Interpret a known old extension only under its exact namespace/version/structure. The 3.4 schema includes frozen old definitions; do not add new source-note velocity or current-Core reference kinds to an unchanged old extension version. Unknown extension versions are not validated as known versions.

Downgrading may be lossy. Report removed fields, IDs, references, translations and relationships by path, and require approval. Pushing new Core into Player-specific extensions is not the standard inverse migration. See the [migration rules](MIGRATION_3_3_TO_3_4.ja.md).

## 14. Conformance and release boundary

Structure is governed by the schema; semantics by identity/reference/time/relationship rules; editing conformance by preservation, non-destructive operations and loss reporting. A reader can declare that it cannot display a feature. A writer that cannot preserve it must refuse saving. Sound identity, generation quality and successful DAW connections are different from format conformance.

Bundled checks are static documentation/data checks: schema, references, examples, field witnesses and preservation comparisons. They are not execution tests of Player, Composer, Editor, Song Writer, Drum Arranger, Live, MIDI hardware, UI or audio quality.

See [release readiness](../RELEASE_READINESS.ja.md). The specification supplies authoritative storage and preservation contracts for the identified common information; it does not guarantee every future requirement or defect-free existing devices.
