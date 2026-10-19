"""Export paper content to JSON for the online practice server (answers kept in separate files)."""
import os, sys, json, re, zipfile, html
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, 'content'))
from build_docs import load_papers, OUT
from common import LEVELS
import extras as X

WEB = os.path.join(OUT, 'docs')
DATA = os.path.join(WEB, 'data')
BASE_DIR = os.path.dirname(OUT)  # Accounting Paper
os.makedirs(DATA, exist_ok=True)


def baseline():
    qj = json.load(open(os.path.join(BASE_DIR, 'mced-quiz', 'questions.json'), encoding='utf8'))
    aj = json.load(open(os.path.join(BASE_DIR, 'mced-quiz', 'answers.json'), encoding='utf8'))
    # explanations from the supplied teacher key (read-only)
    kp = os.path.join(BASE_DIR, 'MCED_District_Account_Assistant_Teacher_Answer_Key.docx')
    exp = {}
    if os.path.exists(kp):
        x = zipfile.ZipFile(kp).read('word/document.xml').decode('utf8')
        paras = [html.unescape(''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', p))) for p in re.findall(r'<w:p[ >].*?</w:p>', x, flags=re.S)]
        for i, t in enumerate(paras):
            m = re.match(r'^(\d+)\. Answer ([A-D]):', t)
            if m and i + 1 < len(paras):
                exp[m.group(1)] = paras[i + 1]
    qs = [dict(id=q['id'], q=q['q'], opts=q['opts'], sub=q['section']) for q in qj['questions']]
    paper = dict(id=0, title='Baseline Diagnostic MCQ Test (original 40 questions)', duration=45, subtopics=qj['sections'],
                 lessons=['Papers 2-5', 'Paper 6', 'Paper 7', 'Paper 8', 'Paper 9', 'Paper 10'], questions=qs)
    ans = {str(q['id']): aj[str(q['id'])] for q in qj['questions']}
    ex = {str(q['id']): dict(exp=exp.get(str(q['id']), ''), concept='') for q in qj['questions']}
    return paper, ans, ex


def main():
    papers, answers, explain = [], {}, {}
    bp, ba, be = baseline()
    papers.append(bp)
    answers['0'], explain['0'] = ba, be
    for p in load_papers():
        qs = [dict(id=i, q=q['q'], opts=q['opts'], sub=q['sub']) for i, q in enumerate(p['questions'], 1)]
        nA = len(qs)
        for j, bq in enumerate(p.get('bank', []), 1):
            qs.append(dict(id=nA + j, q=bq['q'], opts=bq['opts'], sub=bq['sub'], b=1))
        papers.append(dict(id=p['no'], title='Paper %d: %s' % (p['no'], p['title']), duration=p['duration'], subtopics=p['subtopics'], lessons=p['lessons'], questions=qs))
        allq = list(p['questions']) + list(p.get('bank', []))
        answers[str(p['no'])] = {str(i): q['ans'] for i, q in enumerate(allq, 1)}
        explain[str(p['no'])] = {str(i): dict(exp=q['exp'], concept=q['concept']) for i, q in enumerate(allq, 1)}
    lessons = {str(p['no']): [list(b) for b in p['remediation']] for p in load_papers()}
    json.dump(lessons, open(os.path.join(DATA, 'lessons.json'), 'w', encoding='utf8'), ensure_ascii=False)
    ex = dict(exam=X.EXAM, plan=[dict(d, tasks=[list(t) for t in d['tasks']]) for d in X.PLAN], flash=[list(f) for f in X.FLASH], cheat=X.CHEAT,
              mnemonics={str(k): v for k, v in X.MNEMONICS.items()}, quotes=X.QUOTES, praise=X.PRAISE, levels=[list(l) for l in X.LEVELS], personal=X.PERSONAL)
    json.dump(ex, open(os.path.join(DATA, 'extras.json'), 'w', encoding='utf8'), ensure_ascii=False)
    json.dump(papers, open(os.path.join(DATA, 'papers.json'), 'w', encoding='utf8'), ensure_ascii=False)
    json.dump(answers, open(os.path.join(DATA, 'answers.json'), 'w', encoding='utf8'))
    json.dump(explain, open(os.path.join(DATA, 'explain.json'), 'w', encoding='utf8'), ensure_ascii=False)
    print('exported', len(papers), 'papers;', sum(len(p['questions']) for p in papers), 'questions (incl. bank); baseline explanations:', sum(1 for v in be.values() if v['exp']))


if __name__ == '__main__':
    main()
