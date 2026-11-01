#!/usr/bin/env python3
"""Build complete field/enum witnesses and bilingual references from the bundled schema.

This is a documentation generator, not a player, renderer, or migration engine.
It reads local samples only and never retrieves a schema or resource over a network.
Requires Python 3.10+ and jsonschema 4.x. Run check_release.py after regenerating.
"""
from __future__ import annotations
from pathlib import Path
import json
import sys
from typing import Any
import jsonschema
sys.dont_write_bytecode = True
from check_package import load_json

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / 'schema/ostf-3.4.0.schema.json'


def escape(text: str) -> str:
    return str(text).replace('~', '~0').replace('/', '~1')


def pointer_get(value: Any, pointer: str) -> Any:
    if pointer in ('', '#'):
        return value
    for part in pointer.removeprefix('#').removeprefix('/').split('/'):
        part = part.replace('~1', '/').replace('~0', '~')
        value = value[int(part)] if isinstance(value, list) else value[part]
    return value


def inventories(schema: dict) -> tuple[dict, dict, dict]:
    fields: dict[str, dict] = {}
    enums: dict[str, dict] = {}
    constants: dict[str, dict] = {}

    def collect(node: Any, path: str) -> None:
        if not isinstance(node, dict):
            return
        if 'enum' in node:
            enums[path] = node
        if 'const' in node:
            constants[path] = node
        for key, child in node.get('properties', {}).items():
            child_path = path + '/properties/' + escape(key)
            fields[child_path] = child
            collect(child, child_path)
        for key in ('items', 'additionalProperties'):
            if isinstance(node.get(key), dict):
                collect(node[key], path + '/' + key)
        for key in ('oneOf', 'anyOf'):
            for index, child in enumerate(node.get(key, [])):
                collect(child, path + f'/{key}/{index}')
        # allOf/if/then/else/not refinements are fully reproduced in references.
        # Their predicate/restriction copies do not declare new storage fields.

    collect(schema, '#')
    for name, node in schema['$defs'].items():
        if name != 'legacy33':
            collect(node, '#/$defs/' + escape(name))
    return fields, enums, constants


def make_coverage(schema: dict) -> dict:
    fields, enums, constants = inventories(schema)
    hits: dict[str, list] = {path: [] for path in fields}
    enum_hits: dict[str, dict] = {p: {json.dumps(v, ensure_ascii=False): [] for v in n['enum']}
                                 for p, n in enums.items()}
    const_hits: dict[str, list] = {p: [] for p in constants}
    validator = jsonschema.Draft202012Validator(schema)
    examples = []

    def remember(bucket: list, file: str, path: str) -> None:
        entry = {'file': file, 'pointer': path}
        if len(bucket) < 3 and entry not in bucket:
            bucket.append(entry)

    def walk(node: Any, value: Any, sp: str, dp: str, file: str, depth: int = 0) -> None:
        if depth > 80:
            raise ValueError('Unexpected schema recursion depth')
        if not isinstance(node, dict):
            return
        if '$ref' in node:
            ref = node['$ref']
            if not ref.startswith('#/'):
                raise ValueError('External schema reference is not allowed: ' + ref)
            if '/legacy33/' not in ref:
                walk(pointer_get(schema, ref), value, ref, dp, file, depth + 1)
        if sp in enum_hits:
            for option in enums[sp]['enum']:
                if type(option) is type(value) and option == value:
                    remember(enum_hits[sp][json.dumps(option, ensure_ascii=False)], file, dp)
        if sp in const_hits and value == constants[sp]['const']:
            remember(const_hits[sp], file, dp)
        if isinstance(value, dict):
            for key, child in node.get('properties', {}).items():
                if key in value:
                    child_path = sp + '/properties/' + escape(key)
                    if child_path in hits:
                        remember(hits[child_path], file, dp + '/' + escape(key))
                    walk(child, value[key], child_path, dp + '/' + escape(key), file, depth + 1)
            additional = node.get('additionalProperties')
            if isinstance(additional, dict):
                for key in value:
                    if key not in node.get('properties', {}):
                        walk(additional, value[key], sp + '/additionalProperties', dp + '/' + escape(key), file, depth + 1)
        if isinstance(value, list) and isinstance(node.get('items'), dict):
            for index, item in enumerate(value):
                walk(node['items'], item, sp + '/items', dp + '/' + str(index), file, depth + 1)
        for key in ('oneOf', 'anyOf', 'allOf'):
            for index, child in enumerate(node.get(key, [])):
                if validator.evolve(schema=child).is_valid(value):
                    walk(child, value, sp + f'/{key}/{index}', dp, file, depth + 1)

    for directory in ('samples', 'demos'):
        for file in sorted((ROOT / directory).glob('*.ostf')):
            value = load_json(file)
            relative = file.relative_to(ROOT).as_posix()
            examples.append(relative)
            walk(schema, value, '#', '', relative)
    enum_rows = []
    for path, node in enums.items():
        for option in node['enum']:
            enum_rows.append({'schema_pointer': path, 'value': option,
                              'examples': enum_hits[path][json.dumps(option, ensure_ascii=False)]})
    const_rows = [{'schema_pointer': path, 'value': node['const'], 'examples': const_hits[path]}
                  for path, node in constants.items()]
    rows = [{'schema_pointer': path, 'examples': hits[path]} for path in fields]
    return {
        'format_version': '3.4.0',
        'scope': 'Every finite current-Core storage property declaration and every value of its explicit enum declarations. Predicate/refinement copies and frozen legacy definitions excluded from denominator. Open strings, arbitrary map keys, all combinations and runtime behavior are not finite coverage claims.',
        'definition_counts': {'current': len(schema['$defs']) - 1,
                              'frozen_legacy': len(schema['$defs']['legacy33']['$defs'])},
        'documents': examples,
        'property_declarations': len(rows),
        'property_declarations_with_witness': sum(bool(row['examples']) for row in rows),
        'enum_values': len(enum_rows),
        'enum_values_with_witness': sum(bool(row['examples']) for row in enum_rows),
        'constant_declarations': len(const_rows),
        'constant_declarations_with_witness': sum(bool(row['examples']) for row in const_rows),
        'missing_properties': [row['schema_pointer'] for row in rows if not row['examples']],
        'missing_enum_values': [{'schema_pointer': row['schema_pointer'], 'value': row['value']} for row in enum_rows if not row['examples']],
        'fields': rows, 'enum_witnesses': enum_rows, 'constant_witnesses': const_rows,
    }


def typ(node: dict) -> str:
    if '$ref' in node:
        return node['$ref'].removeprefix('#/$defs/')
    if 'const' in node:
        return 'const ' + json.dumps(node['const'], ensure_ascii=False)
    if 'enum' in node:
        return 'enum ' + json.dumps(node['enum'], ensure_ascii=False)
    if node.get('type') == 'array':
        return 'array<' + typ(node.get('items', {})) + '>'
    return str(node.get('type', 'oneOf/anyOf' if any(k in node for k in ('oneOf', 'anyOf')) else 'schema'))


def md(text: Any) -> str:
    return str(text).replace('|', '\\|').replace('\n', '<br>')


def witness(examples: list) -> str:
    return '; '.join(f'[{x["file"]}](../{x["file"]}) `{x["pointer"]}`' for x in examples[:1]) or '—'


def generate_reference(schema: dict, coverage: dict, lang: str) -> str:
    ja = lang == 'ja'
    fields = {row['schema_pointer']: row for row in coverage['fields']}
    lines = [f'# OSTF 3.4.0 — {"全パラメーターリファレンス" if ja else "Complete Parameter Reference"}', '',
             ('正式版3.4.0。同梱Schemaから生成した全定義・全条件の一覧です。' if ja else
              'Official version 3.4.0. All definitions and constraints below are generated from the bundled schema.'), '',
             ('**構造の正本:** [JSON Schema](../schema/ostf-3.4.0.schema.json)。**意味の正本:** [正式仕様書](FORMAT_SPECIFICATION.ja.md)。[マニュアル](COMPLETE_MANUAL.ja.md)と[実例対応表](COVERAGE.md)も参照してください。' if ja else
              '**Structural authority:** [JSON Schema](../schema/ostf-3.4.0.schema.json). **Semantic authority:** [normative Japanese specification](FORMAT_SPECIFICATION.ja.md), with an [English translation](FORMAT_SPECIFICATION.en.md). See the [manual](COMPLETE_MANUAL.en.md) and [witness index](COVERAGE.md).'), '',
             ('「親内必須」は親オブジェクトが存在する場合の必須性です。任意の親を必須にしません。条件付き必須・禁止、相互必須、辞書キー、追加項目可否は各節の完全なSchemaブロックも含めて適用します。defaultは読込時に書き込む値ではありません。' if ja else
              'Required means required within a present parent object. An optional parent remains optional. Apply the full schema blocks, including conditional requirements/prohibitions, dependentRequired, dictionary key constraints and additionalProperties. A default is not an instruction to insert a value.'), '',
             (f'現行Core {coverage["definition_counts"]["current"]}定義＋ルート、互換保持用の凍結旧定義 {coverage["definition_counts"]["frozen_legacy"]}件を収録。現行の実データ宣言 {coverage["property_declarations"]}件、列挙値の宣言別実例 {coverage["enum_values"]}件を照合。旧定義を新Core機能として使いません。' if ja else
              f'Includes {coverage["definition_counts"]["current"]} current definitions plus the root and {coverage["definition_counts"]["frozen_legacy"]} frozen compatibility definitions. Covers {coverage["property_declarations"]} current storage declarations and {coverage["enum_values"]} per-declaration enum values. Legacy definitions do not define alternative current-Core authorities.'), '',
             '## '+('索引' if ja else 'Index'), '', '- [Root](#root)']
    lines += [f'- [{name}](#core-{name.lower()})' for name in schema['$defs'] if name != 'legacy33']
    lines += ['- [Frozen legacy compatibility](#frozen-legacy)', '']

    def section(name: str, node: dict, path: str, anchor: str, legacy: bool = False) -> None:
        lines.extend([f'<a id="{anchor}"></a>', f'## {name}', '', f'`{path}`', ''])
        if node.get('description'):
            lines.extend([node['description'], ''])
        required = node.get('required', [])
        lines.extend([('親内必須: ' if ja else 'Required within this object: ') + (', '.join(f'`{x}`' for x in required) or '—'), ''])
        if node.get('properties'):
            lines.extend(['| '+('項目 | 型 | 親内必須 | 明示制約・説明 | 実例' if ja else 'Property | Type | Required | Explicit constraints / description | Witness')+' |', '|---|---|---|---|---|'])
            for key, child in node['properties'].items():
                constraints = []
                for k in ('minimum','maximum','exclusiveMinimum','exclusiveMaximum','minLength','maxLength','minItems','maxItems','minProperties','maxProperties','pattern','uniqueItems','default','format'):
                    if k in child:
                        constraints.append(k+'='+json.dumps(child[k], ensure_ascii=False))
                if child.get('description'):
                    constraints.append(child['description'])
                p = path + '/properties/' + escape(key)
                hits = fields.get(p, {}).get('examples', [])
                req = ('必須' if ja else 'yes') if key in required else ('任意／条件付き' if ja else 'optional / conditional')
                lines.append(f'| `{key}` | {md(typ(child))} | {req} | {md("; ".join(constraints)) or "—"} | {witness(hits)} |')
            lines.append('')
        lines.extend([('完全な構造定義（参照は同梱Schema内のJSON Pointer）:' if ja else 'Complete structural definition (references are JSON Pointers in the bundled schema):'), '',
                      '```json', json.dumps(node, ensure_ascii=False, indent=2), '```', ''])

    section('Root', {k:v for k,v in schema.items() if k != '$defs'}, '#', 'root')
    for name, node in schema['$defs'].items():
        if name != 'legacy33':
            section(name, node, '#/$defs/'+escape(name), 'core-'+name.lower())
    lines += ['<a id="frozen-legacy"></a>', '## '+('凍結した旧拡張定義（互換保持専用）' if ja else 'Frozen legacy definitions — compatibility only'), '',
              ('次の65定義は原版の構造を維持するための閉じた領域です。現在の296宣言の実例集計には含めません。すべての旧定義が新ルートから到達可能という意味ではありません。3.4のルートに旧songや旧trackを置いてよいという意味でもありません。拡張の版が不明なら既知版と決めつけません。' if ja else
               'The following 65 definitions preserve the old structural contract. They are excluded from the 296 current-field witness denominator. Not every frozen definition is reachable from the current root, and an old song or track definition cannot substitute for its current version. Do not treat an unknown extension version as a known version.'), '',
              '[Compatibility example](../samples/49_frozen_legacy_profiles_compatibility_only.ostf)', '']
    for name, node in schema['$defs']['legacy33']['$defs'].items():
        section('legacy33 / '+name, node, '#/$defs/legacy33/$defs/'+escape(name), 'legacy-'+name.lower(), True)
    lines += ['## '+('Schemaだけでは判定できない規則' if ja else 'Rules not fully expressible in JSON Schema'), '',
              ('IDの種別横断一意性、参照解決、開始順・拍子合計、絶対時間と演算後範囲、voicingの配列同長、候補所有、原型対応、相対音の等式、依存範囲、翻訳対象field・原文存在・重複、数値トークン保持、編集の原子性は正式仕様を併読します。構造上許された値でも意味規則を満たさなければ適合しません。' if ja else
               'Also apply the normative rules for global identity, typed references, ordering, beat-group sums, arithmetic bounds, equal voicing lengths, ownership, phrase mappings, relative-pitch equations, dependencies, localization source fields/existence/uniqueness, numeric-token preservation and atomic edits. Structural acceptance alone is not full conformance.'), '',
              ('`languageMap32`は継承された汎用構造として空文字を許しますが、3.4のlocalization本文では非空翻訳を要求しています。新Coreでは両方を満たす非空の値を使います。これはSchemaの許容範囲と意味要件の区別であり、今回Schemaを書き換えたものではありません。' if ja else
               'The inherited languageMap32 shape permits empty strings, while the 3.4 normative localization rule requires nonempty translations. New Core entries must satisfy both by using nonempty values. This records the distinction between structural permissiveness and semantic requirements; the schema has not been silently altered.'), '',
              ('動作・再生・全組合せの網羅や実装認証を意味しません。' if ja else 'This is not runtime, playback, all-combination coverage or implementation certification.'), '']
    return '\n'.join(lines)


def coverage_markdown(c: dict) -> str:
    lines=['# OSTF 3.4.0 — 全項目・列挙値・サンプル対応表 / Complete Coverage Index', '',
           'Authority: [Schema](../schema/ostf-3.4.0.schema.json) and [normative specification](FORMAT_SPECIFICATION.ja.md).', '',
           '| Metric | Covered / total |','|---|---|',
           f'| Current storage-property declarations / 現行実データ宣言 | {c["property_declarations_with_witness"]} / {c["property_declarations"]} |',
           f'| Explicit enum values, per declaration / 宣言別列挙値 | {c["enum_values_with_witness"]} / {c["enum_values"]} |',
           f'| Explicit constants / 定数宣言 | {c["constant_declarations_with_witness"]} / {c["constant_declarations"]} |',
           f'| Current definitions / 現行定義 | {c["definition_counts"]["current"]} |',
           f'| Frozen compatibility definitions / 凍結互換定義 | {c["definition_counts"]["frozen_legacy"]} |',
           f'| Standalone OSTF 3.4 documents / 独立した.ostf | {len(c["documents"])} |', '',
           '**網羅の定義:** 現行Coreの有限な実データ宣言と明示enumの全値について、実ファイルとJSON Pointerを列挙します。新規項目だけではなく継承項目も含みます。条件判定・制約強化の重複宣言、凍結旧領域、任意の文字列・辞書キー、全組合せ、全数値、全実装の動作は母数に含めません。', '',
           '**Coverage boundary:** Finite current storage declarations and every explicit enum option, including inherited fields. Predicate/refinement copies, frozen legacy internals, open strings/maps, all numeric values, all combinations and runtime behavior are not claimed as exhaustively tested.', '',
           'References list all 77 current definitions plus the root and all 65 frozen definitions. [Sample index](../samples/INDEX.md) explains intentional warnings and boundary cases. [Machine-readable report](../audit/FIELD_COVERAGE.json).', '',
           '## 1. Every current storage declaration / 全実データ宣言', '',
           '| # | Schema Pointer | `.ostf` witness + JSON Pointer |','|---|---|---|']
    for index,row in enumerate(c['fields'],1):
        lines.append(f'| {index} | `{row["schema_pointer"]}` | {witness(row["examples"])} |')
    lines += ['', '## 2. Every explicit enum value / 全明示列挙値', '', '| # | Schema Pointer | Value | Witness |','|---|---|---|---|']
    for index,row in enumerate(c['enum_witnesses'],1):
        lines.append(f'| {index} | `{row["schema_pointer"]}` | `{md(json.dumps(row["value"],ensure_ascii=False))}` | {witness(row["examples"])} |')
    lines += ['', '## 3. Constants / 定数', '', '| Schema Pointer | Value | Witness |','|---|---|---|']
    for row in c['constant_witnesses']:
        lines.append(f'| `{row["schema_pointer"]}` | `{md(json.dumps(row["value"],ensure_ascii=False))}` | {witness(row["examples"])} |')
    return '\n'.join(lines)+'\n'


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    coverage = make_coverage(schema)
    (ROOT/'audit/FIELD_COVERAGE.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for lang in ('ja','en'):
        (ROOT/f'docs/PARAMETER_REFERENCE.{lang}.md').write_text(generate_reference(schema,coverage,lang),encoding='utf-8')
    (ROOT/'docs/COVERAGE.md').write_text(coverage_markdown(coverage),encoding='utf-8')
    print(f'Properties {coverage["property_declarations_with_witness"]}/{coverage["property_declarations"]}; enums {coverage["enum_values_with_witness"]}/{coverage["enum_values"]}; constants {coverage["constant_declarations_with_witness"]}/{coverage["constant_declarations"]}')
    if coverage['missing_properties'] or coverage['missing_enum_values']:
        print(json.dumps({'missing_properties':coverage['missing_properties'],'missing_enum_values':coverage['missing_enum_values']},ensure_ascii=False,indent=2))
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
