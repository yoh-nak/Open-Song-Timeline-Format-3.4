# OSTF 3.4.0 — 正式仕様書

策定日：2026-10-31。形式名：Open Song Timeline Format。拡張子：`.ostf`。

**構造の正本は [3.4 Schema](../schema/ostf-3.4.0.schema.json)、意味の正本は本書です。** 片方だけに適合しても完全適合とはしません。3.3の仕様・Schemaは変更せず保存します。本書にある3.4への追加は今回の設計であり、3.3にもともと存在した項目として扱いません。旧仕様の混在した版表記を3.4の規則として読み替えないでください。

「必須」「禁止」は適合要件、「推奨」は理由があれば別の選択を認める方針です。未指定と明示的な空を区別します。Schemaの`default`は解釈時の既定値であり、読込時にフィールドを追加する命令ではありません。

## 1. 目的・範囲・拡張に依存しない原則

OSTFは曲情報、構成、和声、確定した演奏、歌詞、共有可能な編集関係を交換する形式です。DAWセッションや音源状態の代用品ではありません。

3.4では、キー、転調、全体スケール、言語、履歴、多言語表示、表示色、相対音、フレーズ原型、候補選択、共有生成意図を**名前の決まった型付きCore項目**として定義します。`extensions`、メーカーの名前空間、追加プラグイン、外部サーバー、他人が実装する拡張の存在を、これらの情報の読取・保持の前提にしてはなりません。

`extensions`は任意です。省略した文書だけで全標準機能を記述できます。既存・第三者拡張の保持能力は残しますが、3.4で標準化された現在の曲情報の正本にしてはなりません。未知拡張を削除することも要求しません。既知の旧拡張を移行できない場合も原本を保持し、不明な内容を推測で新Coreへ流し込みません。

音源プリセット、DSP、生成モデル内部状態、Liveの一時的なウィンドウ位置等はアプリ／Live Setに保持します。今回の標準項目を任意JSONの`appData`や`settings`へ逃がす保存方式は採用しません。将来、共通交換が必要な新情報が判明した場合は、意味と型を定義した新しいOSTF版で追加します。

CC、Pitch Bend、Aftertouch、MPE、音声クリップ、歌唱エンジン、チョーク実行、プラグインの完全復元、連続テンポカーブ、完全な楽譜組版は3.4の範囲外です。含まれると宣言したり、対応しないデータを黙って捨てて無損失と表示してはなりません。

## 2. 保存形式・版・数値

UTF-8のJSONオブジェクト一つとします。BOM、同一オブジェクトの重複キー、孤立サロゲート、不正UTF-8、NaN/Infinity、末尾の非空白を禁止します。Core整数はJSON整数トークンで記載し、`1.0`、`1e0`、`true`を整数の代わりに使用しません。最大整数の絶対値は`9007199254740991`です。整数の加算・乗算後もこの範囲を満たす必要があります。

有限の十進JSON数値をbinary64の限界だけで不正としません。未知情報の数値を無損失保存すると表明する実装は、元の数値トークンまたは同等の精度を保持します。表現できなければ読取専用／保存拒否／明示的な損失確認とし、黙って丸めません。キー順・空白のバイト一致と意味上の保持は別です。

ルート必須項目は`format`, `version`, `ppq`, `song`, `timeline`, `harmony`, `tracks`, `soundSlots`, `lyrics`, `resources`の10個です。`format="OSTF"`、`version="3.4.0"`。3.3までは必須だった空の`extensions`を3.4では省略できます。

任意のルート項目は`extensions`, `drumKits`, `contributors`, `document`, `relativePhrases`, `generation`, `presentation`, `phraseLibrary`, `clipChoices`, `localization`, `provenance`です。追加の未定義Coreフィールドは禁止します。SchemaのURLは識別子であり、読込時の取得要求ではありません。

3.0.0／3.1.0／3.2.0／3.3.0は各原版のSchemaと意味で読みます。単に読んだだけで3.4にしません。未知の将来版は未対応と明示し、編集を拒否するか、原文のまま保存する限定モードにします。未来の項目を3.4の既知項目と推測して変更しません。

## 3. 時間軸・ID・参照

`ppq`は四分音符当たりの整数tickで1～960000、推奨960です。全トラック、全標準編集項目に同じ値を用います。拍子変更によってtickの単位は変わりません。Core時刻は0以上、ゲート長は1以上。ノートのクリップ内開始だけは負を許し、絶対開始は0以上です。

区間は`[start, start+duration)`です。変更イベントはその`at`から有効です。同時刻のNote Offを先に、その後Note Onを処理し、各群はnoteIdの辞書順とします。表示の小節・拍、秒数、MIDI番号、配列番号を時刻やIDの代わりにしません。

IDは`^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$`。Core対象のIDは種別をまたいで文書内で一意です。3.4のフレーズ原型、インスタンス、候補グループ、候補、役割定義、生成Process、履歴Record、初期スケール、キー変更も含みます。例外は**各原型の中のsource note ID**で、その原型内だけのIDです。`document.id/revisionId`は別の文書識別空間です。未知拡張や過去版の局所IDをCoreの登録簿へ再帰的に取り込みません。

Refは`{type,id}`。Schemaに列挙した正しい種類へ解決します。同じ文字列の異種別対象、同名の別対象、配列の同じ場所にある対象へ付け替えません。移動ではIDを維持、独立コピーでは新IDを付けます。関連参照を更新できない操作は中止するか、対象が標準編集関係なら後述の状態を更新します。

## 4. 曲情報の正本

| 情報 | 正式な保存先 | 読み手がしてはならないこと |
|---|---|---|
| 原文曲名・副題・説明 | `song.title/subtitle/description` | UI言語に合わせて原文を上書き |
| 代表的な初期キー | `song.key` | 先頭コード・先頭scale・旧拡張から黙って補完 |
| 曲中のキー変更 | `timeline.keyChanges` | ノートを読み込み時に移調 |
| 既定スケール | `song.scale` | キーと同じ情報とみなす |
| 時間付きスケール文脈 | `harmony.scales` | そのたびに全体キーを変更 |
| 初期テンポ・拍子 | `tempoChanges[0]`、`meterChanges[0]`（tick 0） | `song.bpm`等の別正本を作る |
| ジャンル・ムード | `song.genres`、`song.moods` | 認識できない名前をPop等へ置換 |
| 作者等 | `contributors`＋`song.credits` | ソフトの開発者／データ編集者を作曲者にする |
| 主旋律・主歌詞 | `song.primaryMelodyTrackId/primaryLyricDocumentId` | 未指定を先頭要素と同一視 |
| ボイシング | `harmony.chords[].voicing` | 実演奏を勝手に生成／二重再生 |
| 実演奏 | `tracks[].clips[].notes` | 生成設定を実行して再構成 |

`title`だけはsong内必須で、未命名の空文字を許します。その他の任意フィールドがないことは有効な未完成状態です。未指定をC major、120 BPM、Pop、English等へ書き換えてはいけません。ただしテンポ・拍子は後述のとおり元々必須であり、欠落した不正文書を補完して正常扱いしません。

`primaryMelodyTrackId`は既存トラック、`primaryLyricDocumentId`は既存歌詞文書へ解決します。未指定時には特定しません。主旋律指定は追加の発音命令ではなく、主歌詞指定も他の歌詞文書を削除する指示ではありません。

## 5. キー・転調・スケール

### 5.1 キー値

`key.state`は`tonal`, `atonal`, `unspecified`。`tonal`では`tonic`と`mode`が必須、他の二状態ではその両方を禁止します。`label`は任意の原文表示注記です。未指定と明示的なunspecifiedを保存上区別し、どちらも推定キーに置換しません。無調をC majorと表示してはいけません。

`tonic`は`{step,alter}`。stepはA～G、alterは−2～2。自然音C=0,D=2,E=4,F=5,G=7,A=9,B=11にalterを加え12で正規化します。C#とDbの綴りは別に保持します。

`mode`は非空の原文識別文字列です。共通に認識する正確な識別子を`major`, `minor`, `dorian`, `phrygian`, `lydian`, `mixolydian`, `locrian`とします。majorは通常の長調、minorは通常の短調という調性の記述であり、許可ノートの閉集合ではありません。minorを自然短音階のみへの強制指定としません。未知のモードや`blues`などもそのまま保存・表示し、major/minorへ丸めません。未知の意味を解釈しない実装は名称と主音の保持だけでもよいものとします。

`label`はmodeやtonicを変更する別正本ではありません。labelから反対の主音が読み取れるなどの疑義は診断できますが、自動修復しません。Camelot番号、五度圏上の位置、調号は派生表示であり保存する正本を増やしません。対応しないモードをmajor/minorと偽って正確表示しません。

### 5.2 初期キーと変更マップ

初期キーの保存場所は**song.keyだけ**です。`timeline.keyChanges[]`は`id`, `at`, `key`が必須、`label`が任意です。`at`は**1以上**、厳密昇順、同じ時刻の複数変更は禁止します。`at:0`でsong.keyを二重定義しません。

時刻tの有効キーは、`at <= t`を満たす最後の変更、なければsong.key、どちらもなければ未指定です。戻り転調は戻るキー値を別の変更として明示します。局所的な借用和音やコードごとのスケールから転調を自動認定しません。変更は次の変更まで持続し、セクション境界で勝手に初期キーへ戻しません。無調・未指定への遷移も同じマップで記述できます。

時間付きの複数調性を同時に自動合成する機能はありません。多調の解析は複数のスケール文脈等で保持できるものの、このマップは一つの共有調性記述です。多調を単一キーに黙って押し込めません。

### 5.3 全体スケールと局所文脈

任意の`song.scale`は`id, tonic, intervals`必須、label任意の既定スケールです。intervalsは0～11の整数、0を含む厳密昇順・重複なしです。キーのmodeから自動で作ったり、キー変更によって自動で主音をずらしたりしません。初期スケールは時間付きscaleと区別されます。

`harmony.scales[]`は従来の`id,start,duration,tonic,intervals,label?`を維持します。3.4の任意`targets`はsection/track/clip/chord/noteへの明示的Ref配列です。指定対象のいずれかに該当する文脈として扱い、参照の実在を要求します。track対象はその所属clip/note、clip対象は所属note、section対象はその時間範囲との共通部分に適用可能な文脈です。chord/note対象は当該対象への注記です。targetなしは一般の時間付き文脈で、特定のトラック所有を意味しません。

明示的contextIdがある操作はそれを用います。時刻と対象に一致する時間付き文脈が一つならそれを候補に、複数なら複数候補のまま提示します。配列先頭だけを正解としません。一致する文脈がなく、song.scaleがあればそれが既定候補です。実装固有の選択は明示操作として行い、元データの複数文脈を削除しません。

スケールとキーが異なる主音・音集合を持っても、それだけで文書を不正にしません。分析注記と作曲意図は演奏ノートを制限しません。全体キー変更時にも確定済みメロディー、ボイシング、スケール、ドラムを自動更新しません。

### 5.4 読込時キー・一時移調・確定移調

Playerの「Original」は**読み込んだ文書の基準**です。過去の作者の原調を保証しません。初期表示はsong.key、再生位置での表示は有効キーを用い、どちらを表示しているかUIで区別します。

再生だけのTranspose、印刷だけのTranspose、試聴テンポ倍率はアプリの一時状態であり、OSTFの現在の曲情報へ書き込みません。一時移調値を保存して読込時に再適用することは禁止します。

確定移調は明示的な一括編集です。選択した対象の有音高ノート、コードroot/bass・voicing、キー、スケール等を整合するよう更新するか、更新できない関係をstale/unverifiedとして示します。Sound Slot IDとドラムMIDI割当は移調しません。0～127等を外れる値はクリップ／折返しで黙って修正しません。ラベルを安全に更新できない場合も不一致を隠しません。コードのintervals、スケールのintervalsそのものは半音移調では不変です。

フレーズ原型と実体化ノートを両方ずらして二重移調しないよう、リンク関係を再計算するかstaleにします。履歴を記録する場合はprovenanceへ以前のキー等を残せますが、過去情報を現在のsong.keyより優先しません。

## 6. テンポ・拍子・構成・曲長・弱起

`timeline.tempoChanges`は空でなくtick 0から厳密昇順、bpmは有限で0超1000以下。四分音符毎分であり、6/8等でも付点四分音符毎分へ読み替えません。変化はstepで、次の変更点まで一定です。一定区間の秒数は`tick差 × 60 / ppq / bpm`。変更をまたぐ場合は区分積分します。

`meterChanges`もtick 0から厳密昇順、numeratorは1～64、denominatorは1,2,4,8,16,32,64。小節途中の変更を丸めて移動しません。任意`beatGroups`は分母音符単位の正整数列で、合計がnumeratorに一致します。7/8の[2,2,3]等を保持できますが、アクセントやノート時刻の自動変更ではありません。

sectionsは開始順で重複区間なし、隙間・空配列を許します。`id,name,start,duration`必須、roleは自由文字列、localizedNamesは既存の任意表示です。nameをVerse/Chorus判定用のIDにしません。未知roleやセクションを削除しません。セクション境界で演奏ノートを切りません。

任意の`timeline.duration`は名目的な曲配置長（tick、0も可）です。無音の前後区間・空の構成の長さを保存できます。イベントの削除／クロップ命令ではありません。記載長を超えるノートやゲートも保持し、表示・書出では「指定配置長」「配置内容の範囲」「有効ノートの終了」を区別します。未指定なら長さ不明と、素材から算出した表示長を混同しません。旧仕様同様、実演奏終端は有効なノートgateEndの最大値、ノートがなければ0です。

任意`barOrigin`は最初の完全小節の始点です。省略時は0として小節を計算するだけで、保存値を補完しません。0より大きいとき、初期拍子の一小節長`ppq*4*numerator/denominator`未満とし、0とbarOriginの間に拍子変更を置きません。区間[0,barOrigin)は弱起表示、barOriginを小節1の先頭とします。負の絶対時刻を作りません。

barOrigin以降は現在の拍子で小節を積算します。小節途中の拍子変更では直前の小節を部分小節として終え、変更位置から次の小節番号を開始します。元々小節境界なら余分な空小節を増やしません。小節長が分数tickでも計算は有理数のまま行い、実イベントのtickは整数のまま保持します。

## 7. 和声・ボイシング・実演奏の分離

chordsとscalesは空でもよく、それぞれstartの非減少順、重なりを許します。Chordの必須項目はid,start,duration,非空label。rootとintervalsは両方あるか両方なし。bassは任意。intervalsは0～35の整数、0を含む厳密昇順・重複なしで、14を2へ丸めません。

labelだけのコードも有効です。各ソフトの独自コード解析を標準の構造化解釈と偽りません。root/intervals/bassとlabelやvoicingの差は診断できても、自動的に書き換えません。

`voicing.pitches`は順序と同音の重複を保持する0～127の非空配列です。velocitiesは省略でき、ある場合はpitchesと同じ長さ・同じ位置対応、要素は1～127またはnull。nullは未指定であり0ではありません。並べ替えるなら音高とVelocityを対で移動します。

ボイシングはGate/trackを持たないスナップショットです。Coreノートの代わりではありません。コード試聴や伴奏実体化は明示操作に限定し、保存済みトラックと重ねて自動発音させません。voicing.velocitiesと実ノートvelocityも別の値です。

## 8. トラック・クリップ・ノート・打楽器

Trackはid,name,clips必須。role、instrument（name必須・family任意）、enabled、trackType、preferredView、soundSource、localizedNames、drumKitIdは任意です。enabledの解釈既定はtrue。trackTypeはmelodic/drum/mixedで、melodicにはpitchノート、drumにはsoundSlotIdノート、mixedには両種類を許します。未指定の空トラックを勝手にdrum等と断定しません。trackTypeはDAWトラックの種類ではありません。

Clipはid,start,duration,notes必須、name,enabled,localizedNames任意。startは絶対tick、notesのstartはローカルtickです。並びはstart非減少、同時刻では元配列順を保持します。`onset = clip.start + note.start`、`gateEnd = onset + duration`。onsetは0以上、両方MAX以内。弱起、clip後方の発音、clipをまたぐゲート、同音重複を省略・短縮しません。

Noteはid,start,durationと、pitchまたはsoundSlotIdの**どちらか一つ**が必須。pitchは0～127（60=C4、69=A4）。任意velocityは1～127、未指定なら保存時に埋めません。ゲートは音源のリリース時間・一発音のサンプル長・楽譜上の音価ではありません。親trackとclipが両方enabledのときだけ演奏します。無効な内容も保持・検証します。

SoundSlotはid/name必須、role/midiNote/midiMapping/localizedNamesは既存の任意項目です。IDが音楽上の発音対象、midiMappingは外部MIDI対応です。gm1は35～81、customは0～127。customの36をGM Kickと断定しません。midiNoteとmidiMappingを併記するときは番号一致を要求します。番号が同じでも異なるSlotを統合しません。

DrumKitはid,name,soundSlotIds必須、localizedNames任意。順序付きの所属であり音源プリセットではありません。track.drumKitIdを使うときはそのtrack中の全Slot参照がキットに所属し、参照自体も存在することを要求します。Slotを複数Kitで共有することは可能です。

SoundSourceはunassigned/gm1/externalMidi/plugin/hostManagedという情報上のヒントで、identifierを許す種類もSchemaどおりです。音源の自動実行、プリセット復元、機器への自動送信を要求しません。プレビュー用音源を選んでもCoreのInstrumentやSlotを書き換えません。

Mixedのpitch:36とSlotのGM36は別対象です。外部MIDI出力で合流する場合、分離ルーティングまたは情報損失確認が必要です。同音同chの重複、Slot ID消失、PPQ丸め、未対応マッピングも黙って解消しません。未割当SlotからGM番号を推測して正式書出ししません。Player内の近似試聴音とMIDI互換性は別です。

## 9. 歌詞・言語・主歌詞

lyricsはdocuments,phrases,units,alignmentsの4配列必須。空でも有効です。documentはid必須、title/language任意。phraseはid,documentId,text必須、unitはid,phraseId,text必須。どちらもpronunciationと、start/durationの対を任意に持ちます。時間を持つなら絶対tickで終端もMAX以内です。

textが表示原文、pronunciationが発音注記です。自動分割・自動転写・歌唱エンジンの命令ではありません。unitの連結がphrase本文と一致することを要求しません。alignmentのunitIds/noteIdsはそれぞれ非空・重複なしの順序付き配列、実在の対象へ解決します。複数単位と複数音の関係を保存でき、alignmentから追加ノートを生成しません。

`song.languages`は楽曲全体の言語メタデータ、歌詞document.languageは当該文書の言語です。混在を許し、一方から他方へ自動複写しません。song.languagesの省略は不明、空配列は登録なしであり、器楽曲や英語を推測しません。BCP 47表記を推奨しますが、認識できない原文を破棄・正規化しません。言語配列の大文字小文字だけが違う重複は不正です。

代表歌詞は明示されたprimaryLyricDocumentIdのみ。複数言語・複数版の歌詞を一つに結合しません。訳詞は別文書と割当として扱い、名称の翻訳機能で歌詞本文を置換しません。ノートの移動・削除でalignmentを壊す操作は参照を明示的に更新するか、損失を確認するか、中止します。Coreのalignmentはstaleフラグで不正を許容しません。

## 10. ジャンル・ムード・クレジット・権利・素材

song.genresとsong.moodsは任意で、要素はid,name,externalUri?。固定のジャンル／ムード表を設けません。配列順は著者の表示順、同名の異なるIDも保持します。未指定・空・未知名をPopや既定Moodに変換しません。externalUriがあっても読み込み時に取得せず、原文nameを上書きしません。URIは絶対URIとし、その実在を形式適合要件にはしません。

contributorsはid,name,kind?,localizedNames?、song.creditsはid,contributorId,role,label?。roleは既存の開いたASCII意味識別子。参照は実在のcontributorへ解決します。data-editor、software-developer、composer等を同一視しません。氏名の一致で人物を統合しません。

song.rightsはnotice/licenseUri/rightsHolderIdsの任意集合で一つ以上を持ちます。rightsHolderIdsはcontributorsへの重複なし参照です。licenseUriは著者が記載した絶対URI。形式への保存は権利の認証・付与ではありません。未記載のライセンスや著作者を補いません。

resourcesはid,kind,uri必須、name,sha256任意。kindはaudio/midi/text/other。uriは素材参照であり、音声トラックの発音や自動ダウンロード命令ではありません。相対URIは当該OSTFファイル位置を基準に、利用者の明示操作時に解決します。外部取得・プラグイン実行・スクリプト実行は読込だけでは行いません。素材未取得はノート内容の不正を意味しません。

## 11. 共通編集情報のCore化と状態

旧標準拡張の機能を次の正式ルート項目へ移します。名前空間や拡張version/data層はありません。構造・意味は3.4.0に含まれます。

| 3.4 Core | 保存する型付き情報 | 旧保存先（移行元のみ） |
|---|---|---|
| relativePhrases | assignments | org.ostf.relative-phrase.v1 |
| generation | processes | org.ostf.generation-context.v1 |
| presentation | roleDefinitions,sectionRoleAssignments,appearance | org.ostf.appearance.v1 |
| phraseLibrary | templates,instances | org.ostf.phrase-library.v1 |
| clipChoices | groups | org.ostf.clip-choices.v1 |
| localization | entries | org.ostf.localization.v1 |

各Core項目にはstatusとdependenciesが必須です。status=currentは現在のCoreとの対応一致、staleは不一致が判明、unverifiedは未確認です。成熟度や実行成功を意味しません。dependenciesはscope=none/document/objects（objectsなら非空・重複なしrefs）です。

currentではすべての参照を解決し、意味上の対応を満たします。objectsなら当該項目から参照するCore対象をすべて列挙します。列挙できない場合はdocument。親clip/trackの移動やenabled変更による子の絶対位置・有効状態の変化も依存対象の変更です。翻訳・表示・生成・フレーズに参照があるのにnoneと宣言してはいけません。songの翻訳など、Refで対象を列挙できない関係にはscope=documentを用います。

関連するCoreを編集するとき、関係を再計算して一致を確かめるか、stale/unverifiedへ変更します。未対応の編集関係をcurrentのまま残しません。状態の書換えだけを新しい音楽編集として再帰的に無効化しません。stale/unverifiedの参照・内容不一致は警告として保持しますが、型不正・ID重複・管理対象の二重所有は許しません。Core本体の不正参照にもこの緩和を適用しません。

読み込み時には再生成・再抽選・候補の適用・原型の同期を行いません。現在の演奏は常にCoreトラックです。

### 11.1 相対音

assignmentはnoteId,basis,contextId,anchorPitch,index,chromaticOffset。basisはchordTone/scaleDegree。同一noteIdへ重複assignmentを作りません。contextIdはChordまたはScale（song.scaleもScale）で、anchorPitchのピッチクラスはroot/tonicに一致します。

`note.pitch = anchorPitch + context.intervals[index-1] + chromaticOffset`。indexは1始まりで実際の配列長以内、offsetは−24～24。結果は0～127。コード記号の「5th」と配列の5番目を同一視しません。文脈区間外の弱起でも明示的ID参照の関係だけで拒否しません。

staleな相対情報で実ノートを上書きしません。最適な声部進行や新しいコードへの追従方法は、標準の自動実行としては定めません。

### 11.2 生成履歴と生成意図

generation.processesの要素はid,generator,inputs,outputs,protectedNoteIds必須。targetRangeとintentは任意。generatorは非空id/version。inputsはrole,ref,readRange?、outputsは非空Ref配列、保護IDは重複なしです。inputsは空も複数も許します。

intentはgenreNames,moodNames,groove,prompt,seedの明示した項目だけを許します。seedは文字列で精度を保持します。これらは生成意図の記録で、エンジンをまたぐ同一結果を保証しません。promptを自動実行・外部送信してはいけません。標準化していない内部パラメーター辞書やvendorExtensionは3.4のgenerationに設けません。

Grooveにはname、およびunitTicks/longWeight/shortWeightの三つ組を記録できます。三つ組は全部あるか全部なし。unitTicksは元の一分割のtick長、隣接二分割を対とし、比率L:Sなら対の2*unitTicks内の二つ目の開始は`2*unitTicks*L/(L+S)`という生成意図を表します。確定演奏へ再適用しません。明示的に生成する場合に整数tickで表現できなければ、PPQを正確に変更するか損失を確認します。nameから固有グルーヴの音楽的意味を自動推測しません。

生成Genreはsong.genresの代わりではありません。Moodも同様です。適用範囲はinputs/targetRange/outputsで記述し、セクションの名前から推測しません。

保護するnote集合は操作前に固定します。ID、発音対象、絶対onset、duration、velocityの有無と値、track/clipを合わせた有効状態を比較します。保護リストを操作後に削除して保護を回避してはいけません。PPQの変更は有理時間として正確比較できる場合以外は保護比較を拒否します。テンポによる実秒数・音源音色は別の編集対象であり、tick保護と同じ保証にしません。

### 11.3 表示と役割

presentationのroleDefinitionsはid/name/baseRole?、sectionRoleAssignmentsはsection ID→roleDefinition ID。appearanceはroleColors/customRoleColors/objectColors。色は#RRGGBB、objectColorsはtarget/color、同一target重複は禁止です。

色の優先順は、sectionでは自身のobjectColor→割当役割のcustomRoleColor→そのbaseRoleのroleColor→section.roleのroleColor→ホスト既定。track/slotは自身→roleColor→既定。clipは自身→親track、noteは自身→親clip。その他は自身→既定。名前・色から音楽的なroleや発音を決定しません。未解決の色参照を同名対象へ付け替えません。

### 11.4 再利用フレーズとVelocity

Templateはid,duration,notes必須、name任意。durationは反復周期。source notesはid/start/durationとpitchまたはsoundSlotId、任意velocity。IDはそのTemplate内でのみ一意、source notes自体は発音しません。

Instanceはid/templateId/clipId/repeatCount/transpose/noteMap必須、velocityMode任意。Template/InstanceのIDは3.4ではグローバルCore IDです。一つのclipを複数Instanceで所有できません。noteMapはtemplateNoteId/repeatIndex/noteId。繰返しごとのsource note発生と全Core clip noteが過不足なく一対一に対応します。

```
clip.duration = template.duration * repeatCount
note.start = repeatIndex * template.duration + sourceNote.start
note.duration = sourceNote.duration
note.pitch = sourceNote.pitch + instance.transpose   # 有音高だけ
note.soundSlotId = sourceNote.soundSlotId             # 打楽器だけ
```

repeatIndexは0以上repeatCount未満。同一発生の重複、mapped noteの二重所有、clipの二重所有は禁止です。音高・演算後時刻も範囲内とします。弱起・テールを省略しません。currentの整合検査で巨大な直積を生成する必要はなく、件数と各mapを調べられます。

velocityModeの解釈既定はindependent。これは実ノートのVelocityが原型と独立で、原型の明示更新後も存続note IDのVelocityを保持するモードです。新たなノートを実体化する明示操作では原型のVelocityを初期値として複写できますが、その後は自動同期しません。linkedでは、mapped noteとsource noteのVelocityについて、未指定か否かと数値が完全に一致する必要があります。モード変更だけで実ノートを書き換えず、必要な更新を一括操作として提示します。

原型置換は影響する全Instance・Core notes・依存関係を原子的に更新するか失敗します。存続する(repeatIndex,templateNoteId)は既存noteIdを維持します。リンク解除は該当Instanceだけを取り除きCore clip/notesを保持します。勝手に未使用Templateを削除しません。無限反復・確率的な読込時展開は扱いません。

### 11.5 クリップ候補

Groupはid/candidates/selectedCandidateId必須、name任意。Candidateはid/clipIds必須、name任意。グループは候補を一つ以上持ち、候補のclipIdsは重複なしで空の無音候補も可。選択IDは当該候補IDかnull。3.4ではGroupとCandidateのIDもCore全体で一意です。

一つのgroup内で同じclipを複数候補が共有できますが、異なるgroupの管理集合を重ねません。currentでは管理clip自身のenabledが選択候補への所属と一致し、nullならすべて無効です。親track.enabledは別のミュートで変更しません。

選択を変更する操作は全管理clipと選択IDを一括更新します。読み込んだだけでは選択を適用せず、矛盾を診断します。これは既に実体化された演奏clipの組合せであり、曲構成・和声・歌詞を含む全曲シーンではありません。

### 11.6 多言語表示

localization.entriesはtarget/field/values。targetはkindと、song以外ではグローバルCore id。旧profile指定はありません。valuesは言語タグ→非空翻訳です。タグの大文字小文字だけが違う重複を禁止します。SchemaがBCP 47全体を検証するとは主張しません。原文の値を残し、翻訳のない場合は原文に戻します。

| kind | 翻訳可能なfield |
|---|---|
| song | title,subtitle,description,key.label,rights.notice |
| alternateTitle | title |
| contributor,section,track,clip,soundSlot,drumKit,resource,phraseTemplate,clipCandidate,clipChoiceGroup,roleDefinition,genre,mood | name |
| track（追加） | instrument.name |
| credit | label |
| lyricDocument | title |
| keyChange | label,key.label |
| scale | label |

currentでは原文フィールドの存在を要求します。同一対象・field・言語は重複禁止。既存localizedNames/localizedTitlesと同じ翻訳を併記する場合は文字列が完全一致しなければなりません。新規作成はlocalizationへ集約を推奨しますが、旧フィールドも保持します。歌詞本文、音名、コード値、ID、URI、role、modeの意味を翻訳機能で変更しません。

## 12. 文書同一性・履歴・マージ

任意documentはid/revisionId必須、parents/createdBy/modifiedBy任意。idは同じ作業文書の系列、revisionIdは内容が変わるごとに新たに割り当てる不透明な識別子です。単なる再保存で意味内容が変わらなければ維持できます。新たな独立コピーでは新id、元から派生する場合はparentsへ元の組を記録します。同一idの分岐は異なるrevisionIdで区別します。再編集・Undo後の新保存も新しいrevisionとし、過去の組を再利用しません。

parentsの要素はdocumentId/revisionId必須、sha256任意。自分自身と同じ組を親にしません。同一組の重複を禁止し、同一組に異なるhashを付けることも禁止します。IDや親の宣言だけで改変防止・本人認証・安全な自動マージを保証しません。履歴グラフ全体の検証は利用可能な履歴がある場合だけです。

provenance.recordsはid/action必須、description/tool/sources/semitones/beforeKey/afterKey任意。actionはcreate/import/conversion/edit/transpose/merge/generation/other。semitonesを記載できるのはtransposeだけです。現在の音楽値を上書きする命令ではなく、過去の自己申告履歴です。sourcesのdocumentId等は過去文書を指すため、現在のCore IDへ解決しません。resourceIdだけは現在のresourcesへ解決します。ハッシュは入力原本の正確なバイト列で、出力自身のハッシュを自分に埋め込みません。

マージは次の契約で行います。フォーマット自体がどのアプリにも全曲を書き換える権限を与えるものではありません。

- **既定は担当対象だけ。** Drumは明示選択したdrum/mixed対象、Song Writerは明示選択した主旋律等。トラック名や配列位置だけで担当を決めません。未指定primaryMelodyTrackIdを勝手に新しいトラックへ振り替えません。
- **共有情報を別途比較。** 構成、テンポ、拍子、キー、スケール、ジャンル、クレジット、歌詞は独立の差分・承認対象。ノートのマージに便乗して上書きしません。Baseがない場合は安全な三者マージができると主張しません。
- **文書IDを越えて同一IDを盲信しない。** 独立文書の同じnote/slot IDは衝突し得ます。新しいID対応表を作り、既知の全参照を一緒に更新します。未知拡張の内部参照を推測で変更しません。必要な参照を安全に維持できなければ統合を中止します。
- **PPQは有理数で整合。** `tick / ppq`を正確な時間として比較し、整数に正確変換できる共通PPQを使います。LCMが960000超、演算後MAX超、または丸めが必要なら黙って処理せず拒否か明示的な損失確認。ノートだけでなく全時間フィールド、range、フレーズ周期、Groove単位も対象です。
- **位置移動とテンポ変更は分離。** セクションやclipを移動しても、関連するキー/テンポ/拍子が自動で追従するとは限りません。移動対象・取り残す対象と新境界をプレビューし、一括で確定します。
- **全体を原子的に保存。** 操作中の失敗で一部変更された正本を残しません。参照・保護・依存状態を確認してから別名または一括保存します。Unsupported Coreの保持ができないWriterはその編集を拒否します。

マージ時に未知データや未解釈のCore値を失わず保持する要件は、生成機能への対応とは別です。特定デバイスが各標準編集機能を実行できることまでは要求しませんが、非対応を理由に消去してはなりません。

## 13. 旧版・独自拡張との移行境界

3.3以前を直接3.4として扱いません。既存原版の読込、旧データの意味を示した移行プレビュー、明示的な3.4保存を分離します。

3.4文書では標準Coreを優先し、旧拡張と矛盾すれば警告します。Coreがないことを理由に旧Playerメタデータを黙って正本に昇格してはいけません。移行されていないlegacy値は「旧データあり・未移行」と区別します。未知拡張は解析せず保存し、編集が依存関係に影響する場合はstatusをstale/unverifiedへ更新します。

旧標準拡張の正確な対応版は、元の名前空間・版・構造のまま解釈します。3.4 Schemaには旧定義を凍結した別領域を収録し、原型Velocityや新Core参照を旧拡張版へ無言で追加しません。未知の拡張versionは既知の旧版と同じものとして解釈しません。

3.4から旧版への保存は新情報を損失なしに表せない場合があります。削除される項目・ID・参照・翻訳・関係をパス単位で示し、確認なしのダウングレードは禁止します。3.4の新CoreをPlayer専用拡張へ押し戻すことを標準の下位互換とは定義しません。詳細は[移行規則](MIGRATION_3_3_TO_3_4.ja.md)。

## 14. 適合区分・リリース判定

構造適合はSchema、意味適合は本書のID/参照/時間/関係規則、編集適合は保持・非破壊・損失報告の契約で判断します。Readerは表示できない標準機能を未対応と示せます。Writerは未対応情報を保持できなければ保存を拒否します。音色一致、生成結果の優劣、DAW接続の成功は形式適合とは別です。

本配布に同梱するチェックは、Schema・参照・記述例・変更対象・保持比較等の**静的な資料検査**です。Player、Composer、Editor、Song Writer、Drum Arrangerの実行、Live内の再生、MIDI送信、UI、音声品質の動作検証を行ったことにはしません。

公開可否は[リリース判定](../RELEASE_READINESS.ja.md)に記載します。今後の未知の要望・全デバイスの不具合がなくなる保証ではありませんが、今回確認した共通情報の拡張依存を再び必要にしない保存先と保持契約を定めています。
