/* learn: lesson list + lessons (notes, worked examples, interactive practice) + paper list */
const rich = t => esc(t).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>');
const STEP_TITLE = { 1: 'Baseline विश्लेषण', 2: 'Accounting Basics', 3: 'Debit/Credit & Journal', 4: 'Ledger, Cash Book, TB', 5: 'BRS, Depreciation, Final Accounts', 6: 'Taxation (GST, TDS)', 7: 'Budget & Financial Discipline', 8: 'Banking & Digital Payments', 9: 'Computer, Excel, Modern Tools', 10: 'Current Affairs', 11: 'Mock — रणनीती' };

V.learn = function () {
    render('<h1>📚 शिका</h1><p class="mu">क्रमाने शिका: आधी Lesson वाचा, मग Practice. 📖 → ✍️ → 🎯</p>' + [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 11].map(id => {
        const l = latest(id), read = S.lessons[id], p = paper(id);
        return '<div class="card"><div class="row sp"><div><div class="b">' + id + '. ' + STEP_TITLE[id] + '</div><div class="mu sm">' + p.questions.length + ' प्रश्न · ' + p.duration + ' मि.</div></div><div>' + (read ? '<span class="chip ok">समजला ✓</span> ' : '<span class="chip wn">Check बाकी</span> ') + (l ? '<span class="chip ' + cls(pct(l.t, l.o)) + '">' + pct(l.t, l.o) + '%</span>' : '') + '</div></div>'
            + '<div class="row g" style="margin-top:10px"><a class="btn p" href="#/lesson/' + id + '">📖 Lesson</a><a class="btn" href="#/check/' + id + '">🧠 Check</a><a class="btn" href="#/practice/' + id + '">✍️ Practice</a><a class="btn" href="#/exam/' + id + '">📝 Exam</a></div></div>'
    }).join(''))
};

let LQ = {};
V.lesson = function (id) {
    const L = D.lessons[id], p = paper(id); if (!L) return location.hash = '#/learn';
    const mn = (D.extras.mnemonics[id] || []).map(m => '<div class="tip">💡 ' + rich(m) + '</div>').join('');
    let h = '<div class="hero"><div class="mu" style="color:#fff;opacity:.85">Lesson ' + id + '</div><h1>' + STEP_TITLE[id] + '</h1><div class="q">आधी वाचा, उदाहरणे समजून घ्या, मग खाली सराव करा.</div></div>' + mn;
    L.forEach((b, bi) => {
        const t = b[0];
        if (t === 'h') h += b[1] === 1 ? '<h2>' + esc(b[2]) + '</h2>' : '<h3>' + esc(b[2]) + '</h3>';
        else if (t === 'p') h += '<p>' + rich(b[1]) + '</p>';
        else if (t === 'b') h += '<ul class="l">' + b[1].map(x => '<li>' + rich(x) + '</li>').join('') + '</ul>';
        else if (t === 't') h += '<div style="overflow-x:auto"><table>' + b[1].map((r, ri) => '<tr>' + r.map(c => (ri ? '<td>' : '<th>') + rich(c) + (ri ? '</td>' : '</th>')).join('') + '</tr>').join('') + '</table></div>';
        else if (t === 'ex') h += '<div class="ex"><b>✍️ उदाहरण: ' + esc(b[1]) + '</b><div class="sm" style="margin:4px 0"><b>प्रश्न:</b> ' + rich(b[2]) + '</div>' + b[3].split('\n').map(l => '<div class="st">' + rich(l) + '</div>').join('') + '</div>';
        else if (t === 'pq') {
            h += '<h2>🎯 ' + esc(b[1]) + '</h2><p class="mu sm">पर्याय निवडा — लगेच उत्तर आणि कारण दिसेल.</p>';
            b[2].forEach((q, qi) => { h += '<div class="card" id="lq' + bi + '_' + qi + '"><b>P' + (qi + 1) + '. ' + esc(q[0]) + '</b>' + q[1].map((o, k) => '<button class="opt" data-a="lq" data-v="' + bi + ',' + qi + ',' + 'ABCD'[k] + '">' + 'ABCD'[k] + '. ' + esc(o) + '</button>').join('') + '<div class="sm" id="lqf' + bi + '_' + qi + '"></div></div>' })
        }
    });
    h += '<div class="card c"><b>🧠 आता तपासूया — concept खरंच समजला का?</b><p class="mu sm">५ प्रश्न, किमान ४ बरोबर हवेत. तेव्हाच हा Lesson "समजला" मानला जाईल.</p>' + (S.lessons[id] ? '<span class="chip ok">Concept समजला ✓</span> ' : '') + '<a class="btn ok w" style="margin-top:8px" href="#/check/' + id + '">' + (S.lessons[id] ? '🧠 पुन्हा Concept Check' : '✅ Concept Check द्या (+50 XP)') + '</a><a class="btn w" style="margin-top:8px" href="#/practice/' + id + '">✍️ Practice सुरू करा</a></div>';
    render(h)
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
        + D.papers.map(p => { const l = latest(p.id); return '<div class="card"><div class="row sp"><div style="flex:1"><div class="b sm">' + esc(p.title) + '</div><div class="mu sm">' + p.questions.length + ' प्रश्न · ' + p.duration + ' मि.' + (l ? ' · शेवटचा <b>' + pct(l.t, l.o) + '%</b>' : '') + '</div></div></div><div class="row g" style="margin-top:8px"><a class="btn p" href="#/practice/' + p.id + '">Practice</a><a class="btn" href="#/exam/' + p.id + '">Exam</a></div></div>' }).join(''))
};
