"""MCED study-app local server. Serves ../docs (the same app that runs on GitHub Pages) and stores student progress.
Run: python server.py [port]
  POST /api/progress  -> saves a student's progress snapshot (progress/<name>.json + history)
  GET  /api/progress  -> latest snapshot of every student (used by the Tutor Dashboard)
  /progress.csv       -> host PC only: one row per student (latest)"""
import json, sys, socket, os, re, time, mimetypes
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

D = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.join(os.path.dirname(D), 'docs')
PROG = os.path.join(D, 'progress')
os.makedirs(PROG, exist_ok=True)
EXT = {'.webmanifest': 'application/manifest+json', '.html': 'text/html', '.js': 'application/javascript', '.css': 'text/css', '.json': 'application/json', '.png': 'image/png', '.svg': 'image/svg+xml', '.ico': 'image/x-icon'}


def safe(name):
    return re.sub(r'[^0-9A-Za-z_\-]+', '_', name)[:60] or 'student'


def latest():
    out = []
    for f in sorted(os.listdir(PROG)):
        if f.endswith('.json'):
            try:
                out.append(json.load(open(os.path.join(PROG, f), encoding='utf8')))
            except Exception:
                pass
    return out


class H(BaseHTTPRequestHandler):
    def send(self, code, body, ctype='application/json'):
        b = body if isinstance(body, bytes) else body.encode('utf8')
        self.send_response(code)
        self.send_header('Content-Type', ctype + ('; charset=utf-8' if ctype.startswith(('text', 'application/json', 'application/javascript')) else ''))
        self.send_header('Content-Length', str(len(b)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        path = self.path.split('?')[0]
        if path == '/api/progress':
            return self.send(200, json.dumps(latest(), ensure_ascii=False))
        if path == '/progress.csv':
            if self.client_address[0] not in ('127.0.0.1', '::1'):
                return self.send(403, 'host PC only', 'text/plain')
            rows = ['name,last_update,xp,streak,lessons,plan_tasks_done,attempts,cards_known']
            for s in latest():
                rows.append('%s,%s,%s,%s,%s,%s,%s,%s' % (s['name'], time.strftime('%Y-%m-%d %H:%M', time.localtime(s['ts'] / 1000)), s['xp'], s['streak'], len(s['lessons']), len(s['tasks']), len(s['attempts']), s['cards']['known']))
            return self.send(200, '﻿' + '\n'.join(rows), 'text/csv')
        if path == '/':
            path = '/index.html'
        fp = os.path.normpath(os.path.join(WEB, path.lstrip('/')))
        if not fp.startswith(WEB) or not os.path.isfile(fp) or os.path.splitext(fp)[1] not in EXT:
            return self.send(404, 'not found', 'text/plain')
        self.send(200, open(fp, 'rb').read(), EXT[os.path.splitext(fp)[1]])

    def do_POST(self):
        if self.path != '/api/progress':
            return self.send(404, 'nf', 'text/plain')
        try:
            s = json.loads(self.rfile.read(int(self.headers.get('Content-Length', 0))))
            assert isinstance(s.get('name'), str) and isinstance(s.get('attempts'), list)
            n = safe(s['name'])
            json.dump(s, open(os.path.join(PROG, n + '.json'), 'w', encoding='utf8'), ensure_ascii=False)
            with open(os.path.join(PROG, n + '.history.jsonl'), 'a', encoding='utf8') as f:
                f.write(json.dumps({'ts': s.get('ts'), 'xp': s.get('xp'), 'attempts': len(s['attempts']), 'tasks': len(s.get('tasks', []))}) + '\n')
            self.send(200, '{"ok":true}')
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
    print('Tutor Dashboard: http://%s:%d/#/tutor   |   CSV (this PC): http://localhost:%d/progress.csv' % (ip(), port, port), flush=True)
    ThreadingHTTPServer(('0.0.0.0', port), H).serve_forever()
