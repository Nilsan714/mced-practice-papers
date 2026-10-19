/* tutor: Report (student -> WhatsApp/copy code) and Tutor Dashboard (import codes / live from local server) */
const b64u = u8 => { let s = ''; for (let i = 0; i < u8.length; i += 8192) s += String.fromCharCode.apply(null, u8.subarray(i, i + 8192)); return btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '') };
const unb64u = t => { t = t.replace(/-/g, '+').replace(/_/g, '/'); while (t.length % 4) t += '='; const s = atob(t), u = new Uint8Array(s.length); for (let i = 0; i < s.length; i++) u[i] = s.charCodeAt(i); return u };
async function pack(o) {
    const raw = new TextEncoder().encode(JSON.stringify(o));
    if (window.CompressionStream) { const cs = new CompressionStream('deflate-raw'), w = cs.writable.getWriter(); w.write(raw); w.close(); return 'MCEDP2:' + b64u(new Uint8Array(await new Response(cs.readable).arrayBuffer())) }
    return 'MCEDP1:' + b64u(raw)
}
async function unpack(code) {
    const k = code.slice(0, 7), u = unb64u(code.slice(7));
    if (k === 'MCEDP1:') return JSON.parse(new TextDecoder().decode(u));
    const ds = new DecompressionStream('deflate-raw'), w = ds.writable.getWriter(); w.write(u); w.close();
    return JSON.parse(new TextDecoder().decode(await new Response(ds.readable).arrayBuffer()))
}
const TKEY = 'mced_tutor_v1';
const loadT = () => { try { return JSON.parse(localStorage[TKEY] || '{"students":{},"notes":{}}') } catch (e) { return { students: {}, notes: {} } } };
const saveT = t => { try { localStorage[TKEY] = JSON.stringify(t) } catch (e) { } };
const planPct = snap => { const ids = D.extras.plan.flatMap(d => d.tasks.map(t => t[0])); return pct(ids.filter(i => snap.tasks.includes(i)).length, ids.length) };
function subAggSnap(snap) {
    const r = {}; D.papers.forEach(p => { r[p.id] = p.subtopics.map(() => [0, 0]) });
    snap.attempts.filter(a => (a.m === 'exam' || a.m === 'practice' || a.m === 'check') && r[a.p]).forEach(a => (a.s || []).forEach((x, i) => { if (r[a.p][i]) { r[a.p][i][0] += x[0]; r[a.p][i][1] += x[1] } })); return r
}
function weakList(snap) { const ag = subAggSnap(snap), out = []; D.papers.forEach(p => ag[p.id].forEach((x, i) => { if (x[1] >= 3 && pct(x[0], x[1]) < 60) out.push({ p, i, v: pct(x[0], x[1]), n: x[1] }) })); return out.sort((a, b) => a.v - b.v) }
const ago = ts => { const m = Math.round((Date.now() - ts) / 6e4); return m < 60 ? m + ' मिनिटांपूर्वी' : m < 1440 ? Math.round(m / 60) + ' तासांपूर्वी' : Math.round(m / 1440) + ' दिवसांपूर्वी' };

/* ---------- student: report ---------- */
V.report = async function () {
    const sn = snapshot(), wl = weakList(sn), done = planPct(sn);
    const lines = ['📊 ' + S.name + ' — MCED तयारी रिपोर्ट (' + new Date().toLocaleDateString('en-IN') + ')', 'परीक्षेला ' + daysLeft() + ' दिवस बाकी | प्लॅन ' + done + '% | 🔥' + sn.streak + ' दिवस | ⭐' + sn.xp + ' XP', 'Lessons वाचले: ' + sn.lessons.length + ' | Attempts: ' + sn.attempts.length + ' | Flashcards पक्के: ' + sn.cards.known + '/' + sn.cards.total]
        .concat(D.papers.filter(p => sn.attempts.some(x => String(x.p) === String(p.id) && (x.m === 'exam' || x.m === 'practice'))).map(p => { const a = sn.attempts.filter(x => String(x.p) === String(p.id) && (x.m === 'exam' || x.m === 'practice')), l = a[a.length - 1]; return '• Paper ' + p.id + ': ' + pct(l.t, l.o) + '% (' + a.length + ' वेळा)' }))
        .concat(wl.length ? ['⚠️ कमकुवत: ' + wl.slice(0, 3).map(w => w.p.subtopics[w.i] + ' ' + w.v + '%').join(', ')] : []);
    lines.forEach((l, i) => { lines[i] = trs(l) });
    const code = await pack(sn), text = lines.join('\n') + (isEn() ? '\n\nCode for the tutor (paste in Tutor Dashboard):\n' : '\n\nTutor साठी कोड (Tutor Dashboard मध्ये paste करा):\n') + code;
    render('<h1>📤 Tutor ला Report</h1><p class="mu">एका टॅपमध्ये WhatsApp वर पाठवा. Tutor त्यांच्या Dashboard मध्ये paste करतील आणि तुमची प्रगती पाहतील.</p><div class="card"><pre style="white-space:pre-wrap;font:14px/1.5 inherit;margin:0" id="rtxt">' + esc(lines.join('\n')) + '</pre><div class="mu sm" style="margin-top:8px;word-break:break-all">+ कोड (' + code.length + ' अक्षरे)</div></div>'
        + '<div class="grid2"><a class="btn p" target="_blank" rel="noopener" href="https://wa.me/' + waNum() + '?text=' + encodeURIComponent(text) + '">WhatsApp 💬</a><button data-a="rcopy">Copy 📋</button></div>' + (navigator.share ? '<button class="w" style="margin-top:10px" data-a="rshare">Share… ↗</button>' : '') + '<textarea id="rcode" style="display:none">' + esc(text) + '</textarea>');
    window._rep = text
};
ACT.rcopy = async () => { try { await navigator.clipboard.writeText(window._rep); toast('कॉपी झाले ✓') } catch (e) { const t = $('#rcode'); t.style.display = 'block'; t.select(); toast('हे select करून copy करा') } };
ACT.rshare = () => navigator.share({ text: window._rep }).catch(() => { });

/* ---------- tutor dashboard ---------- */
let TSEL = null;
V.tutor = async function (name) {
    const T = loadT(); TSEL = name ? decodeURIComponent(name) : TSEL;
    let live = []; try { const r = await fetch('api/progress'); if (r.ok && (r.headers.get('content-type') || '').includes('json')) live = await r.json() } catch (e) { }
    live.forEach(s => { const a = T.students[s.name] = T.students[s.name] || []; if (!a.some(x => x.ts === s.ts)) a.push(s) });
    Object.values(T.students).forEach(a => a.sort((x, y) => x.ts - y.ts)); saveT(T);
    const names = Object.keys(T.students);
    let h = '<h1>👩‍🏫 Tutor Dashboard</h1><div class="card"><b>विद्यार्थ्याचा Report paste करा</b><textarea id="tin" rows="3" placeholder="WhatsApp मधला संदेश (MCEDP2:… कोडसह) येथे paste करा" style="margin:8px 0"></textarea><button class="p w" data-a="timport">Import ✓</button>' + (live.length ? '<p class="mu sm">🟢 Local server वरून ' + live.length + ' विद्यार्थ्यांचा live data मिळाला.</p>' : '<p class="mu sm">Local server (same Wi-Fi) वरून उघडल्यास data आपोआप येतो.</p>') + '</div>';
    if (!names.length) return render(h + '<div class="card c mu">अजून कोणताही विद्यार्थी नाही.</div>');
    if (!TSEL || !T.students[TSEL]) TSEL = names[0];
    h += '<div class="row wrap g">' + names.map(n => '<a class="chip ' + (n === TSEL ? '' : 'wn') + '" href="#/tutor/' + encodeURIComponent(n) + '">' + esc(n) + '</a>').join('') + '</div>';
    const snaps = T.students[TSEL], s = snaps[snaps.length - 1], wl = weakList(s), ag = subAggSnap(s), pp = planPct(s), idle = Date.now() - s.ts;
    h += '<div class="card"><div class="row sp"><div><div class="b" style="font-size:19px">' + esc(s.name) + '</div><div class="mu sm">शेवटचा Report: ' + ago(s.ts) + '</div></div>' + ring(pp) + '</div>'
        + (idle > 864e5 ? '<div class="tip">⚠️ ' + ago(s.ts) + ' शेवटची activity — आज संपर्क साधा.</div>' : '') + '<div class="grid3" style="margin-top:10px"><div class="c"><div class="b">' + daysLeft() + '</div><div class="mu sm">दिवस बाकी</div></div><div class="c"><div class="b">🔥' + s.streak + '</div><div class="mu sm">Streak</div></div><div class="c"><div class="b">⭐' + s.xp + '</div><div class="mu sm">XP</div></div></div>'
        + '<div class="mu sm" style="margin-top:8px">Lessons ' + s.lessons.length + '/11 · Flashcards ' + s.cards.known + '/' + s.cards.total + ' · उजळणीचे प्रश्न ' + s.wrong + ' · Attempts ' + s.attempts.length + '</div></div>';
    const P = D.extras.personal, lastA = s.attempts.filter(a => a.m !== 'weak').slice(-1)[0], what = lastA ? 'Paper ' + lastA.p + ' ' + pct(lastA.t, lastA.o) + '%' : tt('सराव', 'practice'), V0 = { name: s.name };
    const wa = t => 'https://wa.me/?text=' + encodeURIComponent(fillT(t, Object.assign({ what }, V0)));
    h += '<div class="card"><b>💬 ' + tt(esc(s.name) + ' ला WhatsApp वर पाठवा', 'Send ' + esc(s.name) + ' a WhatsApp message') + '</b><div class="row g wrap" style="margin-top:8px"><a class="btn" target="_blank" href="' + wa(P.wa_praise) + '">💪 ' + tt('कौतुक', 'Praise') + '</a><a class="btn" target="_blank" href="' + wa(P.wa_nudge) + '">👋 ' + tt('आठवण', 'Nudge') + '</a>' + (wl.length ? '<a class="btn" target="_blank" href="' + wa(P.wa_weak.replace('{topic}', wl[0].p.subtopics[wl[0].i]).replace('{v}', wl[0].v)) + '">🎯 ' + tt('कमकुवत topic', 'Weak topic') + '</a>' : '') + '</div></div>';
    h += '<div class="card"><b>🎯 आज काय शिकवायचे (सुचवलेले)</b>' + (wl.length ? wl.slice(0, 4).map(w => '<div class="pill sm" style="margin:8px 0 2px"><span>Paper ' + w.p.id + ' — ' + esc(w.p.subtopics[w.i]) + '</span><b>' + w.v + '%</b></div>' + bar(w.v) + '<div class="mu sm">→ ' + esc(w.p.lessons[w.i]) + ' (' + w.n + ' प्रश्नांवर आधारित)</div>').join('') : '<p class="mu">पुरेसा data नाही किंवा सर्व topics ≥60%. नवीन paper सोडवायला सांगा.</p>') + '</div>';
    const rows = D.papers.map(p => { const a = s.attempts.filter(x => String(x.p) === String(p.id) && (x.m === 'exam' || x.m === 'practice')); if (!a.length) return '<tr><td>' + p.id + '</td><td colspan="3" class="mu">—</td></tr>'; const l = a[a.length - 1], b = Math.max(...a.map(x => pct(x.t, x.o))); return '<tr><td>' + p.id + '</td><td>' + pct(l.t, l.o) + '%</td><td>' + b + '%</td><td>' + a.length + '</td></tr>' }).join('');
    h += '<div class="card"><b>Papers</b><table style="margin-top:8px"><tr><th>#</th><th>शेवटचा</th><th>सर्वोत्तम</th><th>वेळा</th></tr>' + rows + '</table></div>';
    h += '<div class="card"><b>📅 प्लॅन प्रगती</b>' + D.extras.plan.map(d => { const v = pct(d.tasks.filter(t => s.tasks.includes(t[0])).length, d.tasks.length); return '<div class="pill sm" style="margin:8px 0 2px"><span>' + esc(d.title.split('—')[0]) + '</span><b>' + v + '%</b></div>' + bar(v, v === 100 ? 'ok' : '') }).join('') + '</div>';
    h += '<div class="card"><b>🕒 अलीकडचे Attempts</b>' + s.attempts.slice(-10).reverse().map(a => '<div class="pill sm" style="margin:8px 0 2px"><span>' + (a.p === 'W' ? 'कमकुवत Quiz' : 'Paper ' + a.p) + ' · ' + a.m + ' · ' + new Date(a.ts).toLocaleDateString('en-IN') + '</span><b>' + a.t + '/' + a.o + '</b></div>' + bar(pct(a.t, a.o))).join('') + '</div>';
    h += '<div class="card"><b>📝 Tutor Notes</b><textarea id="tnote" rows="3" style="margin:8px 0">' + esc(T.notes[TSEL] || '') + '</textarea><div class="row g"><button data-a="tnote">Save</button><button data-a="tcsv">CSV Export ⬇</button></div></div>';
    render(h)
};
ACT.timport = async () => {
    const codes = ($('#tin').value.match(/MCEDP[12]:[A-Za-z0-9_\-]+/g) || []); if (!codes.length) return toast('कोड सापडला नाही');
    const T = loadT(); let n = 0;
    for (const c of codes) { try { const s = await unpack(c), a = T.students[s.name] = T.students[s.name] || []; if (!a.some(x => x.ts === s.ts)) { a.push(s); n++ } TSEL = s.name } catch (e) { console.error(e) } }
    saveT(T); toast(n + ' Report import झाले ✓'); V.tutor(TSEL)
};
ACT.tnote = () => { const T = loadT(); T.notes[TSEL] = $('#tnote').value; saveT(T); toast('Saved ✓') };
ACT.tcsv = () => {
    const s = loadT().students[TSEL].slice(-1)[0], rows = [['name', 'paper', 'mode', 'date', 'score', 'out_of', 'percent']].concat(s.attempts.map(a => [s.name, a.p, a.m, new Date(a.ts).toISOString().slice(0, 16), a.t, a.o, pct(a.t, a.o)]));
    const blob = new Blob(['﻿' + rows.map(r => r.join(',')).join('\n')], { type: 'text/csv' }), a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = s.name + '_progress.csv'; a.click()
};
