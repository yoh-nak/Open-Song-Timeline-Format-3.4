# OSTF 3.4.0 — Sample Index / サンプル索引

**54 independent `.ostf` files; every root version is `3.4.0`.** All are complete documents, not fragments. The [eleven complete demo songs](../demos/README.md) are catalogued separately.

**54個すべて独立した完全な`.ostf`です。** 機能ごとに読むための小さな記述例であり、Player/DAWでの動作確認済みという意味ではありません。

## Important boundaries / 境界と警告

Only 17, 49 and 50 contain `extensions`, solely to demonstrate legacy/unknown preservation. All other samples and every demo describe standard information without extensions. 17 and 18/41 intentionally demonstrate diagnostic or stale states. 49 retains unverified frozen profiles; the checker validates their structure but does not execute or fully certify legacy profile relationships.

17/49/50のみ互換保持の例として拡張を含みます。28の最大時間、50の精度境界は静的検査用で、再生用の推奨曲ではありません。42〜44は編集前後の記述例で、実行ログではありません。架空の素材URIやハッシュを含む例は外部素材を必要とせず、実在や権利を表明しません。

[All-field and enum coverage](../docs/COVERAGE.md) · [Japanese manual](../docs/COMPLETE_MANUAL.ja.md) · [English manual](../docs/COMPLETE_MANUAL.en.md)

## Catalogue / 一覧

| No. | File | 内容 / Purpose |
|---|---|---|
| 01 | [01_empty_without_extensions.ostf](01_empty_without_extensions.ostf) | 拡張を一切持たない最小の空曲。キー未指定を保持。<br>An empty valid song without extensions; preserve an unspecified key. |
| 02 | [02_trance_metadata_core_only.ostf](02_trance_metadata_core_only.ostf) | E minor / Tranceの情報を正式Coreだけで保存。<br>E minor / Trance metadata in formal Core only. |
| 03 | [03_modulation_atonal_and_unspecified.ostf](03_modulation_atonal_and_unspecified.ostf) | 転調、無調、明示未指定、調性への復帰。<br>Modulation through tonal, atonal and explicitly unspecified states. |
| 04 | [04_scale_without_key.ostf](04_scale_without_key.ostf) | スケールが存在してもキーを自動設定しない。<br>A scale does not automatically establish a song key. |
| 05 | [05_custom_mode_and_scale.ostf](05_custom_mode_and_scale.ostf) | 未知のモードと構造化された音階。<br>An open custom mode and structured pitch collection. |
| 06 | [06_overlapping_scale_contexts.ostf](06_overlapping_scale_contexts.ostf) | 重なったスケール文脈と対象ID。<br>Overlapping targeted scale contexts; no first-entry-wins rule. |
| 07 | [07_pickup_additive_midbar_meter.ostf](07_pickup_additive_midbar_meter.ostf) | 弱起、7/8の加算グループ、小節途中の拍子変更。<br>Pickup bar, additive 7/8 groups and a mid-bar meter change. |
| 08 | [08_note_pickup_and_long_tail.ostf](08_note_pickup_and_long_tail.ostf) | ローカルな負の開始と、名目曲長を超えるゲート。<br>Negative local onset and a gate beyond nominal song length. |
| 09 | [09_languages_genres_moods_credits.ostf](09_languages_genres_moods_credits.ostf) | 言語、未知ジャンル、Mood、クレジット、権利、翻訳。<br>Languages, open genres/moods, credits, rights and localization. |
| 10 | [10_primary_lyrics_and_alignment.ostf](10_primary_lyrics_and_alignment.ostf) | 主歌詞の明示と歌詞ノート割当。<br>Explicit primary lyrics and lyric-to-note alignment. |
| 11 | [11_presentation_no_extension.ostf](11_presentation_no_extension.ostf) | 正式Coreの色・構成役割。<br>Native presentation colors and roles without an extension. |
| 12 | [12_phrase_velocity_linked.ostf](12_phrase_velocity_linked.ostf) | 原型と実ノートのVelocityを連動。<br>Template and performed-note velocities explicitly linked. |
| 13 | [13_phrase_velocity_independent.ostf](13_phrase_velocity_independent.ostf) | 実ノートのVelocityを原型から独立保持。<br>Concrete velocity preserved independently from template velocity. |
| 14 | [14_clip_choices_no_selection.ostf](14_clip_choices_no_selection.ostf) | 無選択のクリップ候補。読み込み時に適用しない。<br>No selected clip candidate; managed clips disabled. |
| 15 | [15_relative_and_generation_intent.ostf](15_relative_and_generation_intent.ostf) | 相対音、生成意図、Grooveを再生成なしで記録。<br>Relative notes and typed generation intent, not executable on import. |
| 16 | [16_identity_provenance_and_transpose.ostf](16_identity_provenance_and_transpose.ostf) | 文書系列、親版、出典、確定移調の履歴。<br>Document/revision identity and non-executable transpose provenance. |
| 17 | [17_legacy_conflict_core_wins.ostf](17_legacy_conflict_core_wins.ostf) | 旧拡張とCoreが競合してもCoreが正本。未知拡張を保全。<br>Intentional Core/legacy conflict and opaque unknown-data preservation. |
| 18 | [18_stale_missing_relation.ostf](18_stale_missing_relation.ostf) | staleな関係の欠落参照は警告として保全。<br>An intentionally stale relationship with an unresolved reference. |
| 19 | [19_mixed_identity_no_drum_transpose.ostf](19_mixed_identity_no_drum_transpose.ostf) | MixedのpitchとSlot、同一MIDI番号の別Slotを区別。<br>Mixed pitched and slot identity; drum mapping is not transposed. |
| 20 | [20_voicing_snapshot_not_double_playback.ostf](20_voicing_snapshot_not_double_playback.ostf) | ボイシングのスナップショットを二重演奏しない。<br>Voicing snapshots do not automatically produce a second performance. |
| 21 | [21_native_drum_template_velocity.ostf](21_native_drum_template_velocity.ostf) | Velocityを持つドラム原型とSlot参照。<br>Native drum template and velocity mapping. |
| 22 | [22_explicit_dependency_scopes.ostf](22_explicit_dependency_scopes.ostf) | objects/none依存範囲を明示した標準Coreモジュール。<br>Explicit object dependencies and empty none-scoped Core objects. |
| 23 | [23_complete_core_metadata_and_localization.ostf](23_complete_core_metadata_and_localization.ostf) | 継承フィールドを含む曲情報、クレジット、翻訳辞書、拍子・演奏・歌詞の正式保存先。<br>Current and inherited metadata, credits, translations, performance and timed lyric units. |
| 24 | [24_all_key_modes_and_enharmonic_spellings.ostf](24_all_key_modes_and_enharmonic_spellings.ostf) | 既知7モードと未知モード、A〜G、重嬰・重変を含む綴り。<br>Seven recognized modes, open modes, A–G and double-accidental spellings. |
| 25 | [25_all_meter_denominators_and_tempo_changes.ostf](25_all_meter_denominators_and_tempo_changes.ostf) | 全7拍子分母、加算拍子、四分音符基準の小数テンポと上限。<br>All seven denominators, additive grouping and fractional/maximum quarter-note BPM. |
| 26 | [26_ppq_minimum_integer_ticks.ostf](26_ppq_minimum_integer_ticks.ostf) | PPQ=1。イベントtickは整数、小節計算は分数になり得る。<br>PPQ=1; integer event ticks, potentially fractional bar lengths. |
| 27 | [27_ppq_maximum_integer_ticks.ostf](27_ppq_maximum_integer_ticks.ostf) | PPQ=960000。イベントtickは整数、小節計算は分数になり得る。<br>PPQ=960000; integer event ticks, potentially fractional bar lengths. |
| 28 | [28_maximum_integer_pitch_velocity_boundaries.ostf](28_maximum_integer_pitch_velocity_boundaries.ostf) | 最大安全整数、音高0/127、Velocity 1/127。極端な長さの静的例で再生用ではない。<br>Maximum safe integer; pitches 0/127 and velocities 1/127. Extreme duration; not for playback. |
| 29 | [29_local_pickups_and_same_pitch_overlaps.ostf](29_local_pickups_and_same_pitch_overlaps.ostf) | 負のローカル開始、同音同時ノート、クリップ重複、配置長を越えるゲート。<br>Local pickups, simultaneous same-pitch voices, overlapping clips and gates beyond nominal length. |
| 30 | [30_muted_and_empty_track_types.ostf](30_muted_and_empty_track_types.ostf) | melodic/drum/mixed/未指定、全表示ヒント、trackとclipの独立したenabled。<br>Declared and untyped empty tracks; all view hints; independent track and clip enabled states. |
| 31 | [31_all_sound_source_kinds.ostf](31_all_sound_source_kinds.ostf) | 音源ヒント全5種。identifierは自動ロード命令ではない。<br>All five sound-source kinds; identifiers never trigger loading or execution. |
| 32 | [32_all_gm1_slots_and_shared_kits.ostf](32_all_gm1_slots_and_shared_kits.ostf) | GM1 35〜81の全47番号。Slot IDと複数Kitの共有所属。<br>All 47 GM1 mapping numbers, stable slot identity and shared membership across kits. |
| 33 | [33_custom_unmapped_and_same_midi_slot_identity.ostf](33_custom_unmapped_and_same_midi_slot_identity.ostf) | 同一番号の異なるSlot、未割当、旧ヒント、customの0/127、音高36との区別。<br>Distinct slots sharing a key, unmapped slots, legacy hints, custom boundaries and pitched 36. |
| 34 | [34_chord_intervals_and_voicing_multiset.ostf](34_chord_intervals_and_voicing_multiset.ostf) | ラベルのみ、スラッシュ低音、14/35半音、順序付き重複音とnull Velocity。<br>Symbol-only chords, slash bass, extended intervals, voicing multiplicity and unspecified velocity. |
| 35 | [35_lyrics_only_timed_units.ostf](35_lyrics_only_timed_units.ostf) | ノートなしで歌詞・読み・行・単位の時間を保存。<br>Lyric-only document with pronunciation, phrase timing and unit timing. |
| 36 | [36_multilingual_many_to_many_alignment.ostf](36_multilingual_many_to_many_alignment.ostf) | 複数歌詞文書と多対多割当。主歌詞と主旋律は明示選択。<br>Parallel lyric documents and many-to-many alignment; explicit primary lyric and melody selection. |
| 37 | [37_resource_kinds_and_provenance_actions.ostf](37_resource_kinds_and_provenance_actions.ostf) | 全4素材種別と全8履歴action。外部素材や履歴は自動実行しない。<br>All four resource kinds and eight provenance actions; no automatic fetching or execution. |
| 38 | [38_all_reference_and_localization_targets.ostf](38_all_reference_and_localization_targets.ostf) | 全26 Ref種別、全19翻訳対象種別と全許可field、共有Core関係を具体IDで記述。<br>All 26 Ref kinds, all 19 localization target kinds and every permitted target/field pair. |
| 39 | [39_all_scale_target_types_and_overlap.ostf](39_all_scale_target_types_and_overlap.ostf) | 全5スケール対象種別と重複する一般文脈。先頭だけを正解にしない。<br>All five scale target kinds and overlapping general context; no first-entry-wins rule. |
| 40 | [40_empty_unverified_core_objects.ostf](40_empty_unverified_core_objects.ostf) | 全6共通編集項目の空・unverified状態。none依存を偽らない例。<br>All six empty common-editing objects in unverified state with honest scope=none. |
| 41 | [41_stale_core_relationships_preserved.ostf](41_stale_core_relationships_preserved.ostf) | 全6項目のstale、相対音・原型・候補の不一致、削除済み翻訳対象を警告として保持。<br>Stale states, inconsistent relative/template/choice relationships and a missing translation target retained with warnings. |
| 42 | [42_linked_phrase_before_replacement.ostf](42_linked_phrase_before_replacement.ostf) | 明示的な原型置換の前。反復発生とnote IDの対応。<br>Before explicit template replacement; stable mapped note IDs across occurrences. |
| 43 | [43_linked_phrase_after_replacement.ostf](43_linked_phrase_after_replacement.ostf) | 置換後の独立した記述例。同じ発生のIDを維持し音高・Velocityを一括更新。<br>After replacement; surviving occurrence IDs retained and linked pitch/velocity updated atomically. |
| 44 | [44_detached_phrase_keeps_notes_and_template.ostf](44_detached_phrase_keeps_notes_and_template.ostf) | リンク解除後。演奏ノートと未使用原型を保持。<br>Detached instance; concrete notes and the unused template remain intact. |
| 45 | [45_choices_shared_clips_and_silent_candidate.ostf](45_choices_shared_clips_and_silent_candidate.ostf) | 同一グループ内のclip共有、無音候補、別グループの所有分離、親mute。<br>Shared clips within one group, silent candidates, disjoint groups and independent parent mute. |
| 46 | [46_generation_protection_and_swing_intent.ostf](46_generation_protection_and_swing_intent.ostf) | 保護ノート、巨大seed文字列、生成用ジャンル・ムード、Swing意図と確定演奏の分離。<br>Protected notes, large seed string, generation genres/moods and swing intent separate from saved notes. |
| 47 | [47_document_branch_and_merge_identity.ostf](47_document_branch_and_merge_identity.ostf) | 同じ文書系列の異なる親改訂。認証や自動マージ成功を意味しない。<br>Distinct parent revisions in one lineage; not authentication or proof of a successful automatic merge. |
| 48 | [48_presentation_color_inheritance.ostf](48_presentation_color_inheritance.ostf) | section役割とobjectColor、track→clip→note、Slotの色優先順位。<br>Section roles, object colors, track-to-clip-to-note inheritance and slot display precedence. |
| 49 | [49_frozen_legacy_profiles_compatibility_only.ostf](49_frozen_legacy_profiles_compatibility_only.ostf) | 既知7名前空間の旧データをunverifiedで保持。現在のCoreの代用ではない。<br>All seven frozen known namespaces retained as unverified historical payloads, not current Core authority. |
| 50 | [50_opaque_future_payload_numeric_precision.ostf](50_opaque_future_payload_numeric_precision.ostf) | 未知JSONの大整数・指数値・整数風実数トークンを保持。Core整数の例ではない。<br>Opaque large integer, extreme exponents and real-token preservation; not Core integer values. |
| 51 | [51_explicit_empty_and_absent_metadata.ostf](51_explicit_empty_and_absent_metadata.ostf) | 未命名、空配列、空の許可文字列、未指定キー。省略とは区別して保持。<br>Untitled song, empty arrays, permitted empty text and explicit unspecified key; distinct from absence. |
| 52 | [52_harmony_only_no_automatic_performance.ostf](52_harmony_only_no_automatic_performance.ostf) | 分析用コード・スケールだけの曲。保存演奏がないとき勝手に発音を生成しない。<br>Harmony-only song; no automatic generation or playback from analysis annotations. |
| 53 | [53_relative_interval_and_offset_boundaries.ostf](53_relative_interval_and_offset_boundaries.ostf) | Chord 36番目、Scale 12番目、±24の補正。indexはコード記号の度数ではない。<br>Chord index 36, scale index 12 and ±24 chromatic offsets; indexes are not chord-degree names. |
| 54 | [54_empty_template_and_independent_velocity.ostf](54_empty_template_and_independent_velocity.ostf) | 空原型、±127移調、局所source IDの再利用、実ノートVelocityの独立。<br>Empty template, ±127 transpose, template-local ID reuse and independent concrete velocities. |
