/* MCED District Account Assistant - Oral Interview Coach Engine & 20-Mark Mock Interview Simulator */
(function () {
    const PROFILE_KEY = 'mced_candidate_profile_v1';
    const COACH_KEY = 'mced_oral_coach_v1';

    // Default Profile
    function defProfile() {
        return {
            name: 'Aishwarya',
            hometown: 'Maharashtra',
            qualification: 'B.Com Graduate',
            college: '',
            gradYear: '2025',
            subjects: 'Financial Accounting, Costing, Auditing, Taxation',
            experience: 'Fresh graduate with practical academic training & written exam cleared',
            software: 'MS Excel (VLOOKUP, SUMIF, formulas), Tally ERP, MS Word',
            languages: 'Marathi, Hindi, English',
            mcedUnderstanding: 'Autonomous body promoting entrepreneurship, EDPs, district centers under Industries Dept',
            interviewDate: 'November 2026',
            jobNotes: 'District Account Assistant (Oral Interview - 20 Marks target)',
            completed: false
        };
    }

    // Default Coach State
    function defCoachState() {
        return {
            currentQId: 'A1',
            activeModule: 'ALL',
            planDone: {},
            history: [],
            mastered: {},
            revisionList: {},
            mockAttempts: [],
            sttLang: 'mr-IN',
            voiceSpeed: 1.0,
            timerSec: 60
        };
    }

    let Profile = defProfile();
    let Coach = defCoachState();

    function loadCoach() {
        try {
            const p = JSON.parse(localStorage[PROFILE_KEY] || 'null');
            if (p) Object.assign(Profile, p);
            const c = JSON.parse(localStorage[COACH_KEY] || 'null');
            if (c) Object.assign(Coach, c);
        } catch (e) { console.error('Failed to load coach state', e); }
    }

    function saveCoach() {
        try {
            localStorage[PROFILE_KEY] = JSON.stringify(Profile);
            localStorage[COACH_KEY] = JSON.stringify(Coach);
        } catch (e) { }
    }

    loadCoach();

    window.COACH_STATE = Coach;
    window.CANDIDATE_PROFILE = Profile;
    window.saveCoach = saveCoach;

    // Speech Synthesis (TTS) Helper with Indian Voice Detection & Separation
    let cachedVoices = [];
    function loadVoices() {
        if ('speechSynthesis' in window) {
            cachedVoices = window.speechSynthesis.getVoices() || [];
        }
    }
    if ('speechSynthesis' in window) {
        loadVoices();
        window.speechSynthesis.onvoiceschanged = loadVoices;
    }

    // Helper to check if device has a Devanagari (Marathi/Hindi) voice installed
    window.hasDevanagariVoice = function () {
        if (!cachedVoices.length) loadVoices();
        return cachedVoices.some(v => v.lang.startsWith('mr') || v.lang.startsWith('hi') || /marathi|hindi|swara|madhur|kalpana|hemant|aarohi|manohar/i.test(v.name));
    };

    // Indian English Speech Engine (Ideal for Panel Questions & English Model Answers)
    window.speakIndianEnglish = function (text) {
        if (!('speechSynthesis' in window)) {
            toast('⚠️ Your browser does not support Speech Synthesis audio.');
            return false;
        }
        speechSynthesis.cancel();
        if (!cachedVoices.length) loadVoices();

        const clean = text.replace(/<[^>]*>/g, '').replace(/[\*\_\[\]]/g, '').trim();
        const u = new SpeechSynthesisUtterance(clean);
        u.lang = 'en-IN';
        u.rate = (Coach.voiceSpeed || 1.0) * 0.92;
        u.pitch = 1.0;

        // Try Indian English voices first (e.g. Neerja, Prabhat, Google English India, Heera, Ravi)
        let voice = cachedVoices.find(v => (v.lang === 'en-IN' || v.lang === 'en_IN') && !/hindi|marathi/i.test(v.name));
        if (!voice) voice = cachedVoices.find(v => /india/i.test(v.name) && v.lang.startsWith('en'));
        if (!voice) voice = cachedVoices.find(v => v.lang.startsWith('en-GB') || v.lang.startsWith('en'));
        if (!voice && cachedVoices.length) voice = cachedVoices[0];

        if (voice) u.voice = voice;
        u.onerror = (e) => { console.warn('TTS Error', e); };
        speechSynthesis.speak(u);
        return true;
    };

    // Marathi & Hindi Speech Engine (Speaks strictly in Marathi/Hindi voices)
    window.speakMarathiHindi = function (text) {
        if (!('speechSynthesis' in window)) {
            toast('⚠️ Your browser does not support Speech Synthesis audio.');
            return false;
        }
        speechSynthesis.cancel();
        if (!cachedVoices.length) loadVoices();

        // Find Marathi or Hindi voice
        let voice = cachedVoices.find(v => v.lang.startsWith('mr') || /marathi|aarohi|manohar/i.test(v.name));
        if (!voice) {
            voice = cachedVoices.find(v => v.lang.startsWith('hi') || /hindi|swara|madhur|kalpana|hemant/i.test(v.name));
        }

        // If no Devanagari voice exists on device (common on default Windows OS)
        if (!voice) {
            toast('ℹ️ तुमच्या डिव्हाइसवर मराठी/हिंदी व्हॉईस इन्स्टॉल नाही. कृपया \'English\' ऑडिओ वापरा किंवा Microsoft Edge / मोबाईलवर उघडा.', 5000);
            return false;
        }

        const clean = text.replace(/<[^>]*>/g, '').replace(/[\*\_\[\]]/g, '').trim();
        const u = new SpeechSynthesisUtterance(clean);
        u.lang = voice.lang || 'mr-IN';
        u.voice = voice;
        u.rate = (Coach.voiceSpeed || 1.0) * 0.90;
        u.pitch = 1.0;
        u.onerror = (e) => { console.warn('TTS Error', e); };
        speechSynthesis.speak(u);
        return true;
    };

    window.speakText = function (text, lang = 'en-IN') {
        if (lang.startsWith('mr') || lang.startsWith('hi')) {
            return window.speakMarathiHindi(text);
        } else {
            return window.speakIndianEnglish(text);
        }
    };

    window.stopSpeech = function () {
        if ('speechSynthesis' in window) speechSynthesis.cancel();
    };

    // Speech Recognition (STT) Helper
    let recognizer = null;
    let isListening = false;

    window.initSpeechRecognition = function (onResult, onStatus) {
        const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!SpeechRec) return null;

        if (!recognizer) {
            recognizer = new SpeechRec();
            recognizer.continuous = true;
            recognizer.interimResults = true;
        }

        recognizer.lang = Coach.sttLang || 'mr-IN';

        recognizer.onstart = () => {
            isListening = true;
            if (onStatus) onStatus(true);
        };

        recognizer.onend = () => {
            isListening = false;
            if (onStatus) onStatus(false);
        };

        recognizer.onerror = (e) => {
            isListening = false;
            if (onStatus) onStatus(false, e.error);
        };

        recognizer.onresult = (event) => {
            let transcript = '';
            for (let i = event.resultIndex; i < event.results.length; i++) {
                transcript += event.results[i][0].transcript;
            }
            if (onResult) onResult(transcript, event.results[event.results.length - 1].isFinal);
        };

        return {
            start: () => {
                try {
                    recognizer.lang = Coach.sttLang || 'mr-IN';
                    recognizer.start();
                } catch (e) { }
            },
            stop: () => {
                try { recognizer.stop(); } catch (e) { }
            },
            isListening: () => isListening
        };
    };

    // Evaluation Logic
    window.evaluateOralAnswer = function (q, answerText) {
        const text = (answerText || '').toLowerCase().trim();
        const words = text.split(/\s+/).filter(w => w.length > 0);
        const wordCount = words.length;

        // Keyword analysis
        const matchedKeywords = [];
        const missingKeywords = [];
        (q.keywords || []).forEach(kw => {
            const lowKw = kw.toLowerCase();
            if (text.includes(lowKw)) {
                matchedKeywords.push(kw);
            } else {
                missingKeywords.push(kw);
            }
        });

        const kwMatchRatio = q.keywords && q.keywords.length ? (matchedKeywords.length / q.keywords.length) : 0.5;

        // Scoring out of 10 for practice
        let score = 0;
        let strengths = [];
        let improvements = [];

        if (wordCount < 10) {
            score = 3;
            strengths.push('तुम्ही उत्तर देण्याचा प्रयत्न केला.');
            improvements.push('उत्तर खूपच त्रोटक (too short) आहे. किमान ३० ते ६० सेकंद समर्पक मुद्द्यांसह बोलण्याचा सराव करा.');
            improvements.push('प्रश्नातील आवश्यक तांत्रिक संकल्पनांचा (technical terms) उल्लेख आला नाही.');
        } else if (wordCount < 30) {
            score = Math.min(6, Math.round(3 + kwMatchRatio * 4));
            if (matchedKeywords.length > 0) {
                strengths.push('काही महत्त्वाचे शब्द उदा. "' + matchedKeywords.slice(0, 3).join(', ') + '" तुम्ही योग्य वापरले.');
            } else {
                strengths.push('बोलण्याचा ओघ चांगला आहे.');
            }
            improvements.push('उत्तरामध्ये अधिक सविस्तर मुद्दे, उदाहरणे आणि प्रॅक्टिकल संदर्भ समाविष्ट करा.');
            if (missingKeywords.length > 0) {
                improvements.push('खालील संकल्पनांचा उल्लेख करायला हवा होता: ' + missingKeywords.slice(0, 3).join(', '));
            }
        } else {
            // Good length
            score = Math.min(10, Math.round(5 + kwMatchRatio * 5));
            strengths.push('आत्मविश्वासपूर्वक आणि सविस्तर मांडणी केली (' + wordCount + ' शब्द).');
            if (matchedKeywords.length > 0) {
                strengths.push('अकाउंटिंगचे महत्त्वाचे शब्द व संकल्पना योग्य वापरल्या: ' + matchedKeywords.slice(0, 4).join(', '));
            }
            if (kwMatchRatio < 0.6 && missingKeywords.length > 0) {
                improvements.push('आणखी अचूकतेसाठी हे मुद्दे उत्तरात जोडा: ' + missingKeywords.slice(0, 3).join(', '));
            } else {
                strengths.push('प्रश्नाला समर्पक आणि व्यावसायिक दृष्टिकोनातून उत्तर दिले.');
            }
            improvements.push('आवाज शांत, स्पष्ट आणि ठाम ठेवा; अनावश्यक filler words टाळा.');
        }

        return {
            score,
            wordCount,
            matchedKeywords,
            missingKeywords,
            strengths,
            improvements,
            modelAnswer: q.modelAnswer.replace(/\[नाव\]/g, Profile.name || 'ऐश्वर्या')
                .replace(/\[गाव\/शहर\]/g, Profile.hometown || 'महाराष्ट्र')
                .replace(/\[कॉलेजचे नाव\]/g, Profile.college || 'महाविद्यालय')
                .replace(/\[वर्ष\]/g, Profile.gradYear || '२०२५'),
            modelAnswer_en: (q.modelAnswer_en || q.modelAnswer)
                .replace(/\[Name\]|\[नाव\]/g, Profile.name || 'Aishwarya')
                .replace(/\[City\/District\]|\[गाव\/शहर\]/g, Profile.hometown || 'Maharashtra')
                .replace(/\[College Name\]|\[कॉलेजचे नाव\]/g, Profile.college || 'College')
                .replace(/\[Year\]|\[वर्ष\]/g, Profile.gradYear || '2025'),
            followUp: q.followUp,
            followUpAnswer: q.followUpAnswer
        };
    };

    // 20-Mark Mock Interview Assessment Logic
    window.generateMockReport = function (mockResults) {
        // mockResults is an array of { q, answer, evalResult }
        const rubricTotals = {
            mced_org: { max: 6, got: 0, weight: 0 },
            situational: { max: 6, got: 0, weight: 0 },
            personality: { max: 4, got: 0, weight: 0 },
            practical_acc: { max: 3, got: 0, weight: 0 },
            computer_office: { max: 1, got: 0, weight: 0 }
        };

        const strongest = [];
        const weakest = [];
        const missedConcepts = [];

        mockResults.forEach(item => {
            const cat = item.q.rubric || 'mced_org';
            const s10 = item.evalResult.score; // 0 to 10
            rubricTotals[cat].weight += 1;
            rubricTotals[cat].got += (s10 / 10);

            if (s10 >= 7) {
                strongest.push({ id: item.q.id, q: item.q.q_en, score: s10 });
            } else {
                weakest.push({ id: item.q.id, q: item.q.q_en, score: s10 });
                if (item.evalResult.missingKeywords && item.evalResult.missingKeywords.length) {
                    missedConcepts.push(...item.evalResult.missingKeywords.slice(0, 2));
                }
            }
        });

        // Scale categories to their exact rubric marks
        let totalScore = 0;
        const categoryBreakdown = {};

        for (const [key, val] of Object.entries(rubricTotals)) {
            const ratio = val.weight > 0 ? (val.got / val.weight) : 0.7; // default average if category had fewer questions
            const awarded = Math.min(val.max, Math.round(ratio * val.max * 10) / 10);
            categoryBreakdown[key] = awarded;
            totalScore += awarded;
        }

        totalScore = Math.min(20, Math.round(totalScore * 10) / 10);

        // Top 5 Areas for Improvement
        const top5 = [
            'MCED ची ध्येये (१९८८, स्वायत्त संस्था, मुख्यालय छत्रपती संभाजीनगर) आणि उद्योजकता विकासाचे महत्त्व अधिक ठामपणे सांगा.',
            'कार्यालयीन प्रसंगात (उदा. अपूर्ण बिले, कॅश तूट) आधी पडताळणी, वरिष्ठांना सूचना आणि अधिकृत प्रक्रियेला प्राधान्य द्या.',
            'Account Assistant ची भूमिका तपासणे, नोंदवणे व अहवाल देणे आहे; स्वतंत्र मंजुरी देण्याचे अधिकार नाहीत हा फरक स्पष्ट करा.',
            'उत्तर माहित नसल्यास चुकीचा अंदाज लावण्याऐवजी प्रामाणिकपणे "तपासून सांगतो" म्हणणे अधिक विश्वासार्ह ठरते.',
            'उत्तर ३० ते ६० सेकंदांत मुद्देसूद संपवा; उत्तर संपल्यावर "धन्यवाद Sir/Madam" म्हणून व्यावसायिक विराम द्या.'
        ];

        return {
            totalScore,
            categoryBreakdown,
            strongest,
            weakest,
            missedConcepts: [...new Set(missedConcepts)].slice(0, 6),
            top5,
            timestamp: Date.now()
        };
    };

})();
