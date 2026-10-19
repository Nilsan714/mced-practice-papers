"""Build docs/data/en/*.json (English overlay) from content/en/e*.py and validate it against the Marathi data."""
import os, sys, json, re, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, 'content'))
sys.path.insert(0, os.path.join(HERE, 'content', 'en'))
from build_docs import OUT, load_papers
import extras as X
import extras_en as XE

DATA = os.path.join(OUT, 'docs', 'data')
EN_DIR = os.path.join(DATA, 'en')
os.makedirs(EN_DIR, exist_ok=True)
rd = lambda n: json.load(open(os.path.join(DATA, n + '.json'), encoding='utf8'))
nums = lambda s: sorted(t.rstrip('.,') for t in re.findall(r'\d[\d,\.]*', s.replace('₹', '')))
errs = []


def main():
    papers, explain, lessons = rd('papers'), rd('explain'), rd('lessons')
    BANK = {q['no']: q.get('bank', []) for q in load_papers()}
    P_en, E_en, L_en = [], {}, {}
    for p in papers:
        pid = p['id']
        EN = importlib.import_module('e%02d' % pid).EN
        nA = len(EN['qs'])
        bank = BANK.get(pid, [])
        if nA + len(bank) != len(p['questions']):
            errs.append('P%d: question count %d (+%d bank) != %d' % (pid, nA, len(bank), len(p['questions'])))
            continue
        qs, ex = [], {}
        for q, (qt, opts, exp, concept) in zip(p['questions'][:nA], EN['qs']):
            o = opts if opts is not None else q['opts']
            if len(o) != 4:
                errs.append('P%d Q%d: opts != 4' % (pid, q['id']))
            if opts is not None:
                for k in range(4):
                    if nums(opts[k]) != nums(q['opts'][k]):
                        errs.append('P%d Q%d opt %s numbers differ: %r vs %r' % (pid, q['id'], 'ABCD'[k], q['opts'][k], opts[k]))
            if {t for t in nums(qt) if len(t) > 1} != {t for t in nums(q['q']) if len(t) > 1}:
                errs.append('P%d Q%d question numbers differ' % (pid, q['id']))
            qs.append(dict(id=q['id'], q=qt, opts=o, sub=q['sub']))
            base = explain[str(pid)][str(q['id'])]
            ex[str(q['id'])] = dict(exp=exp, concept=concept or base.get('concept', ''))
        for q, bq in zip(p['questions'][nA:], bank):
            qs.append(dict(id=q['id'], q=bq['en']['q'], opts=bq['en']['opts'], sub=q['sub'], b=1))
            ex[str(q['id'])] = dict(exp=bq['en']['exp'], concept=bq['en']['concept'])
        P_en.append(dict(id=pid, title=('Paper %d: %s' % (pid, EN['title'])) if pid else EN['title'], duration=p['duration'], subtopics=EN['subtopics'], lessons=EN['lessons'], questions=qs))
        E_en[str(pid)] = ex
        if pid:
            mr = lessons[str(pid)]
            en = EN['rem']
            if len(mr) != len(en):
                errs.append('P%d: lesson blocks %d != %d' % (pid, len(en), len(mr)))
                continue
            out = []
            for bi, (a, b) in enumerate(zip(mr, en)):
                if a[0] != b[0]:
                    errs.append('P%d block %d type %s != %s' % (pid, bi, a[0], b[0]))
                    continue
                if a[0] == 'pq':
                    items = []
                    if len(a[2]) != len(b[2]):
                        errs.append('P%d pq count mismatch' % pid)
                    for (aq, aopts, aans, awhy), (bq, bopts, bans, bwhy) in zip(a[2], b[2]):
                        if aans != bans:
                            errs.append('P%d practice answer mismatch %r' % (pid, bq))
                        items.append([bq, bopts if bopts is not None else aopts, aans, bwhy])
                    out.append(['pq', b[1], items])
                elif a[0] == 't':
                    if len(a[1]) != len(b[1]) or any(len(r1) != len(r2) for r1, r2 in zip(a[1], b[1])):
                        errs.append('P%d table shape mismatch at block %d' % (pid, bi))
                    out.append(list(b))
                elif a[0] == 'b':
                    if len(a[1]) != len(b[1]):
                        errs.append('P%d bullet count mismatch at block %d' % (pid, bi))
                    out.append(list(b))
                elif a[0] == 'ex':
                    if len(a[3].split('\n')) != len(b[3].split('\n')):
                        errs.append('P%d example line count mismatch at block %d' % (pid, bi))
                    out.append(list(b))
                else:
                    out.append(list(b))
            L_en[str(pid)] = out
    # extras
    ex_mr = rd('extras')
    plan = []
    for d in ex_mr['plan']:
        t, g = XE.PLAN_TXT[d['date']]
        tasks = []
        for tk in d['tasks']:
            if tk[0] not in XE.TASK_TXT:
                errs.append('missing English task text %s' % tk[0])
            tasks.append([tk[0], tk[1], tk[2], XE.TASK_TXT.get(tk[0], tk[3])])
        plan.append(dict(date=d['date'], title=t, goal=g, tasks=tasks))
    if len(XE.FLASH) != len(ex_mr['flash']):
        errs.append('flashcards %d != %d' % (len(XE.FLASH), len(ex_mr['flash'])))
    else:
        for a, b in zip(ex_mr['flash'], XE.FLASH):
            if a[0] != b[0]:
                errs.append('flashcard topic mismatch %r' % (b[1],))
    if len(XE.CHEAT) != len(ex_mr['cheat']) or any(len(a['rows']) != len(b['rows']) for a, b in zip(ex_mr['cheat'], XE.CHEAT)):
        errs.append('cheat sheet shape mismatch')
    if len(XE.QUOTES) != len(ex_mr['quotes']) or len(XE.PERSONAL['daily']) != len(ex_mr['personal']['daily']):
        errs.append('quotes/personal count mismatch')
    ex_en = dict(exam=XE.EXAM, plan=plan, flash=[list(f) for f in XE.FLASH], cheat=XE.CHEAT, mnemonics={str(k): v for k, v in XE.MNEMONICS.items()},
                 quotes=XE.QUOTES, praise=XE.PRAISE, levels=ex_mr['levels'], personal=XE.PERSONAL)
    for n, o in (('papers', P_en), ('explain', E_en), ('lessons', L_en), ('extras', ex_en)):
        json.dump(o, open(os.path.join(EN_DIR, n + '.json'), 'w', encoding='utf8'), ensure_ascii=False)
    print('ENGLISH BUILD:', len(errs), 'errors;', sum(len(p['questions']) for p in P_en), 'questions;', len(L_en), 'lessons')
    for e in errs:
        print('ERROR', e)
    return 1 if errs else 0


if __name__ == '__main__':
    sys.exit(main())
