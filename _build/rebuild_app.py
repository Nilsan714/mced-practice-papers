"""One command to refresh the study app data after editing content: python _build/rebuild_app.py
Edit messages/plan in _build/content/extras.py (Marathi) and _build/content/en/extras_en.py (English)."""
import subprocess, sys, os
here = os.path.dirname(os.path.abspath(__file__))
for s in ('validate.py', 'export_web.py', 'build_en.py'):
    r = subprocess.run([sys.executable, os.path.join(here, s), '--nofiles'] if s == 'validate.py' else [sys.executable, os.path.join(here, s)])
    if r.returncode:
        sys.exit(r.returncode)
print('App data rebuilt in docs/data. Commit and push to update the live site.')
