"""Generate Question_Paper_Manifest (.md + .json): every generated file, per-paper stats, sources and verification status."""
import os, sys, json, hashlib, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, 'content'))
from build_docs import load_papers, names, OUT
from common import LEVELS

DESC = {'Student_Question_Paper.docx': 'Student paper (questions + options + answer table only)', 'Student_Question_Paper.pdf': 'Print-ready PDF of the student paper',
        'Teacher_Answer_Key.docx': 'Tutor-only key: answers, explanations, concepts, sources', 'Remediation_Notes.docx': 'Teaching notes: concepts, worked examples, practice + answers'}


def sha(p):
    h = hashlib.sha256()
    h.update(open(p, 'rb').read())
    return h.hexdigest()


def main():
    papers = load_papers()
    files = []
    for root, dirs, fs in os.walk(OUT):
        dirs[:] = [d for d in dirs if d not in ('__pycache__',)]
        for f in sorted(fs):
            if f in ('Question_Paper_Manifest.md', 'Question_Paper_Manifest.json') or f.endswith('.pyc') or f in ('results.jsonl', 'server.log', 'server.err'):
                continue
            p = os.path.join(root, f)
            rel = os.path.relpath(p, OUT).replace('\\', '/')
            d = next((v for k, v in DESC.items() if f.endswith(k)), '')
            if rel.startswith('_build/'):
                d = d or 'Build/validation tooling or content source'
            elif rel.startswith('online_practice/'):
                d = d or 'Online practice server (LAN) file'
            elif f.endswith('.xlsx'):
                d = 'Excel performance tracker (formulas; tutor-only, contains key)'
            elif f == 'README.md':
                d = 'Order of use, file guide, limitations'
            files.append(dict(path=rel, bytes=os.path.getsize(p), sha256=sha(p), description=d))
    pap = []
    for p in papers:
        qs = p['questions']
        pap.append(dict(no=p['no'], title=p['title'], folder='%02d_%s' % (p['no'], p['slug']), questions=len(qs), minutes=p['duration'],
                        levels={LEVELS[k]: sum(1 for q in qs if q['lvl'] == k) for k in 'FIA'},
                        answer_distribution={c: sum(1 for q in qs if q['ans'] == c) for c in 'ABCD'},
                        subtopics={s: sum(1 for q in qs if q['sub'] == i) for i, s in enumerate(p['subtopics'])},
                        numeric_questions_auto_checked=sum(1 for q in qs if q['chk']), sourced_questions=sum(1 for q in qs if q['src']),
                        worked_examples=sum(1 for b in p['remediation'] if b[0] == 'ex'),
                        sources=p['sources'], files={k: v for k, v in names(p).items()}))
    rep = json.load(open(os.path.join(HERE, 'validation_report.json'), encoding='utf8')) if os.path.exists(os.path.join(HERE, 'validation_report.json')) else {}
    man = dict(generated=time.strftime('%Y-%m-%d %H:%M'), note='Practice papers only; not official MCED papers/pattern/marks.', validation=rep, papers=pap, files=files)
    json.dump(man, open(os.path.join(OUT, 'Question_Paper_Manifest.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    md = ['# Question Paper Manifest', '', 'Generated %s. Practice papers only — not official MCED papers, pattern, marks or predictions.' % man['generated'], '',
          'Automated validation at generation: **%s errors, %s warnings** (see `_build/validation_report.json`).' % (len(rep.get('errors', [])), len(rep.get('warnings', []))), '',
          '## Papers', '', '| No | Title | Qs | Min | F/I/A | A/B/C/D | auto-checked numerics | sourced Qs | worked ex |', '|---|---|---|---|---|---|---|---|---|']
    for q in pap:
        md.append('| %d | %s | %d | %d | %s | %s | %d | %d | %d |' % (q['no'], q['title'], q['questions'], q['minutes'], '/'.join(str(v) for v in q['levels'].values()),
                  '/'.join(str(v) for v in q['answer_distribution'].values()), q['numeric_questions_auto_checked'], q['sourced_questions'], q['worked_examples']))
    md += ['', '## Sources and verification status (accessed 2026-10-19)', '', '| Paper | Key | Source | Status |', '|---|---|---|---|']
    for q in pap:
        for s in q['sources']:
            md.append('| %d | %s | [%s](%s) | %s |' % (q['no'], s['key'], s['label'].replace('|', '/'), s['url'], s['status']))
    md += ['', '## Files', '', '| File | Bytes | SHA-256 (first 12) | Purpose |', '|---|---|---|---|']
    for f in files:
        md.append('| %s | %d | %s | %s |' % (f['path'], f['bytes'], f['sha256'][:12], f['description']))
    open(os.path.join(OUT, 'Question_Paper_Manifest.md'), 'w', encoding='utf8').write('\n'.join(md) + '\n')
    print('manifest:', len(files), 'files')


if __name__ == '__main__':
    main()
