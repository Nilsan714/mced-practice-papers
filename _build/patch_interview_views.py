import re

path = 'docs/js/interview_views.js'
with open(path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Coach question audio bar
target_q_audio = """            + '<div class="audio-bar">'
            + '<button class="voice-btn" data-a="listen_q">🔊 प्रश्न ऐका</button>'
            + '<button class="voice-btn" data-a="stop_audio" style="display:none" id="stopBtn">⏹️ थांबवा</button>'
            + '<span class="timer-chip" id="timerBadge">⏱️ 60s</span>'
            + '</div>'"""

repl_q_audio = """            + '<div class="audio-bar" style="display:flex;gap:8px;align-items:center;flex-wrap:wrap">'
            + '<button class="voice-btn" data-a="listen_q_en" title="English Panel Voice">🔊 English (Panel)</button>'
            + '<button class="voice-btn" data-a="listen_q_mr" title="मराठी/हिंदी अनुवाद ऐका">🔊 मराठीत ऐका</button>'
            + '<button class="voice-btn" data-a="stop_audio" style="display:none" id="stopBtn">⏹️ थांबवा</button>'
            + '<span class="timer-chip" id="timerBadge">⏱️ 60s</span>'
            + '</div>'"""

assert target_q_audio in code, "Target q audio bar not found"
code = code.replace(target_q_audio, repl_q_audio)

# 2. Update Model answer in Coach Eval box
target_eval_model = """            // Model Answer
            + '<div class="model-answer-box">'
            + '<div class="row sp">'
            + '<b>💡 साध्या भाषेत आदर्श उत्तर (Model Answer):</b>'
            + '<button class="voice-btn" data-a="listen_model" style="padding:4px 10px;font-size:12px">🔊 ऐका</button>'
            + '</div>'
            + '<p style="margin:8px 0;line-height:1.6">' + esc(res.modelAnswer).replace(/\\n/g, '<br>') + '</p>'
            + '</div>'"""

repl_eval_model = """            // Model Answer
            + '<div class="model-answer-box">'
            + '<div class="row sp wrap" style="align-items:center;gap:8px">'
            + '<b>💡 साध्या भाषेत आदर्श उत्तर (Model Answer):</b>'
            + '<div style="display:flex;gap:6px;flex-wrap:wrap">'
            + '<button class="voice-btn" data-a="listen_model_en" style="padding:4px 10px;font-size:12px" title="English मध्ये उत्तर ऐका">🔊 English ऐका</button>'
            + '<button class="voice-btn" data-a="listen_model_mr" style="padding:4px 10px;font-size:12px" title="मराठी/हिंदीत उत्तर ऐका">🔊 मराठी/हिंदीत ऐका</button>'
            + '</div>'
            + '</div>'
            + '<div style="margin:8px 0;display:flex;gap:6px">'
            + '<button class="pill active" id="btnModelMr" data-a="show_model_mr" style="cursor:pointer;padding:4px 12px;font-size:12px">मराठी / हिंदी</button>'
            + '<button class="pill" id="btnModelEn" data-a="show_model_en" style="cursor:pointer;padding:4px 12px;font-size:12px">English Model Answer</button>'
            + '</div>'
            + '<p id="modelAnsBoxMr" style="margin:8px 0;line-height:1.6">' + esc(res.modelAnswer).replace(/\\n/g, '<br>') + '</p>'
            + '<p id="modelAnsBoxEn" style="margin:8px 0;line-height:1.6;display:none;background:var(--card-hover,#f8fafc);padding:10px 14px;border-radius:8px;border-left:3px solid var(--p)">' + esc(res.modelAnswer_en || curActiveQ.modelAnswer_en || res.modelAnswer).replace(/\\n/g, '<br>') + '</p>'
            + '</div>'"""

assert target_eval_model in code, "Target eval model answer not found"
code = code.replace(target_eval_model, repl_eval_model)

# 3. Update Actions for Coach
target_coach_acts = """    ACT.listen_q = () => {
        if (!curActiveQ) return;
        const stopBtn = $('#stopBtn');
        if (stopBtn) stopBtn.style.display = 'inline-flex';
        window.speakText(curActiveQ.q_en + '. ' + curActiveQ.q_mr, 'en-IN');
    };

    ACT.listen_model = () => {
        if (!curActiveQ) return;
        const stopBtn = $('#stopBtn');
        if (stopBtn) stopBtn.style.display = 'inline-flex';
        const modelTxt = curActiveQ.modelAnswer.replace(/\\[.*?\\]/g, ' ');
        window.speakText(modelTxt, 'hi-IN');
    };

    ACT.stop_audio = () => {
        window.stopSpeech();
        const stopBtn = $('#stopBtn');
        if (stopBtn) stopBtn.style.display = 'none';
    };"""

repl_coach_acts = """    ACT.listen_q_en = () => {
        if (!curActiveQ) return;
        const stopBtn = $('#stopBtn');
        if (stopBtn) stopBtn.style.display = 'inline-flex';
        window.speakIndianEnglish(curActiveQ.q_en);
    };

    ACT.listen_q_mr = () => {
        if (!curActiveQ) return;
        const stopBtn = $('#stopBtn');
        if (stopBtn) stopBtn.style.display = 'inline-flex';
        window.speakMarathiHindi(curActiveQ.q_mr);
    };

    ACT.listen_model_en = () => {
        if (!curActiveQ) return;
        const stopBtn = $('#stopBtn');
        if (stopBtn) stopBtn.style.display = 'inline-flex';
        const enTxt = (curActiveQ.modelAnswer_en || curActiveQ.modelAnswer).replace(/\\[.*?\\]/g, ' ');
        window.speakIndianEnglish(enTxt);
    };

    ACT.listen_model_mr = () => {
        if (!curActiveQ) return;
        const stopBtn = $('#stopBtn');
        if (stopBtn) stopBtn.style.display = 'inline-flex';
        const mrTxt = curActiveQ.modelAnswer.replace(/\\[.*?\\]/g, ' ');
        window.speakMarathiHindi(mrTxt);
    };

    ACT.show_model_mr = () => {
        const mrP = $('#modelAnsBoxMr');
        const enP = $('#modelAnsBoxEn');
        const btnMr = $('#btnModelMr');
        const btnEn = $('#btnModelEn');
        if (mrP && enP) {
            mrP.style.display = 'block';
            enP.style.display = 'none';
        }
        if (btnMr && btnEn) {
            btnMr.classList.add('active');
            btnEn.classList.remove('active');
        }
    };

    ACT.show_model_en = () => {
        const mrP = $('#modelAnsBoxMr');
        const enP = $('#modelAnsBoxEn');
        const btnMr = $('#btnModelMr');
        const btnEn = $('#btnModelEn');
        if (mrP && enP) {
            mrP.style.display = 'none';
            enP.style.display = 'block';
        }
        if (btnMr && btnEn) {
            btnEn.classList.add('active');
            btnMr.classList.remove('active');
        }
    };

    ACT.stop_audio = () => {
        window.stopSpeech();
        const stopBtn = $('#stopBtn');
        if (stopBtn) stopBtn.style.display = 'none';
        const stopMockBtn = $('#stopMockBtn');
        if (stopMockBtn) stopMockBtn.style.display = 'none';
    };"""

assert target_coach_acts in code, "Target coach acts not found"
code = code.replace(target_coach_acts, repl_coach_acts)

# 4. Update Mock question audio bar and language selector
target_mock_bar = """            + '<div class="audio-bar">'
            + '<button class="voice-btn" data-a="listen_mock_q">🔊 पॅनेलचा आवाज ऐका</button>'
            + '<span class="timer-chip" id="mockTimer">⏱️ 60s</span>'
            + '</div>'

            + '<div class="mic-container">'
            + '<button class="mic-btn" id="mockMicBtn" data-a="toggle_mock_mic">🎙️</button>'
            + '<div id="mockMicStatus" class="mu sm" style="margin-top:6px">माईकवर टॅप करून उत्तर बोला किंवा खाली टाईप करा</div>'
            + '</div>'

            + '<textarea class="answer-textarea" id="mockAns" placeholder="येथे तुमचे उत्तर दिसेल..."></textarea>'"""

repl_mock_bar = """            + '<div class="audio-bar" style="display:flex;gap:8px;align-items:center;flex-wrap:wrap">'
            + '<button class="voice-btn" data-a="listen_mock_en">🔊 English (Panel)</button>'
            + '<button class="voice-btn" data-a="listen_mock_mr">🔊 मराठीत ऐका</button>'
            + '<button class="voice-btn" data-a="stop_audio" style="display:none" id="stopMockBtn">⏹️ थांबवा</button>'
            + '<span class="timer-chip" id="mockTimer">⏱️ 60s</span>'
            + '</div>'

            + '<div class="mic-container">'
            + '<button class="mic-btn" id="mockMicBtn" data-a="toggle_mock_mic">🎙️</button>'
            + '<div id="mockMicStatus" class="mu sm" style="margin-top:6px">माईकवर टॅप करून उत्तर बोला किंवा खाली टाईप करा</div>'
            + '</div>'

            + '<div class="row sp" style="margin-bottom:6px;align-items:center">'
            + '<span class="mu sm">उत्तर भाषा:</span>'
            + '<select id="mockSttLangSelect" style="font-size:12px;padding:2px 8px;border-radius:8px;border:1px solid var(--bd);background:var(--card);color:var(--fg)">'
            + '<option value="mr-IN"' + (coach.sttLang === 'mr-IN' ? ' selected' : '') + '>मराठी (mr-IN)</option>'
            + '<option value="hi-IN"' + (coach.sttLang === 'hi-IN' ? ' selected' : '') + '>हिंदी (hi-IN)</option>'
            + '<option value="en-IN"' + (coach.sttLang === 'en-IN' ? ' selected' : '') + '>English (en-IN)</option>'
            + '</select>'
            + '</div>'

            + '<textarea class="answer-textarea" id="mockAns" placeholder="येथे तुमचे उत्तर दिसेल..."></textarea>'"""

assert target_mock_bar in code, "Target mock bar not found"
code = code.replace(target_mock_bar, repl_mock_bar)

# 5. Update Mock auto-speak and mock actions
target_mock_auto = """        // Auto speak panel question
        setTimeout(() => {
            window.speakText(q.q_en + '. ' + q.q_mr, 'en-IN');
        }, 300);"""

repl_mock_auto = """        // Auto speak panel question in clean Indian English
        setTimeout(() => {
            window.speakIndianEnglish(q.q_en);
        }, 300);

        // Bind mock language select
        const mockLangSel = $('#mockSttLangSelect');
        if (mockLangSel) {
            mockLangSel.onchange = (e) => {
                coach.sttLang = e.target.value;
                window.saveCoach();
                toast('उत्तर भाषा बदलली: ' + e.target.options[e.target.selectedIndex].text);
            };
        }"""

assert target_mock_auto in code, "Target mock auto not found"
code = code.replace(target_mock_auto, repl_mock_auto)

# 6. Update Mock actions
target_mock_acts = """    ACT.listen_mock_q = () => {
        if (!mockSession) return;
        const q = mockSession.questions[mockSession.currentIdx];
        window.speakText(q.q_en + '. ' + q.q_mr, 'en-IN');
    };"""

repl_mock_acts = """    ACT.listen_mock_en = () => {
        if (!mockSession) return;
        const q = mockSession.questions[mockSession.currentIdx];
        const stopBtn = $('#stopMockBtn');
        if (stopBtn) stopBtn.style.display = 'inline-flex';
        window.speakIndianEnglish(q.q_en);
    };

    ACT.listen_mock_mr = () => {
        if (!mockSession) return;
        const q = mockSession.questions[mockSession.currentIdx];
        const stopBtn = $('#stopMockBtn');
        if (stopBtn) stopBtn.style.display = 'inline-flex';
        window.speakMarathiHindi(q.q_mr);
    };"""

assert target_mock_acts in code, "Target mock acts not found"
code = code.replace(target_mock_acts, repl_mock_acts)

with open(path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Successfully updated docs/js/interview_views.js with clean Indian audio TTS separation!")
