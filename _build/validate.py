"""Automated validation of paper content + generated files. Exit code 1 on any ERROR."""
import os, sys, re, zipfile, html, difflib, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, 'content'))
from build_docs import load_papers, names, OUT
from common import inr

errs, warns = [], []
E = lambda m: errs.append(m)
W = lambda m: warns.append(m)


def docx_text(path):
    x = zipfile.ZipFile(path).read('word/document.xml').decode('utf8')
    return html.unescape('\n'.join(''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', p)) for p in re.findall(r'<w:p[ >].*?</w:p>', x, flags=re.S)))


def norm(s):
    return re.sub(r'[^\w]+', ' ', s.lower()).strip()


def main(files=True):
    papers = load_papers()
    seen = []
    lv = {'F': 0, 'I': 1, 'A': 2}
    for p in papers:
        t = 'P%02d' % p['no']
        qs = p['questions']
        keys = {s['key'] for s in p['sources']}
        cited = set()
        if not (20 <= len(qs) <= 40):
            W('%s: %d questions (target 20-25 per brief; mixed mock may be larger)' % (t, len(qs)))
        if len(p['subtopics']) != len(p['lessons']):
            E('%s: subtopics/lessons length mismatch' % t)
        last = -1
        for i, q in enumerate(qs, 1):
            tag = '%s Q%d' % (t, i)
            if len(q['opts']) != 4:
                E('%s: needs exactly 4 options (has %d)' % (tag, len(q['opts'])))
                continue
            if any(not str(o).strip() for o in q['opts']):
                E('%s: empty option' % tag)
            if len({norm(o) for o in q['opts']}) != 4:
                E('%s: duplicate options' % tag)
            if q['ans'] not in 'ABCD' or len(q['ans']) != 1:
                E('%s: invalid answer letter %r' % (tag, q['ans']))
                continue
            if not q['exp'].strip() or not q['concept'].strip():
                E('%s: missing explanation/concept' % tag)
            if not (0 <= q['sub'] < len(p['subtopics'])):
                E('%s: bad subtopic index' % tag)
            if q['lvl'] not in lv:
                E('%s: bad level' % tag)
            elif lv[q['lvl']] < last:
                E('%s: difficulty not progressive (%s after higher level)' % (tag, q['lvl']))
            else:
                last = lv[q['lvl']]
            if q['chk']:
                val = eval(q['chk'], {'__builtins__': {}}, {})
                f = inr(val)
                ci = 'ABCD'.index(q['ans'])
                good = re.search(r'(?<![\d,])' + re.escape(f) + r'(?![\d,])', q['opts'][ci])
                bad = [k for k, o in enumerate(q['opts']) if k != ci and re.search(r'(?<![\d,])' + re.escape(f) + r'(?![\d,])', o)]
                if not good:
                    E('%s: calc %s = %s not found in correct option %s' % (tag, q['chk'], f, q['ans']))
                if bad:
                    W('%s: calculated value also appears in distractor(s) %s (ok only if intentional e.g. Dr vs Cr)' % (tag, bad))
                if f not in q['exp'] and inr(val).replace(',', '') not in q['exp'].replace(',', ''):
                    W('%s: explanation does not show computed value %s' % (tag, f))
            if q['src']:
                k = q['src'].split(':')[0].strip()
                if k not in keys:
                    E('%s: source key %r not in sources list' % (tag, k))
                cited.add(k)
            n = norm(q['q'])
            for (pt, ot) in seen:
                r = difflib.SequenceMatcher(None, n, ot).ratio()
                if r > 0.82 and len(n) > 45:
                    E('%s: near-duplicate of %s (ratio %.2f)' % (tag, pt, r))
            seen.append((tag, n))
        for s in p['sources']:
            if not s['url'].startswith('http'):
                E('%s: source %s has bad URL' % (t, s['key']))
            if s['key'] not in cited:
                W('%s: source %s is never cited by a question' % (t, s['key']))
        # answer distribution
        dist = {c: sum(1 for q in qs if q['ans'] == c) for c in 'ABCD'}
        if max(dist.values()) > 0.4 * len(qs):
            W('%s: answer letters skewed %s' % (t, dist))
        if files:
            nm = names(p)
            d = os.path.join(OUT, '%02d_%s' % (p['no'], p['slug']))
            for k, ext in (('student', 'docx'), ('student', 'pdf'), ('key', 'docx'), ('rem', 'docx')):
                if not os.path.exists(os.path.join(d, nm[k] + '.' + ext)):
                    E('%s: missing file %s.%s' % (t, nm[k], ext))
            sp = os.path.join(d, nm['student'] + '.docx')
            kp = os.path.join(d, nm['key'] + '.docx')
            if os.path.exists(sp):
                st = docx_text(sp)
                for bad in ('सही उत्तर', 'Answer:', '✔', 'Teacher Answer Key', 'Concept शिकायचा'):
                    if bad in st:
                        E('%s: student paper leaks %r' % (t, bad))
                for q in qs:
                    if q['exp'][:40] in st:
                        E('%s: student paper contains explanation text' % t)
                        break
                nq = len(re.findall(r'^\d+\. ', st, flags=re.M))
                if nq != len(qs):
                    E('%s: student paper has %d numbered questions, expected %d' % (t, nq, len(qs)))
                for k in range(1, len(qs) + 1):
                    if not re.search(r'^%d\. ' % k, st, flags=re.M):
                        E('%s: student paper missing question number %d' % (t, k))
            if os.path.exists(kp):
                kt = docx_text(kp)
                got = re.findall(r'^(\d+)\.\s*\[.*?\]\n', kt, flags=re.M)
                ans = re.findall(r'Answer: ([A-D])\.', kt)
                if len(ans) != len(qs):
                    E('%s: key has %d answer entries, expected %d' % (t, len(ans), len(qs)))
                else:
                    for i, (a, q) in enumerate(zip(ans, qs), 1):
                        if a != q['ans']:
                            E('%s Q%d: key file letter %s != data %s' % (t, i, a, q['ans']))
            pdf = os.path.join(d, nm['student'] + '.pdf')
            if os.path.exists(pdf):
                import pymupdf
                doc = pymupdf.open(pdf)
                txt = ''.join(pg.get_text() for pg in doc)
                if len(doc) < 2:
                    E('%s: pdf has <2 pages' % t)
                for bad in ('Answer:', 'सही उत्तर'):
                    if bad in txt:
                        E('%s: student PDF leaks %r' % (t, bad))
    print('ERRORS: %d   WARNINGS: %d' % (len(errs), len(warns)))
    for m in errs:
        print('ERROR  ', m)
    for m in warns:
        print('warning', m)
    json.dump({'errors': errs, 'warnings': warns, 'papers': len(papers), 'questions': sum(len(p['questions']) for p in papers)},
              open(os.path.join(HERE, 'validation_report.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    return 1 if errs else 0


if __name__ == '__main__':
    sys.exit(main(files='--nofiles' not in sys.argv))
