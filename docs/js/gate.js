/* gate: day unlocking. A day opens only if (1) the previous day is PASSED and (2) its date is within 3 days from today (today + 2).
   A day is PASSED when 100% of its tasks are done AND every paper of the day has a timed Exam attempt of at least PASS %. */
const PASS = 80, AHEAD_DAYS = 2;
const hasTask = (tasks, id) => Array.isArray(tasks) ? tasks.includes(id) : !!tasks[id];
const examBest = (attempts, pid) => Math.max(0, ...attempts.filter(a => (a.m === 'exam') && String(a.p) === String(pid)).map(a => pct(a.t, a.o)));
const dayPapers = d => [...new Set(d.tasks.filter(t => ['lesson', 'practice', 'quiz'].includes(t[1]) && Number(t[2]) > 0).map(t => Number(t[2])))];
function gate(tasks, attempts, eb) {
    const cutoff = dstr(new Date(Date.now() + AHEAD_DAYS * 864e5)), out = [];
    D.extras.plan.forEach((d, i) => {
        const done = d.tasks.filter(t => hasTask(tasks, t[0])).length, total = d.tasks.length;
        const req = dayPapers(d).map(p => ({ p, best: eb ? (eb[p] || 0) : examBest(attempts, p) }));
        const scoreOk = req.every(r => r.best >= PASS), passed = done === total && scoreOk, prev = i === 0 || out[i - 1].passed, cal = d.date <= cutoff;
        out.push({ done, total, req, scoreOk, passed, prev, cal, unlocked: prev && cal })
    });
    return out
}
const myGate = () => gate(S.tasks, S.attempts);
function paperDay(pid) {
    const i = D.extras.plan.findIndex(d => d.tasks.some(t => ['lesson', 'practice', 'quiz'].includes(t[1]) && String(t[2]) === String(pid)));
    return i
}
function paperAllowed(pid) {
    if (TUTOR_MODE) return true;
    const i = paperDay(pid); if (i < 0) return true;
    return myGate()[i].unlocked
}
function lockReason(g, i) {
    const d = D.extras.plan[i];
    if (!g[i].prev) return tt('🔒 आधी Day ' + i + ' पूर्ण करा (सर्व tasks + Exam ≥' + PASS + '%).', '🔒 First complete Day ' + i + ' (all tasks + Exam ≥' + PASS + '%).');
    if (!g[i].cal) return tt('🔒 हा दिवस ' + d.date.slice(8) + ' Oct ला उघडेल (एका वेळी फक्त 3 दिवसांचे काम).', '🔒 This day opens on ' + d.date.slice(8) + ' Oct (only 3 days of work at a time).');
    return ''
}
