/* core: state, data, router, XP/streak/badges, helpers */
const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
const esc = s => SENT_A + String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;') + SENT_B;
const V = {}, ACT = {};
let D = {}, S = null, BASE = null;
const TUTOR_MODE = !!window.TUTOR_MODE;
const KEY = TUTOR_MODE ? 'mced_app_tutor' : 'mced_app_v2';
const dstr = d => { const x = d || new Date(); return x.getFullYear() + '-' + String(x.getMonth() + 1).padStart(2, '0') + '-' + String(x.getDate()).padStart(2, '0') };
const today = () => dstr();
const mainQs = p => p.questions.filter(q => !q.b);
const isMain = a => a.m === 'exam' || a.m === 'practice';
const pct = (a, b) => b ? Math.round(a / b * 100) : 0;
const pick = a => a[Math.floor(Math.random() * a.length)];
const cls = p => p >= 75 ? 'ok' : p >= 50 ? 'wn' : 'bad';

function defState() { return { seen: {}, theme: 'auto', tutor: { name: 'Nilshi', phone: '' }, dayDone: {}, rev: {}, lang: 'mr', name: 'Aishwarya', named: false, xp: 0, streak: { last: '', n: 0 }, tasks: {}, lessons: {}, cards: {}, attempts: [], wrong: {}, badges: [], checks: {}, created: Date.now() } }
function loadState() { S = defState(); try { const x = JSON.parse(localStorage[KEY] || 'null'); if (x) Object.assign(S, x) } catch (e) { } }
function save() { try { localStorage[KEY] = JSON.stringify(S) } catch (e) { } }
const J = n => fetch('data/' + n + '.json').then(r => r.json());

const paper = id => D.papers.find(p => String(p.id) === String(id));
const lvlOf = xp => { let l = D.extras.levels[0]; for (const x of D.extras.levels) if (xp >= x[0]) l = x; return l };
const nextLvl = xp => D.extras.levels.find(x => x[0] > xp);
const examTime = () => new Date(D.extras.exam.date).getTime();
const daysLeft = () => Math.max(0, Math.ceil((examTime() - Date.now()) / 864e5));
const render = h => { $('#view').innerHTML = trHTML(h) };

function toast(m, ms = 2600) { const t = document.createElement('div'); t.className = 'toast'; t.textContent = trs(m).replace(/[⁠⁡]/g, ''); document.body.appendChild(t); setTimeout(() => t.remove(), ms) }
function burst(em = ['🎉', '⭐', '✨', '🏆', '🔥']) {
    for (let i = 0; i < 18; i++) {
        const s = document.createElement('div'); s.className = 'bt'; s.textContent = pick(em);
        s.style.left = (30 + Math.random() * 40) + '%'; s.style.top = '55%';
        s.style.setProperty('--x', (Math.random() * 240 - 120) + 'px'); s.style.setProperty('--y', (-160 - Math.random() * 220) + 'px');
        document.body.appendChild(s); setTimeout(() => s.remove(), 1500)
    }
}
function addXP(n, why) { const before = lvlOf(S.xp)[1]; S.xp += n; const after = lvlOf(S.xp)[1]; save(); if (after !== before) { toast('🎊 नवीन Level: ' + after); burst() } else if (why) toast('+' + n + ' XP ' + why, 1600) }

function touchStreak() {
    const t = today(), y = dstr(new Date(Date.now() - 864e5));
    if (S.streak.last === t) return;
    S.streak.n = S.streak.last === y ? S.streak.n + 1 : 1; S.streak.last = t; S.xp += 10; save()
}

const BADGES = [
    ['first', '🌱', 'पहिले पाऊल', () => S.attempts.length > 0 || Object.keys(S.lessons).length > 0],
    ['read3', '📘', '3 Lessons', () => Object.keys(S.lessons).length >= 3],
    ['readall', '🎓', 'सर्व Lessons', () => Object.keys(S.lessons).length >= 10],
    ['s3', '🔥', '3 दिवस सलग', () => S.streak.n >= 3],
    ['s7', '⚡', '7 दिवस सलग', () => S.streak.n >= 7],
    ['p80', '🏅', 'एका paper मध्ये 80%', () => S.attempts.some(a => pct(a.t, a.o) >= 80)],
    ['all', '🗺️', 'सर्व Papers सोडवले', () => new Set(S.attempts.map(a => a.p)).size >= 11],
    ['cards', '🃏', '30 Cards पक्के', () => Object.values(S.cards).filter(c => c >= 3).length >= 30],
    ['day', '✅', 'एक दिवसाचा प्लॅन पूर्ण', () => D.extras.plan.some(d => d.tasks.every(t => S.tasks[t[0]]))],
    ['up', '📈', '20% सुधारणा', () => improvement() >= 20],
];
function improvement() { let best = 0; const by = {}; S.attempts.filter(isMain).forEach(a => { (by[a.p] = by[a.p] || []).push(pct(a.t, a.o)) }); Object.values(by).forEach(v => { if (v.length > 1) best = Math.max(best, Math.max(...v) - v[0]) }); return best }
function checkBadges() { BADGES.forEach(b => { if (!S.badges.includes(b[0]) && b[3]()) { S.badges.push(b[0]); save(); toast('🏆 नवीन Badge: ' + b[2]); burst() } }) }

function autoMark(type, ref) {
    const g = gate(S.tasks, S.attempts); let n = 0;
    outer: for (let i = 0; i < D.extras.plan.length; i++) {
        if (!g[i].unlocked) continue;
        for (const t of D.extras.plan[i].tasks) if (t[1] === type && String(t[2]) === String(ref) && !S.tasks[t[0]]) { S.tasks[t[0]] = Date.now(); n++; break outer }
    }
    if (n) {
        save(); addXP(20, '(प्लॅन task पूर्ण)'); checkBadges();
        gate(S.tasks, S.attempts).forEach((x, i) => { const d = D.extras.plan[i]; if (x.passed && !S.dayDone[d.date]) { S.dayDone[d.date] = 1; save(); setTimeout(() => say('day'), 1800) } })
    }
}

function recordAttempt(a) {
    a.ts = Date.now(); S.attempts.push(a);
    const key = (p, q) => p + ':' + q;
    (a.wrongIds || []).forEach(q => { S.wrong[key(a.p, q)] = 1 });
    (a.rightIds || []).forEach(q => { delete S.wrong[key(a.p, q)] });
    delete a.wrongIds; delete a.rightIds;
    save(); checkBadges(); sync()
}

function snapshot() {
    const cards = D.extras.flash.length;
    return {
        v: 1, name: S.name, ts: Date.now(), xp: S.xp, streak: S.streak.n, tasks: Object.keys(S.tasks), eb: Object.fromEntries(D.papers.map(p => [p.id, examBest(S.attempts, p.id)]).filter(x => x[1] > 0)), lessons: Object.keys(S.lessons),
        cards: { known: Object.values(S.cards).filter(c => c >= 3).length, total: cards }, wrong: Object.keys(S.wrong).length,
        attempts: S.attempts.slice(-40).map(a => ({ p: a.p, m: a.m, ts: a.ts, t: a.t, o: a.o, s: a.subs, d: a.d, f: a.f, bl: a.bl }))
    }
}
function sync() { if (TUTOR_MODE) return; try { fetch('api/progress', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(snapshot()) }).catch(() => { }) } catch (e) { } }

function setNav(n) { const map = { home: 'home', plan: 'plan', learn: 'learn', lesson: 'learn', check: 'learn', papers: 'papers', exam: 'papers', practice: 'papers', weak: 'papers', result: 'papers' }; const k = TUTOR_MODE ? 'tutor' : (map[n] || 'more'); $$('#nav a').forEach(a => a.classList.toggle('on', a.dataset.n === k)) }
let curTimer = null;
function route() {
    clearInterval(curTimer);
    const h = location.hash.replace(/^#\/?/, '') || 'home', [n, ...a] = h.split('/');
    if ('speechSynthesis' in window) speechSynthesis.cancel();
    setNav(n); window.scrollTo(0, 0);
    if (!TUTOR_MODE && ['lesson', 'check', 'practice', 'exam'].includes(n) && a[0] !== undefined && !paperAllowed(a[0])) { toast(tt('🔒 हा भाग अजून बंद आहे — आधी प्लॅनमधील आधीचा दिवस पूर्ण करा.', '🔒 This part is still locked — complete the earlier day in the plan first.'), 4200); location.hash = '#/plan'; return }
    try { (V[n] || V.home)(...a) } catch (e) { render('<div class="card">काहीतरी चुकले: ' + esc(e.message) + '<br><a href="#/home">होमवर जा</a></div>'); console.error(e) }
}
document.addEventListener('click', e => {
    const el = e.target.closest('[data-a]'); if (!el) return;
    const f = ACT[el.dataset.a]; if (f) { e.preventDefault(); f(el.dataset.v, el) }
});
window.addEventListener('hashchange', route);

async function boot() {
    loadState();
    const names = ['papers', 'answers', 'explain', 'lessons', 'extras'];
    try { const r = await Promise.all(names.map(J)); D = { papers: r[0], answers: r[1], explain: r[2], lessons: r[3], extras: r[4] }; BASE = { papers: D.papers, explain: D.explain, lessons: D.lessons, extras: D.extras }; if (S.lang === 'en') await loadEn() }
    catch (e) { render('<div class="card">Data load झाला नाही. Internet तपासा आणि पान refresh करा.</div>'); return }
    navLabels(); applyTheme();
    if (TUTOR_MODE) { S.named = true; if (!location.hash) location.hash = '#/tutor'; return route() }
    if (!S.named) return V.welcome();
    touchStreak(); checkBadges(); sync(); route();
    if ([3, 5, 7].includes(S.streak.n) && S.streak.shown !== today()) { S.streak.shown = today(); save(); setTimeout(() => say('streak', { n: S.streak.n }), 2500) }
}
V.welcome = function () {
    render(langToggle() + '<div class="hero"><h1>👋 नमस्कार!</h1><div class="q">MCED District Account Assistant परीक्षा 27 Oct 2026 साठी तुमचा स्वतःचा तयारी App.<br>रोज थोडे शिका, सराव करा, आणि पास व्हा!</div></div>'
        + '<div class="card"><b>तुमचे नाव</b><input type="text" id="nm" value="' + esc(S.name) + '" style="margin:8px 0"><button class="p w" data-a="start">सुरू करूया 🚀</button></div>'
        + '<div class="card sm mu">हा practice App आहे; official MCED paper नाही. तुमची प्रगती फक्त या फोनमध्ये सेव्ह होते. Tutor ला पाठवण्यासाठी "अधिक → Tutor ला Report" वापरा.</div>')
};
ACT.start = () => { const v = $('#nm').value.trim(); if (v) S.name = v; S.named = true; save(); touchStreak(); checkBadges(); sync(); location.hash = '#/home'; route() };

async function loadEn() {
    const miss = [];
    for (const n of ['papers', 'explain', 'lessons', 'extras']) {
        try { const r = await fetch('data/en/' + n + '.json'); if (!r.ok) throw 0; D[n] = await r.json() } catch (e) { D[n] = BASE[n]; miss.push(n) }
    }
    if (miss.length) toast('English content (' + miss.join(', ') + ') is not available yet — UI in English, content in Marathi', 4000)
}
ACT.lang = async v => { S.lang = v; save(); if (v === 'en') await loadEn(); else { D.papers = BASE.papers; D.explain = BASE.explain; D.lessons = BASE.lessons; D.extras = BASE.extras } navLabels(); route() };

/* personal messages from the tutor (Nilesh) */
const tt = (mr, en) => isEn() ? en : mr;
const fillT = (t, v) => String(t).replace(/\{(\w+)\}/g, (a, k) => k === 'name' ? ((v && v.name) || S.name) : k === 'from' ? D.extras.personal.sender : (v && v[k] != null ? v[k] : ''));
function say(kind, v) { const P = D.extras.personal; if (!P || !P[kind]) return; toast('✉️ ' + P.sender + ': ' + fillT(P[kind], v), 6500); burst(['✨', '🌟', '🎉']) }
function dailyNote() { const P = D.extras.personal, t = today(); if (t === '2026-10-26') return fillT(P.eve); if (t === '2026-10-27') return fillT(P.exam); return fillT(P.daily[new Date().getDate() % P.daily.length]) }
const waNum = () => { const d = ((S.tutor && S.tutor.phone) || '').replace(/\D/g, ''); return d.length === 10 ? '91' + d : d };

ACT.theme = v => { S.theme = v; save(); applyTheme(); if (S.named) route(); else V.welcome() };
