/* MCED District Account Assistant - Oral Interview UI Views (Coach, Mock 20M, 14-Day Plan, Syllabus, Profile) */

(function () {
    const DATA = window.INTERVIEW_DATA;
    let curActiveQ = null;
    let oralTimer = null;
    let timeLeft = 60;
    let sttEngine = null;
    let mockSession = null;

    // Helper to get questions
    function getQuestions(moduleFilter) {
        if (!moduleFilter || moduleFilter === 'ALL') return DATA.questions;
        if (moduleFilter === 'REVISION') {
            const rev = window.COACH_STATE.revisionList || {};
            const list = DATA.questions.filter(q => rev[q.id]);
            return list.length ? list : DATA.questions;
        }
        return DATA.questions.filter(q => q.module === moduleFilter);
    }

    function getQuestionById(id) {
        return DATA.questions.find(q => q.id === id) || DATA.questions[0];
    }

    // =========================================================================
    // VIEW 1: ORAL COACH (मुलाखत प्रशिक्षक - One Question At A Time)
    // =========================================================================
    V.coach = function (qId) {
        if ('speechSynthesis' in window) speechSynthesis.cancel();
        clearInterval(oralTimer);

        const prof = window.CANDIDATE_PROFILE;
        const coach = window.COACH_STATE;

        // If profile not completed, show Step 1 Profiling Dialog first
        if (!prof.completed && !coach.skipProfile) {
            return V.candidateProfileStep(1);
        }

        const qList = getQuestions(coach.activeModule);
        curActiveQ = qId ? getQuestionById(qId) : (qList.find(q => q.id === coach.currentQId) || qList[0]);
        coach.currentQId = curActiveQ.id;
        window.saveCoach();

        const modInfo = DATA.modules[curActiveQ.module] || { name: 'मुलाखत सराव', icon: '🎙️' };
        const rubricInfo = DATA.rubric[curActiveQ.rubric] || { name: 'मूल्यमापन', marks: 5 };
        const isMastered = !!(coach.mastered && coach.mastered[curActiveQ.id]);
        const isRevision = !!(coach.revisionList && coach.revisionList[curActiveQ.id]);

        // Module filter pills
        const modMap = {
            ALL: 'सर्व (All)',
            MCED: '🏛️ MCED व पद (30%)',
            SITUATIONAL: '🏢 कार्यालयीन प्रसंग (30%)',
            HR: '👤 HR व व्यक्तिमत्व (20%)',
            PRACTICAL_ACC: '📊 प्रॅक्टिकल अकाउंट्स (15%)',
            COMPUTER: '💻 कॉम्प्युटर/एक्सेल (5%)',
            REVISION: '🔖 उजळणी'
        };
        const modPills = ['ALL', 'MCED', 'SITUATIONAL', 'HR', 'PRACTICAL_ACC', 'COMPUTER', 'REVISION'].map(m => {
            const label = modMap[m] || m;
            const active = coach.activeModule === m ? 'p' : '';
            return '<button class="sm ' + active + '" data-a="set_module" data-v="' + m + '" style="margin:2px 3px">' + label + '</button>';
        }).join('');

        render(
            '<div class="coach-hero">'
            + '<div class="row sp"><div><span class="chip" style="background:rgba(255,255,255,.2);color:#fff">🎯 लक्ष्य: 20/20 Marks</span></div>'
            + '<a href="#/profile" style="color:#fff;text-decoration:none;font-size:13px;opacity:.9">👤 ' + esc(prof.name || 'उमेदवार') + ' (बदला)</a></div>'
            + '<h1 style="margin:8px 0 4px">MCED मुलाखत प्रशिक्षक</h1>'
            + '<div class="q" style="opacity:.92">District Account Assistant मौखिक मुलाखत तयारी · एकावेळी एकच प्रश्न</div>'
            + '</div>'

            + '<div class="card" style="padding:10px 14px"><div class="mu sm" style="margin-bottom:6px">विषय निवडा:</div><div class="row wrap">' + modPills + '</div></div>'

            + '<div class="card">'
            + '<div class="row sp wrap" style="margin-bottom:8px">'
            + '<span class="mod-pill">' + modInfo.icon + ' ' + esc(modInfo.name) + '</span>'
            + '<span class="rubric-badge">⚖️ ' + esc(rubricInfo.name) + ' (' + rubricInfo.marks + 'M)</span>'
            + '</div>'

            + '<div class="q-title">' + esc(curActiveQ.q_en) + '</div>'
            + '<div class="q-sub">' + esc(curActiveQ.q_mr) + '</div>'

            + '<div class="audio-bar">'
            + '<button class="voice-btn" data-a="listen_q">🔊 प्रश्न ऐका</button>'
            + '<button class="voice-btn" data-a="stop_audio" style="display:none" id="stopBtn">⏹️ थांबवा</button>'
            + '<span class="timer-chip" id="timerBadge">⏱️ 60s</span>'
            + '</div>'

            // Speech Recognition & Typing Area
            + '<div class="mic-container">'
            + '<button class="mic-btn" id="micBtn" data-a="toggle_mic" title="माईक सुरू करा">🎙️</button>'
            + '<div id="micStatus" class="mu sm" style="margin-top:8px">माईक सुरू करण्यासाठी टॅप करा किंवा खाली उत्तर टाईप करा</div>'
            + '</div>'

            + '<div class="answer-box">'
            + '<div class="row sp" style="margin-bottom:4px">'
            + '<span class="mu sm">तुमचे उत्तर (बोला किंवा टाईप करा):</span>'
            + '<select id="sttLangSelect" style="font-size:12px;padding:2px 8px;border-radius:8px;border:1px solid var(--bd);background:var(--card);color:var(--fg)">'
            + '<option value="mr-IN"' + (coach.sttLang === 'mr-IN' ? ' selected' : '') + '>मराठी (mr-IN)</option>'
            + '<option value="hi-IN"' + (coach.sttLang === 'hi-IN' ? ' selected' : '') + '>हिंदी (hi-IN)</option>'
            + '<option value="en-IN"' + (coach.sttLang === 'en-IN' ? ' selected' : '') + '>English (en-IN)</option>'
            + '</select>'
            + '</div>'
            + '<textarea class="answer-textarea" id="ansText" placeholder="येथे तुमचे उत्तर दिसेल किंवा स्वतः टाईप करा..."></textarea>'
            + '<div class="row sp"><span class="mu sm" id="charCount">0 शब्द</span>'
            + '<div><button class="sm" data-a="clear_ans">पुसा</button></div></div>'
            + '</div>'

            + '<div style="margin-top:14px">'
            + '<button class="p w" data-a="submit_ans">✓ उत्तर तपासा व मूल्यमापन पाहा</button>'
            + '</div>'

            + '<div id="evalContainer"></div>'

            + '<div class="row sp" style="margin-top:18px">'
            + '<button data-a="prev_q" class="sm">← मागील प्रश्न</button>'
            + '<button data-a="toggle_rev" class="sm ' + (isRevision ? 'wn' : '') + '">' + (isRevision ? '★ उजळणीतून काढा' : '☆ उजळणीसाठी जोडा') + '</button>'
            + '<button data-a="next_q" class="p sm">पुढचा प्रश्न →</button>'
            + '</div>'
            + '</div>'
        );

        // Bind language select
        const langSel = $('#sttLangSelect');
        if (langSel) {
            langSel.onchange = (e) => {
                coach.sttLang = e.target.value;
                window.saveCoach();
                toast('भाषा बदलली: ' + e.target.options[e.target.selectedIndex].text);
            };
        }

        // Live word counter
        const ansArea = $('#ansText');
        if (ansArea) {
            ansArea.oninput = () => {
                const words = ansArea.value.trim().split(/\s+/).filter(w => w.length > 0);
                $('#charCount').textContent = words.length + ' शब्द';
            };
        }

        // Setup STT
        sttEngine = window.initSpeechRecognition(
            (transcript, isFinal) => {
                const t = $('#ansText');
                if (t) {
                    t.value = transcript;
                    const words = transcript.trim().split(/\s+/).filter(w => w.length > 0);
                    $('#charCount').textContent = words.length + ' शब्द';
                }
            },
            (listening, err) => {
                const btn = $('#micBtn');
                const stat = $('#micStatus');
                if (!btn || !stat) return;
                if (listening) {
                    btn.classList.add('listening');
                    btn.innerHTML = '⏹️';
                    stat.innerHTML = '🔴 <b>ऐकत आहे... शांतपणे उत्तर बोला.</b> <div class="equalizer"><span></span><span></span><span></span><span></span></div>';
                    startTimer();
                } else {
                    btn.classList.remove('listening');
                    btn.innerHTML = '🎙️';
                    stat.textContent = err ? 'माईक एरर: ' + err + ' (टाईप करूनही उत्तर देऊ शकता)' : 'माईक थांबवला. उत्तर तपासण्यासाठी खालील बटण दाबा.';
                    stopTimer();
                }
            }
        );
    };

    function startTimer() {
        clearInterval(oralTimer);
        timeLeft = 60;
        const b = $('#timerBadge');
        if (b) {
            b.textContent = '⏱️ ' + timeLeft + 's';
            b.classList.remove('urgent');
        }
        oralTimer = setInterval(() => {
            timeLeft--;
            const tb = $('#timerBadge');
            if (!tb) return clearInterval(oralTimer);
            tb.textContent = '⏱️ ' + timeLeft + 's';
            if (timeLeft <= 15) tb.classList.add('urgent');
            if (timeLeft <= 0) {
                clearInterval(oralTimer);
                if (sttEngine && sttEngine.isListening()) sttEngine.stop();
                toast('⏱️ वेळ संपली! आता तुमचे उत्तर तपासा.');
            }
        }, 1000);
    }

    function stopTimer() {
        clearInterval(oralTimer);
    }

    // Coach Actions
    ACT.set_module = (m) => {
        window.COACH_STATE.activeModule = m;
        window.saveCoach();
        V.coach();
    };

    ACT.listen_q = () => {
        if (!curActiveQ) return;
        const stopBtn = $('#stopBtn');
        if (stopBtn) stopBtn.style.display = 'inline-flex';
        window.speakText(curActiveQ.q_en + '. ' + curActiveQ.q_mr, 'en-IN');
    };

    ACT.listen_model = () => {
        if (!curActiveQ) return;
        const stopBtn = $('#stopBtn');
        if (stopBtn) stopBtn.style.display = 'inline-flex';
        const modelTxt = curActiveQ.modelAnswer.replace(/\[.*?\]/g, ' ');
        window.speakText(modelTxt, 'hi-IN');
    };

    ACT.stop_audio = () => {
        window.stopSpeech();
        const stopBtn = $('#stopBtn');
        if (stopBtn) stopBtn.style.display = 'none';
    };

    ACT.toggle_mic = () => {
        if (!sttEngine) {
            toast('⚠️ माईक सपोर्ट या ब्राउझरमध्ये उपलब्ध नाही. तुम्ही खाली उत्तर टाईप करू शकता.');
            return;
        }
        if (sttEngine.isListening()) {
            sttEngine.stop();
        } else {
            sttEngine.start();
        }
    };

    ACT.clear_ans = () => {
        const t = $('#ansText');
        if (t) {
            t.value = '';
            $('#charCount').textContent = '0 शब्द';
        }
    };

    ACT.submit_ans = () => {
        const text = ($('#ansText') ? $('#ansText').value : '').trim();
        if (!text) {
            toast('⚠️ कृपया आधी काही बोला किंवा उत्तर टाईप करा!');
            return;
        }
        if (sttEngine && sttEngine.isListening()) sttEngine.stop();
        stopTimer();

        const res = window.evaluateOralAnswer(curActiveQ, text);
        const evalBox = $('#evalContainer');
        if (!evalBox) return;

        // Mark mastery if score >= 8
        if (res.score >= 8) {
            window.COACH_STATE.mastered[curActiveQ.id] = true;
            delete window.COACH_STATE.revisionList[curActiveQ.id];
            addXP(25, '(उत्तम उत्तर!)');
        } else {
            window.COACH_STATE.revisionList[curActiveQ.id] = true;
            addXP(10, '(सराव प्रयत्न)');
        }
        window.saveCoach();

        const scoreColor = res.score >= 8 ? 'var(--ok)' : res.score >= 5 ? 'var(--wn)' : 'var(--bad)';
        const scoreTitle = res.score >= 8 ? '🎉 उत्तम उत्तर! (' + res.score + '/10)' : res.score >= 5 ? '👍 चांगला प्रयत्न! (' + res.score + '/10)' : '⚠️ आणखी सुधारणा हवी (' + res.score + '/10)';

        evalBox.innerHTML =
            '<div class="eval-card card" style="border:2px solid ' + scoreColor + ';margin-top:16px">'
            + '<div class="row sp">'
            + '<h2 style="margin:0;color:' + scoreColor + '">' + scoreTitle + '</h2>'
            + '<span class="chip" style="font-size:13px">' + res.wordCount + ' शब्द</span>'
            + '</div>'

            // Strengths
            + '<div class="eval-strength">'
            + '<b style="color:var(--ok)">🟢 काय चांगलं सांगितले (Strengths):</b>'
            + '<ul class="l">' + res.strengths.map(s => '<li>' + esc(s) + '</li>').join('') + '</ul>'
            + '</div>'

            // Improvements
            + '<div class="eval-improve">'
            + '<b style="color:#c05621">🟡 काय सुटले किंवा सुधारणेची गरज (Areas to Improve):</b>'
            + '<ul class="l">' + res.improvements.map(s => '<li>' + esc(s) + '</li>').join('') + '</ul>'
            + '</div>'

            // Model Answer
            + '<div class="model-answer-box">'
            + '<div class="row sp">'
            + '<b>💡 साध्या भाषेत आदर्श उत्तर (Model Answer):</b>'
            + '<button class="voice-btn" data-a="listen_model" style="padding:4px 10px;font-size:12px">🔊 ऐका</button>'
            + '</div>'
            + '<p style="margin:8px 0;line-height:1.6">' + esc(res.modelAnswer).replace(/\n/g, '<br>') + '</p>'
            + '</div>'

            // Follow Up Question
            + (res.followUp ? (
                '<div class="followup-box">'
                + '<b>❓ पॅनेलचा संभाव्य फॉलो-अप प्रश्न (Follow-Up):</b>'
                + '<p style="margin:4px 0 6px;font-weight:600">' + esc(res.followUp) + '</p>'
                + '<div class="sm mu"><b>त्याचे आदर्श उत्तर:</b> ' + esc(res.followUpAnswer) + '</div>'
                + '</div>'
            ) : '')

            + '<div class="row wrap g" style="margin-top:14px">'
            + '<button class="p" data-a="retry_own">🔁 स्वतःच्या शब्दांत पुन्हा प्रयत्न करा</button>'
            + '<button data-a="next_q">पुढचा प्रश्न →</button>'
            + '</div>'
            + '</div>';

        // Scroll to evaluation
        evalBox.scrollIntoView({ behavior: 'smooth' });
    };

    ACT.retry_own = () => {
        const t = $('#ansText');
        if (t) {
            t.value = '';
            t.focus();
        }
        const evalBox = $('#evalContainer');
        if (evalBox) evalBox.innerHTML = '';
        toast('पुन्हा बोला किंवा टाईप करा! यावेळी सर्व आवश्यक मुद्दे सांगा.');
    };

    ACT.prev_q = () => {
        const qList = getQuestions(window.COACH_STATE.activeModule);
        const idx = qList.findIndex(q => q.id === curActiveQ.id);
        const prevIdx = (idx - 1 + qList.length) % qList.length;
        V.coach(qList[prevIdx].id);
    };

    ACT.next_q = () => {
        const qList = getQuestions(window.COACH_STATE.activeModule);
        const idx = qList.findIndex(q => q.id === curActiveQ.id);
        const nextIdx = (idx + 1) % qList.length;
        V.coach(qList[nextIdx].id);
    };

    ACT.toggle_rev = () => {
        if (!curActiveQ) return;
        const rev = window.COACH_STATE.revisionList;
        if (rev[curActiveQ.id]) {
            delete rev[curActiveQ.id];
            toast('उजळणी यादीतून काढले');
        } else {
            rev[curActiveQ.id] = true;
            toast('उजळणी यादीत जोडले ⭐');
        }
        window.saveCoach();
        V.coach(curActiveQ.id);
    };

    // =========================================================================
    // STEP 1 CANDIDATE PROFILING DIALOG ("Understand The Candidate")
    // =========================================================================
    const PROFILE_QUESTIONS = [
        { key: 'name', title: 'पूर्ण नाव आणि गाव/शहर', desc: 'तुमचे पूर्ण नाव आणि मूळ गाव किंवा जिल्हा कोणता आहे?', ph: 'उदा. ऐश्वर्या सुरेश पाटील, नाशिक' },
        { key: 'qualification', title: 'शिक्षण आणि उत्तीर्ण वर्ष', desc: 'तुमची पदवी (B.Com / M.Com), कॉलेजचे नाव आणि उत्तीर्ण वर्ष काय आहे?', ph: 'उदा. B.Com, KTHM College Nashik, 2025' },
        { key: 'subjects', title: 'मुख्य विषय', desc: 'कॉमर्समध्ये तुमचे मुख्य विषय कोणते होते?', ph: 'उदा. Accountancy, Auditing, Costing, Taxation' },
        { key: 'software', title: 'कॉम्प्युटर व सॉफ्टवेअर ज्ञान', desc: 'MS Excel, Tally किंवा इतर सॉफ्टवेअरचे तुमचे ज्ञान कसे आहे?', ph: 'उदा. MS Excel (VLOOKUP, SUMIF, Billing), Tally ERP 9, Word' },
        { key: 'experience', title: 'कामाचा किंवा प्रॅक्टिकल अनुभव', desc: 'काही आधीचा कामाचा अनुभव, इंटर्नशिप किंवा प्रॅक्टिकल एक्सपोजर आहे का?', ph: 'उदा. Fresh graduate / CA फर्ममध्ये 6 महिने इंटर्नशिप' },
        { key: 'languages', title: 'बोलण्याच्या सोयीच्या भाषा', desc: 'मुलाखतीत तुम्ही कोणत्या भाषांमध्ये सहज बोलू शकता?', ph: 'उदा. मराठी (चांगली), हिंदी (चांगली), इंग्रजी (बेसिक/व्यावसायिक)' },
        { key: 'mcedUnderstanding', title: 'MCED बद्दल तुमची माहिती', desc: 'MCED संस्था आणि तिच्या कार्याबद्दल तुम्हाला काय माहिती आहे?', ph: 'उदा. उद्योजकता विकास संस्था, EDPs, जिल्हा केंद्रे' },
        { key: 'interviewDate', title: 'मुलाखतीची अंदाजित तारीख', desc: 'तुमची तोंडी मुलाखत कधी अपेक्षित आहे?', ph: 'उदा. 15 नोव्हेंबर 2026' }
    ];

    V.candidateProfileStep = function (stepNum) {
        stepNum = stepNum || 1;
        const totalSteps = PROFILE_QUESTIONS.length;
        const q = PROFILE_QUESTIONS[stepNum - 1];
        const prof = window.CANDIDATE_PROFILE;

        render(
            '<div class="coach-hero">'
            + '<h1>पहिला टप्पा: तुमची माहिती</h1>'
            + '<div class="q">प्रश्नांची उत्तरे तुमच्या पार्श्वभूमीनुसार वैयक्तिकृत (Personalize) करण्यासाठी ही माहिती आवश्यक आहे.</div>'
            + '</div>'

            + '<div class="card">'
            + '<div class="row sp" style="margin-bottom:12px">'
            + '<span class="chip">प्रश्न ' + stepNum + ' / ' + totalSteps + '</span>'
            + '<span class="mu sm">' + Math.round((stepNum / totalSteps) * 100) + '% पूर्ण</span>'
            + '</div>'
            + '<div class="bar" style="margin-bottom:16px"><i style="width:' + ((stepNum / totalSteps) * 100) + '%"></i></div>'

            + '<h2 style="margin:4px 0 6px">' + esc(q.title) + '</h2>'
            + '<p class="mu" style="margin-bottom:14px">' + esc(q.desc) + '</p>'

            + '<input type="text" id="profInput" value="' + esc(prof[q.key] || '') + '" placeholder="' + esc(q.ph) + '" style="font-size:16px;padding:12px;margin-bottom:16px">'

            + '<div class="row sp">'
            + (stepNum > 1 ? '<button data-a="prof_prev" data-v="' + stepNum + '">← मागे</button>' : '<div></div>')
            + (stepNum < totalSteps
                ? '<button class="p" data-a="prof_next" data-v="' + stepNum + '">पुढे जा →</button>'
                : '<button class="ok p" data-a="prof_finish">✓ पूर्ण झाले, मुलाखत सुरू करा 🚀</button>')
            + '</div>'
            + '</div>'
        );
        setTimeout(() => { const el = $('#profInput'); if (el) el.focus() }, 100);
    };

    ACT.prof_next = (step) => {
        step = parseInt(step);
        const val = ($('#profInput') ? $('#profInput').value : '').trim();
        const q = PROFILE_QUESTIONS[step - 1];
        if (val) window.CANDIDATE_PROFILE[q.key] = val;
        window.saveCoach();
        V.candidateProfileStep(step + 1);
    };

    ACT.prof_prev = (step) => {
        step = parseInt(step);
        V.candidateProfileStep(step - 1);
    };

    ACT.prof_finish = () => {
        const val = ($('#profInput') ? $('#profInput').value : '').trim();
        const q = PROFILE_QUESTIONS[PROFILE_QUESTIONS.length - 1];
        if (val) window.CANDIDATE_PROFILE[q.key] = val;
        window.CANDIDATE_PROFILE.completed = true;
        window.saveCoach();
        toast('🎉 प्रोफाइल सेव्ह झाली! आता एकावेळी एका प्रश्नाचा सराव करूया.');
        V.coach();
    };

    // =========================================================================
    // VIEW 2: OFFICIAL 20-MARK MOCK INTERVIEW PANEL SIMULATOR
    // =========================================================================
    V.mock = function () {
        if ('speechSynthesis' in window) speechSynthesis.cancel();

        // If mock session is active, draw the current mock question
        if (mockSession && mockSession.active) {
            return drawMockQuestion();
        }

        const coach = window.COACH_STATE;
        const attempts = coach.mockAttempts || [];
        const bestScore = attempts.length ? Math.max(...attempts.map(a => a.totalScore)) : 0;

        render(
            '<div class="coach-hero">'
            + '<div class="row sp"><div><span class="chip" style="background:rgba(255,255,255,.2);color:#fff">ऑफिशियल पॅनेल सिम्युलेटर</span></div>'
            + '<b>लक्ष्य: 20/20</b></div>'
            + '<h1>MCED तोंडी मुलाखत: २० गुण</h1>'
            + '<div class="q">प्रत्यक्ष MCED निवड समितीसमोर बसल्याचा अनुभव · अचूक २० गुणांचे मूल्यमापन</div>'
            + '</div>'

            + '<div class="card">'
            + '<h2>📋 अधिकृत गुणदान आराखडा (Practice Rubric)</h2>'
            + '<div class="rubric-row"><span>1. MCED Organisation & Job Role (30%)</span><b>6 Marks</b></div>'
            + '<div class="rubric-row"><span>2. Real-Life Workplace Simulations (30%)</span><b>6 Marks</b></div>'
            + '<div class="rubric-row"><span>3. Personality, HR & Behaviour (20%)</span><b>4 Marks</b></div>'
            + '<div class="rubric-row"><span>4. Practical Accounting & Controls (15%)</span><b>3 Marks</b></div>'
            + '<div class="rubric-row"><span>5. Computer & Office Knowledge (5%)</span><b>1 Mark</b></div>'
            + '<div class="rubric-row" style="font-weight:800;font-size:16px;border-top:2px solid var(--bd);margin-top:6px;padding-top:10px"><span>एकूण गुण (Total)</span><span style="color:var(--pr)">20 Marks</span></div>'
            + '</div>'

            + '<div class="card">'
            + '<h2>🎯 पॅनेलचे नियम</h2>'
            + '<ul class="l">'
            + '<li>पॅनेल तुम्हाला एकावेळी एकच प्रश्न विचारेल (एकूण 10 प्रश्न).</li>'
            + '<li>प्रत्येक प्रश्नाचे उत्तर शांतपणे, आत्मविश्वासाने आणि पुरेसे सविस्तर द्या.</li>'
            + '<li>मुलाखत चालू असताना मध्येच गुण सांगितले जाणार नाहीत; संपूर्ण मुलाखत संपल्यावर विस्तृत रिपोर्ट कार्ड मिळेल.</li>'
            + '</ul>'
            + '<button class="p w" data-a="start_mock_session" style="font-size:17px;margin-top:12px">🚀 २० गुणांची प्रत्यक्ष मॉक मुलाखत सुरू करा</button>'
            + '</div>'

            + (attempts.length ? (
                '<div class="card">'
                + '<h2>📊 आधीच्या मॉक मुलाखतींचे रेकॉर्ड</h2>'
                + '<div class="mu sm" style="margin-bottom:8px">सर्वोत्तम गुण: <b>' + bestScore + '/20</b> · एकूण Attempts: ' + attempts.length + '</div>'
                + attempts.slice(-5).reverse().map((a, i) => (
                    '<div class="pill sm" style="padding:8px 0;border-bottom:1px dashed var(--bd)">'
                    + '<span>' + new Date(a.timestamp).toLocaleDateString('mr-IN') + ' · Mock #' + (attempts.length - i) + '</span>'
                    + '<b style="color:' + (a.totalScore >= 16 ? 'var(--ok)' : a.totalScore >= 12 ? 'var(--wn)' : 'var(--bad)') + '">' + a.totalScore + ' / 20 Marks</b>'
                    + '</div>'
                )).join('')
                + '</div>'
            ) : '')
        );
    };

    ACT.start_mock_session = () => {
        // Select balanced 10 questions strictly following new priorities:
        // 30% MCED (3 Qs), 30% Situational (3 Qs), 20% HR (2 Qs), 15% Practical Acc (1 Q), 5% Computer (1 Q) = 10 Questions
        const mcedQs = DATA.questions.filter(q => q.rubric === 'mced_org').sort(() => Math.random() - .5).slice(0, 3);
        const sitQs = DATA.questions.filter(q => q.rubric === 'situational').sort(() => Math.random() - .5).slice(0, 3);
        const hrQs = DATA.questions.filter(q => q.rubric === 'personality').sort(() => Math.random() - .5).slice(0, 2);
        const pracQs = DATA.questions.filter(q => q.rubric === 'practical_acc').sort(() => Math.random() - .5).slice(0, 1);
        const compQs = DATA.questions.filter(q => q.rubric === 'computer_office').sort(() => Math.random() - .5).slice(0, 1);

        const fullList = [...mcedQs, ...sitQs, ...hrQs, ...pracQs, ...compQs].sort(() => Math.random() - .5);

        mockSession = {
            active: true,
            questions: fullList,
            currentIdx: 0,
            answers: [],
            startTime: Date.now()
        };

        toast('पॅनेल सदस्य उपस्थित आहेत. प्रश्न क्रमांक १ समोर येत आहे.');
        drawMockQuestion();
    };

    function drawMockQuestion() {
        const s = mockSession;
        const q = s.questions[s.currentIdx];
        const panelMember = s.currentIdx % 3 === 0 ? 'पॅनेल अध्यक्ष (Chairman)' : s.currentIdx % 3 === 1 ? 'विषय तज्ज्ञ (Accounts Officer)' : 'जिल्हा प्रकल्प अधिकारी (MCED)';

        render(
            '<div class="top">'
            + '<b>MCED मुलाखत पॅनेल</b>'
            + '<span class="chip">प्रश्न ' + (s.currentIdx + 1) + ' / ' + s.questions.length + '</span>'
            + '<button class="sm" data-a="abort_mock" style="color:var(--bad)">रद्द करा</button>'
            + '</div>'
            + '<div class="bar" style="margin:4px 0 12px"><i style="width:' + (((s.currentIdx + 1) / s.questions.length) * 100) + '%"></i></div>'

            + '<div class="card">'
            + '<div class="mu sm" style="margin-bottom:4px">विचारणारे: <b>' + panelMember + '</b></div>'
            + '<div class="q-title" style="margin-top:2px">' + esc(q.q_en) + '</div>'
            + '<div class="q-sub">' + esc(q.q_mr) + '</div>'

            + '<div class="audio-bar">'
            + '<button class="voice-btn" data-a="listen_mock_q">🔊 पॅनेलचा आवाज ऐका</button>'
            + '<span class="timer-chip" id="mockTimer">⏱️ 60s</span>'
            + '</div>'

            + '<div class="mic-container">'
            + '<button class="mic-btn" id="mockMicBtn" data-a="toggle_mock_mic">🎙️</button>'
            + '<div id="mockMicStatus" class="mu sm" style="margin-top:6px">माईकवर टॅप करून उत्तर बोला किंवा खाली टाईप करा</div>'
            + '</div>'

            + '<textarea class="answer-textarea" id="mockAns" placeholder="येथे तुमचे उत्तर दिसेल..."></textarea>'
            + '<div class="row sp" style="margin-top:4px"><span class="mu sm" id="mockWordCount">0 शब्द</span>'
            + '<button class="sm" data-a="clear_mock_ans">पुसा</button></div>'

            + '<div style="margin-top:16px">'
            + '<button class="p w" data-a="submit_mock_answer" style="font-size:16px">'
            + (s.currentIdx < s.questions.length - 1 ? 'पुढील प्रश्नाकडे जा →' : '✓ मुलाखत पूर्ण करा व 20-Mark Scorecard पाहा 🏆')
            + '</button>'
            + '</div>'
            + '</div>'
        );

        // Word count listener
        const ta = $('#mockAns');
        if (ta) {
            ta.oninput = () => {
                const words = ta.value.trim().split(/\s+/).filter(w => w.length > 0);
                $('#mockWordCount').textContent = words.length + ' शब्द';
            };
        }

        // Auto speak panel question
        setTimeout(() => {
            window.speakText(q.q_en + '. ' + q.q_mr, 'en-IN');
        }, 300);

        // Setup STT
        sttEngine = window.initSpeechRecognition(
            (transcript) => {
                const t = $('#mockAns');
                if (t) {
                    t.value = transcript;
                    const words = transcript.trim().split(/\s+/).filter(w => w.length > 0);
                    $('#mockWordCount').textContent = words.length + ' शब्द';
                }
            },
            (listening) => {
                const btn = $('#mockMicBtn');
                const stat = $('#mockMicStatus');
                if (!btn || !stat) return;
                if (listening) {
                    btn.classList.add('listening');
                    stat.innerHTML = '🔴 <b>ऐकत आहे... शांतपणे उत्तर बोला.</b>';
                } else {
                    btn.classList.remove('listening');
                    stat.textContent = 'माईक थांबवला.';
                }
            }
        );
    }

    ACT.listen_mock_q = () => {
        if (!mockSession) return;
        const q = mockSession.questions[mockSession.currentIdx];
        window.speakText(q.q_en + '. ' + q.q_mr, 'en-IN');
    };

    ACT.toggle_mock_mic = () => {
        if (!sttEngine) return toast('⚠️ माईक उपलब्ध नाही. खाली टाईप करा.');
        if (sttEngine.isListening()) sttEngine.stop();
        else sttEngine.start();
    };

    ACT.clear_mock_ans = () => {
        const t = $('#mockAns');
        if (t) {
            t.value = '';
            $('#mockWordCount').textContent = '0 शब्द';
        }
    };

    ACT.abort_mock = () => {
        if (confirm('मॉक मुलाखत मध्येच रद्द करायची आहे का?')) {
            mockSession = null;
            if (sttEngine && sttEngine.isListening()) sttEngine.stop();
            V.mock();
        }
    };

    ACT.submit_mock_answer = () => {
        if (!mockSession) return;
        const s = mockSession;
        const q = s.questions[s.currentIdx];
        const text = ($('#mockAns') ? $('#mockAns').value : '').trim();

        if (sttEngine && sttEngine.isListening()) sttEngine.stop();

        const evalRes = window.evaluateOralAnswer(q, text);
        s.answers.push({ q, answer: text, evalResult: evalRes });

        if (s.currentIdx < s.questions.length - 1) {
            s.currentIdx++;
            drawMockQuestion();
        } else {
            // Mock finished! Generate Official 20-Mark Diagnostic Report
            const report = window.generateMockReport(s.answers);
            window.COACH_STATE.mockAttempts.push(report);
            window.saveCoach();
            burst(['🏆', '⭐', '🎊', '✨']);
            mockSession = null;
            drawMockScorecard(report, s.answers);
        }
    };

    function drawMockScorecard(rep, answers) {
        const cat = rep.categoryBreakdown;
        const prof = window.CANDIDATE_PROFILE;
        const tutor = window.S ? window.S.tutor : { phone: '' };

        // Generate WhatsApp report text
        const waMsg = encodeURIComponent(
            '*MCED District Account Assistant — Oral Interview Scorecard*\n'
            + 'उमेदवार: ' + (prof.name || 'ऐश्वर्या') + '\n'
            + 'अंतिम गुण: ' + rep.totalScore + ' / 20 Marks\n\n'
            + 'गुणदान विश्लेषण:\n'
            + '• Accounting Knowledge: ' + cat.accounting + '/6\n'
            + '• Practical Skills: ' + cat.practical + '/5\n'
            + '• MCED & Govt Awareness: ' + cat.mced + '/3\n'
            + '• Communication & Clarity: ' + cat.communication + '/3\n'
            + '• Confidence & Behaviour: ' + cat.confidence + '/3\n\n'
            + 'सुधारणेचे महत्त्वाचे मुद्दे:\n'
            + rep.top5.slice(0, 3).map((m, i) => (i + 1) + '. ' + m).join('\n')
        );

        render(
            '<div class="coach-hero" style="text-align:center">'
            + '<div class="chip" style="background:rgba(255,255,255,.25);color:#fff">अधिकृत मॉक निकाल</div>'
            + '<h1 style="margin:8px 0 2px">MCED मुलाखत निकाल पत्रक</h1>'
            + '<div style="margin:14px 0">'
            + '<div class="score-badge">' + rep.totalScore + ' / 20 Marks</div>'
            + '</div>'
            + '<div class="q">' + (rep.totalScore >= 16 ? 'उत्कृष्ट तयारी! प्रत्यक्ष पॅनेलसमोर असेच उत्तर द्या.' : rep.totalScore >= 12 ? 'चांगली प्रगती! कमकुवत विषयांवर भर द्या.' : 'अधिक सराव आवश्यक. खालील सुधारणा वाचा.') + '</div>'
            + '</div>'

            // Rubric breakdown
            + '<div class="card">'
            + '<h2>📊 वर्गवारीनुसार गुण (Rubric Breakdown)</h2>'
            + '<div class="rubric-row"><span>1. MCED & Job Role Awareness (30%)</span><b>' + (cat.mced_org || 0) + ' / 6</b></div>'
            + bar(pct(cat.mced_org || 0, 6), (cat.mced_org || 0) >= 4.5 ? 'ok' : 'wn')
            + '<div class="rubric-row" style="margin-top:10px"><span>2. Real-Life Workplace Simulations (30%)</span><b>' + (cat.situational || 0) + ' / 6</b></div>'
            + bar(pct(cat.situational || 0, 6), (cat.situational || 0) >= 4.5 ? 'ok' : 'wn')
            + '<div class="rubric-row" style="margin-top:10px"><span>3. Personality, HR & Behaviour (20%)</span><b>' + (cat.personality || 0) + ' / 4</b></div>'
            + bar(pct(cat.personality || 0, 4), (cat.personality || 0) >= 3 ? 'ok' : 'wn')
            + '<div class="rubric-row" style="margin-top:10px"><span>4. Practical Accounting & Controls (15%)</span><b>' + (cat.practical_acc || 0) + ' / 3</b></div>'
            + bar(pct(cat.practical_acc || 0, 3), (cat.practical_acc || 0) >= 2 ? 'ok' : 'wn')
            + '<div class="rubric-row" style="margin-top:10px"><span>5. Computer & Office Knowledge (5%)</span><b>' + (cat.computer_office || 0) + ' / 1</b></div>'
            + bar(pct(cat.computer_office || 0, 1), (cat.computer_office || 0) >= 0.8 ? 'ok' : 'wn')
            + '</div>'

            // Top 5 Areas for Improvement
            + '<div class="card">'
            + '<h2>🎯 सुधारणेचे ५ मुख्य मुद्दे (Top 5 Areas for Improvement)</h2>'
            + '<ul class="l">' + rep.top5.map(t => '<li>' + esc(t) + '</li>').join('') + '</ul>'
            + '</div>'

            // Strongest vs Weakest
            + '<div class="card">'
            + '<h2>📝 प्रश्नांचे विश्लेषण</h2>'
            + (rep.strongest.length ? '<div style="margin-bottom:10px"><b style="color:var(--ok)">✓ उत्तम दिलेली उत्तरे:</b><ul class="l">' + rep.strongest.map(s => '<li>' + esc(s.q) + '</li>').join('') + '</ul></div>' : '')
            + (rep.weakest.length ? '<div><b style="color:var(--bad)">⚠️ ज्या प्रश्नांवर पुन्हा तयारी हवी:</b><ul class="l">' + rep.weakest.map(w => '<li>' + esc(w.q) + '</li>').join('') + '</ul></div>' : '')
            + '</div>'

            // Action Buttons
            + '<div class="card">'
            + '<div class="row wrap g">'
            + '<a class="btn p w" target="_blank" href="https://wa.me/' + (tutor.phone ? ('91' + tutor.phone.replace(/\D/g, '')) : '') + '?text=' + waMsg + '">📤 Tutor (Nilesh) ला WhatsApp वर निकाल पाठवा</a>'
            + '<button class="w" data-a="start_mock_session">🔁 पुन्हा 20-Mark मॉक मुलाखत द्या</button>'
            + '<a class="btn w" href="#/coach">🎙️ एकावेळी एका प्रश्नाचा सराव सुरू ठेवा</a>'
            + '</div>'
            + '</div>'
        );
    }

    // =========================================================================
    // VIEW 3: 14-DAY ADAPTIVE PREPARATION PLAN
    // =========================================================================
    V.plan = function () {
        const plan = DATA.plan14;
        const coach = window.COACH_STATE;
        const doneMap = coach.planDone || {};

        render(
            '<div class="coach-hero">'
            + '<h1>📅 14 दिवसांचा मुलाखत प्लॅन</h1>'
            + '<div class="q">तोंडी परीक्षेची पद्धतशीर आणि टप्प्याटप्प्याने तयारी · रोज ९० ते १२० मिनिटे</div>'
            + '</div>'

            + '<div class="card" style="padding:10px 14px">'
            + '<div class="row sp"><span class="mu sm">प्लॅन प्रगती: ' + Object.keys(doneMap).length + ' / 14 दिवस पूर्ण</span>'
            + '<b>' + Math.round((Object.keys(doneMap).length / 14) * 100) + '%</b></div>'
            + '<div class="bar" style="margin-top:6px">' + bar(pct(Object.keys(doneMap).length, 14), 'ok') + '</div>'
            + '</div>'

            + plan.map(d => {
                const isDone = !!doneMap[d.day];
                return (
                    '<div class="card day ' + (isDone ? 'done' : '') + '">'
                    + '<div class="row sp">'
                    + '<div>'
                    + '<span class="chip ' + (isDone ? 'ok' : '') + '">' + (isDone ? '✓ पूर्ण' : 'दिवस ' + d.day) + '</span>'
                    + '<div class="b" style="margin-top:6px;font-size:16px">' + esc(d.title) + '</div>'
                    + '<div class="mu sm">' + esc(d.desc) + '</div>'
                    + '</div>'
                    + '<button class="ck" data-a="toggle_day_done" data-v="' + d.day + '">' + (isDone ? '✓' : '') + '</button>'
                    + '</div>'
                    + '<div class="sm mu" style="margin-top:8px;background:color-mix(in srgb,var(--pr) 6%,var(--card));padding:8px 10px;border-radius:10px">💡 <b>टीप:</b> ' + esc(d.tips) + '</div>'
                    + '<div style="margin-top:10px">'
                    + (d.module === 'MOCK' || d.module === 'FINAL'
                        ? '<a class="btn p sm" href="#/mock">🏆 20-Mark मॉक मुलाखत द्या →</a>'
                        : '<button class="p sm" data-a="start_day_practice" data-v="' + d.module + '">🎙️ या दिवसाचा सराव सुरू करा →</button>')
                    + '</div>'
                    + '</div>'
                );
            }).join('')
        );
    };

    ACT.toggle_day_done = (day) => {
        const coach = window.COACH_STATE;
        coach.planDone = coach.planDone || {};
        if (coach.planDone[day]) {
            delete coach.planDone[day];
        } else {
            coach.planDone[day] = Date.now();
            burst();
            toast('दिवस ' + day + ' पूर्ण म्हणून नोंदवला ✓');
        }
        window.saveCoach();
        V.plan();
    };

    ACT.start_day_practice = (mod) => {
        window.COACH_STATE.activeModule = mod;
        window.saveCoach();
        location.hash = '#/coach';
    };

    // =========================================================================
    // VIEW 4: SYLLABUS & QUESTION BANK
    // =========================================================================
    V.syllabus = function (activeMod) {
        activeMod = activeMod || 'ALL';
        const qList = getQuestions(activeMod);

        const sylMap = {
            ALL: 'सर्व (All)',
            MCED: '🏛️ MCED व पद (30%)',
            SITUATIONAL: '🏢 कार्यालयीन प्रसंग (30%)',
            HR: '👤 HR व व्यक्तिमत्व (20%)',
            PRACTICAL_ACC: '📊 प्रॅक्टिकल अकाउंट्स (15%)',
            COMPUTER: '💻 कॉम्प्युटर/एक्सेल (5%)'
        };
        const modButtons = ['ALL', 'MCED', 'SITUATIONAL', 'HR', 'PRACTICAL_ACC', 'COMPUTER'].map(m => {
            const act = activeMod === m ? 'p' : '';
            const lbl = sylMap[m] || m;
            return '<button class="sm ' + act + '" data-a="filter_syl" data-v="' + m + '" style="margin:2px 3px">' + lbl + '</button>';
        }).join('');

        render(
            '<div class="coach-hero">'
            + '<h1>📚 मुलाखत प्रश्नसंग्रह (Syllabus)</h1>'
            + '<div class="q">एकूण ' + DATA.questions.length + ' प्रत्यक्ष विचारले जाणारे प्रश्न · साध्या भाषेतील आदर्श उत्तरे</div>'
            + '</div>'

            + '<div class="card"><div class="mu sm" style="margin-bottom:6px">Module निवडा:</div><div class="row wrap">' + modButtons + '</div></div>'

            + qList.map((q, i) => (
                '<details class="card" style="margin:10px 0">'
                + '<summary style="font-size:15px;line-height:1.4">'
                + '<span class="chip" style="margin-right:6px">' + q.id + '</span> '
                + '<b>' + esc(q.q_en) + '</b><br>'
                + '<span class="mu sm" style="margin-left:28px">' + esc(q.q_mr) + '</span>'
                + '</summary>'

                + '<div style="margin-top:12px;border-top:1px dashed var(--bd);padding-top:10px">'
                + '<div class="row sp" style="margin-bottom:8px">'
                + '<span class="rubric-badge">' + esc(DATA.rubric[q.rubric].name) + '</span>'
                + '<a class="btn sm" href="#/coach/' + q.id + '">🎙️ हा प्रश्न बोला</a>'
                + '</div>'

                + '<div class="model-answer-box">'
                + '<b>💡 साध्या भाषेत आदर्श उत्तर:</b>'
                + '<p style="margin:6px 0;line-height:1.6">' + esc(q.modelAnswer).replace(/\n/g, '<br>') + '</p>'
                + '</div>'

                + '<div style="margin:8px 0">'
                + '<b class="sm">🔑 मुख्य मुद्दे (Key Concepts):</b>'
                + '<ul class="l">' + (q.keyPoints || []).map(k => '<li>' + esc(k) + '</li>').join('') + '</ul>'
                + '</div>'

                + (q.commonMistakes && q.commonMistakes.length ? (
                    '<div class="eval-improve" style="padding:8px 12px;margin:8px 0">'
                    + '<b class="sm" style="color:var(--bad)">⚠️ टाळायच्या चुका:</b>'
                    + '<ul class="l">' + q.commonMistakes.map(m => '<li>' + esc(m) + '</li>').join('') + '</ul>'
                    + '</div>'
                ) : '')

                + (q.followUp ? (
                    '<div class="followup-box" style="padding:8px 12px;margin:8px 0">'
                    + '<b class="sm">❓ संभाव्य फॉलो-अप:</b> ' + esc(q.followUp) + '<br>'
                    + '<span class="sm mu"><b>उत्तर:</b> ' + esc(q.followUpAnswer) + '</span>'
                    + '</div>'
                ) : '')
                + '</div>'
                + '</details>'
            )).join('')
        );
    };

    ACT.filter_syl = (m) => {
        V.syllabus(m);
    };

    // =========================================================================
    // VIEW 5: CANDIDATE PROFILE & TRACKER (अधिक / प्रोफाइल)
    // =========================================================================
    V.profile = function () {
        const prof = window.CANDIDATE_PROFILE;
        const coach = window.COACH_STATE;
        const tutor = window.S ? window.S.tutor : { name: 'Nilesh', phone: '' };

        const masteredCount = Object.keys(coach.mastered || {}).length;
        const revisionCount = Object.keys(coach.revisionList || {}).length;
        const mockCount = (coach.mockAttempts || []).length;
        const bestMock = mockCount ? Math.max(...coach.mockAttempts.map(a => a.totalScore)) : 0;

        render(
            '<div class="coach-hero">'
            + '<h1>👤 उमेदवार प्रोफाइल व प्रगती</h1>'
            + '<div class="q">तुमची माहिती आणि तोंडी मुलाखत तयारीचा संपूर्ण ताळेबंद</div>'
            + '</div>'

            + '<div class="grid3">'
            + '<div class="card c"><div class="big" style="color:var(--ok)">' + masteredCount + '</div><div class="mu">पक्के प्रश्न</div></div>'
            + '<div class="card c"><div class="big" style="color:var(--wn)">' + revisionCount + '</div><div class="mu">उजळणी बाकी</div></div>'
            + '<div class="card c"><div class="big" style="color:var(--pr)">' + bestMock + '/20</div><div class="mu">सर्वोत्तम मॉक</div></div>'
            + '</div>'

            + '<div class="card">'
            + '<div class="row sp">'
            + '<h2>📝 उमेदवाराची माहिती</h2>'
            + '<button class="sm" data-a="edit_profile_dialog">बदला ✏️</button>'
            + '</div>'
            + '<table style="margin-top:6px">'
            + '<tr><td style="width:38%"><b>नाव</b></td><td>' + esc(prof.name) + '</td></tr>'
            + '<tr><td><b>मूळ गाव/जिल्हा</b></td><td>' + esc(prof.hometown) + '</td></tr>'
            + '<tr><td><b>शिक्षण व वर्ष</b></td><td>' + esc(prof.qualification) + ' (' + esc(prof.gradYear) + ')</td></tr>'
            + '<tr><td><b>कॉलेज</b></td><td>' + esc(prof.college || '—') + '</td></tr>'
            + '<tr><td><b>मुख्य विषय</b></td><td>' + esc(prof.subjects) + '</td></tr>'
            + '<tr><td><b>सॉफ्टवेअर</b></td><td>' + esc(prof.software) + '</td></tr>'
            + '<tr><td><b>अनुभव</b></td><td>' + esc(prof.experience) + '</td></tr>'
            + '<tr><td><b>भाषा</b></td><td>' + esc(prof.languages) + '</td></tr>'
            + '<tr><td><b>मुलाखतीची तारीख</b></td><td>' + esc(prof.interviewDate) + '</td></tr>'
            + '</table>'
            + '</div>'

            + '<div class="card">'
            + '<h2>📲 Tutor (Nilesh) WhatsApp रिपोर्ट</h2>'
            + '<div class="mu sm">Tutor चा नंबर: <b>' + (tutor.phone || 'नंबर सेट नाही') + '</b></div>'
            + '<input type="text" id="tutorPhoneInput" value="' + esc(tutor.phone || '') + '" placeholder="10 अंकी मोबाइल नंबर" style="margin:8px 0">'
            + '<div class="row g"><button data-a="save_tutor_phone">नंबर सेव्ह करा</button>'
            + '<button class="p" data-a="share_oral_report">📤 प्रगती रिपोर्ट पाठवा</button></div>'
            + '</div>'

            + '<div class="card">'
            + '<h2>📚 लेखी परीक्षेचे आधीचे अभ्यास साहित्य</h2>'
            + '<p class="mu sm">तुम्ही आधी सोडवलेले पेपर्स, Flashcards आणि Cheat Sheet पाहू शकता:</p>'
            + '<div class="row wrap g">'
            + '<a class="btn sm" href="#/cheat">📄 Cheat Sheet</a>'
            + '<a class="btn sm" href="#/cards/all">🃏 Flashcards</a>'
            + '<a class="btn sm" href="#/papers">✍️ जुने लेखी पेपर्स (Archive)</a>'
            + '</div>'
            + '</div>'

            + '<div class="card">'
            + '<button data-a="reset_oral_data" style="color:var(--bad)">⚠️ मुलाखतीचा सर्व सराव डेटा पुसा (Reset)</button>'
            + '</div>'
        );
    };

    ACT.edit_profile_dialog = () => {
        V.candidateProfileStep(1);
    };

    ACT.save_tutor_phone = () => {
        const p = ($('#tutorPhoneInput') ? $('#tutorPhoneInput').value : '').replace(/\D/g, '');
        if (window.S) {
            window.S.tutor.phone = p;
            window.save();
        }
        toast('Tutor चा नंबर सेव्ह झाला ✓');
    };

    ACT.share_oral_report = () => {
        const prof = window.CANDIDATE_PROFILE;
        const coach = window.COACH_STATE;
        const tutor = window.S ? window.S.tutor : { phone: '' };
        const mockCount = (coach.mockAttempts || []).length;
        const bestMock = mockCount ? Math.max(...coach.mockAttempts.map(a => a.totalScore)) : 0;

        const msg = encodeURIComponent(
            '*MCED Oral Interview Daily Report*\n'
            + 'उमेदवार: ' + (prof.name || 'ऐश्वर्या') + '\n'
            + 'पक्के प्रश्न (Mastered): ' + Object.keys(coach.mastered || {}).length + '\n'
            + 'उजळणी बाकी: ' + Object.keys(coach.revisionList || {}).length + '\n'
            + '14-Day प्लॅन दिवस पूर्ण: ' + Object.keys(coach.planDone || {}).length + '/14\n'
            + 'मॉक मुलाखती दिल्यात: ' + mockCount + ' (Best: ' + bestMock + '/20)\n\n'
            + 'आजचा सराव पूर्ण झाला आहे!'
        );

        const url = 'https://wa.me/' + (tutor.phone ? ('91' + tutor.phone.replace(/\D/g, '')) : '') + '?text=' + msg;
        window.open(url, '_blank');
    };

    ACT.reset_oral_data = () => {
        if (confirm('सर्व तोंडी मुलाखतीचा डेटा (मॉक स्कोअर, प्रगती) पुसला जाईल. खात्री आहे?')) {
            localStorage.removeItem('mced_oral_coach_v1');
            location.reload();
        }
    };

})();
