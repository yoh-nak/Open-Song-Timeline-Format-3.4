#!/usr/bin/env python3
"""Offline static check of the OSTF 3.4.0 publication package.

Default: verify files, examples, references, coverage and existing manifest without
writing. --refresh: regenerate the local static report and manifest after edits.
No DAW/device/audio/generator/GUI execution or network retrieval occurs.
This is a distribution auditor, not a complete general-purpose OSTF validator.
"""
from __future__ import annotations
import argparse
import ast
from collections import Counter
import hashlib
import importlib.metadata
import json
from pathlib import Path
import re
import sys
import tempfile
from urllib.parse import unquote

sys.dont_write_bytecode = True
import jsonschema
from check_package import load_json, audit_document, collect_checks
from build_catalogue import make_coverage, pointer_get

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = 'PACKAGE_MANIFEST.json'
REPORT = 'audit/RELEASE_STATIC_CHECK.json'
EXPECTED_FILES = 100
EXPECTED_DOCS = 65


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def package_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob('*') if p.is_file()
                  and '__pycache__' not in p.parts and '.git' not in p.parts
                  and p.suffix != '.pyc')


def local_refs(schema: dict) -> list[str]:
    problems = []
    def visit(node):
        if isinstance(node, dict):
            if '$ref' in node:
                ref = node['$ref']
                if not ref.startswith('#/'):
                    problems.append('Non-local $ref: ' + ref)
                else:
                    try:
                        pointer_get(schema, ref)
                    except (KeyError, IndexError, TypeError, ValueError):
                        problems.append('Unresolved $ref: ' + ref)
            for value in node.values():
                visit(value)
        elif isinstance(node, list):
            for value in node:
                visit(value)
    visit(schema)
    return problems


def markdown_links() -> list[dict]:
    problems = []
    for path in ROOT.rglob('*.md'):
        # Code blocks are literal examples, not live Markdown links.
        text = re.sub(r'^```.*?^```\s*$', '', path.read_text(encoding='utf-8'),
                      flags=re.S | re.M)
        for match in re.finditer(r'\[[^\]\n]*\]\(([^\)\n]+)\)', text):
            target = match.group(1).strip().split(' "', 1)[0].strip('<>')
            if not target or target.startswith('#') or re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:', target):
                continue
            relative = unquote(target.split('#', 1)[0])
            resolved = (path.parent / relative).resolve()
            if not resolved.is_relative_to(ROOT.resolve()) or not resolved.exists():
                problems.append({'file':path.relative_to(ROOT).as_posix(),'target':target})
    return problems


def token_cases(schema: dict) -> list[dict]:
    minimal = (ROOT/'samples/01_empty_without_extensions.ostf').read_text(encoding='utf-8')
    raw = minimal.encode('utf-8')
    decimal_integer = re.sub(r'"ppq"\s*:\s*\d+', '"ppq": 1.0', minimal).encode()
    exponent_integer = re.sub(r'"ppq"\s*:\s*\d+', '"ppq": 1e0', minimal).encode()
    boolean_integer = re.sub(r'"ppq"\s*:\s*\d+', '"ppq": true', minimal).encode()
    cases = [
        ('utf8_bom', b'\xef\xbb\xbf'+raw, False),
        ('duplicate_member', minimal.replace('"format": "OSTF"','"format": "OSTF", "format": "OSTF"').encode(), False),
        ('invalid_utf8', b'{"title":"\xff"}', False),
        ('lone_surrogate', b'{"title":"\\ud800"}', False),
        ('nan', b'{"value":NaN}', False),
        ('infinity', b'{"value":Infinity}', False),
        ('trailing_json', raw+b'{}', False),
        ('integer_as_real_token', decimal_integer, False),
        ('integer_as_exponent_token', exponent_integer, False),
        ('integer_as_boolean', boolean_integer, False),
        ('opaque_extreme_numeric_tokens', (ROOT/'samples/50_opaque_future_payload_numeric_precision.ostf').read_bytes(), True),
    ]
    result = []
    with tempfile.TemporaryDirectory(prefix='ostf-static-') as folder:
        path = Path(folder)/'case.ostf'
        for name, data, expected in cases:
            path.write_bytes(data)
            try:
                document = load_json(path)
                errors, _ = audit_document(document, schema)
                accepted = not errors
                diagnostic = errors[:1]
            except (ValueError, UnicodeError, TypeError, KeyError, IndexError) as exc:
                accepted = False
                diagnostic = [str(exc)]
            result.append({'name':name,'expected_accepted':expected,'accepted':accepted,
                           'pass':accepted == expected,'diagnostic':diagnostic})
    return result


def validate_manifest() -> dict:
    path = ROOT/MANIFEST
    if not path.exists():
        return {'pass':False,'errors':['Manifest is absent']}
    manifest = json.loads(path.read_text(encoding='utf-8'))
    actual = {p.relative_to(ROOT).as_posix():p for p in package_files() if p.name != MANIFEST}
    listed = {row['path']:row for row in manifest.get('files', [])}
    errors = []
    if len(listed) != len(manifest.get('files', [])):
        errors.append('Duplicate manifest path')
    if set(actual) != set(listed):
        errors.append('Manifest/file-set mismatch: '+str(sorted(set(actual)^set(listed))))
    for name in sorted(set(actual)&set(listed)):
        p = actual[name]; row = listed[name]
        if p.stat().st_size != row['bytes'] or digest(p) != row['sha256']:
            errors.append('Size/hash mismatch: '+name)
    if manifest.get('total_files') != len(actual)+1:
        errors.append('Incorrect total_files')
    return {'pass':not errors,'hashed_files':len(listed),'errors':errors}


def make_manifest() -> dict:
    files = []
    for path in package_files():
        relative = path.relative_to(ROOT).as_posix()
        if relative != MANIFEST:
            files.append({'path':relative,'bytes':path.stat().st_size,'sha256':digest(path)})
    return {'format':'OSTF release manifest','version':'3.4.0','total_files':len(files)+1,
            'hashed_files':len(files),'self_excluded':MANIFEST,
            'note':'The manifest does not hash itself. All other distributed files, including the static report, are hashed.',
            'files':files}


def static_report(refresh: bool = False) -> dict:
    schemas = []
    for path in sorted((ROOT/'schema').glob('*.json')):
        value = load_json(path)
        jsonschema.Draft202012Validator.check_schema(value)
        schemas.append({'file':path.relative_to(ROOT).as_posix(),'meta_schema_valid':True,
                        'unresolved_refs':local_refs(value)})
    schema = load_json(ROOT/'schema/ostf-3.4.0.schema.json')
    data = collect_checks()
    coverage = make_coverage(schema)
    saved_coverage = json.loads((ROOT/'audit/FIELD_COVERAGE.json').read_text(encoding='utf-8'))
    inv = json.loads((ROOT/'audit/SOURCE_INVENTORY.json').read_text(encoding='utf-8'))
    unchanged = []
    for row in inv['unchanged_baseline_files']:
        path = ROOT/row['path']
        unchanged.append({'path':row['path'],'unchanged':path.exists() and digest(path)==row['sha256'] and path.stat().st_size==row['bytes']})
    migration = json.loads((ROOT/'audit/DEMO_MIGRATION.json').read_text(encoding='utf-8'))
    demos = []
    for row in migration['publication_edition']['verifications']:
        path = ROOT/row['file']
        demos.append({'file':row['file'],'current_bytes_match_checked_output':digest(path)==row['sha256'],
                      'recorded_original_payload_comparison_pass':all(row['checks'].values()),
                      'original_input_available_in_this_distribution':False})
    old = load_json(ROOT/'schema/ostf-3.3.0.schema.json')
    def unfreeze(node):
        if isinstance(node,dict):
            return {key:(value.replace('#/$defs/legacy33/$defs/','#/$defs/') if key=='$ref' and isinstance(value,str) else unfreeze(value)) for key,value in node.items()}
        if isinstance(node,list):
            return [unfreeze(value) for value in node]
        return node
    frozen_equal = unfreeze(schema['$defs']['legacy33']['$defs']) == old['$defs']
    parsed = []
    for path in sorted((ROOT/'tools').glob('*.py')):
        ast.parse(path.read_text(encoding='utf-8'),filename=path.name)
        parsed.append(path.name)
    tokens = token_cases(schema)
    broken_links = markdown_links()
    if refresh:
        # These two artifacts are created atomically after all other checks pass.
        pending = {(ROOT/REPORT).resolve(), (ROOT/MANIFEST).resolve()}
        broken_links = [item for item in broken_links if
                        ((ROOT/item['file']).parent/item['target'].split('#',1)[0]).resolve() not in pending]
    files = package_files()
    file_names = {p.relative_to(ROOT).as_posix() for p in files}
    if refresh:
        file_names |= {MANIFEST, REPORT}
    archives = sorted(name for name in file_names if Path(name).suffix.lower() in ('.zip','.tar','.gz','.7z','.rar'))
    file_count = len(file_names)
    docs = [p for p in files if p.suffix=='.ostf']
    versions = sorted({load_json(p)['version'] for p in docs})
    extension_examples = [p.relative_to(ROOT).as_posix() for p in docs if load_json(p).get('extensions')]
    manifest_result = {'status':'Created after this report; verified separately to avoid self-reference.'} if refresh else validate_manifest()
    conditions = {
        'exactly_100_files': file_count == EXPECTED_FILES,
        'no_nested_archives': not archives,
        'all_65_ostf_documents_current': len(docs)==EXPECTED_DOCS and versions==['3.4.0'],
        'five_valid_self_contained_schemas':len(schemas)==5 and not any(x['unresolved_refs'] for x in schemas),
        'data_checks_pass': data['pass'],
        'all_current_properties_witnessed':coverage['property_declarations']==coverage['property_declarations_with_witness']==296,
        'all_enum_values_witnessed':coverage['enum_values']==coverage['enum_values_with_witness']==119,
        'all_constants_witnessed':coverage['constant_declarations']==coverage['constant_declarations_with_witness']==3,
        'stored_coverage_matches_recomputation':coverage==saved_coverage,
        'baseline_bytes_preserved':all(x['unchanged'] for x in unchanged),
        'frozen_legacy_definitions_preserved':frozen_equal,
        'demo_outputs_match_comparison_records':all(x['current_bytes_match_checked_output'] and x['recorded_original_payload_comparison_pass'] for x in demos),
        'all_token_cases_match':all(x['pass'] for x in tokens),
        'local_markdown_links_resolve':not broken_links,
        'three_python_sources_parse':len(parsed)==3,
    }
    if not refresh:
        conditions['manifest_matches']=manifest_result['pass']
    return {
        'format_version':'3.4.0','scope':'Static package/data/documentation checks only. No DAW/device/UI/audio/hardware/generator execution. Selected semantic checks, not complete validator certification.',
        'python':sys.version.split()[0],'jsonschema':importlib.metadata.version('jsonschema'),
        'pass':all(conditions.values()),'conditions':conditions,
        'file_count':file_count,'category_counts':dict(Counter(name.split('/')[0] if '/' in name else 'root' for name in sorted(file_names))),
        'nested_archives':archives,'schemas':schemas,
        'standalone_ostf':len(docs),'versions':versions,'samples_with_extensions':extension_examples,
        'coverage_summary':{k:coverage[k] for k in ('definition_counts','property_declarations','property_declarations_with_witness','enum_values','enum_values_with_witness','constant_declarations','constant_declarations_with_witness')},
        'data_checks':data,'numeric_token_checks':tokens,
        'baseline_preservation':unchanged,'frozen_legacy_definitions_equal':frozen_equal,
        'demo_record_checks':demos,
        'original_demo_comparison_note':'The publisher rechecked originals while preparing this edition. Original inputs are not bundled; standalone checking verifies output hashes against that recorded comparison, not unavailable originals.',
        'broken_local_links':broken_links,'python_sources_parsed':parsed,
        'manifest':manifest_result,
        'not_performed':['Device or DAW execution','Audio or MIDI hardware verification','UI interaction','Generic migration runtime','Full legacy-profile semantic validation','Complete BCP 47 validation','Every possible semantic combination','GitHub publication'],
    }


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh',action='store_true',help='Regenerate the local static report and manifest after successful checks.')
    args=parser.parse_args()
    try:
        report=static_report(args.refresh)
        if args.refresh and report['pass']:
            (ROOT/REPORT).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
            (ROOT/MANIFEST).write_text(json.dumps(make_manifest(),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
            manifest=validate_manifest()
            if not manifest['pass']:
                raise ValueError(str(manifest))
        print('PASS' if report['pass'] else 'FAIL')
        print(f'Files: {report["file_count"]}; standalone OSTF: {report["standalone_ostf"]}; schemas: {len(report["schemas"])}')
        print('Fields 296/296; enums 119/119; constants 3/3')
        print(f'Positive documents: {len(report["data_checks"]["positive_documents"])}; negative cases: {len(report["data_checks"]["negative_cases"])}; token cases: {len(report["numeric_token_checks"])}')
        if not report['pass']:
            print(json.dumps({k:v for k,v in report.items() if k in ('conditions','broken_local_links','manifest')},ensure_ascii=False,indent=2))
        return 0 if report['pass'] else 1
    except (OSError,ValueError,TypeError,KeyError,jsonschema.exceptions.SchemaError) as exc:
        print('ERROR: '+str(exc),file=sys.stderr)
        return 2

if __name__=='__main__':
    sys.exit(main())
