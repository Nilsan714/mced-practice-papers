/* learn: lesson list + lessons (notes, worked examples, interactive practice) + paper list */
const rich = t => esc(t).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>');
const STEP_TITLE = { 1: 'Baseline विश्लेषण', 2: 'Accounting Basics', 3: 'Debit/Credit & Journal', 4: 'Ledger, Cash Book, TB', 5: 'BRS, Depreciation, Final Accounts', 6: 'Taxation (GST, TDS)', 7: 'Budget & Financial Discipline', 8: 'Banking & Digital Payments', 9: 'Computer, Excel, Modern Tools', 10: 'Current Affairs', 11: 'Mock — रणनीती' };

V.learn = function () {
    render('<h1>📚 शिका</h1><p class="mu">क्रमाने शिका: आधी Lesson वाचा, मग Practice. 📖 → ✍️ → 🎯</p>' + [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 11].map(id => {
        const l = latest(id), read = S.lessons[id], p = paper(id);
        return '<div class="card"><div class="row sp"><div><div class="b">' + id + '. ' + STEP_TITLE[id] + '</div><div class="mu sm">' + mainQs(p).length + ' प्रश्न · ' + p.duration + ' मि.</div></div><div>' + (read ? '<span class="chip ok">समजला ✓</span> ' : '<span class="chip wn">Check बाकी</span> ') + (l ? '<span class="chip ' + cls(pct(l.t, l.o)) + '">' + pct(l.t, l.o) + '%</span>' : '') + '</div></div>'
            + '<div class="row g" style="margin-top:10px"><a class="btn p" href="#/lesson/' + id + '">📖 Lesson</a><a class="btn" href="#/check/' + id + '">🧠 Check</a><a class="btn" href="#/practice/' + id + '">✍️ Practice</a><a class="btn" href="#/exam/' + id + '">📝 Exam</a></div></div>'
    }).join(''))
};

let LQ = {}, LST = { id: null, step: 0, total: 0 };
function lessonSections(L) {
    const secs = []; let cur = null;
    L.forEach((b, bi) => {
        if (b[0] === 'h' && b[1] === 1) { cur = { title: b[2], blocks: [] }; secs.push(cur) }
        else { if (!cur) { cur = { title: null, blocks: [] }; secs.push(cur) } cur.blocks.push([b, bi]) }
    });
    const pages = [];
    secs.forEach(sc => {
        let c = { title: sc.title, blocks: [] }, n = 1;
        sc.blocks.forEach(x => { c.blocks.push(x); if (x[0][0] === 'ex' || x[0][0] === 'pq') { pages.push(c); n++; c = { title: sc.title ? sc.title + ' (' + n + ')' : null, blocks: [] } } });
        if (c.blocks.length) pages.push(c)
    });
    return pages
}
function renderBlock(b, bi) {
    const t = b[0];
    if (t === 'h') return b[1] === 1 ? '<h2>' + esc(b[2]) + '</h2>' : '<h3>' + esc(b[2]) + '</h3>';
    if (t === 'p') return '<p>' + rich(b[1]) + '</p>';
    if (t === 'b') return '<ul class="l">' + b[1].map(x => '<li>' + rich(x) + '</li>').join('') + '</ul>';
    if (t === 't') return '<div style="overflow-x:auto"><table>' + b[1].map((r, ri) => '<tr>' + r.map(c => (ri ? '<td>' : '<th>') + rich(c) + (ri ? '</td>' : '</th>')).join('') + '</tr>').join('') + '</table></div>';
    if (t === 'ex') {
        const lines = b[3].split('\n');
        return '<div class="ex"><b>✍️ ' + tt('उदाहरण', 'Example') + ': ' + esc(b[1]) + '</b><div style="margin:6px 0"><b>' + tt('प्रश्न', 'Question') + ':</b> ' + rich(b[2]) + '</div><div class="steps">' + lines.map((l, k) => '<div class="st" style="' + (k ? 'display:none' : '') + '">' + (k ? '' : '👉 ') + rich(l) + '</div>').join('')
            + '</div>' + (lines.length > 1 ? '<div class="row g" style="margin-top:8px"><button class="sm p" data-a="exnext">' + tt('👉 पुढची पायरी', '👉 Next step') + '</button><button class="sm" data-a="exall">' + tt('सर्व दाखवा', 'Show all') + '</button></div>' : '') + '</div>'
    }
    if (t === 'pq') {
        let h = '<h2>🎯 ' + esc(b[1]) + '</h2><p class="mu sm">' + tt('पर्याय निवडा — लगेच उत्तर आणि कारण दिसेल.', 'Choose an option — the answer and reason appear instantly.') + '</p>';
        b[2].forEach((q, qi) => { h += '<div class="card" id="lq' + bi + '_' + qi + '"><b>P' + (qi + 1) + '. ' + esc(q[0]) + '</b>' + q[1].map((o, k) => '<button class="opt" data-a="lq" data-v="' + bi + ',' + qi + ',' + 'ABCD'[k] + '">' + 'ABCD'[k] + '. ' + esc(o) + '</button>').join('') + '<div class="sm" id="lqf' + bi + '_' + qi + '"></div></div>' });
        return h
    }
    return ''
}
V.lesson = function (id, step) {
    const L = D.lessons[id], p = paper(id); if (!L) return location.hash = '#/learn';
    const secs = lessonSections(L), total = secs.length + 1; step = Math.max(0, Math.min(total - 1, +step || 0));
    LST = { id, step, total };
    const fs = S.fs || 'm', last = step === total - 1;
    let h = '<div class="top"><a href="#/learn" class="btn sm" style="padding:6px 12px">←</a><b>' + tt('Lesson', 'Lesson') + ' ' + id + ' · ' + (step + 1) + '/' + total + '</b><span class="row g"><button class="sm" data-a="fs" data-v="s" style="padding:6px 10px">A−</button><button class="sm" data-a="fs" data-v="b" style="padding:6px 10px">A+</button><button class="sm" data-a="speak" style="padding:6px 10px">🔊</button></span></div>' + bar(pct(step + 1, total));
    h += '<div class="lesson fs-' + fs + '"><div class="lbody">';
    if (!last) {
        const sc = secs[step];
        if (step === 0) {
            h += '<div class="hero" style="margin-top:10px"><div style="opacity:.9;font-size:13px">Lesson ' + id + '</div><h1>' + STEP_TITLE[id] + '</h1><div class="q">' + tt('एका वेळी एकच भाग वाचा. उदाहरणात "पुढची पायरी" दाबा.', 'Read one part at a time. In examples tap "Next step".') + '</div></div>' + (D.extras.mnemonics[id] || []).map(m => '<div class="tip">💡 ' + rich(m) + '</div>').join('')
        }
        if (sc.title) h += '<h2 class="sec">' + esc(sc.title) + '</h2>';
        h += sc.blocks.map(x => renderBlock(x[0], x[1])).join('');
    } else {
        h += '<div class="card c" style="margin-top:14px"><div class="big">🧠</div><b>' + tt('आता तपासूया — concept खरंच समजला का?', 'Let us check — is the concept really clear?') + '</b><p class="mu sm">' + tt('५ प्रश्न, किमान ४ बरोबर हवेत. तेव्हाच हा Lesson "समजला" मानला जाईल.', '5 questions, at least 4 must be correct. Only then is this Lesson counted as "understood".') + '</p>'
            + (S.lessons[id] ? '<span class="chip ok">' + tt('Concept समजला ✓', 'Concept understood ✓') + '</span> ' : '') + '<a class="btn ok w" style="margin-top:8px" href="#/check/' + id + '">' + (S.lessons[id] ? tt('🧠 पुन्हा Concept Check', '🧠 Concept Check again') : tt('✅ Concept Check द्या (+50 XP)', '✅ Take Concept Check (+50 XP)')) + '</a><a class="btn w" style="margin-top:8px" href="#/practice/' + id + '">' + tt('✍️ Practice सुरू करा', '✍️ Start Practice') + '</a></div>'
            + '<div class="card"><b>📋 ' + tt('या lesson मध्ये काय शिकलो', 'What we learned in this lesson') + '</b><ul class="l">' + secs.filter(s => s.title).map(s => '<li>' + esc(s.title) + '</li>').join('') + '</ul></div>'
    }
    h += '</div></div><div style="height:78px"></div><div class="lnav"><button data-a="lstep" data-v="-1" ' + (step ? '' : 'disabled') + '>← ' + tt('मागे', 'Back') + '</button><div class="dots">' + Array.from({ length: total }, (_, k) => '<i class="' + (k === step ? 'on' : k < step ? 'dn' : '') + '"></i>').join('') + '</div><button class="p" data-a="lstep" data-v="1" ' + (last ? 'disabled' : '') + '>' + tt('पुढे', 'Next') + ' →</button></div>';
    render(h)
};
ACT.lstep = d => { location.hash = '#/lesson/' + LST.id + '/' + (LST.step + (+d)) };
ACT.fs = v => { const o = ['m', 'l', 'xl'], i = o.indexOf(S.fs || 'm'); S.fs = o[Math.max(0, Math.min(2, i + (v === 'b' ? 1 : -1)))]; save(); V.lesson(LST.id, LST.step) };
ACT.exnext = (v, el) => { const ex = el.closest('.ex'), n = [...ex.querySelectorAll('.st')].find(s => s.style.display === 'none'); if (n) { n.style.display = ''; n.style.animation = 'fade .3s' } if (![...ex.querySelectorAll('.st')].some(s => s.style.display === 'none')) el.disabled = true };
ACT.exall = (v, el) => { const ex = el.closest('.ex'); ex.querySelectorAll('.st').forEach(s => { s.style.display = '' }); const b = ex.querySelector('[data-a="exnext"]'); if (b) b.disabled = true };
ACT.speak = () => {
    if (!('speechSynthesis' in window)) return toast(tt('या फोनमध्ये आवाज सुविधा नाही', 'Voice is not available on this phone'));
    if (speechSynthesis.speaking) { speechSynthesis.cancel(); return }
    const el = $('.lbody'); if (!el) return;
    const u = new SpeechSynthesisUtterance(el.innerText.replace(/[₹→✓✗👉💡✍️🎯]/g, ' ')), vs = speechSynthesis.getVoices(), want = isEn() ? 'en' : 'mr';
    u.lang = isEn() ? 'en-IN' : 'mr-IN'; const v = vs.find(x => x.lang.toLowerCase().startsWith(want)) || (isEn() ? null : vs.find(x => x.lang.toLowerCase().startsWith('hi'))); if (v) { u.voice = v; u.lang = v.lang } u.rate = .9; speechSynthesis.speak(u)
};
ACT.lq = (v, el) => {
    const [bi, qi, L] = v.split(','), id = location.hash.split('/')[2], q = D.lessons[id][bi][2][qi], card = el.closest('.card'), f = $('#lqf' + bi + '_' + qi);
    if (card.dataset.done) return; card.dataset.done = 1;
    $$('.opt', card).forEach(b => { const l = b.dataset.v.split(',')[2]; if (l === q[2]) b.classList.add('ok'); else if (l === L) b.classList.add('no'); b.disabled = true });
    f.innerHTML = (L === q[2] ? '<b style="color:var(--ok)">✓ बरोबर! ' + pick(D.extras.praise) + '</b>' : '<b style="color:var(--bad)">✗ बरोबर उत्तर: ' + q[2] + '</b>') + '<br>' + rich(q[3]);
    if (L === q[2]) addXP(5)
};
ACT.read = id => { S.lessons[id] = Date.now(); save(); addXP(50, '(Lesson पूर्ण)'); autoMark('lesson', id); checkBadges(); burst(['✅', '⭐']); V.lesson(id) };

V.papers = function () {
    render('<h1>✍️ सराव</h1><p class="mu"><b>Practice</b> = प्रत्येक प्रश्नानंतर लगेच explanation (शिकण्यासाठी). <b>Exam</b> = वेळेसह, शेवटी निकाल (परीक्षेची सवय).</p>'
        + '<div class="card"><div class="row sp"><div><div class="b">🎯 कमकुवत प्रश्नांचा Quiz</div><div class="mu sm">आधी चुकलेले ' + Object.keys(S.wrong).length + ' प्रश्न पुन्हा</div></div><a class="btn p" href="#/weak">सुरू</a></div></div>'
        + D.papers.map(p => { const l = latest(p.id); return '<div class="card"><div class="row sp"><div style="flex:1"><div class="b sm">' + esc(p.title) + '</div><div class="mu sm">' + mainQs(p).length + ' प्रश्न · ' + p.duration + ' मि.' + (l ? ' · शेवटचा <b>' + pct(l.t, l.o) + '%</b>' : '') + '</div></div></div><div class="row g" style="margin-top:8px"><a class="btn p" href="#/practice/' + p.id + '">Practice</a><a class="btn" href="#/exam/' + p.id + '">Exam</a></div></div>' }).join(''))
};
