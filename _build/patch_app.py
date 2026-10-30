# -*- coding: utf-8 -*-
import os

DOCS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'docs')

# 1. Patch docs/index.html
index_path = os.path.join(DOCS, 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Update title
html = html.replace('<title>MCED तयारी</title>', '<title>MCED मुलाखत प्रशिक्षक (Oral Interview Coach)</title>')

# Update nav
old_nav = '''<nav class="nav" id="nav">
<a href="#/home" data-n="home"><span>🏠</span>होम</a><a href="#/plan" data-n="plan"><span>📅</span>प्लॅन</a>
<a href="#/learn" data-n="learn"><span>📚</span>शिका</a><a href="#/papers" data-n="papers"><span>✍️</span>सराव</a><a href="#/more" data-n="more"><span>☰</span>अधिक</a>
</nav>'''

new_nav = '''<nav class="nav" id="nav">
<a href="#/coach" data-n="coach"><span>🎙️</span>मुलाखत</a>
<a href="#/mock" data-n="mock"><span>🏆</span>Mock 20M</a>
<a href="#/plan" data-n="plan"><span>📅</span>१४-दिवस</a>
<a href="#/syllabus" data-n="syllabus"><span>📚</span>Syllabus</a>
<a href="#/profile" data-n="more"><span>👤</span>प्रोफाइल</a>
</nav>'''
html = html.replace(old_nav, new_nav)

# Add script tags
old_scripts = '<script src="js/tutor.js"></script>'
new_scripts = '''<script src="js/tutor.js"></script>
<script src="js/interview_data.js"></script>
<script src="js/interview_coach.js"></script>
<script src="js/interview_views.js"></script>'''

if 'interview_views.js' not in html:
    html = html.replace(old_scripts, new_scripts)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print('Patched docs/index.html')

# 2. Patch docs/js/core.js
core_path = os.path.join(DOCS, 'js', 'core.js')
with open(core_path, 'r', encoding='utf-8') as f:
    core = f.read()

core = core.replace(
    "const map = { home: 'home', plan: 'plan', learn: 'learn', lesson: 'learn', check: 'learn', papers: 'papers', exam: 'papers', practice: 'papers', weak: 'papers', result: 'papers' }; const k = TUTOR_MODE ? 'tutor' : (map[n] || 'more');",
    "const map = { coach: 'coach', mock: 'mock', plan: 'plan', syllabus: 'syllabus', more: 'more', profile: 'more', home: 'coach', learn: 'syllabus', papers: 'syllabus' }; const k = TUTOR_MODE ? 'tutor' : (map[n] || 'coach');"
)

core = core.replace(
    "const h = location.hash.replace(/^#\\/?/, '') || 'home', [n, ...a] = h.split('/');",
    "const rawH = location.hash.replace(/^#\\/?/, ''); const h = (!rawH || rawH === 'home') ? 'coach' : rawH; const [n, ...a] = h.split('/');"
)

core = core.replace(
    "try { (V[n] || V.home)(...a) }",
    "try { (V[n] || V.coach || V.home)(...a) }"
)

core = core.replace(
    "location.hash = '#/home'; route()",
    "location.hash = '#/coach'; route()"
)

with open(core_path, 'w', encoding='utf-8') as f:
    f.write(core)
print('Patched docs/js/core.js')

# 3. Patch docs/tutor.html to also include interview data and coach reports
tutor_path = os.path.join(DOCS, 'tutor.html')
with open(tutor_path, 'r', encoding='utf-8') as f:
    tutor_html = f.read()

if 'interview_views.js' not in tutor_html:
    tutor_html = tutor_html.replace(
        '<script src="js/tutor.js"></script>',
        '<script src="js/tutor.js"></script>\n<script src="js/interview_data.js"></script>\n<script src="js/interview_coach.js"></script>\n<script src="js/interview_views.js"></script>'
    )
    with open(tutor_path, 'w', encoding='utf-8') as f:
        f.write(tutor_html)
    print('Patched docs/tutor.html')

# 4. Patch docs/js/tutor.js
tutor_js = os.path.join(DOCS, 'js', 'tutor.js')
with open(tutor_js, 'r', encoding='utf-8') as f:
    tj = f.read()

target = "+ '<div class=\"mu sm\" style=\"margin-top:8px\">Lessons ' + s.lessons.length + '/11 · Flashcards ' + s.cards.known + '/' + s.cards.total + ' · उजळणीचे प्रश्न ' + s.wrong + ' · Attempts ' + s.attempts.length + '</div></div>';"

addition = """+ '<div class="mu sm" style="margin-top:8px">Lessons ' + s.lessons.length + '/11 · Flashcards ' + s.cards.known + '/' + s.cards.total + ' · उजळणीचे प्रश्न ' + s.wrong + ' · Attempts ' + s.attempts.length + '</div></div>';
    
    // Oral Interview Coach Section for Tutor
    const coachData = window.COACH_STATE || {};
    const profData = window.CANDIDATE_PROFILE || {};
    const mockAtts = coachData.mockAttempts || [];
    const latestMock = mockAtts.length ? mockAtts[mockAtts.length - 1] : null;
    h += '<div class="card" style="border:2px solid var(--pr)">'
        + '<div class="row sp"><div class="b" style="font-size:18px">🎙️ तोंडी मुलाखत सराव (Oral Interview - 20 Marks)</div>'
        + '<span class="chip" style="font-size:12px">टार्गेट: 20/20</span></div>'
        + '<div class="mu sm" style="margin:6px 0">उमेदवार: <b>' + esc(profData.name || s.name) + '</b> (' + esc(profData.qualification || 'B.Com') + ' · ' + esc(profData.hometown || 'महाराष्ट्र') + ')</div>'
        + '<div class="grid3" style="margin:10px 0">'
        + '<div class="c"><div class="b" style="color:var(--ok)">' + Object.keys(coachData.mastered || {}).length + '</div><div class="mu sm">पक्के प्रश्न</div></div>'
        + '<div class="c"><div class="b" style="color:var(--wn)">' + Object.keys(coachData.revisionList || {}).length + '</div><div class="mu sm">उजळणी बाकी</div></div>'
        + '<div class="c"><div class="b" style="color:var(--pr)">' + (latestMock ? (latestMock.totalScore + '/20') : '—') + '</div><div class="mu sm">शेवटचा मॉक</div></div>'
        + '</div>'
        + (latestMock ? (
            '<div class="sm" style="margin-top:6px;padding:8px;background:color-mix(in srgb,var(--pr) 7%,var(--card));border-radius:10px">'
            + '<b>शेवटचा मॉक निकाल (' + new Date(latestMock.timestamp).toLocaleDateString('mr-IN') + '): ' + latestMock.totalScore + ' / 20 Marks</b><br>'
            + '• Accounting: ' + latestMock.categoryBreakdown.accounting + '/6 · Practical: ' + latestMock.categoryBreakdown.practical + '/5<br>'
            + '• MCED: ' + latestMock.categoryBreakdown.mced + '/3 · Comm: ' + latestMock.categoryBreakdown.communication + '/3 · Conf: ' + latestMock.categoryBreakdown.confidence + '/3'
            + '</div>'
        ) : '<div class="mu sm">अजून 20-Mark मॉक दिलेला नाही. विद्यार्थ्याला मॉक देण्यास सांगा.</div>')
        + '<div style="margin-top:10px"><a class="btn sm p" href="index.html#/coach">मुलाखत प्रशिक्षक उघडा →</a></div>'
        + '</div>';"""

if 'Oral Interview Coach Section for Tutor' not in tj:
    tj = tj.replace(target, addition)
    with open(tutor_js, 'w', encoding='utf-8') as f:
        f.write(tj)
    print('Patched docs/js/tutor.js')
