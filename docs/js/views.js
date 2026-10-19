/* views: home, plan, more, cards, cheat sheet, exam-day, progress */
const WD = ['रवि', 'सोम', 'मंगळ', 'बुध', 'गुरु', 'शुक्र', 'शनि'];
const ring = (p, c = 'var(--pr)') => '<div class="ring"><svg width="74" height="74"><circle cx="37" cy="37" r="31" fill="none" stroke="var(--bd)" stroke-width="8"/><circle cx="37" cy="37" r="31" fill="none" stroke="' + c + '" stroke-width="8" stroke-linecap="round" stroke-dasharray="' + (195 * p / 100) + ' 195"/></svg><b>' + p + '%</b></div>';
const bar = (p, c) => '<div class="bar ' + (c || cls(p)) + '"><i style="width:' + p + '%"></i></div>';
const papersOf = a => a.filter(isMain);
const latest = id => { const a = papersOf(S.attempts).filter(x => String(x.p) === String(id)); return a.length ? a[a.length - 1] : null };
const best = id => Math.max(0, ...papersOf(S.attempts).filter(x => String(x.p) === String(id)).map(a => pct(a.t, a.o)));
function subAgg(id) { const p = paper(id), r = p.subtopics.map(() => [0, 0]); S.attempts.filter(a => String(a.p) === String(id) && (isMain(a) || a.m === 'check')).forEach(a => (a.subs || a.s || []).forEach((x, i) => { if (r[i]) { r[i][0] += x[0]; r[i][1] += x[1] } })); return r }
function taskGo(t) {
    const [, ty, ref] = t;
    location.hash = ty === 'lesson' ? '#/lesson/' + ref : ty === 'practice' ? '#/practice/' + ref : ty === 'quiz' ? '#/exam/' + ref : ty === 'weak' ? '#/weak' : ty === 'revise' ? '#/revise' : ty === 'cards' ? '#/cards/' + encodeURIComponent(ref) : ty === 'cheat' ? '#/cheat' : '#/examday'
}
const ICON = { revise: '🔁', lesson: '📖', practice: '✍️', quiz: '📝', weak: '🎯', cards: '🃏', cheat: '📄', exam: '🎒' };
const planDay = () => { const t = today(); return D.extras.plan.find(d => d.date === t) || D.extras.plan.find(d => d.date > t) || D.extras.plan[D.extras.plan.length - 1] };
const dayPct = d => pct(d.tasks.filter(t => S.tasks[t[0]]).length, d.tasks.length);
function nextTask() { const t = today(); for (const d of D.extras.plan) { if (d.date > t) break; for (const k of d.tasks) if (!S.tasks[k[0]]) return k } const d = planDay(); return d.tasks.find(k => !S.tasks[k[0]]) || null }
function accuracyAll() { const a = papersOf(S.attempts); return pct(a.reduce((s, x) => s + x.t, 0), a.reduce((s, x) => s + x.o, 0)) }

V.home = function () {
    const d = planDay(), q = D.extras.quotes[new Date().getDate() % D.extras.quotes.length].replace('{name}', S.name), nt = nextTask(), lv = lvlOf(S.xp), nl = nextLvl(S.xp);
    const done = D.extras.plan.reduce((s, x) => s + x.tasks.filter(t => S.tasks[t[0]]).length, 0), tot = D.extras.plan.reduce((s, x) => s + x.tasks.length, 0);
    render(langToggle() + '<div class="hero"><div class="mu" style="color:#fff;opacity:.85">नमस्कार 👋</div><h1>' + esc(S.name) + '</h1><div class="q">' + esc(q) + '</div>'
        + '<div class="cd" id="cd"></div><div class="bubble"><small>✉️ ' + tt(esc(D.extras.personal.sender) + ' कडून', 'From ' + esc(D.extras.personal.sender)) + '</small><b>' + esc(dailyNote()) + '</b></div></div>'
        + (nt ? '<div class="card"><div class="mu">👉 पुढचे काम</div><div class="b" style="margin:4px 0 10px">' + ICON[nt[1]] + ' ' + esc(nt[3]) + '</div><button class="p w" data-a="go" data-v="' + nt[0] + '">आत्ता सुरू करा</button></div>'
            : '<div class="card c"><div class="big">🎉</div><b>आजचे सर्व काम पूर्ण!</b><p class="mu">सराव किंवा Flashcards करत रहा.</p><a class="btn p" href="#/papers">आणखी सराव</a></div>')
        + '<div class="card"><div class="row"><div>' + ring(dayPct(d)) + '</div><div style="flex:1"><div class="b">' + esc(d.title) + '</div><div class="mu sm">' + esc(d.goal) + '</div><a href="#/plan" class="sm">पूर्ण प्लॅन पाहा →</a></div></div></div>'
        + (dueIds().length ? '<div class="card row sp"><div><div class="b">🔁 उजळणीची वेळ</div><div class="mu sm">' + dueIds().length + ' topic(s) — जे शिकले ते पक्के करा</div></div><a class="btn p" href="#/revise">सुरू</a></div>' : '')
        + '<div class="grid3"><div class="card c"><div class="big">🔥' + S.streak.n + '</div><div class="mu">दिवस सलग</div></div><div class="card c"><div class="big">⭐' + S.xp + '</div><div class="mu">XP</div></div><div class="card c"><div class="big">' + (S.attempts.length ? accuracyAll() + '%' : '—') + '</div><div class="mu">अचूकता</div></div></div>'
        + '<div class="card"><div class="row sp"><b>' + esc(lv[1]) + '</b><span class="mu sm">' + (nl ? nl[0] - S.xp + ' XP → ' + esc(nl[1]) : 'सर्वोच्च Level!') + '</span></div><div style="margin-top:8px">' + bar(nl ? pct(S.xp - lv[0], nl[0] - lv[0]) : 100) + '</div>'
        + '<div class="mu sm" style="margin-top:8px">एकूण प्लॅन: ' + done + '/' + tot + ' tasks पूर्ण</div>' + bar(pct(done, tot), 'ok') + '</div>'
        + '<h2>📊 विषयानुसार प्रगती</h2><div class="card">' + D.papers.filter(p => p.id >= 2 && p.id <= 10).map(p => { const l = latest(p.id), v = l ? pct(l.t, l.o) : 0; return '<div class="pill sm" style="margin:8px 0 2px"><span>' + esc(p.title.replace(/^Paper \d+: /, '')) + '</span><b>' + (l ? v + '%' : '—') + '</b></div>' + bar(v) }).join('') + '</div>'
        + '<h2>🏆 Badges</h2><div class="card">' + BADGES.map(b => '<span class="badge ' + (S.badges.includes(b[0]) ? 'on' : '') + '"><span>' + b[1] + '</span>' + b[2] + '</span>').join('') + '</div>'
        + '<div class="card row sp"><div class="sm">Tutor ला प्रगती पाठवा</div><a class="btn p" href="#/report">📤 Report</a></div>');
    const tick = () => { const ms = Math.max(0, examTime() - Date.now()), el = $('#cd'); if (!el) return; el.innerHTML = trs('<div><b>' + Math.floor(ms / 864e5) + '</b><span>दिवस</span></div><div><b>' + Math.floor(ms % 864e5 / 36e5) + '</b><span>तास</span></div><div><b>' + Math.floor(ms % 36e5 / 6e4) + '</b><span>मिनिटे</span></div><div style="flex:1;text-align:left"><span>परीक्षा</span><br><b style="font-size:15px">27 Oct, 11:00</b></div>') }; tick(); curTimer = setInterval(tick, 30000)
};
ACT.go = id => { for (const d of D.extras.plan) for (const t of d.tasks) if (t[0] === id) return taskGo(t) };

V.plan = function () {
    const t = today();
    render('<h1>📅 8 दिवसांचा प्लॅन</h1><p class="mu">रोज task करा, आपोआप tick होईल. थोडे चुकले तरी चालेल, पुढे चालत रहा!</p>' + D.extras.plan.map(d => {
        const dt = new Date(d.date + 'T00:00:00'), isT = d.date === t, late = d.date < t && dayPct(d) < 100;
        return '<div class="card day ' + (isT ? 'today' : '') + '"><div class="row sp"><div><span class="chip ' + (isT ? '' : late ? 'bad' : 'ok') + '">' + dt.getDate() + ' Oct, ' + WD[dt.getDay()] + (isT ? ' · आज' : late ? ' · बाकी' : '') + '</span><div class="b" style="margin-top:6px">' + esc(d.title) + '</div><div class="mu sm">' + esc(d.goal) + '</div></div>' + ring(dayPct(d), dayPct(d) === 100 ? 'var(--ok)' : 'var(--pr)') + '</div>'
            + d.tasks.map(k => '<div class="task ' + (S.tasks[k[0]] ? 'done' : '') + '"><button class="ck" data-a="tog" data-v="' + k[0] + '">' + (S.tasks[k[0]] ? '✓' : '') + '</button><div style="flex:1" class="t sm">' + ICON[k[1]] + ' ' + esc(k[3]) + '</div><button class="sm" data-a="go" data-v="' + k[0] + '">›</button></div>').join('') + '</div>'
    }).join(''))
};
ACT.tog = id => { if (S.tasks[id]) delete S.tasks[id]; else { S.tasks[id] = Date.now(); addXP(20, ''); toast(pick(D.extras.praise)); checkBadges() } save(); V.plan() };

V.more = function () {
    const it = (h, i, t, s) => '<a class="card row" href="' + h + '" style="text-decoration:none;color:inherit"><span style="font-size:28px">' + i + '</span><div style="flex:1"><div class="b">' + t + '</div><div class="mu sm">' + s + '</div></div>›</a>';
    render(langToggle() + '<h1>☰ अधिक</h1>' + it('#/cards/all', '🃏', 'Flashcards', 'सूत्रे, full forms, नियम — 10 मिनिटांत उजळणी') + it('#/cheat', '📄', 'Cheat Sheet', 'एका पानात सर्व सूत्रे आणि entries') + it('#/weak', '🎯', 'कमकुवत प्रश्नांचा Quiz', 'आधी चुकलेले प्रश्न पुन्हा') + it('#/revise', '🔁', 'उजळणी (Revision)', 'आधी शिकलेले topics पुन्हा तपासा')
        + it('#/progress', '📈', 'माझी प्रगती', 'Papers, topic-wise अचूकता, Badges') + it('#/examday', '🎒', 'परीक्षेचा दिवस', 'Checklist, venue, वेळ') + it('#/report', '📤', 'Tutor ला Report पाठवा', 'WhatsApp वर एका टॅपमध्ये')
        + '<div class="card"><b>नाव</b><input type="text" id="nm2" value="' + esc(S.name) + '" style="margin:8px 0"><div class="row g"><button data-a="rename">नाव बदला</button><button data-a="reset" style="color:var(--bad)">सर्व data पुसा</button></div></div>'
        + '<div class="card"><b>' + tt('Tutor (' + esc(S.tutor.name) + ') चा WhatsApp नंबर', 'Tutor (' + esc(S.tutor.name) + ') WhatsApp number') + '</b><div class="mu sm">' + tt('Report थेट त्यांच्याकडे जाईल (10 अंकी नंबर)', 'Reports go straight to them (10-digit number)') + '</div><input type="text" id="tph" inputmode="numeric" value="' + esc(S.tutor.phone || '') + '" style="margin:8px 0"><button data-a="savetutor">Save</button></div>')
};
ACT.savetutor = () => { S.tutor.phone = $('#tph').value.replace(/\D/g, ''); save(); toast('Saved ✓') };
ACT.rename = () => { const v = $('#nm2').value.trim(); if (v) { S.name = v; save(); toast('नाव बदलले'); sync() } };
ACT.reset = () => { if (confirm(trs('सर्व प्रगती (XP, tasks, attempts) पुसली जाईल. खात्री आहे?'))) { localStorage.removeItem(KEY); location.hash = '#/home'; location.reload() } };

/* flashcards */
let DECK = null;
V.cards = function (topic) {
    topic = decodeURIComponent(topic || 'all');
    const topics = [...new Set(D.extras.flash.map(f => f[0]))];
    if (!DECK || DECK.topic !== topic || DECK.fin) {
        const idx = D.extras.flash.map((f, i) => i).filter(i => (topic === 'all' || D.extras.flash[i][0] === topic || (topic === 'Taxation' && D.extras.flash[i][0] === 'Budget') || (topic === 'Banking' && D.extras.flash[i][0] === 'Computer')));
        const todo = idx.filter(i => (S.cards[i] || 0) < 3); DECK = { topic, list: (todo.length ? todo : idx).sort(() => Math.random() - .5).slice(0, 15), i: 0, flip: false, got: 0, fin: false }
    }
    const chips = '<div class="row wrap g" style="margin:6px 0">' + ['all'].concat(topics).map(t => '<a class="chip ' + (t === topic ? '' : 'wn') + '" href="#/cards/' + encodeURIComponent(t) + '" data-a="resetdeck">' + (t === 'all' ? 'सर्व' : t) + '</a>').join('') + '</div>';
    if (DECK.i >= DECK.list.length) { DECK.fin = true; autoMark('cards', topic); addXP(30, '(Flashcards पूर्ण)'); return render('<h1>🃏 Flashcards</h1><div class="card c"><div class="big">🎉</div><b>' + DECK.got + '/' + DECK.list.length + ' लक्षात आले</b><p class="mu">जे अजून नीट नाही ते पुन्हा येईल. रोज 10 मिनिटे पुरे!</p><a class="btn p" href="#/cards/' + encodeURIComponent(topic) + '" data-a="resetdeck">पुन्हा करा</a></div>') }
    const f = D.extras.flash[DECK.list[DECK.i]], known = Object.values(S.cards).filter(c => c >= 3).length;
    render('<h1>🃏 Flashcards</h1>' + chips + '<div class="mu sm">' + (DECK.i + 1) + '/' + DECK.list.length + ' · पक्के झालेले: ' + known + '/' + D.extras.flash.length + '</div>' + bar(pct(DECK.i, DECK.list.length))
        + '<div class="fc ' + (DECK.flip ? 'back' : '') + '" data-a="flip"><div class="in">' + esc(DECK.flip ? f[2] : f[1]) + '</div></div>'
        + (DECK.flip ? '<div class="grid2"><button data-a="cardno">↻ पुन्हा दाखवा</button><button class="ok" data-a="cardyes">✓ समजले</button></div>' : '<button class="p w" data-a="flip">उत्तर पाहा</button>') + '<p class="mu c sm">कार्डवर टॅप करा</p>')
};
ACT.resetdeck = () => { DECK = null };
ACT.flip = () => { DECK.flip = !DECK.flip; V.cards(DECK.topic) };
ACT.cardyes = () => { const i = DECK.list[DECK.i]; S.cards[i] = Math.min(3, (S.cards[i] || 0) + 1); DECK.got++; DECK.i++; DECK.flip = false; save(); addXP(3); checkBadges(); V.cards(DECK.topic) };
ACT.cardno = () => { S.cards[DECK.list[DECK.i]] = 0; DECK.i++; DECK.flip = false; save(); V.cards(DECK.topic) };

V.cheat = function () {
    autoMark('cheat', 0);
    render('<h1>📄 Cheat Sheet</h1><p class="mu">परीक्षेपूर्वी हे वाचा. (print/screenshot घेऊ शकता)</p>' + D.extras.cheat.map(s => '<div class="card"><b>' + esc(s.title) + '</b><table style="margin-top:8px">' + s.rows.map(r => '<tr><td style="width:36%"><b>' + esc(r[0]) + '</b></td><td>' + esc(r[1]) + '</td></tr>').join('') + '</table></div>').join(''))
};

V.examday = function () {
    autoMark('exam', 0);
    const E = D.extras.exam;
    render('<div class="hero"><h1>🎒 परीक्षेचा दिवस</h1><div class="q">27 ऑक्टोबर 2026 · सकाळी 11:00</div><div class="cd" id="cd"></div></div><div class="card"><b>📍 ठिकाण</b><p>' + esc(E.venue) + '</p><a class="btn" target="_blank" href="https://www.google.com/maps/search/' + encodeURIComponent('M.C.E.D. A-38 MIDC Area Chhatrapati Sambhajinagar') + '">नकाशा उघडा</a></div>'
        + '<div class="card"><b>✅ सोबत घ्यायचे</b>' + E.carry.map((c, i) => '<div class="task ' + (S.checks['c' + i] ? 'done' : '') + '"><button class="ck" data-a="chk" data-v="c' + i + '">' + (S.checks['c' + i] ? '✓' : '') + '</button><div class="t" style="flex:1">' + esc(c) + '</div></div>').join('') + '</div>'
        + '<div class="card"><b>🧠 टिप्स</b><ul class="l"><li>10:30 पर्यंत पोहोचा; आदल्या दिवशी मार्ग पाहून ठेवा.</li><li>आधी सोपे प्रश्न (full forms, definitions), मग गणित.</li><li>गणित: उत्तर options शी जुळवा.</li><li>आदल्या रात्री लवकर झोपा; सकाळी हलका नाश्ता.</li><li>नवीन काही शिकू नका; Cheat sheet एकदा वाचा.</li></ul></div><div class="card sm mu">' + esc(E.note) + '</div>');
    const tick = () => { const ms = Math.max(0, examTime() - Date.now()), el = $('#cd'); if (!el) return; el.innerHTML = trs('<div><b>' + Math.floor(ms / 864e5) + '</b><span>दिवस</span></div><div><b>' + Math.floor(ms % 864e5 / 36e5) + '</b><span>तास</span></div><div><b>' + Math.floor(ms % 36e5 / 6e4) + '</b><span>मिनिटे</span></div>') }; tick(); curTimer = setInterval(tick, 30000)
};
ACT.chk = k => { S.checks[k] = !S.checks[k]; save(); V.examday() };

V.progress = function () {
    const rows = D.papers.map(p => { const l = latest(p.id), n = papersOf(S.attempts).filter(a => String(a.p) === String(p.id)).length; return '<tr><td>' + esc(p.title.replace(/^Paper (\d+): /, '$1. ')) + '</td><td>' + (l ? pct(l.t, l.o) + '%' : '—') + '</td><td>' + (n ? best(p.id) + '%' : '—') + '</td><td>' + n + '</td></tr>' }).join('');
    const weak = [];
    D.papers.forEach(p => subAgg(p.id).forEach((x, i) => { if (x[1] >= 3 && pct(x[0], x[1]) < 60) weak.push([p, i, pct(x[0], x[1])]) }));
    render('<h1>📈 माझी प्रगती</h1><div class="grid3"><div class="card c"><div class="big">' + S.attempts.length + '</div><div class="mu">Attempts</div></div><div class="card c"><div class="big">' + Object.keys(S.lessons).length + '</div><div class="mu">Lessons वाचले</div></div><div class="card c"><div class="big">' + Object.keys(S.wrong).length + '</div><div class="mu">उजळणीचे प्रश्न</div></div></div>'
        + '<div class="card"><b>Papers</b><table style="margin-top:8px"><tr><th>Paper</th><th>शेवटचा</th><th>सर्वोत्तम</th><th>वेळा</th></tr>' + rows + '</table></div>'
        + '<div class="card"><b>🧠 Concept स्थिती (topic-wise)</b><div class="mu sm">पक्के = ≥80% (किमान 3 प्रश्नांवर) · शिकत आहे = 50–79% · कमकुवत &lt;50% · नवीन = अजून पुरेसा सराव नाही</div>' + D.papers.filter(p => p.id >= 2 && p.id <= 10).map(p => { const ag = subAgg(p.id), st = ag.map(x => x[1] < 3 ? 'n' : pct(x[0], x[1]) >= 80 ? 'm' : pct(x[0], x[1]) >= 50 ? 'l' : 'w'), c = k => st.filter(z => z === k).length; return '<div class="pill sm" style="margin:10px 0 2px"><span>' + esc(p.title.replace(/^Paper (\d+): /, '$1. ')) + (S.lessons[p.id] ? ' ✓' : '') + '</span><span>✅' + c('m') + ' 📘' + c('l') + ' ⚠️' + c('w') + ' ⚪' + c('n') + '</span></div>' + bar(pct(c('m'), st.length)) }).join('') + '</div>'
        + '<div class="card"><b>🎯 आधी शिकायचे (topic-wise अचूकता &lt;60%)</b>' + (weak.length ? weak.sort((a, b) => a[2] - b[2]).slice(0, 8).map(w => '<div class="pill sm" style="margin:8px 0 2px"><span>' + esc(w[0].subtopics[w[1]]) + '</span><b>' + w[2] + '%</b></div>' + bar(w[2]) + '<a class="sm" href="#/lesson/' + w[0].id + '">→ ' + esc(w[0].lessons[w[1]]) + '</a>').join('') : '<p class="mu">अजून पुरेसा data नाही, किंवा सर्व topics चांगले आहेत. सराव करत रहा!</p>') + '</div>'
        + '<div class="card"><b>🏆 Badges</b><br>' + BADGES.map(b => '<span class="badge ' + (S.badges.includes(b[0]) ? 'on' : '') + '"><span>' + b[1] + '</span>' + b[2] + '</span>').join('') + '</div>')
};
