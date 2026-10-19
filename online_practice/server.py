"""MCED online practice server (all papers). Run: python server.py [port]
Scores on the server; answers/explanations are only returned after a candidate submits.
Results (host PC only): /results and /results.csv"""
import json, sys, socket, time, os, csv, io
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

D = os.path.dirname(os.path.abspath(__file__))
rd = lambda n: json.load(open(os.path.join(D, 'data', n), encoding='utf8'))
PAPERS = {str(p['id']): p for p in rd('papers.json')}
ANS = rd('answers.json')
EXP = rd('explain.json')
RES = os.path.join(D, 'results.jsonl')


def score(pid, ans):
    p = PAPERS[pid]
    subs = [[0, 0] for _ in p['subtopics']]
    for q in p['questions']:
        s = subs[q['sub']]
        s[1] += 1
        if ans.get(str(q['id'])) == ANS[pid][str(q['id'])]:
            s[0] += 1
    return subs


def rows():
    return [json.loads(l) for l in open(RES, encoding='utf8')] if os.path.exists(RES) else []


class H(BaseHTTPRequestHandler):
    def send(self, code, body, ctype='application/json', extra=None):
        b = body if isinstance(body, bytes) else body.encode('utf8')
        self.send_response(code)
        self.send_header('Content-Type', ctype + '; charset=utf-8')
        self.send_header('Content-Length', str(len(b)))
        self.send_header('Cache-Control', 'no-store')
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(b)

    def local(self):
        return self.client_address[0] in ('127.0.0.1', '::1')

    def do_GET(self):
        path = self.path.split('?')[0]
        if path in ('/', '/index.html'):
            self.send(200, open(os.path.join(D, 'index.html'), 'rb').read(), 'text/html')
        elif path == '/api/papers':
            self.send(200, json.dumps([dict(id=p['id'], title=p['title'], n=len(p['questions']), duration=p['duration']) for p in PAPERS.values()], ensure_ascii=False))
        elif path.startswith('/api/paper/'):
            p = PAPERS.get(path.rsplit('/', 1)[1])
            if not p:
                return self.send(404, '{"error":"no such paper"}')
            self.send(200, json.dumps(p, ensure_ascii=False))
        elif path in ('/results', '/results.csv'):
            if not self.local():
                return self.send(403, 'Results only on host PC.', 'text/plain')
            rs = rows()
            if path == '/results.csv':
                o = io.StringIO()
                w = csv.writer(o)
                w.writerow(['time', 'name', 'paper', 'total', 'out_of', 'elapsed_s', 'subtopic_scores'])
                for r in rs:
                    w.writerow([r['time'], r['name'], r['paper'], r['total'], r['out_of'], r['elapsed'], ' | '.join('%s: %s/%s' % (n, a, b) for n, (a, b) in zip(PAPERS[str(r['paper'])]['subtopics'], r['subs']))])
                return self.send(200, o.getvalue().encode('utf-8-sig'), 'text/csv', {'Content-Disposition': 'attachment; filename=results.csv'})
            h = ''.join('<tr><td>%s<td>%s<td>%s<td>%s/%s<td>%s<td>%s</tr>' % (
                r['time'], r['name'].replace('<', '&lt;'), r['paper'], r['total'], r['out_of'], r['elapsed'],
                '<br>'.join('%s: %s/%s' % (n, a, b) for n, (a, b) in zip(PAPERS[str(r['paper'])]['subtopics'], r['subs']))) for r in reversed(rs))
            self.send(200, "<meta name=viewport content='width=device-width'><style>body{font:14px sans-serif;padding:12px}td,th{border:1px solid #ccc;padding:5px;vertical-align:top}table{border-collapse:collapse}</style>"
                      "<h2>Results</h2><p><a href=/results.csv>Download CSV</a></p><table><tr><th>Time<th>Name<th>Paper<th>Score<th>Sec<th>Topic-wise</tr>" + h + "</table>", 'text/html')
        else:
            self.send(404, 'not found', 'text/plain')

    def do_POST(self):
        if self.path != '/api/submit':
            return self.send(404, 'nf', 'text/plain')
        try:
            d = json.loads(self.rfile.read(int(self.headers.get('Content-Length', 0))))
            pid = str(d.get('paper'))
            p = PAPERS[pid]
            name = str(d.get('name', '')).strip()[:80] or 'Anonymous'
            ans = {str(k): v for k, v in d.get('answers', {}).items() if v in ('A', 'B', 'C', 'D')}
            subs = score(pid, ans)
            total = sum(s[0] for s in subs)
            rec = dict(time=time.strftime('%Y-%m-%d %H:%M:%S'), name=name, paper=int(pid), total=total, out_of=len(p['questions']),
                       subs=subs, elapsed=int(d.get('elapsed', 0)), answers=ans)
            with open(RES, 'a', encoding='utf8') as f:
                f.write(json.dumps(rec, ensure_ascii=False) + '\n')
            review = [dict(id=q['id'], yours=ans.get(str(q['id'])), correct=ANS[pid][str(q['id'])], **EXP[pid][str(q['id'])]) for q in p['questions']]
            self.send(200, json.dumps(dict(total=total, out_of=len(p['questions']), subs=subs, review=review), ensure_ascii=False))
        except Exception as e:
            self.send(400, json.dumps({'error': str(e)}))

    def log_message(self, *a):
        pass


def ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        return s.getsockname()[0]
    except Exception:
        return '127.0.0.1'
    finally:
        s.close()


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print('Open on phone (same Wi-Fi): http://%s:%d' % (ip(), port))
    print('Results (this PC only): http://localhost:%d/results' % port, flush=True)
    ThreadingHTTPServer(('0.0.0.0', port), H).serve_forever()
