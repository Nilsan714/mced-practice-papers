import sys
sys.stdout.reconfigure(encoding='utf8')
sys.path.insert(0,'content')
import importlib
n=sys.argv[1]
P=importlib.import_module('p'+n).PAPER
print(P['title'],'|',P['subtopics'],'|',P['lessons'])
for i,q in enumerate(P['questions'],1):
    print(i,q['q'],'||',' ## '.join(q['opts']),'||',q['exp'],'||',q['concept'])
for b in P['remediation']: print(b)
