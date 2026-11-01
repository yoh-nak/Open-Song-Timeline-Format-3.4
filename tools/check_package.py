#!/usr/bin/env python3
"""Static OSTF 3.4 release-data auditor, not a DAW/renderer implementation.
Checks the documented subset of semantic constraints as well as JSON Schema.
No audio, device code, network retrieval or generation is performed.
Requires Python 3.10+ and jsonschema 4.x.
"""
from __future__ import annotations
from pathlib import Path
from decimal import Decimal
from fractions import Fraction
from collections import defaultdict
import json, sys, re
sys.dont_write_bytecode = True
import jsonschema

MAX = 9007199254740991
ROOT = Path(__file__).resolve().parents[1]
MODULES = ('relativePhrases','generation','presentation','phraseLibrary','clipChoices','localization')

def load_json(path: Path):
    def pairs(values):
        result = {}
        for key,value in values:
            if key in result: raise ValueError(f'Duplicate JSON member: {key}')
            result[key] = value
        return result
    raw=path.read_bytes()
    if raw.startswith(b'\xef\xbb\xbf'): raise ValueError('UTF-8 BOM is not allowed')
    result = json.loads(raw.decode('utf-8'), object_pairs_hook=pairs, parse_float=Decimal,
                        parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))
    def scalar_strings(value):
        if isinstance(value,str):
            if any(0xD800 <= ord(char) <= 0xDFFF for char in value):
                raise ValueError('Lone Unicode surrogate is not allowed')
        elif isinstance(value,dict):
            for key,item in value.items(): scalar_strings(key); scalar_strings(item)
        elif isinstance(value,list):
            for item in value: scalar_strings(item)
    scalar_strings(result)
    return result

def semantic_issues(d: dict) -> tuple[list[str],list[str]]:
    errors, warnings = [], []
    reg, by_id, parents = {}, {}, {}
    required_refs=defaultdict(set)
    def issue(code,detail,soft=False):
        (warnings if soft else errors).append(code+': '+str(detail))
    def current(m): return d[m]['status']=='current'
    def add(kind,o,parent=None):
        identifier=o['id'];pair=(kind,identifier)
        if identifier in by_id: issue('DUPLICATE_ID',identifier)
        by_id[identifier]=kind;reg[pair]=o
        if parent:parents[identifier]=parent
    def check_ref(kind,identifier,where,module=None):
        if module:required_refs[module].add((kind,identifier))
        o=reg.get((kind,identifier))
        if o is None:issue('UNRESOLVED_REFERENCE',f'{where}: {kind}/{identifier}',bool(module and not current(module)))
        return o
    def relation(ok,where,module):
        if not ok:issue('RELATION_MISMATCH',where,not current(module))
    def order(xs,field,where,strict=False):
        values=[x[field] for x in xs]
        if any((a>=b if strict else a>b) for a,b in zip(values,values[1:])):issue('TIME_ORDER',where)
    def range_end(o,where):
        if 'start' in o and 'duration' in o and abs(o['start']+o['duration'])>MAX:issue('END_OVERFLOW',where)
    for field,kind in [('resources','resource'),('contributors','contributor'),('soundSlots','soundSlot'),('drumKits','drumKit')]:
        for o in d.get(field,[]):add(kind,o)
    for field,kind in [('genres','genre'),('moods','mood'),('credits','credit'),('alternateTitles','alternateTitle')]:
        for o in d['song'].get(field,[]):add(kind,o)
    if 'scale' in d['song']:add('scale',d['song']['scale'])
    for field,kind in [('sections','section'),('keyChanges','keyChange')]:
        for o in d['timeline'].get(field,[]):add(kind,o)
    for field,kind in [('chords','chord'),('scales','scale')]:
        for o in d['harmony'][field]:add(kind,o)
    for t in d['tracks']:
        add('track',t)
        for c in t['clips']:
            add('clip',c,t['id'])
            for n in c['notes']:add('note',n,c['id'])
    for field,kind in [('documents','lyricDocument'),('phrases','lyricPhrase'),('units','lyricUnit'),('alignments','lyricAlignment')]:
        for o in d['lyrics'][field]:add(kind,o)
    for o in d.get('presentation',{}).get('roleDefinitions',[]):add('roleDefinition',o)
    for field,kind in [('templates','phraseTemplate'),('instances','phraseInstance')]:
        for o in d.get('phraseLibrary',{}).get(field,[]):add(kind,o)
    for g in d.get('clipChoices',{}).get('groups',[]):
        add('clipChoiceGroup',g)
        for o in g['candidates']:add('clipCandidate',o,g['id'])
    for o in d.get('generation',{}).get('processes',[]):add('generationProcess',o)
    for o in d.get('provenance',{}).get('records',[]):add('provenanceRecord',o)
    for (kind,i),o in reg.items():
        range_end(o,kind+'/'+i)
        if kind in ('chord','scale') and 'intervals' in o:
            iv=o['intervals']
            if 0 not in iv or iv!=sorted(set(iv)):issue('INTERVALS_ORDER',i)
        if kind=='chord' and 'voicing' in o:
            v=o['voicing']
            if 'velocities' in v and len(v['pitches'])!=len(v['velocities']):issue('VOICING_LENGTH',i)
        for fld in ('localizedNames','localizedTitles'):
            if fld in o and len(o[fld])!=len({x.lower() for x in o[fld]}):issue('LANGUAGE_DUPLICATE',i)
    for k,typ in [('primaryMelodyTrackId','track'),('primaryLyricDocumentId','lyricDocument')]:
        if k in d['song']:check_ref(typ,d['song'][k],'song.'+k)
    for c in d['song'].get('credits',[]):check_ref('contributor',c['contributorId'],c['id'])
    for i in d['song'].get('rights',{}).get('rightsHolderIds',[]):check_ref('contributor',i,'song.rights')
    langs=d['song'].get('languages',[])
    if len(langs)!=len({a.lower() for a in langs}):issue('LANGUAGE_DUPLICATE','song.languages')
    for o in d['song'].get('genres',[])+d['song'].get('moods',[]):
        if 'externalUri' in o and not re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:',o['externalUri']):issue('ABSOLUTE_URI',o['id'])
    lic=d['song'].get('rights',{}).get('licenseUri')
    if lic is not None and not re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:',lic):issue('ABSOLUTE_URI','licenseUri')
    tl=d['timeline']
    for fld in ('tempoChanges','meterChanges'):
        order(tl[fld],'at',fld,True)
        if tl[fld][0]['at']!=0:issue('INITIAL_EVENT',fld)
    order(tl.get('keyChanges',[]),'at','keyChanges',True)
    for m in tl['meterChanges']:
        if 'beatGroups' in m and sum(m['beatGroups'])!=m['numerator']:issue('BEAT_GROUP_SUM',m)
    origin=tl.get('barOrigin',0)
    m=tl['meterChanges'][0]
    if origin>0 and (origin>=Fraction(d['ppq']*4*m['numerator'],m['denominator']) or any(0<x['at']<origin for x in tl['meterChanges'])):issue('BAR_ORIGIN',origin)
    order(tl['sections'],'start','sections')
    if any(a['start']+a['duration']>b['start'] for a,b in zip(tl['sections'],tl['sections'][1:])):issue('SECTION_OVERLAP','sections')
    for fld in ('chords','scales'):order(d['harmony'][fld],'start',fld)
    for sc in d['harmony']['scales']:
        for r in sc.get('targets',[]):check_ref(r['type'],r['id'],sc['id'])
    for kit in d.get('drumKits',[]):
        for i in kit['soundSlotIds']:check_ref('soundSlot',i,kit['id'])
    for slot in d['soundSlots']:
        if 'midiNote' in slot and 'midiMapping' in slot and slot['midiNote']!=slot['midiMapping']['note']:issue('MIDI_MAPPING_CONFLICT',slot['id'])
    for t in d['tracks']:
        order(t['clips'],'start',t['id'])
        kit=check_ref('drumKit',t['drumKitId'],t['id']) if 'drumKitId' in t else None
        for c in t['clips']:
            order(c['notes'],'start',c['id'])
            for n in c['notes']:
                onset=c['start']+n['start'];end=onset+n['duration']
                if onset<0 or end>MAX:issue('NOTE_ABSOLUTE_TIME',n['id'])
                if 'soundSlotId' in n:
                    check_ref('soundSlot',n['soundSlotId'],n['id'])
                    if kit and n['soundSlotId'] not in kit['soundSlotIds']:issue('KIT_MEMBERSHIP',n['id'])
                    if t.get('trackType')=='melodic':issue('TRACK_TYPE',n['id'])
                elif t.get('trackType')=='drum':issue('TRACK_TYPE',n['id'])
    for p in d['lyrics']['phrases']:check_ref('lyricDocument',p['documentId'],p['id'])
    for u in d['lyrics']['units']:check_ref('lyricPhrase',u['phraseId'],u['id'])
    for a in d['lyrics']['alignments']:
        for i in a['unitIds']:check_ref('lyricUnit',i,a['id'])
        for i in a['noteIds']:check_ref('note',i,a['id'])
    # Relative assignments.
    used=set()
    for a in d.get('relativePhrases',{}).get('assignments',[]):
        mod='relativePhrases';i=a['noteId']
        if i in used:issue('DUPLICATE_ASSIGNMENT',i)
        used.add(i);n=check_ref('note',i,i,mod);kind='chord' if a['basis']=='chordTone' else 'scale';c=check_ref(kind,a['contextId'],i,mod)
        if c is not None and n is not None:
            iv=c.get('intervals',[]);root=c.get('root' if kind=='chord' else 'tonic')
            valid='pitch' in n and root is not None and 1<=a['index']<=len(iv)
            if valid:
                pc=({'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11}[root['step']]+root['alter'])%12
                valid=a['anchorPitch']%12==pc and n['pitch']==a['anchorPitch']+iv[a['index']-1]+a['chromaticOffset']
            relation(valid,i,mod)
    # Generation references, not execution.
    for p in d.get('generation',{}).get('processes',[]):
        for a in p['inputs']:
            r=a['ref'];check_ref(r['type'],r['id'],p['id'],'generation')
            if 'readRange' in a:range_end(a['readRange'],p['id'])
        for r in p['outputs']:check_ref(r['type'],r['id'],p['id'],'generation')
        for i in p['protectedNoteIds']:check_ref('note',i,p['id'],'generation')
        if 'targetRange' in p:range_end(p['targetRange'],p['id'])
    # Presentation references.
    p=d.get('presentation')
    if p:
        for sid,rid in p['sectionRoleAssignments'].items():check_ref('section',sid,'presentation','presentation');check_ref('roleDefinition',rid,'presentation','presentation')
        for rid in p['appearance']['customRoleColors']:check_ref('roleDefinition',rid,'customRoleColors','presentation')
        targets=set()
        for o in p['appearance']['objectColors']:
            r=o['target'];pair=(r['type'],r['id'])
            if pair in targets:issue('DUPLICATE_OBJECT_COLOR',pair)
            targets.add(pair);check_ref(*pair,'objectColors','presentation')
    # Phrase links; cardinalities checked without expansion.
    ph=d.get('phraseLibrary')
    if ph:
        for t in ph['templates']:
            ids=[n['id'] for n in t['notes']]
            if len(ids)!=len(set(ids)):issue('DUPLICATE_TEMPLATE_NOTE',t['id'])
            order(t['notes'],'start',t['id'])
            for n in t['notes']:
                range_end(n,t['id'])
                if 'soundSlotId' in n:check_ref('soundSlot',n['soundSlotId'],t['id'],'phraseLibrary')
        owned_clips=set();mapped=set()
        for i in ph['instances']:
            mod='phraseLibrary';tid=i['templateId'];cid=i['clipId'];t=check_ref('phraseTemplate',tid,i['id'],mod);c=check_ref('clip',cid,i['id'],mod)
            if cid in owned_clips:issue('PHRASE_CLIP_OWNERSHIP',cid)
            owned_clips.add(cid);pairs=set()
            src={n['id']:n for n in t['notes']} if t else {}
            for a in i['noteMap']:
                pair=(a['repeatIndex'],a['templateNoteId'])
                if pair in pairs:issue('PHRASE_DUPLICATE_OCCURRENCE',i['id'])
                pairs.add(pair)
                if a['noteId'] in mapped:issue('PHRASE_NOTE_OWNERSHIP',a['noteId'])
                mapped.add(a['noteId']);n=check_ref('note',a['noteId'],i['id'],mod);sn=src.get(a['templateNoteId'])
                valid=n is not None and sn is not None and t is not None and c is not None and 0<=a['repeatIndex']<i['repeatCount']
                if valid:
                    valid=parents.get(n['id'])==cid and n['start']==a['repeatIndex']*t['duration']+sn['start'] and n['duration']==sn['duration']
                    valid=valid and (n.get('pitch')==sn['pitch']+i['transpose'] if 'pitch' in sn else n.get('soundSlotId')==sn['soundSlotId'] and 'pitch' not in n)
                    if i.get('velocityMode','independent')=='linked':valid=valid and (('velocity' in n)==('velocity' in sn)) and n.get('velocity')==sn.get('velocity')
                relation(valid,i['id']+'/'+a['noteId'],mod)
            if t is not None and c is not None:
                valid=c['duration']==t['duration']*i['repeatCount'] and len(i['noteMap'])==len(t['notes'])*i['repeatCount'] and {x['noteId'] for x in i['noteMap']}=={n['id'] for n in c['notes']}
                relation(valid,i['id'],mod)
    # Clip choices.
    owner={}
    for g in d.get('clipChoices',{}).get('groups',[]):
        mod='clipChoices';selected=next((x for x in g['candidates'] if x['id']==g['selectedCandidateId']),None)
        relation(g['selectedCandidateId'] is None or selected is not None,g['id'],mod)
        if selected:check_ref('clipCandidate',selected['id'],g['id'],mod)
        selected_ids=set(selected['clipIds']) if selected else set();all_ids=set()
        for a in g['candidates']:
            all_ids.update(a['clipIds'])
            for cid in a['clipIds']:check_ref('clip',cid,g['id'],mod)
        for cid in all_ids:
            if cid in owner:issue('CHOICE_CLIP_OWNERSHIP',cid)
            owner[cid]=g['id'];c=reg.get(('clip',cid))
            if c:relation(c.get('enabled',True)==(cid in selected_ids),g['id']+'/'+cid,mod)
    # Translations: exact permitted source field, no arbitrary JSON paths.
    allowed={k:{'name'} for k in ['contributor','section','track','clip','soundSlot','drumKit','resource','phraseTemplate','clipCandidate','clipChoiceGroup','roleDefinition','genre','mood']}
    allowed.update(song={'title','subtitle','description','key.label','rights.notice'},alternateTitle={'title'},credit={'label'},lyricDocument={'title'},keyChange={'label','key.label'},scale={'label'})
    allowed['track'].add('instrument.name');seen=set()
    for a in d.get('localization',{}).get('entries',[]):
        mod='localization';target=a['target'];kind=target['kind'];identifier=target.get('id','');field=a['field'];o=d['song'] if kind=='song' else check_ref(kind,identifier,'localization',mod)
        if field not in allowed.get(kind,set()):issue('LOCALIZATION_FIELD',kind+'.'+field);continue
        value=o
        for step in field.split('.'):
            value=value.get(step) if isinstance(value,dict) else None
        relation(isinstance(value,str),kind+'/'+identifier+'/'+field,mod)
        for lang,text in a['values'].items():
            if not text:issue('LOCALIZATION_EMPTY_TRANSLATION',kind+'/'+identifier+'/'+field)
            pair=(kind,identifier,field,lang.lower())
            if pair in seen:issue('LOCALIZATION_DUPLICATE',pair)
            seen.add(pair)
            # Backward dictionaries must agree with Core translations when overlapping.
            source=o;dictionary='localizedTitles' if kind=='song' and field=='title' else 'localizedNames'
            if kind=='track' and field=='instrument.name':source=o.get('instrument',{}) if o else None
            if source is not None and ((field=='name') or (kind=='song' and field=='title') or (kind=='track' and field=='instrument.name')):
                for old_lang,old_text in source.get(dictionary,{}).items():
                    if old_lang.lower()==lang.lower() and old_text!=text:issue('LOCALIZATION_LEGACY_CONFLICT',pair)
    # Dependencies are truthful; document is the conservative default for shared relations.
    for mod in MODULES:
        if mod not in d:continue
        deps=d[mod]['dependencies'];refs=required_refs[mod]
        # Song-local translations still depend on the document even without a song Ref.
        has_song=mod=='localization' and any(x['target']['kind']=='song' for x in d[mod]['entries'])
        if deps['scope']=='none' and (refs or has_song):relation(False,mod+' dependency scope=none',mod)
        if deps['scope']=='objects':
            declared={(x['type'],x['id']) for x in deps['refs']}
            for k,i in declared:check_ref(k,i,mod+' dependencies',mod)
            relation(refs.issubset(declared) and not has_song,mod+' incomplete dependencies',mod)
    # Historical identities and current resource references.
    doc=d.get('document')
    if doc:
        seen_parents=set()
        for p in doc.get('parents',[]):
            pair=(p['documentId'],p['revisionId'])
            if pair==(doc['id'],doc['revisionId']):issue('REVISION_SELF_PARENT',pair)
            if pair in seen_parents:issue('REVISION_DUPLICATE_PARENT',pair)
            seen_parents.add(pair)
    for p in d.get('provenance',{}).get('records',[]):
        for src in p.get('sources',[]):
            if 'resourceId' in src:check_ref('resource',src['resourceId'],p['id'])
    # This auditor does not execute legacy profiles; they are schema-frozen and retained.
    legacy=d.get('extensions',{}).get('org.yohnak.player.metadata',{}).get('data',{})
    if isinstance(legacy,dict) and any(k in legacy for k in ('originalKey','genre','voicings','keyChanges')):
        warnings.append('LEGACY_NOT_AUTHORITY: legacy Player metadata is retained; Core is the only 3.4 authority.')
    return errors,warnings

def audit_document(d,schema):
    validator=jsonschema.Draft202012Validator(schema)
    errors=[f'SCHEMA /{"/".join(map(str,e.absolute_path))}: {e.message}' for e in validator.iter_errors(d)]
    if errors:return errors,[]
    return semantic_issues(d)

def collect_checks() -> dict:
    schema=load_json(ROOT/'schema/ostf-3.4.0.schema.json')
    jsonschema.Draft202012Validator.check_schema(schema)
    records=[]
    for directory in ('samples','demos'):
        for p in sorted((ROOT/directory).glob('*.ostf')):
            try:
                d=load_json(p);errors,warnings=audit_document(d,schema)
            except Exception as exc:errors=[f'INPUT: {exc}'];warnings=[]
            records.append({'file':p.relative_to(ROOT).as_posix(),'errors':errors,'warnings':warnings})
    negatives=[]
    for c in load_json(ROOT/'audit/NEGATIVE_CASES.json')['cases']:
        errors,warnings=audit_document(c['document'],schema)
        actual='schema' if any(x.startswith('SCHEMA ') for x in errors) else 'semantic' if errors else 'accepted'
        negatives.append({'name':c['name'],'expected':c['expected'],'actual':actual,'matches':actual==c['expected'],'diagnostics':errors})
    passed=not any(r['errors'] for r in records) and all(x['matches'] for x in negatives)
    result={'scope':'Static JSON and selected specification-invariant checks only. No device, renderer, generator or DAW execution. Not a full general-purpose OSTF validator.','schema_meta_valid':True,'positive_documents':records,'negative_cases':negatives,'pass':passed}
    return result

def main() -> int:
    result=collect_checks()
    records=result['positive_documents']; negatives=result['negative_cases']; passed=result['pass']
    print(f'Positive documents: {len(records)}; with errors: {sum(bool(x["errors"]) for x in records)}')
    print(f'Negative cases: {len(negatives)}; unexpected results: {sum(not x["matches"] for x in negatives)}')
    for r in records:
        if r['errors']:print(r['file'],r['errors'][:4])
    for r in negatives:
        if not r['matches']:print(r['name'],r['expected'],r['actual'])
    return 0 if passed else 1

if __name__=='__main__':sys.exit(main())
