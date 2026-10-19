"""Shared helpers for paper content modules."""
LEVELS = {'F': 'Foundational', 'I': 'Intermediate', 'A': 'Application'}
ACCESSED = '2026-10-19'


def Q(sub, lvl, q, opts, ans, exp, concept, chk=None, src=None):
    """sub: index into PAPER['subtopics']; lvl F/I/A; opts: 4 strings (A-D order);
    ans: 'A'-'D'; exp: explanation incl. working + why other options wrong;
    chk: python expression string; its Indian-formatted value must appear in the correct option only."""
    return dict(sub=sub, lvl=lvl, q=q, opts=opts, ans=ans, exp=exp, concept=concept, chk=chk, src=src)


def inr(n):
    """Indian digit grouping, e.g. 1234567 -> 12,34,567"""
    n = int(round(n))
    s = str(abs(n))
    if len(s) > 3:
        head, tail = s[:-3], s[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        if head:
            parts.insert(0, head)
        s = ','.join(parts) + ',' + tail
    return ('-' if n < 0 else '') + s


def S(key, label, url, status):
    """Source record. key is cited at the start of Q src text ('KEY: note').
    status: 'verified-primary' | 'verified-secondary' | 'secondary-unconfirmed' | 'static-knowledge'"""
    return dict(key=key, label=label, url=url, accessed=ACCESSED, status=status)


import re as _re


def place(qs, mapping):
    """Move the correct option of question N (1-indexed) to the given letter by swapping options.
    Refuses if the explanation refers to options by letter (would go stale)."""
    for n, L in mapping.items():
        q = qs[n - 1]
        if _re.search(r'(?<![\w/=+.-])[A-D] (ही|मध्ये|म्हणजे|चे|चा|साठी|उलट|नुसार|मात्र)', q['exp']):
            raise ValueError('Q%d explanation refers to option letters; cannot place()' % n)
        a, b = 'ABCD'.index(q['ans']), 'ABCD'.index(L)
        q['opts'][a], q['opts'][b] = q['opts'][b], q['opts'][a]
        q['ans'] = L
    return qs
