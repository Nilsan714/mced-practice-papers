# -*- coding: utf-8 -*-
import os

DOCS_JS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'docs', 'js')

# 1. Update interview_coach.js
coach_js_path = os.path.join(DOCS_JS, 'interview_coach.js')
with open(coach_js_path, 'r', encoding='utf-8') as f:
    c = f.read()

old_rubric_totals = """        const rubricTotals = {
            accounting: { max: 6, got: 0, weight: 0 },
            practical: { max: 5, got: 0, weight: 0 },
            mced: { max: 3, got: 0, weight: 0 },
            communication: { max: 3, got: 0, weight: 0 },
            confidence: { max: 3, got: 0, weight: 0 }
        };"""

new_rubric_totals = """        const rubricTotals = {
            mced_org: { max: 6, got: 0, weight: 0 },
            situational: { max: 6, got: 0, weight: 0 },
            personality: { max: 4, got: 0, weight: 0 },
            practical_acc: { max: 3, got: 0, weight: 0 },
            computer_office: { max: 1, got: 0, weight: 0 }
        };"""

c = c.replace(old_rubric_totals, new_rubric_totals)

old_cat = "const cat = item.q.rubric || 'accounting';"
new_cat = "const cat = item.q.rubric || 'mced_org';"
c = c.replace(old_cat, new_cat)

old_top5 = """        const top5 = [
            'अकाउंटिंग संकल्पना स्पष्ट करताना सुवर्ण नियम व लेजर उदाहरणे स्वतःच्या शब्दांत देण्याचा सराव करा.',
            'शासकीय ऑफिस कामातील व्हाउचर चेकिंग, टॅक्स इनव्हॉईस व स्टॉक एन्ट्री पडताळणी पद्धतशीर सांगा.',
            'MCED चे कार्य, मुख्यालय (छत्रपती संभाजीनगर) व उद्योजकता योजना (CMEGP/PMEGP) यावर ठाम माहिती ठेवा.',
            'बोलताना अनावश्यक दडपण न घेता इंग्रजी व मराठीत आत्मविश्वासपूर्ण शब्दोच्चार (Clear Pronunciation) ठेवा.',
            'उत्तर ३० ते ६० सेकंदांत मुद्देसूद संपवा; उत्तर संपल्यावर "धन्यवाद Sir/Madam" म्हणून पूर्ण विराम द्या.'
        ];"""

new_top5 = """        const top5 = [
            'MCED ची ध्येये (१९८८, स्वायत्त संस्था, मुख्यालय छत्रपती संभाजीनगर) आणि उद्योजकता विकासाचे महत्त्व अधिक ठामपणे सांगा.',
            'कार्यालयीन प्रसंगात (उदा. अपूर्ण बिले, कॅश तूट) आधी पडताळणी, वरिष्ठांना सूचना आणि अधिकृत प्रक्रियेला प्राधान्य द्या.',
            'Account Assistant ची भूमिका तपासणे, नोंदवणे व अहवाल देणे आहे; स्वतंत्र मंजुरी देण्याचे अधिकार नाहीत हा फरक स्पष्ट करा.',
            'उत्तर माहित नसल्यास चुकीचा अंदाज लावण्याऐवजी प्रामाणिकपणे "तपासून सांगतो" म्हणणे अधिक विश्वासार्ह ठरते.',
            'उत्तर ३० ते ६० सेकंदांत मुद्देसूद संपवा; उत्तर संपल्यावर "धन्यवाद Sir/Madam" म्हणून व्यावसायिक विराम द्या.'
        ];"""

c = c.replace(old_top5, new_top5)

with open(coach_js_path, 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated interview_coach.js')

# 2. Update interview_views.js
views_js_path = os.path.join(DOCS_JS, 'interview_views.js')
with open(views_js_path, 'r', encoding='utf-8') as f:
    v = f.read()

old_mod_pills = "const modPills = ['ALL', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'REVISION'].map(m => {"
new_mod_pills = """const modMap = {
            ALL: 'सर्व (All)',
            MCED: '🏛️ MCED व पद (30%)',
            SITUATIONAL: '🏢 कार्यालयीन प्रसंग (30%)',
            HR: '👤 HR व व्यक्तिमत्व (20%)',
            PRACTICAL_ACC: '📊 प्रॅक्टिकल अकाउंट्स (15%)',
            COMPUTER: '💻 कॉम्प्युटर/एक्सेल (5%)',
            REVISION: '🔖 उजळणी'
        };
        const modPills = ['ALL', 'MCED', 'SITUATIONAL', 'HR', 'PRACTICAL_ACC', 'COMPUTER', 'REVISION'].map(m => {"""

v = v.replace(old_mod_pills, new_mod_pills)
v = v.replace("const label = m === 'ALL' ? 'सर्व' : m === 'REVISION' ? '🔖 उजळणी (' + Object.keys(coach.revisionList || {}).length + ')' : ('Mod ' + m);", "const label = modMap[m] || m;")

old_rubric_display = """            + '<div class="rubric-row"><span>1. Accounting Knowledge (लेखांकन ज्ञान)</span><b>6 Marks</b></div>'
            + '<div class="rubric-row"><span>2. Practical Accounting Skills (कार्यालयीन हिशेब)</span><b>5 Marks</b></div>'
            + '<div class="rubric-row"><span>3. MCED & Govt Awareness (संस्था व योजना ज्ञान)</span><b>3 Marks</b></div>'
            + '<div class="rubric-row"><span>4. Communication & Clarity (संभाषण कौशल्य)</span><b>3 Marks</b></div>'
            + '<div class="rubric-row"><span>5. Confidence & Professional Behaviour (आत्मविश्वास)</span><b>3 Marks</b></div>'"""

new_rubric_display = """            + '<div class="rubric-row"><span>1. MCED Organisation & Job Role (30%)</span><b>6 Marks</b></div>'
            + '<div class="rubric-row"><span>2. Real-Life Workplace Simulations (30%)</span><b>6 Marks</b></div>'
            + '<div class="rubric-row"><span>3. Personality, HR & Behaviour (20%)</span><b>4 Marks</b></div>'
            + '<div class="rubric-row"><span>4. Practical Accounting & Controls (15%)</span><b>3 Marks</b></div>'
            + '<div class="rubric-row"><span>5. Computer & Office Knowledge (5%)</span><b>1 Mark</b></div>'"""

v = v.replace(old_rubric_display, new_rubric_display)

old_mock_select = """        // Select balanced 10 questions across categories
        const accQs = DATA.questions.filter(q => q.rubric === 'accounting').sort(() => Math.random() - .5).slice(0, 3);
        const pracQs = DATA.questions.filter(q => q.rubric === 'practical').sort(() => Math.random() - .5).slice(0, 3);
        const mcedQs = DATA.questions.filter(q => q.rubric === 'mced').sort(() => Math.random() - .5).slice(0, 2);
        const hrQs = DATA.questions.filter(q => q.rubric === 'communication' || q.rubric === 'confidence').sort(() => Math.random() - .5).slice(0, 2);

        const fullList = [...accQs, ...pracQs, ...mcedQs, ...hrQs].sort(() => Math.random() - .5);"""

new_mock_select = """        // Select balanced 10 questions strictly following new priorities:
        // 30% MCED (3 Qs), 30% Situational (3 Qs), 20% HR (2 Qs), 15% Practical Acc (1 Q), 5% Computer (1 Q) = 10 Questions
        const mcedQs = DATA.questions.filter(q => q.rubric === 'mced_org').sort(() => Math.random() - .5).slice(0, 3);
        const sitQs = DATA.questions.filter(q => q.rubric === 'situational').sort(() => Math.random() - .5).slice(0, 3);
        const hrQs = DATA.questions.filter(q => q.rubric === 'personality').sort(() => Math.random() - .5).slice(0, 2);
        const pracQs = DATA.questions.filter(q => q.rubric === 'practical_acc').sort(() => Math.random() - .5).slice(0, 1);
        const compQs = DATA.questions.filter(q => q.rubric === 'computer_office').sort(() => Math.random() - .5).slice(0, 1);

        const fullList = [...mcedQs, ...sitQs, ...hrQs, ...pracQs, ...compQs].sort(() => Math.random() - .5);"""

v = v.replace(old_mock_select, new_mock_select)

old_scorecard_bars = """            + '<div class="rubric-row"><span>1. Accounting Knowledge (लेखांकन ज्ञान)</span><b>' + cat.accounting + ' / 6</b></div>'
            + bar(pct(cat.accounting, 6), cat.accounting >= 4.5 ? 'ok' : 'wn')
            + '<div class="rubric-row" style="margin-top:10px"><span>2. Practical Accounting Skills (कार्यालयीन हिशेब)</span><b>' + cat.practical + ' / 5</b></div>'
            + bar(pct(cat.practical, 5), cat.practical >= 4 ? 'ok' : 'wn')
            + '<div class="rubric-row" style="margin-top:10px"><span>3. MCED & Govt Awareness (संस्था व योजना ज्ञान)</span><b>' + cat.mced + ' / 3</b></div>'
            + bar(pct(cat.mced, 3), cat.mced >= 2 ? 'ok' : 'wn')
            + '<div class="rubric-row" style="margin-top:10px"><span>4. Communication & Clarity (संभाषण कौशल्य)</span><b>' + cat.communication + ' / 3</b></div>'
            + bar(pct(cat.communication, 3), cat.communication >= 2 ? 'ok' : 'wn')
            + '<div class="rubric-row" style="margin-top:10px"><span>5. Confidence & Behaviour (आत्मविश्वास व देहबोली)</span><b>' + cat.confidence + ' / 3</b></div>'
            + bar(pct(cat.confidence, 3), cat.confidence >= 2 ? 'ok' : 'wn')"""

new_scorecard_bars = """            + '<div class="rubric-row"><span>1. MCED & Job Role Awareness (30%)</span><b>' + (cat.mced_org || 0) + ' / 6</b></div>'
            + bar(pct(cat.mced_org || 0, 6), (cat.mced_org || 0) >= 4.5 ? 'ok' : 'wn')
            + '<div class="rubric-row" style="margin-top:10px"><span>2. Real-Life Workplace Simulations (30%)</span><b>' + (cat.situational || 0) + ' / 6</b></div>'
            + bar(pct(cat.situational || 0, 6), (cat.situational || 0) >= 4.5 ? 'ok' : 'wn')
            + '<div class="rubric-row" style="margin-top:10px"><span>3. Personality, HR & Behaviour (20%)</span><b>' + (cat.personality || 0) + ' / 4</b></div>'
            + bar(pct(cat.personality || 0, 4), (cat.personality || 0) >= 3 ? 'ok' : 'wn')
            + '<div class="rubric-row" style="margin-top:10px"><span>4. Practical Accounting & Controls (15%)</span><b>' + (cat.practical_acc || 0) + ' / 3</b></div>'
            + bar(pct(cat.practical_acc || 0, 3), (cat.practical_acc || 0) >= 2 ? 'ok' : 'wn')
            + '<div class="rubric-row" style="margin-top:10px"><span>5. Computer & Office Knowledge (5%)</span><b>' + (cat.computer_office || 0) + ' / 1</b></div>'
            + bar(pct(cat.computer_office || 0, 1), (cat.computer_office || 0) >= 0.8 ? 'ok' : 'wn')"""

v = v.replace(old_scorecard_bars, new_scorecard_bars)

# Syllabus filter buttons update
old_syl_btns = "const modButtons = ['ALL', 'A', 'B', 'C', 'D', 'E', 'F', 'G'].map(m => {"
new_syl_btns = """const sylMap = {
            ALL: 'सर्व (All)',
            MCED: '🏛️ MCED व पद (30%)',
            SITUATIONAL: '🏢 कार्यालयीन प्रसंग (30%)',
            HR: '👤 HR व व्यक्तिमत्व (20%)',
            PRACTICAL_ACC: '📊 प्रॅक्टिकल अकाउंट्स (15%)',
            COMPUTER: '💻 कॉम्प्युटर/एक्सेल (5%)'
        };
        const modButtons = ['ALL', 'MCED', 'SITUATIONAL', 'HR', 'PRACTICAL_ACC', 'COMPUTER'].map(m => {"""

v = v.replace(old_syl_btns, new_syl_btns)
v = v.replace("const lbl = m === 'ALL' ? 'सर्व (All)' : ('Module ' + m);", "const lbl = sylMap[m] || m;")

with open(views_js_path, 'w', encoding='utf-8') as f:
    f.write(v)
print('Updated interview_views.js')
