# OSTF — Open Song Timeline Format

## 正式版 3.4.0

**曲情報・演奏・共通編集情報を、独自拡張に依存せず交換する楽曲タイムライン形式です。**

ファイル拡張子は`.ostf`、内容はUTF-8 JSON。曲構成、テンポ、拍子、コード、スケール、主旋律、演奏ノート、ドラム、歌詞、多言語表示、編集関係を保存します。

[English README](README.md) · [全網羅マニュアル](docs/COMPLETE_MANUAL.ja.md) · [全網羅リファレンス](docs/PARAMETER_REFERENCE.ja.md) · [正式仕様書](docs/FORMAT_SPECIFICATION.ja.md)

## 3.4の基本方針

通常の曲情報を扱うために、Player専用のメタデータ拡張や別の開発者が実装する追加機能を必要としません。初期キー・転調・全体スケール・言語・履歴・共通編集機能は正式な型付きCoreです。旧・未知拡張は必要に応じて保持しますが、現在のCoreを上書きする正本ではありません。

保存演奏の正本はtracks内のnotesです。読み込み時に再生成、再抽選、再Swing、コードや原型の自動実体化をしません。未指定をC major/Popへ置換せず、原文・ID・音高・ゲート・Velocity・歌詞・未知情報を保持します。

## 公開資料

| 資料 | 内容 |
|---|---|
| [マニュアル日本語](docs/COMPLETE_MANUAL.ja.md) / [英語](docs/COMPLETE_MANUAL.en.md) | 作成手順、全機能の意味、マージ・移行・よくある誤り |
| [リファレンス日本語](docs/PARAMETER_REFERENCE.ja.md) / [英語](docs/PARAMETER_REFERENCE.en.md) | ルート、現行77定義、凍結65定義、全条件分岐 |
| [正式仕様](docs/FORMAT_SPECIFICATION.ja.md) / [英訳](docs/FORMAT_SPECIFICATION.en.md) | 日本語が意味の正本。Schemaと併用 |
| [JSON Schema](schema/ostf-3.4.0.schema.json) | 構造の正本。旧3.0〜3.3 Schemaも同梱 |
| [全項目・列挙値対応表](docs/COVERAGE.md) | 296宣言・119列挙値・3定数と実ファイル内の位置 |
| [サンプル54件](samples/INDEX.md) | 機能別・境界・互換保持の完全な.ostf |
| [デモ11曲](demos/README.md) | 拡張を必要としない3.4移行済みの完成楽曲 |
| [移行規則](docs/MIGRATION_3_3_TO_3_4.ja.md) / [共通デバイス契約](docs/DEVICE_CONTRACT.ja.md) | 版・所有範囲・正本・保持・競合・損失の扱い |
| [実装チェックリスト](docs/IMPLEMENTATION_CHECKLIST.md) / [問題台帳](docs/ISSUE_REGISTER.ja.md) | 対応事項と28項目の設計対処 |

## ファイル数

**展開後ちょうど100ファイル**です。入れ子ZIPはありません。54構造例＋11曲＝65個の`.ostf`はすべて独立ファイル、root version 3.4.0です。資料12、Schema5、サンプルと索引55、デモと索引12、監査5、ツール3、ルート8で構成します。

前回確定した日本語仕様と5版のSchemaを保持しています。今回の主目的は公開資料の全網羅化・日英化・実例補完・ファイル整理であり、Coreの意味を無断変更することではありません。旧原本ZIPは同梱せず、出典とハッシュを[audit/SOURCE_INVENTORY.json](audit/SOURCE_INVENTORY.json)に記録します。

## 検査と対応状況

```sh
python -m pip install -r requirements.txt
python tools/check_release.py
```

同梱データの静的検査です。依存導入後の検査では外部Schemaや素材を取得しません。音声、Live/Max for Live、UI、外部MIDI、生成、デバイスの保存復帰は動作検証していません。既存のPlayer・Composer等が3.4対応済みという意味ではなく、改修済みamxdは含みません。

[リリース判定](RELEASE_READINESS.ja.md) · [静的検査結果](audit/RELEASE_STATIC_CHECK.json) · [GitHub公開手順](docs/GITHUB_PUBLISHING.ja.md)

## 適用範囲と利用条件

CC/Pitch Bend/Aftertouch/MPE、音声クリップ、音源の完全復元、連続テンポカーブ、完全な楽譜組版は3.4の対象外です。未完成事項を「誰かの拡張実装が必須」という形で残していません。

仕様・Schema・資料・人工的な小規模サンプルは元配布のCC BY 4.0、参照コードはMITを継承します。別途提供された11デモの楽曲・歌詞・編曲に、変換が新しい権利やライセンスを与えるものではありません。[LICENSE](LICENSE.md)を確認してください。

推奨リポジトリ名は`Open-Song-Timeline-Format-3.4`、タグは`v3.4.0`です。GitHubへのアップロード・Release作成はこの生成作業では行っていません。
