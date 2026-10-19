/* quiz engine: exam mode (timed), practice mode (instant feedback), weak-topic quiz, results */
let RUN = null, RES = null;
document.addEventListener('visibilitychange', () => { if (document.hidden && RUN) RUN.bl = (RUN.bl || 0) + 1 });
const shown = () => { if (RUN && RUN.sk !== RUN.i) { RUN.sk = RUN.i; RUN.qt = Date.now(); RUN.t0 = RUN.t0 || Date.now() } };
const quick = () => { if (RUN && RUN.qt && Date.now() - RUN.qt < 3000) RUN.fast = (RUN.fast || 0) + 1 };
const ans = (pid, q) => D.answers[pid][q.id];
const expl = (pid, q) => D.explain[pid][q.id] || {};
const fmtT = s => String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0');
const leftS = () => Math.max(0, RUN.dur * 60 - Math.floor((Date.now() - RUN.start) / 1000));
function qOf(i) { return RUN.qs[i] }

/* ---------- EXAM ---------- */
V.exam = function (id) {
    const p = paper(id);
    if (S.run && S.run.mode === 'exam' && String(S.run.pid) === String(id)) { RUN = S.run; return drawExam() }
    render('<div class="hero"><h1>📝 ' + esc(p.title) + '</h1><div class="q">' + p.questions.length + ' प्रश्न · ' + p.duration + ' मिनिटे · 1 mark each · no negative marking (practice rule)</div></div>'
        + '<div class="card"><p>परीक्षेसारखे वेळेत सोडवा. आधी सोपे प्रश्न, मग गणित. निकाल व explanation शेवटी दिसेल.</p><button class="p w" data-a="exstart" data-v="' + id + '">▶ सुरू करा</button><a class="btn w" style="margin-top:8px;text-align:center" href="#/practice/' + id + '">आधी Practice mode करा</a></div>')
};
ACT.exstart = id => { const p = paper(id); RUN = S.run = { mode: 'exam', pid: id, dur: p.duration, qs: p.questions.map(q => ({ pid: id, q })).sort(() => Math.random() - .5), i: 0, ans: {}, start: Date.now() }; save(); drawExam() };
function drawExam() {
    shown();
    const p = paper(RUN.pid), N = RUN.qs.length, it = qOf(RUN.i), q = it.q, n = Object.keys(RUN.ans).length;
    render('<div class="top"><b>Q ' + (RUN.i + 1) + '/' + N + '</b><span class="mu sm">उत्तरे ' + n + '/' + N + '</span><b id="tm">' + fmtT(leftS()) + '</b></div>' + bar(pct(RUN.i + 1, N))
        + '<div class="card"><div class="mu sm">' + esc(p.subtopics[q.sub]) + '</div><p><b>' + esc(q.q) + '</b></p>' + q.opts.map((o, k) => '<button class="opt ' + (RUN.ans[q.id] === 'ABCD'[k] ? 's' : '') + '" data-a="exopt" data-v="' + 'ABCD'[k] + '"><b>' + 'ABCD'[k] + '.</b> ' + esc(o) + '</button>').join('') + '</div>'
        + '<div class="row sp"><button data-a="exnav" data-v="-1" ' + (RUN.i ? '' : 'disabled') + '>← मागे</button><button data-a="exov">सर्व प्रश्न</button><button class="p" data-a="exnav" data-v="1">' + (RUN.i < N - 1 ? 'पुढे →' : 'संपवा') + '</button></div>');
    clearInterval(curTimer); curTimer = setInterval(() => { const t = $('#tm'); if (t) t.textContent = fmtT(leftS()); if (leftS() <= 0) { clearInterval(curTimer); finish(true) } }, 1000)
}
ACT.exopt = L => { if (RUN.ans[qOf(RUN.i).q.id] === undefined) quick(); RUN.ans[qOf(RUN.i).q.id] = L; save(); drawExam() };
ACT.exnav = d => { d = +d; if (RUN.i + d >= RUN.qs.length) return ACT.exov(); RUN.i = Math.max(0, RUN.i + d); save(); drawExam() };
ACT.exov = () => {
    const N = RUN.qs.length, n = Object.keys(RUN.ans).length;
    render('<div class="top"><b>सर्व प्रश्न</b><b id="tm">' + fmtT(leftS()) + '</b></div><div class="card"><div style="display:grid;grid-template-columns:repeat(6,1fr);gap:8px">' + RUN.qs.map((x, k) => '<button class="' + (RUN.ans[x.q.id] ? 'p' : '') + '" style="padding:10px 0" data-a="exjump" data-v="' + k + '">' + (k + 1) + '</button>').join('') + '</div><p class="mu sm">उत्तरे दिली ' + n + '/' + N + ' · बाकी ' + (N - n) + '</p></div>'
        + '<div class="row sp"><button data-a="exnav" data-v="0">← परत</button><button class="p" data-a="exsubmit">✅ Submit</button></div>')
};
ACT.exjump = k => { RUN.i = +k; save(); drawExam() };
ACT.exsubmit = () => { const n = RUN.qs.length - Object.keys(RUN.ans).length; if (confirm(trs('Submit करायचे? ' + n + ' प्रश्न बाकी आहेत.'))) finish(false) };

/* ---------- PRACTICE / WEAK / REVISE / CONCEPT CHECK (instant feedback) ---------- */
const MODE_LABEL = { practice: '✍️ Practice', exam: '📝 Exam', weak: '🎯 कमकुवत Quiz', revise: '🔁 उजळणी', check: '🧠 Concept Check' };
const isMulti = m => m === 'weak' || m === 'revise';
V.practice = function (id) {
    const p = paper(id); RUN = { mode: 'practice', pid: id, qs: p.questions.map(q => ({ pid: id, q })), i: 0, ans: {}, fb: {} }; drawPractice()
};
V.check = function (id) {
    const p = paper(id), bySub = {}; p.questions.forEach(q => (bySub[q.sub] = bySub[q.sub] || []).push(q));
    const subs = Object.keys(bySub).sort(() => Math.random() - .5).slice(0, 5), qs = subs.map(s => pick(bySub[s]));
    while (qs.length < 5) { const q = pick(p.questions); if (!qs.includes(q)) qs.push(q) }
    RUN = { mode: 'check', pid: id, qs: qs.map(q => ({ pid: id, q })), i: 0, ans: {}, fb: {} }; drawPractice()
};
V.weak = function () {
    const keys = Object.keys(S.wrong).sort(() => Math.random() - .5).slice(0, 10);
    if (!keys.length) { autoMark('weak', 0); return render('<h1>🎯 कमकुवत प्रश्न</h1><div class="card c"><div class="big">🌟</div><b>सध्या चुकलेला एकही प्रश्न बाकी नाही!</b><p class="mu">आधी काही Practice/Exam करा. चुकलेले प्रश्न इथे येतील आणि बरोबर केल्यावर निघून जातील.</p><a class="btn p" href="#/papers">सराव सुरू करा</a></div>') }
    RUN = { mode: 'weak', pid: 'W', qs: keys.map(k => { const [pid, qid] = k.split(':'); return { pid, q: paper(pid).questions.find(x => String(x.id) === qid) } }), i: 0, ans: {}, fb: {} }; drawPractice()
};
const lastSeen = id => S.rev[id] || S.lessons[id] || 0;
const dueIds = () => Object.keys(S.lessons).filter(id => Date.now() - lastSeen(id) > 20 * 36e5);
V.revise = function () {
    const ids = Object.keys(S.lessons).sort((a, b) => lastSeen(a) - lastSeen(b)).slice(0, 4);
    if (!ids.length) return render('<h1>🔁 उजळणी</h1><div class="card c"><div class="big">📘</div><b>आधी एक Lesson पूर्ण करा</b><p class="mu">Lesson वाचून Concept Check पास केल्यावर, त्या topic ची उजळणी इथे येईल. (जे शिकले ते लक्षात राहावे म्हणून)</p><a class="btn p" href="#/learn">Lessons</a></div>');
    const qs = []; ids.forEach(id => { const p = paper(id); [...p.questions].sort(() => Math.random() - .5).slice(0, 3).forEach(q => qs.push({ pid: id, q })) });
    RUN = { mode: 'revise', pid: 'R', qs: qs.sort(() => Math.random() - .5), i: 0, ans: {}, fb: {} }; drawPractice()
};
const qk = it => it.pid + ':' + it.q.id;
function drawPractice() {
    shown();
    const N = RUN.qs.length, it = qOf(RUN.i), q = it.q, p = paper(it.pid), a = RUN.ans[qk(it)], fb = a !== undefined, right = ans(it.pid, q);
    render('<div class="top"><b>' + MODE_LABEL[RUN.mode] + ' · ' + (RUN.i + 1) + '/' + N + '</b><a href="#/papers" class="sm">बाहेर</a></div>' + bar(pct(RUN.i + (fb ? 1 : 0), N))
        + (RUN.mode === 'check' ? '<div class="tip">५ पैकी किमान ४ बरोबर आले की concept पक्का समजला असे मानू.</div>' : '')
        + '<div class="card"><div class="mu sm">' + (isMulti(RUN.mode) ? esc(p.title) + ' · ' : '') + esc(p.subtopics[q.sub]) + '</div><p><b>' + esc(q.q) + '</b></p>'
        + q.opts.map((o, k) => { const L = 'ABCD'[k]; return '<button class="opt ' + (fb ? (L === right ? 'ok' : L === a ? 'no' : '') : '') + '" ' + (fb ? 'disabled' : '') + ' data-a="pans" data-v="' + L + '"><b>' + L + '.</b> ' + esc(o) + '</button>' }).join('')
        + (fb ? '<div class="sm" style="margin-top:8px">' + (a === right ? '<b style="color:var(--ok)">✓ बरोबर! ' + pick(D.extras.praise) + '</b>' : '<b style="color:var(--bad)">✗ बरोबर उत्तर: ' + right + '</b>') + '<p>' + rich(expl(it.pid, q).exp || '') + '</p><div class="tip">📌 ' + rich(expl(it.pid, q).concept || '') + '</div></div>' : '') + '</div>'
        + (fb ? '<button class="p w" data-a="pnext">' + (RUN.i < N - 1 ? 'पुढचा प्रश्न →' : 'निकाल पाहा 🏁') + '</button>' : ''))
}
ACT.pans = L => { const it = qOf(RUN.i); quick(); RUN.ans[qk(it)] = L; if (L === ans(it.pid, it.q)) addXP(8); drawPractice() };
ACT.pnext = () => { if (RUN.i < RUN.qs.length - 1) { RUN.i++; drawPractice() } else finish(false) };

/* ---------- FINISH + RESULT ---------- */
function finish(auto) {
    clearInterval(curTimer);
    const R = RUN, mode = R.mode, multi = isMulti(mode), pid = R.pid, prev = (multi || mode === 'check') ? null : latest(pid);
    let t = 0; const wrongIds = [], rightIds = [], review = [];
    const subs = multi ? [] : paper(pid).subtopics.map(() => [0, 0]);
    R.qs.forEach(it => {
        const a = R.ans[qk(it)] !== undefined ? R.ans[qk(it)] : R.ans[it.q.id], ok = a === ans(it.pid, it.q);
        if (!multi) { subs[it.q.sub][1]++; if (ok) subs[it.q.sub][0]++ }
        if (ok) { t++; rightIds.push(it.q.id); if (multi) delete S.wrong[qk(it)] } else { wrongIds.push(it.q.id); if (multi) S.wrong[qk(it)] = 1 }
        review.push({ it, a, ok })
    });
    const o = R.qs.length, at = { p: multi ? (mode === 'weak' ? 'W' : 'R') : pid, m: mode, t, o, subs, d: Math.round((Date.now() - (R.start || R.t0 || Date.now())) / 1000), f: R.fast || 0, bl: R.bl || 0 };
    if (!multi) { at.wrongIds = wrongIds; at.rightIds = rightIds }
    RES = { mode, pid, t, o, subs, review, prev: prev ? pct(prev.t, prev.o) : null, auto, passed: null };
    recordAttempt(at);
    S.run = null; save();
    if (mode === 'exam') addXP(t * 5, '(Exam)');
    if (mode === 'check') {
        RES.need = Math.ceil(o * .8); RES.passed = t >= RES.need;
        if (RES.passed) { const first = !S.lessons[pid]; S.lessons[pid] = S.lessons[pid] || Date.now(); S.rev[pid] = Date.now(); save(); if (first) addXP(50, '(Concept समजला)'); autoMark('lesson', pid); checkBadges(); burst(['✅', '⭐', '🎉']) }
    }
    if (mode === 'revise') { new Set(R.qs.map(x => x.pid)).forEach(id => { S.rev[id] = Date.now() }); save(); addXP(t * 3, '(उजळणी)') }
    if (mode === 'exam') { if (String(pid) === '0' || pct(t, o) >= PASS) autoMark('quiz', pid); else toast(tt('Exam मध्ये किमान ' + PASS + '% हवे — Lesson पुन्हा वाचून पुन्हा Exam द्या.', 'You need at least ' + PASS + '% in the Exam — revisit the Lesson and retake the Exam.'), 5000) }
    else if (mode !== 'check') autoMark(mode, multi ? 0 : pid);
    if (mode === 'exam' || mode === 'practice') say(pct(t, o) >= 75 ? 'high' : pct(t, o) >= 50 ? 'mid' : 'low', { pct: pct(t, o) }); else if (pct(t, o) >= 75) burst();
    RUN = null; location.hash = '#/result'; route()
}
V.result = function () {
    if (!RES) return (location.hash = '#/home');
    const r = RES, p = pct(r.t, r.o), multi = isMulti(r.mode), P = multi ? null : paper(r.pid), chk = r.mode === 'check';
    const msg = chk ? (r.passed ? '✅ Concept पक्का समजला! ' + pick(D.extras.praise) : '📖 अजून थोडे बाकी आहे — Lesson मधील खालील भाग पुन्हा वाचा आणि Concept Check पुन्हा द्या. (' + r.need + ' बरोबर हवेत)')
        : p >= 75 ? '🌟 उत्तम काम, ' + S.name + '! असेच चालू ठेवा.' : p >= 50 ? '👍 छान प्रयत्न! थोडी उजळणी केली की अजून चांगले होईल.' : '💪 काळजी करू नका. चुका म्हणजे शिकण्याची सुरुवात. खालील Lesson वाचा आणि पुन्हा प्रयत्न करा.';
    let h = '<div class="hero c"><div class="q">' + MODE_LABEL[r.mode] + (P ? ' · ' + esc(P.title) : '') + '</div><div class="big" style="font-size:54px">' + r.t + '/' + r.o + '</div><div class="q">' + p + '%' + (r.auto ? ' · वेळ संपली, auto-submit' : '') + '</div></div>'
        + '<div class="card"><b>' + msg + '</b>' + (r.prev !== null && !multi && !chk ? '<p class="sm">मागच्या वेळेपेक्षा: <b style="color:var(--' + (p >= r.prev ? 'ok' : 'bad') + ')">' + (p >= r.prev ? '+' : '') + (p - r.prev) + '%</b> ' + (p > r.prev ? '📈 सुधारणा!' : '') + '</p>' : '') + '</div>';
    if (!multi) {
        h += '<div class="card"><b>Topic-wise अचूकता</b><div class="mu sm">(&lt;50% पुन्हा शिका · 50–74% सराव · ≥75% पक्के) — फक्त total वरून ठरवू नका</div>' + r.subs.map((s, k) => { if (!s[1]) return ''; const v = pct(s[0], s[1]); return '<div class="pill sm" style="margin:10px 0 2px"><span>' + esc(P.subtopics[k]) + '</span><b>' + s[0] + '/' + s[1] + '</b></div>' + bar(v) + (v < 50 ? '<a class="sm" href="#/lesson/' + r.pid + '">📖 ' + esc(P.lessons[k]) + ' वाचा</a>' : '') }).join('') + '</div>'
    }
    h += '<details><summary>सर्व प्रश्न आणि explanation (' + r.review.filter(x => !x.ok).length + ' चुकले)</summary>' + r.review.map((x, i) => {
        const q = x.it.q, right = ans(x.it.pid, q), e = expl(x.it.pid, q);
        return '<div style="margin:12px 0;padding-bottom:10px;border-bottom:1px dashed var(--bd)"><div class="sm"><b>' + (i + 1) + '. ' + esc(q.q) + '</b></div><div class="sm" style="color:var(--' + (x.ok ? 'ok' : 'bad') + ')">' + (x.ok ? '✓' : '✗') + ' तुमचे: ' + (x.a ? x.a + '. ' + esc(q.opts['ABCD'.indexOf(x.a)]) : '—') + '</div>' + (x.ok ? '' : '<div class="sm" style="color:var(--ok)">बरोबर: ' + right + '. ' + esc(q.opts['ABCD'.indexOf(right)]) + '</div>') + '<div class="mu sm">' + rich(e.exp || '') + '</div></div>'
    }).join('') + '</details>'
        + '<div class="card"><div class="row g wrap">' + (chk && !r.passed ? '<a class="btn p" href="#/lesson/' + r.pid + '">📖 Lesson पुन्हा वाचा</a><a class="btn" href="#/check/' + r.pid + '">🧠 पुन्हा Check</a>' : (!multi ? '<a class="btn p" href="#/lesson/' + r.pid + '">📖 Lesson</a>' : '')) + (chk && r.passed ? '<a class="btn p" href="#/practice/' + r.pid + '">✍️ Practice करा</a>' : '') + '<a class="btn" href="#/weak">🎯 कमकुवत Quiz</a>' + (multi || chk ? '' : '<a class="btn" href="#/practice/' + r.pid + '">पुन्हा Practice</a>') + '<a class="btn" href="#/revise">🔁 उजळणी</a><a class="btn" href="#/home">🏠 होम</a><a class="btn" href="#/report">📤 Tutor ला पाठवा</a></div></div>';
    render(h)
};
