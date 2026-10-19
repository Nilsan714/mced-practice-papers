"""Build student paper, teacher key and remediation notes (.docx) for each paper module."""
import importlib, os, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, 'content'))
from lib_docx import Doc
from common import LEVELS

OUT = os.path.dirname(HERE)
NOTE = 'Practice paper (not an official MCED paper, pattern, marks scheme or prediction).'


def load_papers():
    papers = []
    for f in sorted(glob.glob(os.path.join(HERE, 'content', 'p[0-9][0-9].py'))):
        papers.append(importlib.import_module(os.path.basename(f)[:-3]).PAPER)
    return papers


def folder(p):
    d = os.path.join(OUT, '%02d_%s' % (p['no'], p['slug']))
    os.makedirs(d, exist_ok=True)
    return d


def names(p):
    n = '%02d_%s' % (p['no'], p['slug'])
    return dict(student='%s_Student_Question_Paper' % n, key='%s_Teacher_Answer_Key' % n, rem='%s_Remediation_Notes' % n)


def student(p):
    d = Doc('MCED Practice Paper %d - %s' % (p['no'], p['title']))
    d.title('MCED DISTRICT ACCOUNT ASSISTANT')
    d.p('Practice Paper %d: %s' % (p['no'], p['title']), bold=True, size=14, align='center', color='2F5496')
    d.p('Hindi–Marathi mix | English technical terms | Exam preparation date: 27 October 2026', italic=True, size=9, align='center')
    d.p('Candidate Name: ______________________________   Date: ______________   Attempt No.: ____', before=120)
    n = len(p['questions'])
    d.p('Suggested time: %d minutes | Total: %d questions | 1 mark each | No negative marking (practice rule)' % (p['duration'], n), bold=True, size=10)
    d.p('सूचना / Instructions: प्रत्येक प्रश्नासाठी एकच best answer निवडा. Answer key पाहू नका; आधी स्वतः सोडवा. '
        'उत्तर माहीत नसेल तर अंदाज लावा, पण शेवटी answer table मध्ये option लिहा. ' + NOTE, size=10, shade='F2F2F2')
    for i, q in enumerate(p['questions'], 1):
        d.p('%d. %s' % (i, q['q']), bold=True, keep_next=True, before=140, after=40)
        for k, o in enumerate(q['opts']):
            d.p('%s. %s' % ('ABCD'[k], o), indent=360, keep_lines=True, keep_next=(k < 3), after=20)
    d.pagebreak()
    d.h(1, 'Answer Table / उत्तरपत्रिका')
    rows = [['Q', 'Ans', 'Q', 'Ans', 'Q', 'Ans', 'Q', 'Ans']]
    per = (n + 3) // 4
    for r in range(per):
        row = []
        for c in range(4):
            qi = r + c * per + 1
            row += [str(qi) if qi <= n else '', '']
        rows.append(row)
    d.table(rows, widths=[600, 1800] * 4, center_cols=range(8), size=11)
    d.p('Candidate signature: ____________________     Tutor: ____________________', before=200)
    path = os.path.join(folder(p), names(p)['student'] + '.docx')
    d.save(path)
    return path


def key(p):
    d = Doc('Teacher Answer Key - Paper %d (TUTOR ONLY)' % p['no'])
    qs = p['questions']
    d.title('Teacher Answer Key — Paper %d' % p['no'])
    d.p(p['title'], bold=True, size=14, align='center', color='2F5496')
    d.p('हा key विद्यार्थ्याने paper submit केल्यानंतरच उघडा. ' + NOTE, size=10, shade='FFF2CC')
    d.h(2, 'Quick key')
    n = len(qs)
    per = (n + 3) // 4
    rows = [['Q', 'Ans', 'Q', 'Ans', 'Q', 'Ans', 'Q', 'Ans']]
    for r in range(per):
        row = []
        for c in range(4):
            qi = r + c * per
            row += [str(qi + 1), qs[qi]['ans']] if qi < n else ['', '']
        rows.append(row)
    d.table(rows, widths=[600, 1800] * 4, center_cols=range(8), size=11)
    d.h(2, 'Subtopic map (topic-wise analysis साठी)')
    rows = [['#', 'Subtopic', 'Questions', 'Remedial lesson']]
    for si, s in enumerate(p['subtopics']):
        nums = [str(i + 1) for i, q in enumerate(qs) if q['sub'] == si]
        rows.append([str(si + 1), s, ', '.join(nums), p['lessons'][si]])
    d.table(rows, widths=[400, 3000, 2700, 3500], size=9)
    d.h(2, 'Practice scoring rule (official नाही)')
    d.p('1 mark per correct answer; wrong/unanswered = 0; no negative marking. Total ÷ %d × 100 = %%. '
        'Candidate ला फक्त total score वरून weak/strong ठरवू नका; subtopic-wise accuracy पहा (खाली map आणि Excel tracker). '
        'Subtopic मध्ये किमान 3 questions असल्यास: <50%% = re-teach, 50–74%% = practice, ≥75%% = relatively secure (हे teaching guide आहे, official cutoff नाही).' % n, size=10)
    d.h(2, 'Error category (चूक का झाली?)')
    d.table([['Category', 'अर्थ', 'उपाय'],
             ['Conceptual', 'मूळ concept चुकला', 'Remediation Notes मधील concept पुन्हा शिकवा'],
             ['Calculation', 'concept बरोबर, गणित चुकले', 'Step-by-step पुन्हा सोडवा; similar numerical द्या'],
             ['Terminology', 'शब्द/abbreviation/full form गोंधळ', 'Glossary + flashcards'],
             ['Careless', 'माहीत होते, पण घाईत चूक', 'Re-read habit; वेळेचे नियोजन']], widths=[1800, 3600, 4200], size=9)
    d.pagebreak()
    d.h(1, 'Answers with explanations')
    for i, q in enumerate(qs, 1):
        d.p('%d. [%s | %s]' % (i, LEVELS[q['lvl']], p['subtopics'][q['sub']]), bold=True, color='2F5496', keep_next=True, before=160, after=20, size=9)
        d.p(q['q'], keep_next=True, size=10, after=20)
        for k, o in enumerate(q['opts']):
            L = 'ABCD'[k]
            d.p('%s%s. %s%s' % ('✔ ' if L == q['ans'] else '', L, o, '' if L != q['ans'] else '  ← सही उत्तर'),
                indent=360, keep_next=True, keep_lines=True, after=0, size=10, bold=(L == q['ans']))
        d.p('**Answer: %s.** %s' % (q['ans'], q['exp']), size=10, before=40, after=20)
        d.p('**Concept शिकायचा:** ' + q['concept'], size=10, after=20)
        if q.get('src'):
            d.p('**Source/Verification:** ' + q['src'], size=9, italic=True, after=20)
    d.h(1, 'Sources and verification record')
    if p['sources']:
        d.table([['Key / Source', 'URL', 'Accessed', 'Status']] + [[s['key'] + ': ' + s['label'], s['url'], s['accessed'], s['status']] for s in p['sources']],
                widths=[2800, 3700, 1100, 2000], size=8)
    else:
        d.p('या paper मध्ये बदलणारे external facts नाहीत; content stable accounting/computer concepts वर आधारित आहे.', size=10)
    d.p('Changing facts वर "as of 2026-10-19" असे नमूद आहे. जे verify झाले नाही ते confirmed म्हणून दिलेले नाही.', size=9, italic=True)
    path = os.path.join(folder(p), names(p)['key'] + '.docx')
    d.save(path)
    return path


def rem(p):
    d = Doc('Remediation Notes - Paper %d' % p['no'])
    d.title('Remediation Notes — Paper %d' % p['no'])
    d.p(p['title'], bold=True, size=14, align='center', color='2F5496')
    d.p('Tutor साठी शिकवण्याच्या नोट्स: basics → worked examples → practice. ' + NOTE, size=10, shade='FFF2CC')
    answers = []
    for blk in p['remediation']:
        t = blk[0]
        if t == 'h':
            d.h(blk[1], blk[2])
        elif t == 'p':
            d.p(blk[1], size=10.5)
        elif t == 'b':
            d.bullets(blk[1])
        elif t == 't':
            d.table(blk[1], widths=blk[2] if len(blk) > 2 else None, size=9)
        elif t == 'ex':
            d.p('Worked Example: ' + blk[1], bold=True, color='1F6E43', keep_next=True, before=140, after=20)
            d.p('**प्रश्न:** ' + blk[2], size=10, keep_next=True, after=20, indent=240)
            for line in blk[3].split('\n'):
                d.p(line, size=10, indent=480, after=10, keep_lines=True)
        elif t == 'pq':
            d.h(3, blk[1])
            for qn, (qq, opts, ans, why) in enumerate(blk[2], 1):
                d.p('P%d. %s' % (qn, qq), bold=True, size=10, keep_next=True, before=60, after=10)
                for k, o in enumerate(opts):
                    d.p('%s. %s' % ('ABCD'[k], o), indent=360, size=10, after=0, keep_next=(k < 3))
                answers.append((blk[1], qn, ans, why))
    if answers:
        d.h(2, 'Practice answers / उत्तरे (विद्यार्थ्याने प्रयत्न केल्यानंतर)')
        cur = None
        for sec, qn, ans, why in answers:
            if sec != cur:
                d.p(sec, bold=True, size=10, before=80)
                cur = sec
            d.p('P%d → **%s** — %s' % (qn, ans, why), size=10, indent=240, after=10)
    d.h(2, 'शिकवणी नंतरचा short remedial quiz')
    d.p('वरील practice questions सोडवल्यावर, सुमारे 5 questions चा short quiz घ्या (मुख्य paper मधील चुकलेल्या subtopic मधून). '
        'Quiz मध्ये ≥4/5 आले तरच पुढील कठीण topic कडे जा; अन्यथा worked examples पुन्हा करा.', size=10)
    path = os.path.join(folder(p), names(p)['rem'] + '.docx')
    d.save(path)
    return path


if __name__ == '__main__':
    only = [int(a) for a in sys.argv[1:]]
    for p in load_papers():
        if only and p['no'] not in only:
            continue
        print(p['no'], student(p), key(p), rem(p), sep='\n  ')
