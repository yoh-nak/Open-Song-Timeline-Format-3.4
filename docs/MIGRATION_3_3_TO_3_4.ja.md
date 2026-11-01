# OSTF 3.0–3.3 → 3.4 移行規則

本書は[3.4正式仕様](FORMAT_SPECIFICATION.ja.md)の移行契約を具体化します。今回の11曲の変換と、任意の旧ファイルを扱う一般的な移行実装は区別します。配布ツールは汎用自動移行アプリではありません。

## 1. 共通手順

1. 入力を元のversionのSchema・意味で読む。原本のバイト列・SHA-256・版を確保する。形式不正と、読取ソフト未対応と、拡張に情報があるだけの状態を区別する。
2. 正式Core、解釈可能な正確な版の旧標準拡張、既知のベンダー拡張、未知データを分類する。名前が似ているだけで同じ意味にしない。
3. 変更する保存先、残す情報、競合、推定が必要になる項目を提示する。必要な判断を済ませるまで原本を上書きしない。
4. 新Coreへ明示変換する。現在のノート、歌詞、構成、テンポ、拍子など、対象外のデータを保持する。数値トークン精度を保てない入力は無損失変換と表明しない。
5. 全IDと全既知参照、状態、範囲、保護条件を確認する。rootを3.4.0として**別ファイルに保存**する。旧版のversionだけを変更する操作を移行完了と呼ばない。

3.4 Readerは旧ファイルを自動的に3.4へ書き換えません。3.4 Writerも、読み込んだ旧曲の欠けたキー・ジャンル・言語・スケールを推測して埋めません。

## 2. 既存Coreは原位置を継承

| 情報 | 移行先 | 規則 |
|---|---|---|
| 曲名・副題・説明・別タイトル | songの同名項目 | 原文・IDを保持 |
| ジャンル | song.genres | 既存値を優先。未知名・空配列・順序を保持 |
| 作者等 | contributors / song.credits | 実際の役割を保持。開発者を作曲者にしない |
| ボイシング | harmony.chords[].voicing | スナップショット。ノートを生成しない |
| 初期テンポ・拍子と変更 | timeline.tempoChanges / meterChanges | at:0を維持し、別のsong.bpm等を作らない |
| スケール文脈 | harmony.scales | 先頭スケールからsong.keyを自動生成しない |
| 主旋律 | song.primaryMelodyTrackId | 未指定から先頭trackを選ばない |
| 演奏・ドラム・歌詞 | 既存の保存先 | 配置・ゲート・Velocity・有効状態・Slot ID・歌詞割付を保持 |
| 素材参照 | resources | 履歴を素材と同一視しない |

3.0にはないVelocity、3.1にはないボイシング等を、元々存在したフィールドとして扱いません。元版ごとの規則を確認し、追加できることと、値が既知であることを分離します。

## 3. Playerメタデータの既知デモに対する変換

次の表は本会話に提供された11曲の`org.yohnak.player.metadata`を検査した結果に基づきます。同名の拡張や別バージョンが常に同じ構造であることを保証しません。

| 旧data項目 | 3.4で使用する場所 | 競合・注意 |
|---|---|---|
| originalKey | song.key | tonal/tonic/modeを構造化。旧表記はlabelにも保持。曖昧なら推定せず止める |
| keyChanges | timeline.keyChanges | tick 0は初期値との一致を確認してsong.keyへ一本化。非0には新しい安定ID |
| genre | song.genres | 既存Coreがあればそちらを保持。違いがあれば報告。複合名を勝手に分割しない |
| language | song.languages | 今回は旧English→enの明示対応だけ。歌詞文書のlanguageは変更しない |
| credits | contributors＋song.credits | 今回のdataEditorはdata-editor。composerへ昇格しない |
| voicings | 対応するchord.voicing.pitches | chord IDによる対応。ID欠落・不一致・既存voicing競合は未解決として報告 |
| featureSummary | song.description | 既存説明がある場合は競合確認。上書き・勝手な連結をしない |
| provenance | provenance.records | 過去の変換・編集・出典説明として保持。現在のCoreを上書きしない |

たとえばE minorの曲に全体スケールが保存されていなければ、song.keyだけを設定しsong.scaleは未指定のままにします。A bluesもminorへ変換せず、mode="blues"の原文を保持します。

## 4. 旧標準拡張から正式Coreへ

対象は正確な対応版だけです。旧6暫定profileは`1.0.0-draft.1`、旧Localizationは`1.0.0`。旧legacy-importは現在の音楽表現ではなく、原本保全・移行監査のための過去資料として扱います。

| 名前空間 | 新Core | 主な調整 |
|---|---|---|
| org.ostf.relative-phrase.v1 | relativePhrases | 外側のstatus/dependenciesを保持しdata.assignmentsを直下へ |
| org.ostf.generation-context.v1 | generation | processesを移す。vendorExtensionを新Coreへ無理に移さない |
| org.ostf.appearance.v1 | presentation | roleDefinitions、sectionRoleAssignments、appearanceを移す |
| org.ostf.phrase-library.v1 | phraseLibrary | 原型/instanceのIDをCore全体へ統合。Velocityの旧意味を保持 |
| org.ostf.clip-choices.v1 | clipChoices | group/candidateの局所IDをCore全体へ統合 |
| org.ostf.localization.v1 | localization | profile付き対象を正しく解決して新グローバルIDへ。profile指定を除く |

名前空間・版・dataの包みを除くだけでは十分ではありません。次の処理が必要です。

### IDと参照

旧拡張の局所IDがCoreまたは別拡張と衝突する場合、**旧名前空間・旧種別・旧ローカルスコープ・旧ID**の組から新IDへの対応表を作ります。同じ文字列だからと一括置換してはいけません。各Instance、noteMap、候補選択、役割割当、翻訳、dependenciesなどすべての既知参照を対応表で更新します。

原型内のsource note IDは引き続き原型ローカルです。Core noteのIDと衝突しても同じ対象ではありません。旧候補ID等の参照が複数の局所スコープへ解決してしまう場合は自動選択せず、変換を保留して原本を残します。意味の分からない未知拡張の内部文字列は変更しません。

### 状態と依存

currentの関係は新しいCore上でも一致する場合だけcurrentを維持します。原本がstale/unverifiedなら検証せずcurrentへ昇格しません。依存対象の列挙範囲が不足する場合は文書全体へ広げることを記録します。songを翻訳するlocalizationなど、対象をRefだけで列挙できない場合はscope=documentです。

### Velocity

旧フレーズ原型にはVelocityの項目がありません。3.4への移行では原型に架空のVelocityを追加せず、instanceのvelocityModeはindependentとして解釈し、実ノートのVelocityを保持します。linkedへの切替は別の明示編集です。

### 生成設定

旧vendorExtensionの未知設定からgenreNames、Groove、seed等を推測しません。今回の型付きintentで正確に表せるものだけ移します。残りは旧原本や互換保持用拡張として残すか、独立アプリ設定へ明示的に移します。標準曲内容の読込をその設定の存在に依存させてはいけません。

## 5. 旧拡張を削除できる条件

同等の現在情報がCoreへ移り、全既知参照・翻訳・依存関係が更新され、残る情報がないことを確認した場合にだけ、その旧拡張を削除できます。未知拡張が当該旧データを利用している可能性を安全に扱えない場合は保持します。

旧記録を保持する場合はCoreを上書きしない互換資料とします。変換が旧関係を壊したのにcurrentと偽らずstale/unverifiedにします。旧データと新Coreの二重正本は作りません。旧拡張の構造・版は凍結した旧Schemaで扱い、3.4の新しい項目を旧versionへ混ぜません。

## 6. 同梱11曲について実施した範囲

11曲の入力にはPlayerメタデータと標準Appearance以外の拡張はありませんでした。各既知項目を表のとおり移行し、拡張を持たない3.4ファイルを作成しました。**楽曲を再作曲・再生成したものではありません。** 原本は前回のリリースパッケージに保管されています。この100ファイル版には原本ZIPを入れ子で同梱せず、[出典一覧](../audit/SOURCE_INVENTORY.json)に原本のSHA-256と今回の保持比較を記録しています。

変換結果の件数・ハッシュ・保持比較は[移行監査JSON](../audit/DEMO_MIGRATION.json)。11曲中10曲の1,328個のボイシングスナップショットを移行しました。Feature Demoのジャンルは旧値`Progressive Pop / Fusion`を一つの名前のまま登録しています。欠けていた全体スケール、代表歌詞、作者名を推定で追加していません。

## 7. 旧版への逆変換と対応デバイス

3.4の新Core情報、ID、翻訳、依存関係を旧版へ落とす場合はパス単位の損失報告と利用者の承認が必須です。3.4を3.3と偽るversion変更は禁止です。Player独自拡張への押戻しは標準逆変換ではありません。

既存Player v1.1.3や他の3.3用デバイスが3.4を読めるとは保証しません。今回の配布に改修済みデバイスは含まれません。原版を残し、デバイス側が3.4の正式フィールドに対応した後で新デモを使用してください。
