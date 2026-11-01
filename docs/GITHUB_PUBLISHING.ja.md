# OSTF 3.4.0 — GitHub公開ガイド

## 公開名

- Repository: `Open-Song-Timeline-Format-3.4`
- Release tag: `v3.4.0`
- Release title: `OSTF 3.4.0 — Native Core Metadata & Composition Interchange`

Description欄用:

```text
Open Song Timeline Format 3.4 — native key, modulation and composition metadata, concrete note timelines, lyrics, drums, and portable editing relationships. Complete bilingual documentation and 65 OSTF examples.
```

## 配置

ZIPを一度展開し、**中の100ファイルを階層を保ったままリポジトリ直下へ配置**します。README.mdがルートに来る配置です。ZIPを一つ置くだけではドキュメントやサンプルをGitHub上で閲覧できません。入れ子ZIPや隠しサンプルはありません。

ルート8、docs12、schema5、samples55、demos12、audit5、tools3の計100ファイルです。旧3.3のリポジトリを上書きする必要はありません。原本と旧リリースは別途保持してください。

## 公開前

[LICENSE](../LICENSE.md)の適用範囲と、別途提供されたデモ曲を公開するための権利を確認します。READMEとリリースノートには動作未検証・デバイス未改修の境界を記載しています。

ローカルでPythonの依存を用意した場合:

```sh
python -m pip install -r requirements.txt
python tools/check_release.py
```

編集せずに配布する場合は、同梱Manifestと実ファイルの一致を維持してください。資料を書き換えた場合は、変更履歴を更新して静的検査・Manifestを作り直します。スキーマや規範の意味を変える場合は、単なる資料再生成として隠さず版管理してください。

```sh
python tools/build_catalogue.py
python tools/check_release.py --refresh
python tools/check_release.py
```

`--refresh`はローカルの監査報告とManifestを再生成する保守用処理です。GitHubにアップロードする操作ではありません。

## Commit・Release本文

Commit summary:

```text
Release OSTF 3.4.0 with complete bilingual docs and native Core examples
```

Commit body:

```text
Define shared song metadata and editing relationships without private Player extensions.
Publish complete manuals, references, schema and full field/enum coverage.
Include 54 focused examples and 11 complete OSTF 3.4 demo songs.
Preserve original-version schemas and document explicit migration and loss boundaries.
Package exactly 100 files; static checks only, no device or audio runtime certification.
```

Release本文は[RELEASE_NOTES.md](../RELEASE_NOTES.md)を使用します。必要なら配布ZIPをReleaseの添付資産として追加します。仕様の正式版であり、旧Player等の3.4対応済みを意味する表現は使用しません。

この生成作業ではGitHubへの作成・アップロード・Commit・Release公開を行っていません。
