# -*- coding: utf-8 -*-
"""Redesigned Oral Interview Question Bank for MCED District Account Assistant
Priorities:
- 30% MCED Organisation & Job Role Awareness
- 30% Real-Life Workplace & Situational Simulations
- 20% Personal Interview, HR & Behavioural
- 15% Practical Accounting & Financial Controls
- 5% Computer & Office Knowledge
"""

QUESTIONS = [
    # =========================================================================
    # PART 1: MCED ORGANISATION & JOB ROLE AWARENESS (30% Weightage)
    # =========================================================================
    {
        'id': 'M1',
        'module': 'MCED',
        'category': 'MCED Organisation Knowledge',
        'rubric': 'mced_org',
        'q_en': 'What is MCED and what was the vision behind establishing it in Maharashtra?',
        'q_mr': 'MCED म्हणजे काय आणि महाराष्ट्रात तिची स्थापना कोणत्या दृष्टीकोनातून करण्यात आली?',
        'q_hi': 'MCED क्या है और इसकी स्थापना किस उद्देश्य से की गई थी?',
        'keyPoints': [
            'Full form: Maharashtra Centre for Entrepreneurship Development (महाराष्ट्र उद्योजकता विकास केंद्र)',
            'Established in 1988 as an autonomous society supported by Government of Maharashtra (Industries Department)',
            'Headquarters: Chhatrapati Sambhajinagar (Aurangabad)',
            'Vision: Spreading entrepreneurship culture across Maharashtra, particularly in rural and semi-urban areas',
            'Acts as a nodal agency for entrepreneurship training and skill development'
        ],
        'modelAnswer': 'सर, MCED चे पूर्ण रूप "Maharashtra Centre for Entrepreneurship Development" (महाराष्ट्र उद्योजकता विकास केंद्र) आहे. ही संस्था १९८८ मध्ये महाराष्ट्र शासनाच्या उद्योग विभागांतर्गत (Directorate of Industries) एक स्वायत्त संस्था (Autonomous Society) म्हणून स्थापन करण्यात आली. याचे मुख्यालय छत्रपती संभाजीनगर येथे आहे.\nसंस्थेचा मुख्य उद्देश हा आहे की राज्यातील तरुण-तरुणींमध्ये केवळ नोकरी शोधण्याची मानसिकता न राहता स्वतःचा उद्योग-व्यवसाय सुरू करण्याची उद्योजकीय वृत्ती (Entrepreneurship Mindset) निर्माण व्हावी. विशेषतः ग्रामीण आणि निमशहरी भागात उद्योग संस्कृती रुजवून स्वयंरोजगाराला चालना देणे ही MCED ची मुख्य भूमिका आहे.',
        'commonMistakes': [
            'Calling it a private coaching institute or bank',
            'Not knowing headquarters location (Chhatrapati Sambhajinagar)',
            'Not knowing the year of establishment (1988)'
        ],
        'followUp': 'Which government department oversees the functioning of MCED?',
        'followUpAnswer': 'उद्योग संचालनालय, उद्योग व कामगार विभाग, महाराष्ट्र शासन (Department of Industries, Government of Maharashtra).',
        'keywords': ['mced', 'maharashtra centre for entrepreneurship development', '1988', 'autonomous', 'industries department', 'chhatrapati sambhajinagar', 'entrepreneurship culture', 'rural']
    },
    {
        'id': 'M2',
        'module': 'MCED',
        'category': 'MCED Organisation Knowledge',
        'rubric': 'mced_org',
        'q_en': 'What does MCED actually do for aspiring and existing entrepreneurs?',
        'q_mr': 'MCED नवीन आणि विद्यमान उद्योजकांसाठी प्रत्यक्ष काय कार्य करते?',
        'q_hi': 'MCED नए और मौजूदा उद्यमियों के लिए क्या काम करता है?',
        'keyPoints': [
            'Conducts Entrepreneurship Development Programmes (EDPs)',
            'Provides project identification, business plan / DPR preparation assistance',
            'Imparts vocational, technical and management skill trainings',
            'Guides on government subsidy schemes (CMEGP, PMEGP, Mudra)',
            'Offers post-training escort services and handholding till enterprise establishment'
        ],
        'modelAnswer': 'मॅडम, MCED उद्योजकांसाठी सुरुवातीच्या कल्पनेपासून ते उद्योग सुरू होईपर्यंत संपूर्ण मार्गदर्शन (Handholding & Escort Services) पुरवते:\n१. व्यवसाय संधी शोधणे: उमेदवाराच्या आवडीनुसार स्थानिक पातळीवर कोणत्या व्यवसायाला वाव आहे हे ओळखणे.\n२. प्रशिक्षण (EDPs): व्यवसाय कसा चालवावा, फायनान्शियल मॅनेजमेंट, मार्केटिंग आणि शासकीय नियमांचे प्रशिक्षण देणे.\n३. प्रकल्प अहवाल (DPR): बँकेकडून कर्ज मंजूर होण्यासाठी आवश्यक असणारा तपशीलवार प्रकल्प अहवाल (Project Report) तयार करण्यास मदत करणे.\n४. शासकीय योजनांचा लाभ: मुख्यमंत्री रोजगार निर्मिती कार्यक्रम (CMEGP), PMEGP किंवा मुद्रा कर्जाची माहिती व अर्ज प्रक्रिया समजावणे.\n५. नेटवर्किंग: यशस्वी उद्योजक, बँक अधिकारी आणि उद्योग तज्ज्ञांशी प्रशिक्षणार्थींचा थेट संवाद घडवून आणणे.',
        'commonMistakes': [
            'Thinking MCED directly provides bank loans (Banks provide loans, MCED provides training/guidance)',
            'Forgetting the handholding/escort service aspect'
        ],
        'followUp': 'Does MCED provide loans from its own funds?',
        'followUpAnswer': 'नाही सर, MCED स्वतः कर्ज वाटप करत नाही. MCED ही प्रशिक्षण आणि प्रकल्प मार्गदर्शन देणारी संस्था आहे; कर्ज मंजुरीचे काम राष्ट्रीयकृत व इतर बँकांमार्फत होते.',
        'keywords': ['edp', 'entrepreneurship', 'training', 'dpr', 'project report', 'bank loan', 'cmegp', 'pmegp', 'handholding', 'guidance']
    },
    {
        'id': 'M3',
        'module': 'MCED',
        'category': 'MCED Organisation Knowledge',
        'rubric': 'mced_org',
        'q_en': 'What are Entrepreneurship Development Programmes (EDPs) and what different types of trainings does MCED conduct?',
        'q_mr': 'उद्योजकता विकास कार्यक्रम (EDP) म्हणजे काय आणि MCED कोणत्या प्रकारची विविध प्रशिक्षणे आयोजित करते?',
        'q_hi': 'EDP कार्यक्रम क्या होते हैं और MCED किस-किस तरह के प्रशिक्षण आयोजित करता है?',
        'keyPoints': [
            'Structured training courses designed to instill managerial, financial and operational skills',
            'General EDPs (for youth starting micro-enterprises)',
            'Special target group EDPs: Women Entrepreneurship EDPs, SC/ST, Minority, Ex-servicemen',
            'Technical & Vocational Skill Training: Agro-processing, food technology, solar installation, electrical, mobile repair',
            'Scheme-specific mandatory EDPs: CMEGP and PMEGP mandatory beneficiary training'
        ],
        'modelAnswer': 'सर, EDP (Entrepreneurship Development Programme) हा एक सुनियोजित अभ्यासक्रम असतो, ज्याद्वारे एखाद्या व्यक्तीमधील सुप्त उद्योजकीय गुणांना चालना देऊन तिला यशस्वी व्यवसाय मालक बनवले जाते.\nMCED द्वारे आयोजित प्रमुख प्रशिक्षण प्रकार:\n१. जनरल ईडीपी (General EDPs): नवीन व्यवसाय सुरू करू इच्छिणाऱ्या सुशिक्षित बेरोजगारांसाठी २ ते ४ आठवड्यांचे प्रशिक्षण.\n२. तांत्रिक व कौशल्य विकास प्रशिक्षण: शेतीपूरक प्रक्रिया (Agro Food Processing), सौर ऊर्जा (Solar), डिजिटल मार्केटिंग, ब्युटी अँड वेलनेस, फॅशन डिझायनिंग इत्यादी.\n३. विशेष घटकांसाठी प्रशिक्षण: महिलांसाठी विशेष उद्योजकता शिबिरे, अनुसूचित जाती/जमाती व ग्रामीण युवकांसाठी विशेष कार्यशाळा.\n४. शासकीय योजनांनुसार अनिवार्य प्रशिक्षण: CMEGP आणि PMEGP अंतर्गत कर्ज मंजूर झालेल्या उमेदवारांसाठी अनिवार्य निवासी/अनिवासी प्रशिक्षण.',
        'commonMistakes': [
            'Only mentioning theoretical lectures',
            'Not knowing that technical and skill trainings are also conducted'
        ],
        'followUp': 'Why is mandatory EDP training required before bank loan disbursement under CMEGP?',
        'followUpAnswer': 'कारण व्यवसायाचे बेसिक ज्ञान आणि आर्थिक शिस्त असल्याशिवाय कर्ज घेतल्यास व्यवसाय बुडण्याची शक्यता असते. प्रशिक्षणामुळे कर्जफेडीची क्षमता (Repayment Capacity) वाढते.',
        'keywords': ['edp', 'general edp', 'skill training', 'women entrepreneurship', 'agro processing', 'cmegp', 'mandatory training', 'technical']
    },
    {
        'id': 'M4',
        'module': 'MCED',
        'category': 'MCED Organisation Knowledge',
        'rubric': 'mced_org',
        'q_en': 'Why is the network of District Centres critical for MCED across Maharashtra?',
        'q_mr': 'महाराष्ट्रात जिल्हा स्तरावरील केंद्रे (District Centres) असणे MCED च्या कार्यासाठी का महत्त्वाचे आहे?',
        'q_hi': 'MCED के लिए जिला स्तर पर केंद्र होना क्यों आवश्यक है?',
        'keyPoints': [
            'Decentralized delivery: Reaching grassroots youth without needing them to travel to headquarters',
            'Local resource & market alignment: Understanding specific district strengths (e.g. grapes in Nashik, textiles in Solapur)',
            'Close coordination with local District Industries Centre (DIC), Lead Bank, and District Collector office',
            'Direct access for rural youth, women self-help groups (SHGs), and local farmers'
        ],
        'modelAnswer': 'मॅडम, महाराष्ट्र हा भौगोलिकदृष्ट्या मोठा आणि वैविध्यपूर्ण आहे. प्रत्येक जिल्ह्याची स्थानिक आर्थिक ताकद वेगळी असते (उदा. नाशिकमध्ये कृषी-प्रक्रिया, सोलापूरमध्ये टेक्सटाईल, विदर्भात कापूस/सोयाबीन). जर सर्व काम छत्रपती संभाजीनगर मुख्यालयातून चालले तर ग्रामीण तरुणांना तिथे पोहोचणे शक्य होणार नाही.\nजिल्हा केंद्रांचे महत्व:\n१. तळागाळापर्यंत पोहोच (Grassroots Outreach): ग्रामीण भागातील युवक-युवतींना त्यांच्याच जिल्ह्यात प्रशिक्षण उपलब्ध होते.\n२. जिल्हा यंत्रणेशी समन्वय: जिल्हा उद्योग केंद्र (DIC), अग्रणी बँक (Lead Bank) आणि स्थानिक प्रशासन यांच्याशी दैनंदिन समन्वय ठेवता येतो.\n३. स्थानिक बाजारपेठेनुसार प्रशिक्षण: त्या जिल्ह्यातील कच्च्या मालावर आधारित प्रक्रिया उद्योगांचे प्रशिक्षण देता येते.\nया जिल्हा कार्यालयाचा संपूर्ण आर्थिक व्यवहार आणि खर्चाचा ताळेबंद ठेवणे हे डिस्ट्रिक्ट अकाउंट असिस्टंटचे मुख्य काम असते.',
        'commonMistakes': [
            'Giving a generic answer without mentioning district-level coordination with DIC or Lead Bank'
        ],
        'followUp': 'What is the full form of DIC and what is its connection to the MCED district centre?',
        'followUpAnswer': 'DIC म्हणजे District Industries Centre (जिल्हा उद्योग केंद्र). DIC हे शासनाचे जिल्हा स्तरावरील औद्योगिक कार्यालय आहे आणि MCED त्यांच्यासोबत समन्वय ठेवून शासकीय योजना राबवते.',
        'keywords': ['district centre', 'dic', 'grassroots', 'local market', 'coordination', 'lead bank', 'decentralization', 'rural youth']
    },
    {
        'id': 'M5',
        'module': 'MCED',
        'category': 'Job Role Awareness',
        'rubric': 'job_role',
        'q_en': 'What do you understand by the District Account Assistant position in MCED? What are the core responsibilities?',
        'q_mr': 'MCED मधील डिस्ट्रिक्ट अकाउंट असिस्टंट (District Account Assistant) या पदाबद्दल तुमची काय समज आहे? या पदाच्या मुख्य जबाबदाऱ्या काय असतात?',
        'q_hi': 'District Account Assistant पद की मुख्य जिम्मेदारियाँ क्या हैं?',
        'keyPoints': [
            'Maintaining books of accounts (Cash Book, Bank Book, Ledger) of the District Office',
            'Scrutinizing bills of training batches (Hall rent, trainer fees, tea/refreshments, stationery)',
            'Preparing Payment and Receipt vouchers with proper budget head classification',
            'Monthly Bank Reconciliation (BRS) and tracking bank transactions',
            'Preparing monthly/quarterly Expenditure Statements for submission to Regional/Head Office',
            'Facilitating audit inspections and maintaining voucher guard files'
        ],
        'modelAnswer': 'सर, MCED च्या जिल्हा केंद्रात "डिस्ट्रिक्ट अकाउंट असिस्टंट" हे पद जिल्हा स्तरावरील संपूर्ण आर्थिक पारदर्शकता, अचूक नोंदणी आणि नियमांचे पालन सुनिश्चित करणारे महत्त्वाचे पद आहे.\nमुख्य जबाबदाऱ्या:\n१. वह्या आणि लेजर्स ठेवणे: दैनंदिन कॅश बुक, बँक बुक आणि विविध खर्चाचे लेजर्स अद्ययावत ठेवणे.\n२. बिलांची पडताळणी व व्हाउचर्स: प्रशिक्षण शिबिरांचे हॉल भाडे, ट्रेनर मानधन, स्टेशनरी आणि रिफ्रेशमेंटची बिले तपासून पेमेंट व्हाउचर तयार करणे.\n३. बँक रिकन्सिलिएशन (BRS): दर महिन्याअखेरीस बँक स्टेटमेंट आणि कॅश बुकमधील बँक रकान्याचा ताळेबंद तयार करणे.\n४. खर्चाचे विवरण (Expenditure Statement): मंजूर बजेटनुसार खर्च झाला आहे का हे तपासून मासिक खर्चाचे विवरणपत्र तयार करून प्रादेशिक कार्यालय किंवा मुख्यालयाला वेळेवर पाठवणे.\n५. फायलिंग व ऑडिट तयारी: सर्व व्हाउचर, पावत्या आणि सँक्शन ऑर्डर्स क्रमाने फाईल करून ठेवणे, जेणेकरून अंतर्गत व वैधानिक ऑडिट सुरळीत पार पडेल.',
        'commonMistakes': [
            'Thinking this post has independent power to approve or sanction bills',
            'Limiting the role only to data entry or typing'
        ],
        'followUp': 'Do you have the independent power to sanction or release payment to a vendor as an Account Assistant?',
        'followUpAnswer': 'नाही सर. अकाउंट असिस्टंट म्हणून माझे काम बिल तपासणे, व्हाउचर तयार करणे आणि नियमांनुसार शिफारस (Check & Recommend) करणे असते; बिल मंजूर (Sanction) करण्याचे आणि धनादेशावर स्वाक्षरी करण्याचे अधिकार सक्षम प्राधिकारी (District Project Officer/Coordinator) यांनाच असतात.',
        'keywords': ['district account assistant', 'cash book', 'bank book', 'vouchers', 'brs', 'expenditure statement', 'audit', 'bill scrutiny', 'documentation']
    },
    {
        'id': 'M6',
        'module': 'MCED',
        'category': 'Job Role Awareness',
        'rubric': 'job_role',
        'q_en': 'Explain the critical difference between preparing, checking, recording, reporting and authorising/sanctioning financial transactions.',
        'q_mr': 'आर्थिक व्यवहारात तयार करणे (Preparing), तपासणे (Checking), नोंदवणे (Recording), अहवाल देणे (Reporting) आणि मंजूर करणे (Sanctioning/Authorising) यातील फरक स्पष्ट करा.',
        'q_hi': 'वित्तीय लेन-देन में Preparing, Checking, Recording, Reporting और Authorising में क्या अंतर है?',
        'keyPoints': [
            'Preparing: Draft voucher, calculate net payable, attach supporting documents',
            'Checking: Scrutinize rules, sanction order, arithmetic accuracy, tax deductions',
            'Recording: Enter in Cash Book, Ledger, Excel registers',
            'Reporting: Compiling monthly expenditure statements for superiors and Head Office',
            'Authorising / Sanctioning: Exercising administrative financial power (Senior Officer / DPO only)'
        ],
        'modelAnswer': 'मॅडम, शासकीय आणि स्वायत्त संस्थांमध्ये आर्थिक गैरव्यवहार रोखण्यासाठी अधिकारांची स्पष्ट विभागणी (Segregation of Duties) असते:\n१. Preparing (तयार करणे): बिल आल्यावर प्राथमिक आकडेमोड करून पेमेंट व्हाउचर ड्राफ्ट करणे आणि सर्व सपोर्टिंग पेपर्स जोडणे.\n२. Checking (तपासणे): खर्चाला योग्य अधिकाऱ्याची पूर्वमंजुरी (Sanction) आहे का, जीएसटी/टीडीएस बरोबर कापला आहे का, आणि दर नियमांनुसार आहेत का हे तपासणे.\n३. Recording (नोंदवणे): मंजूर व्यवहार कॅश बुक, बँक बुक किंवा अकाउंटिंग सॉफ्टवेअर/एक्सेलमध्ये रीतसर नोंदवणे.\n४. Reporting (अहवाल देणे): महिनाभरातील एकूण खर्चाचा तपशील, युटिलायझेशन आणि प्रगती अहवाल वरिष्ठांना सादर करणे.\n५. Authorising / Sanctioning (मंजूर करणे): खर्चाला प्रशासकीय मान्यता देणे आणि बँकेच्या धनादेशावर स्वाक्षरी करणे. हा अधिकार फक्त सक्षम अधिकाऱ्यांना (District In-charge / DPO) असतो, अकाउंट असिस्टंटला नसतो. अकाउंट असिस्टंट आधीच्या चार टप्प्यांचे काम करते.',
        'commonMistakes': [
            'Confusing checking with authorising',
            'Thinking the person who writes the voucher can also sign and release the cheque alone'
        ],
        'followUp': 'Why is segregation of financial duties mandatory in public finance?',
        'followUpAnswer': 'कारण तयार करणारा, तपासणारा आणि स्वाक्षरी करणारा वेगवेगळा असेल तर चुका तात्काळ पकडल्या जातात आणि कोणत्याही एका व्यक्तीकडून आर्थिक अफरातफर किंवा गैरवापर होणे अशक्य होते.',
        'keywords': ['segregation of duties', 'preparing', 'checking', 'recording', 'reporting', 'authorising', 'sanctioning', 'internal control']
    },
    {
        'id': 'M7',
        'module': 'MCED',
        'category': 'MCED Organisation Knowledge',
        'rubric': 'mced_org',
        'q_en': 'Why is strict financial management and timely reporting important in MCED programmes?',
        'q_mr': 'MCED च्या कार्यक्रमांमध्ये कडक आर्थिक शिस्त आणि वेळेवर अहवाल देणे (Timely Reporting) का अत्यंत महत्त्वाचे आहे?',
        'q_hi': 'MCED के कार्यक्रमों में सख्त वित्तीय प्रबंधन और समय पर रिपोर्टिंग क्यों आवश्यक है?',
        'keyPoints': [
            'Government funds and public money accountability',
            'Timely submission of Utilization Certificates (UC) is required to unlock subsequent grant installments',
            'Statutory audits (AG audit / Chartered Accountant audit) require flawless records',
            'Prevents fund diversion and ensures money reaches intended training beneficiaries'
        ],
        'modelAnswer': 'सर, MCED ही शासकीय योजना आणि जनतेचा निधी हाताळणारी संस्था आहे. कडक वित्तीय व्यवस्थापन खालील कारणांसाठी अनिवार्य आहे:\n१. पुढील हप्ते मिळणे (Next Installments): शासनाकडून किंवा प्रायोजक संस्थांकडून पुढील निधी मिळण्यासाठी आधीच्या खर्चाचे वेळेवर युटिलायझेशन सर्टिफिकेट (UC) आणि हिशेब सादर करावे लागतात. अहवाल उशिरा गेला तर जिल्हा कार्यालयाचे पुढील कार्यक्रम रखडतात.\n२. बजेटची मर्यादा (Budget Compliance): मंजूर हेडपेक्षा जास्त खर्च होणार नाही आणि निधी योग्य कारणासाठीच खर्च होईल याची खात्री होते.\n३. ऑडिट सुरक्षितता: स्थानिक निधी लेखापरीक्षण किंवा महालेखाकार (AG) ऑडिटमध्ये कोणतीही गंभीर त्रुटी (Audit Para) निघू नये म्हणून प्रत्येक व्हाउचरचा ताळेबंद वेळेवर असावा लागतो.\n४. पारदर्शकता: सार्वजनिक पैशाचा प्रत्येक रुपया योग्य व्यक्तीपर्यंत पोहोचला आहे हे सिद्ध होते.',
        'commonMistakes': [
            'Giving a generic answer without mentioning Utilization Certificates (UC) or next grant installments'
        ],
        'followUp': 'What happens if a district office fails to submit its monthly accounts to the Head Office for two consecutive months?',
        'followUpAnswer': 'मुख्यालयाकडून त्या जिल्ह्याचा पुढील निधी रोखला जाऊ शकतो, कर्मचाऱ्यांचे पगार व प्रशिक्षण खर्च थांबतात आणि संबंधित अधिकाऱ्यांना प्रशासकीय जाब विचारला जाऊ शकतो.',
        'keywords': ['financial management', 'utilization certificate', 'uc', 'grant in aid', 'audit para', 'transparency', 'public money', 'head office']
    },
    {
        'id': 'M8',
        'module': 'MCED',
        'category': 'Job Role Awareness',
        'rubric': 'job_role',
        'q_en': 'How does an Account Assistant coordinate with District Project Officers, Training Coordinators, and the Head Office?',
        'q_mr': 'अकाउंट असिस्टंट म्हणून तुम्ही जिल्हा प्रकल्प अधिकारी, ट्रेनिंग कोऑर्डिनेटर्स आणि मुख्यालयाशी कसा समन्वय ठेवाल?',
        'q_hi': 'District Project Officer, Training Coordinators और Head Office के साथ आप समन्वय कैसे बनाएंगे?',
        'keyPoints': [
            'Training Coordinators: Guiding them beforehand on required bill formats, attendance sheets, and voucher requirements',
            'District Project Officer: Briefing on budget availability, pending bills, and obtaining necessary sanctions',
            'Head Office / Regional Office: Submitting monthly accounts, compliance replies, and resolving fund queries on time',
            'Maintaining professional, proactive and solution-oriented communication'
        ],
        'modelAnswer': 'मॅडम, अकाउंट्स हे वेगळे बेट नसून संपूर्ण कार्यालयाला जोडणारा दुवा आहे. मी खालीलप्रमाणे समन्वय ठेवेन:\n१. ट्रेनिंग कोऑर्डिनेटर्ससोबत: बॅच सुरू होण्यापूर्वीच त्यांना लागणारी कागदपत्रे (उदा. उपस्थिती पत्रके, मूळ जीएसटी बिले, फोटोग्राफ्स) कोणती लागतील याची स्पष्ट कल्पना देईन, जेणेकरून नंतर बिलांमध्ये त्रुटी येणार नाहीत.\n२. जिल्हा प्रकल्प अधिकाऱ्यांसोबत (DPO): रोजच्या पेमेंटची फायली मंजुरीसाठी मांडताना बजेट हेडमधील शिल्लक निधीची माहिती देईन आणि काही अडचण असल्यास त्यांच्या मार्गदर्शनाने तोडगा काढेन.\n३. मुख्यालयासोबत (Head Office): महिन्याच्या ५ तारखेच्या आत मासिक खर्चाचा अहवाल आणि BRS मुख्यालयाच्या फायनान्स विभागाला सादर करेन आणि त्यांच्याकडून आलेल्या कोणत्याही ऑडिट किंवा पडताळणी प्रश्नांची तात्काळ उत्तरे पाठवेन.',
        'commonMistakes': [
            'Sounding like an isolated record-keeper who only finds faults without guiding colleagues'
        ],
        'followUp': 'What should you do if a training coordinator finds it difficult to understand accounting voucher formats?',
        'followUpAnswer': 'मी शांतपणे आणि सहकार्याच्या भावनेने त्यांना नमुना व्हाउचर (Sample Voucher) दाखवेन आणि कोणते पेपर कुठे जोडायचे हे प्रत्यक्ष समजावून सांगेन.',
        'keywords': ['coordination', 'district project officer', 'training coordinator', 'head office', 'sample voucher', 'teamwork', 'communication']
    },

    # =========================================================================
    # PART 2: REAL-LIFE WORKPLACE SIMULATIONS & PRACTICAL JUDGEMENT (30% Weightage)
    # =========================================================================
    {
        'id': 'S1',
        'module': 'SITUATIONAL',
        'category': 'Workplace Simulation',
        'rubric': 'situational',
        'q_en': 'Workplace Scenario 1: A 15-day EDP training programme has just been completed at your District Centre. How will you systematically compile, verify, and maintain its complete expense records?',
        'q_mr': 'कार्यालयीन प्रसंग १: तुमच्या जिल्हा केंद्रात १५ दिवसांचा उद्योजकता प्रशिक्षण कार्यक्रम नुकताच संपला आहे. तुम्ही या कार्यक्रमाच्या खर्चाचे संपूर्ण रेकॉर्ड पद्धतशीरपणे कसे गोळा, तपासून आणि फाईल करून ठेवाल?',
        'q_hi': '15-दिवसीय प्रशिक्षण कार्यक्रम समाप्त होने पर आप उसके खर्चों का लेखा-जोखा कैसे तैयार और फाइल करेंगे?',
        'keyPoints': [
            'Step 1: Check administrative sanction and approved budget estimate for the batch',
            'Step 2: Collect all bills: Hall rent, Guest lecture honorarium/attendance, participant tea/refreshment, stationery, kit bags, banner/photography',
            'Step 3: Verify participant attendance register and completion list signed by coordinator',
            'Step 4: Verify GSTIN, PAN, and deduct TDS where applicable (e.g. 194J on guest lecturers)',
            'Step 5: Prepare batch-wise expenditure statement and compare with sanctioned limit',
            'Step 6: Submit for DPO signature, make payments via NEFT/cheque, and archive in a dedicated Batch Guard File'
        ],
        'modelAnswer': 'सर, १५ दिवसांचा कार्यक्रम संपल्यावर मी खालील पायऱ्यांनुसार काम करेन:\n१. सँक्शन तपासणे: त्या बॅचसाठी मुख्यालयाने किंवा शासनाने मंजूर केलेले मूळ बजेट आणि मंजुरी आदेश (Sanction Order) आधी फाईलमध्ये पाहीन.\n२. बिले गोळा करणे: हॉल भाडे, दररोजचे अल्पोपहार (Tea/Snacks) बिल, स्टेशनरी, बॅनर, फोटोग्राफ्स आणि गेस्ट लेक्चरर्सचे मानधन बिले गोळा करेन.\n३. अनिवार्य कागदपत्रे तपासणे: प्रत्येक बिलासोबत प्रशिक्षणार्थींची दररोजची हजेरी पत्रके (Attendance Sheets), व्हेंडरचे मूळ टॅक्स इन्व्हॉईस आणि स्टॉक रजिस्टरमधील नोंद जोडेन.\n४. टॅक्स व टीडीएस: नियमानुसार ट्रेनर्सच्या मानधनातून Section 194J नुसार आणि कंत्राटदाराच्या बिलातून 194C नुसार TDS वजा करेन.\n५. बॅच खर्चाचे विवरण: एका एक्सेल शीटमध्ये एकूण खर्च आणि मंजूर मर्यादा यांची तुलना करून बॅचनिहाय खर्चाचे विवरण तयार करेन.\n६. मंजुरी व फायलिंग: जिल्हा प्रकल्प अधिकाऱ्यांची अंतिम स्वाक्षरी घेऊन बँक ट्रान्सफर करेन आणि "Batch No. / Year" अशी स्वतंत्र फाईल तयार करून कपाटात सुरक्षित ठेवेन.',
        'commonMistakes': [
            'Forgetting to cross-verify participant attendance sheets with food/kit bills',
            'Missing TDS deduction on guest speaker fees'
        ],
        'followUp': 'Why is participant attendance sheet considered a critical financial supporting document for catering bills?',
        'followUpAnswer': 'कारण हजेरी पत्रकावरील उपस्थित विद्यार्थ्यांच्या संख्येवरूनच दररोज दिलेल्या चहा-नाश्त्याच्या प्लेट्सची संख्या बरोबर आहे की बिलात फुगवून दाखवली आहे हे ऑडिटला सिद्ध करता येते.',
        'keywords': ['batch file', 'sanction order', 'attendance sheet', 'hall rent', 'trainer honorarium', 'refreshment', 'tds 194j', 'batch expenditure']
    },
    {
        'id': 'S2',
        'module': 'SITUATIONAL',
        'category': 'Workplace Simulation',
        'rubric': 'situational',
        'q_en': 'Workplace Scenario 2: A senior officer or coordinator submits a bill of ₹8,500 for vehicle hire / field visit travel, but the log book and toll receipts are missing. What will you do?',
        'q_mr': 'कार्यालयीन प्रसंग २: एका अधिकाऱ्याने फिल्ड व्हिजिटसाठी ₹८,५०० चे वाहन भाड्याचे बिल सादर केले, परंतु त्यासोबत वाहनाचे लॉग बुक आणि टोल पावत्या जोडलेल्या नाहीत. तुम्ही काय पावले उचलाल?',
        'q_hi': 'वाहन किराए के बिल में लॉग बुक और टोल रसीदें न होने पर आप क्या करेंगे?',
        'keyPoints': [
            'What to do first: Politely explain standard audit requirement for travel reimbursement',
            'What documents to check: Vehicle tour approval, driver log book (starting/closing km), fuel/toll slips',
            'Whom to coordinate with: The officer concerned and DPO',
            'Approval status: Bill cannot be processed for payment without supporting proof',
            'Resolution: Request officer to attach the vehicle log sheet countersigned by the tour in-charge'
        ],
        'modelAnswer': 'मॅडम, अशा प्रसंगी माझी कृती खालीलप्रमाणे असेल:\n१. प्रथम काय करणार: मी बिल बाजूला ठेवून संबंधित अधिकाऱ्यांना अत्यंत आदरपूर्वक आणि नम्रपणे सांगेन की, "सर, लेखा परीक्षण (Audit) नियमांनुसार वाहन बिलासोबत वाहनाचा प्रवास तपशील (Log Book - सुरुवातीचे व शेवटचे किमी, प्रवासाचा उद्देश) आणि टोल पावत्या असणे अनिवार्य आहे, अन्यथा ऑडिटमध्ये रिकव्हरी निघू शकते."\n२. काय तपासणार: दौऱ्याची पूर्वमंजुरी (Tour Sanction) आणि लॉग बुकची पडताळणी करेन.\n३. मंजुरी: आवश्यक कागदपत्रे जोडल्याशिवाय मी हे बिल पेमेंटसाठी पुढे सादर करणार नाही.\n४. तोडगा: अधिकाऱ्यांना संबंधित गाडीचे लॉग शीट भरून स्वाक्षरीसह जोडून देण्याची विनंती करेन. कागदपत्रे पूर्ण झाल्यानंतरच व्हाउचर तयार करून वरिष्ठांच्या स्वाक्षरीसाठी मांडेन.',
        'commonMistakes': [
            'Approving the bill blindly out of fear of senior',
            'Being rude or shouting at the officer'
        ],
        'followUp': 'What if the officer insists: "Pass it today, I will give toll slips next week"?',
        'followUpAnswer': 'मी नम्रपणे सांगेन, "सर, एकदा चेक किंवा बँक ट्रान्सफर झाल्यावर अपूर्ण व्हाउचर ऑडिटच्या निशाण्यावर येते. कृपया कागदपत्रे जोडून द्या, मी तात्काळ एका तासात बिल प्रोसेस करतो."'
        ,
        'keywords': ['log book', 'toll receipts', 'travel bill', 'audit objection', 'polite explanation', 'supporting documents', 'tour sanction']
    },
    {
        'id': 'S3',
        'module': 'SITUATIONAL',
        'category': 'Workplace Simulation',
        'rubric': 'situational',
        'q_en': 'Workplace Scenario 3: The sanctioned administrative approval for printing training booklets is ₹15,000, but the submitted printing bill is ₹17,800. How will you handle this?',
        'q_mr': 'कार्यालयीन प्रसंग ३: प्रशिक्षण पुस्तके छपाईसाठी प्रशासकीय मंजुरी ₹१५,००० ची आहे, परंतु प्रिंटरने प्रत्यक्ष ₹१७,८०० चे बिल दिले आहे. तुम्ही हे कसे हाताळाल?',
        'q_hi': 'स्वीकृत राशि ₹15,000 है लेकिन बिल ₹17,800 का आया है। आप इसे कैसे संभालेंगे?',
        'keyPoints': [
            'Rule: No payment can exceed sanctioned budget without revised sanction',
            'What to do first: Verify why amount increased (Did quantity increase or extra pages added?)',
            'What to record: Difference of ₹2,800 excess',
            'Whom to coordinate with: Printing coordinator and District Project Officer',
            'Approval requirement: Revised / Ex-post facto sanction required from competent authority before paying excess amount'
        ],
        'modelAnswer': 'सर, अकाउंटिंगच्या नियमांनुसार मंजूर मर्यादेपेक्षा (Sanctioned Limit) एका रुपयाचेही जास्त पेमेंट थेट करता येत नाही.\nमाझी कृती:\n१. पडताळणी: मी बिलातील संख्या आणि दर तपासेन. छपाईची पुस्तके वाढली होती का, पाने वाढली होती की व्हेंडरने दर जास्त लावला आहे हे शोधेन.\n२. वरिष्ठांना अवगत करणे: मी जिल्हा प्रकल्प अधिकाऱ्यांच्या निदर्शनास आणून देईन की बिल मंजूर रकमेपेक्षा ₹२,८०० ने जास्त आहे.\n३. पर्याय: जर अतिरिक्त छपाई खरोखर आवश्यक होती आणि कार्यालयाच्या आदेशाने झाली असेल, तर सक्षम अधिकाऱ्यांकडून ₹२,८०० साठी अतिरिक्त प्रशासकीय मंजुरी (Revised Sanction / Ex-post facto approval) घ्यावी लागेल.\n४. जोपर्यंत सुधारित मंजुरी मिळत नाही, तोपर्यंत नियमानुसार मूळ मंजूर रकमेएवढेच (₹१५,०००) पेमेंट करता येईल किंवा संपूर्ण मंजुरी आल्यावरच पूर्ण बिल पास केले जाईल.',
        'commonMistakes': [
            'Processing the full ₹17,800 without revised sanction',
            'Arbitrarily cutting vendor payment without checking reasons'
        ],
        'followUp': 'Can a District Account Assistant approve the excess amount of ₹2,800 on their own authority?',
        'followUpAnswer': 'नाही सर, कोणत्याही आर्थिक वाढीला मंजुरी देण्याचा अधिकार फक्त सक्षम प्रशासकीय अधिकाऱ्याला असतो; अकाउंट असिस्टंट फक्त तफावत निदर्शनास आणू शकते.',
        'keywords': ['sanctioned limit', 'excess bill', 'revised sanction', 'ex-post facto approval', 'verification', 'dpo approval', 'arithmetical check']
    },
    {
        'id': 'S4',
        'module': 'SITUATIONAL',
        'category': 'Workplace Simulation',
        'rubric': 'situational',
        'q_en': 'Workplace Scenario 4: While scrutinizing payment requests, you discover that an invoice of ₹12,000 from a stationery supplier has already been processed and paid last month. What are your exact steps?',
        'q_mr': 'कार्यालयीन प्रसंग ४: बिलांची छाननी करताना तुमच्या लक्षात आले की एका स्टेशनरी व्हेंडरचे ₹१२,००० चे जे बिल आले आहे, तेच बिल गेल्या महिन्यात आधीच पास होऊन त्याचे पेमेंट झाले आहे. तुम्ही नेमके काय कराल?',
        'q_hi': 'यदि वही बिल दोबारा भुगतान के लिए प्रस्तुत हुआ है, तो आप क्या कदम उठाएंगे?',
        'keyPoints': [
            'Immediate alert: Stop any further processing of the duplicate bill',
            'Trace the earlier payment: Find earlier voucher number, date, cheque/UTR number, and bank statement entry',
            'Cross-examine physical invoice: Check if it is a duplicate/photocopy or same invoice number',
            'Report in writing to the District Project Officer with proof of earlier payment',
            'Action with vendor: Politely return the duplicate invoice with earlier payment details; check if genuine clerical error or foul play',
            'Preventive measure: Mark physical bills "PAID & CANCELLED" immediately upon payment'
        ],
        'modelAnswer': 'मॅडम, हा एक गंभीर प्रकार असू शकतो. माझी तत्काळ पावले खालीलप्रमाणे असतील:\n१. तात्काळ थांबवणे: त्या बिलाची कोणतीही पुढील प्रक्रिया किंवा व्हाउचर बनवणे त्वरित थांबवेन.\n२. आधीच्या नोंदी शोधणे: गेल्या महिन्यातील लेजर, कॅश बुक आणि व्हाउचर फाईल उघडून त्या बिलाचा व्हाउचर क्रमांक, पेमेंटची तारीख आणि बँक UTR क्रमांक शोधून त्याची प्रत काढेन.\n३. वरिष्ठांना अहवाल: दोन्ही कागदपत्रे सोबत जोडून जिल्हा प्रकल्प अधिकाऱ्यांच्या (DPO) निदर्शनास लेखी स्वरूपात आणेन की हे बिल आधीच या तारखेला अदा करण्यात आले आहे.\n४. व्हेंडरशी संपर्क: व्हेंडरला अधिकृत पत्र किंवा मेलद्वारे कळवले जाईल की सदर बिलाचे पेमेंट आधीच झाले आहे. नजरचुकीने पुन्हा बिल आले आहे का याची खात्री केली जाईल.\n५. प्रतिबंधात्मक उपाय: कार्यालयात असा प्रकार पुन्हा घडू नये म्हणून प्रत्येक बिलावर पेमेंट होताच मोठ्या लाल अक्षरात "PAID & CANCELLED" असा शिक्का मारण्याची शिस्त कडक ठेवेन.',
        'commonMistakes': [
            'Quietly throwing the bill in dustbin without informing the officer',
            'Passing the bill without checking past records'
        ],
        'followUp': 'How does maintaining a Vendor-wise Bill Register or Excel tracker prevent duplicate payments?',
        'followUpAnswer': 'एक्सेल ट्रॅकरमध्ये व्हेंडरच्या इनव्हॉईस नंबरचा कॉलम असतो. Data Validation किंवा COUNTIF फॉर्म्युला लावला तर तोच इनव्हॉईस नंबर पुन्हा टाईप करताच सिस्टीम तात्काळ एरर दाखवते.',
        'keywords': ['duplicate bill', 'stop processing', 'trace earlier voucher', 'utr proof', 'report to dpo', 'paid and cancelled', 'bill register']
    },
    {
        'id': 'S5',
        'module': 'SITUATIONAL',
        'category': 'Workplace Simulation',
        'rubric': 'situational',
        'q_en': 'Workplace Scenario 5: Head Office or the Regional Officer demands the Monthly Financial Expenditure Statement by 5:00 PM today, but two trainer bills are still pending verification. How will you manage this deadline without sacrificing accuracy?',
        'q_mr': 'कार्यालयीन प्रसंग ५: मुख्यालय किंवा विभागीय कार्यालयाने आज संध्याकाळी ५ वाजेपर्यंत मासिक खर्चाचे विवरण मागितले आहे, परंतु दोन ट्रेनर्सची बिले अजून पडताळणी बाकी आहेत. अचूकता न गमावता तुम्ही ही डेडलाईन कशी सांभाळाल?',
        'q_hi': 'आज शाम तक मासिक व्यय विवरण भेजना अनिवार्य है लेकिन दो बिल लंबित हैं। आप इसे कैसे संभालेंगे?',
        'keyPoints': [
            'Principle: Never include unverified or unapproved expenses in actual cash/expenditure statements',
            'Prioritize: Complete verified transactions up to yesterday/today immediately',
            'Quick action: Immediately contact training coordinator for missing verification papers for those 2 bills',
            'Transparency in report: If bills cannot be verified by 4:00 PM, submit the statement with actual booked expenditures, and add a clear footnote of "Pending / Outstanding liabilities"',
            'Communicate with DPO before emailing Head Office'
        ],
        'modelAnswer': 'सर, अशा वेळी घाईगडबडीत न तपासलेले बिल खर्चात दाखवणे किंवा चुकीचा रिपोर्ट पाठवणे दोन्ही ऑडिटच्या दृष्टीने धोकादायक ठरेल.\nमाझी कृती:\n१. त्वरित समन्वय (Immediate Action): दुपारी २ वाजेपर्यंत मी संबंधित ट्रेनिंग कोऑर्डिनेटरशी संपर्क साधून त्या दोन बिलांची अपूर्ण कागदपत्रे तात्काळ पूर्ण करून घेण्याचा प्रयत्न करेन.\n२. जर कागदपत्रे ४ वाजेपर्यंत मिळाली नाहीत: तर शासकीय अकाउंटिंगच्या नियमांनुसार जे खर्च प्रत्यक्षात पूर्ण तपासले आहेत आणि ज्यांचे पेमेंट झाले आहे, तेवढाच प्रत्यक्ष खर्च (Actual Expenditure) स्टेटमेन्टमध्ये दाखवेन.\n३. फुटनोट / शेरा: स्टेटमेन्टच्या खाली स्पष्ट टीप (Footnote) लिहीन: "Note: Two trainer bills totaling ₹X are under scrutiny and will be included in the next period upon approval."\n४. वरिष्ठांची मान्यता: हा अहवाल जिल्हा प्रकल्प अधिकाऱ्यांना दाखवून त्यांच्या स्वाक्षरीने संध्याकाळी ५ च्या आत मुख्यालयाला पाठवून देईन. यामुळे डेडलाईनही पाळली जाईल आणि रिपोर्टही १००% खरा राहील.',
        'commonMistakes': [
            'Booking unverified bills in accounts to show more expenditure',
            'Missing the deadline without informing anyone'
        ],
        'followUp': 'Why is adding a clear footnote better than delaying the entire financial report?',
        'followUpAnswer': 'कारण मुख्यालयाला संपूर्ण राज्याचा एकत्रित ताळेबंद करायचा असतो. अहवाल वेळेवर गेल्याने त्यांचे काम थांबत नाही आणि फुटनोटमुळे खरी परिस्थितीही समोर राहते.',
        'keywords': ['monthly expenditure statement', 'deadline', 'unverified bills', 'footnote', 'transparency', 'actual expenditure', 'dpo signature']
    },
    {
        'id': 'S6',
        'module': 'SITUATIONAL',
        'category': 'Workplace Simulation',
        'rubric': 'situational',
        'q_en': 'Workplace Scenario 6: At the end of the day, physical cash in the office cash box is ₹4,200, but the Cash Book closing balance shows ₹4,700 (a shortfall of ₹500). What are your immediate and next-day steps?',
        'q_mr': 'कार्यालयीन प्रसंग ६: दिवसअखेर कार्यालयाच्या कॅश बॉक्समध्ये प्रत्यक्ष रोख रक्कम ₹४,२०० भरली, परंतु कॅश बुकची शिल्लक ₹४,७०० दाखवत आहे (₹५०० ची तूट). तुमची आजची आणि उद्याची नेमकी कृती काय असेल?',
        'q_hi': 'कैश बॉक्स में ₹500 की कमी पाई गई। आपकी आज की और कल की क्या कार्रवाई होगी?',
        'keyPoints': [
            'Golden Ethical Rule: Never put personal money from purse to hide the shortfall',
            'Immediate step: Re-total cash book columns, check today’s receipt & payment vouchers',
            'Check unrecorded petty expenses (e.g. postage, courier, tea paid in afternoon)',
            'Report immediately to District Project Officer',
            'Record actual counted cash in Daily Cash Register with officer countersignature',
            'Next day: Systematic investigation; if genuinely untraceable, record according to official procedure under Cash Shortage'
        ],
        'modelAnswer': 'मॅडम, अकाउंट्समध्ये प्रामाणिकपणा सर्वात महत्त्वाचा असतो. मी माझ्या स्वतःच्या खिशातून ₹५०० टाकून तूट कधीही लपवणार नाही.\nआजची तात्काळ कृती:\n१. फेरपडताळणी: आजच्या सर्व रिसिट आणि पेमेंट व्हाउचर्सची बेरीज पुन्हा करेन. दिवसभरात चहा-नाश्ता किंवा कुरिअरचा काही किरकोळ खर्च झाला आहे का आणि त्याचे व्हाउचर लिहायचे राहिले आहे का ते पाहीन.\n२. अधिकाऱ्यांना माहिती: तूट कायम असल्यास लगेच जिल्हा प्रकल्प अधिकाऱ्यांना (DPO) प्रत्यक्ष परिस्थिती सांगेन.\n३. नोंद व स्वाक्षरी: कॅश रजिस्टरमध्ये "प्रत्यक्ष मोजलेली कॅश ₹४,२००, पुस्तकी शिल्लक ₹४,७००, तूट ₹५००" असा शेरा लिहून अधिकाऱ्यांची स्वाक्षरी घेईन आणि कॅश बॉक्स कुलूपबंद करेन.\nदुसऱ्या दिवसाची कृती:\nसकाळी आदल्या दिवसाच्या प्रत्येक व्यवहाराचा बँक आणि पावत्यांशी ताळेबंद घालेन. तरीही चूक न सापडल्यास अधिकाऱ्यांच्या अधिकृत आदेशानुसार पुढील योग्य प्रशासकीय नोंद करेन.',
        'commonMistakes': [
            'Putting personal money to cover the gap (grave ethical and audit offense)',
            'Tampering with cash book totals to match the physical cash'
        ],
        'followUp': 'What should be done if the reverse happens—physical cash is ₹500 MORE than the cash book?',
        'followUpAnswer': 'अधिकची रक्कमही स्वतःकडे न ठेवता कॅश बॉक्समध्येच ठेवली जाईल, रजिस्टरमध्ये नोंद करून वरिष्ठांच्या लक्षात आणून दिली जाईल आणि कोणत्या पावतीची नोंद करायची राहिली आहे का याचा शोध घेतला जाईल.',
        'keywords': ['cash shortage', 'no personal money', 're-verification', 'petty expense check', 'dpo reporting', 'cash register signature', 'integrity']
    },
    {
        'id': 'S7',
        'module': 'SITUATIONAL',
        'category': 'Workplace Simulation',
        'rubric': 'situational',
        'q_en': 'Workplace Scenario 7: The sanctioned budget for "Training Refreshment" in your district is almost 95% exhausted, but an officer brings a bill for an upcoming new batch. What will you do?',
        'q_mr': 'कार्यालयीन प्रसंग ७: तुमच्या जिल्ह्यातील "प्रशिक्षण अल्पोपहार" (Refreshment) या हेडखालील मंजूर बजेट ९५% संपले आहे, तरीही एका नवीन बॅचसाठी खर्चाची मागणी आली आहे. तुम्ही काय कराल?',
        'q_hi': 'बजट 95% समाप्त हो चुका है और नए बैच का खर्च सामने आया है। आप क्या करेंगे?',
        'keyPoints': [
            'Financial discipline: An office cannot commit expenditure beyond available sanctioned grant',
            'What to do first: Check Budget Register for exact remaining unspent balance',
            'Whom to coordinate with: District Project Officer and Training Coordinator',
            'Can you divert funds from another head (e.g. Travel) on your own? NO, unauthorized diversion is illegal',
            'Resolution: Prepare a formal request note for additional budget allocation / re-appropriation to Head Office'
        ],
        'modelAnswer': 'सर, आर्थिक शिस्तीनुसार बजेट संपलेले असताना नवीन खर्च परस्पर करणे किंवा दुसऱ्या हेडचा निधी (उदा. प्रवास खर्च) परस्पर इकडे वळवणे (Diversion of Funds) पूर्णपणे बेकायदेशीर आहे.\nमाझी कृती:\n१. बजेट तपासणे: मी बजेट रजिस्टर उघडून नेमकी किती रक्कम शिल्लक आहे (फक्त ५%) हे पाहीन.\n२. अधिकाऱ्यांना लेखी कल्पना: मी जिल्हा प्रकल्प अधिकाऱ्यांना (DPO) ताळेबंद दाखवून सांगेन की, "सर, या हेडखाली आता नवीन बॅचचा खर्च भागवणे शक्य नाही."\n३. प्रस्ताव तयार करणे: मुख्यालयाकडे (Head Office) तात्काळ अतिरिक्त निधी मिळण्यासाठी (Additional Grant / Re-appropriation) प्रस्ताव किंवा पत्र तयार करेन.\n४. जोपर्यंत मुख्यालयाकडून अतिरिक्त निधी मंजूर होत नाही, तोपर्यंत व्हेंडरला नवीन कमिटमेंट किंवा पेमेंटचे आश्वासन दिले जाणार नाही.',
        'commonMistakes': [
            'Diverting money from another budget head without Head Office approval',
            'Processing the bill into negative budget'
        ],
        'followUp': 'What is "Re-appropriation of funds" in government budgeting?',
        'followUpAnswer': 'एका बजेट हेडमध्ये बचत झाली असल्यास ती रक्कम दुसऱ्या तुटवडा असलेल्या हेडकडे वळवण्यासाठी सक्षम प्राधिकाऱ्याकडून (Head Office) घेतली जाणारी अधिकृत मंजुरी.',
        'keywords': ['budget exhausted', 'budget register', 'no fund diversion', 're-appropriation', 'additional grant', 'head office proposal']
    },
    {
        'id': 'S8',
        'module': 'SITUATIONAL',
        'category': 'Workplace Simulation',
        'rubric': 'situational',
        'q_en': 'Workplace Scenario 8: During a statutory audit inspection, the audit officer demands the original bill and tender quotations for office furniture purchased 3 years ago. What will you do?',
        'q_mr': 'कार्यालयीन प्रसंग ८: वैधानिक लेखापरीक्षणादरम्यान (Audit) ऑडिट अधिकाऱ्यांनी ३ वर्षांपूर्वी खरेदी केलेल्या ऑफिस फर्निचरचे मूळ बिल आणि कोटेशन्सची मागणी केली. तुम्ही हे कसे हाताळाल?',
        'q_hi': 'ऑडिट के दौरान 3 साल पुराने फर्नीचर बिल और कोटेशन मांगे जाने पर आप क्या करेंगे?',
        'keyPoints': [
            'Preservation of records: Financial records in government bodies must be maintained as per retention schedule (usually 8-10 years)',
            'Action: Stay calm, check the Voucher Index / Record Register for that financial year',
            'Retrieve the relevant Voucher Guard File from the record room',
            'Verify Deadstock / Asset Register page number where the furniture was recorded',
            'Present the documents politely and properly before the audit team'
        ],
        'modelAnswer': 'मॅडम, शासकीय आणि स्वायत्त संस्थांमध्ये आर्थिक नोंदी आणि व्हाउचर्स किमान ८ ते १० वर्षे सुरक्षित ठेवणे बंधनकारक असते.\nमाझी कृती:\n१. शांत राहणे व शोध घेणे: घाबरून न जाता, मी त्या आर्थिक वर्षाचे (उदा. २०२३-२४) व्हाउचर्स इंडेक्स रजिस्टर पाहीन.\n२. गार्ड फाईल काढणे: रेकॉर्ड रूममधील संबंधित महिन्याची व्हाउचर गार्ड फाईल शोधून त्यातील मूळ टॅक्स इन्व्हॉईस, ३ कोटेशन्स आणि तुलनात्मक तक्ता (Comparative Statement) काढून घेईन.\n३. डेडस्टॉक रजिस्टर: सोबतच कार्यालयाचे डेडस्टॉक रजिस्टर (Deadstock / Fixed Asset Register) काढून, त्यावर त्या फर्निचरची झालेली नोंद आणि पेज नंबर दाखवेन.\n४. ऑडिट टीमसमोर सादरीकरण: सर्व कागदपत्रे नम्रतेने ऑडिट अधिकाऱ्यांसमोर सादर करेन. जर फाईल शोधायला थोडा वेळ लागत असेल, तर अधिकाऱ्यांना नम्रपणे विनंती करून थोडा वेळ मागेन, पण शोधून नक्की सादर करेन.',
        'commonMistakes': [
            'Saying "It was before my joining so I am not responsible"',
            'Arguing with the auditor that 3-year-old records are not needed'
        ],
        'followUp': 'What is a Deadstock Register?',
        'followUpAnswer': 'कार्यालयाने खरेदी केलेल्या सर्व कायमस्वरूपी मालमत्तांची (फर्निचर, कॉम्प्युटर, कपाट, प्रिंटर) तपशीलवार नोंद ठेवणारे अधिकृत मालमत्ता रजिस्टर.',
        'keywords': ['audit inspection', 'record retention', 'voucher guard file', 'deadstock register', 'comparative statement', 'quotations', 'polite presentation']
    },
    {
        'id': 'S9',
        'module': 'SITUATIONAL',
        'category': 'Workplace Simulation',
        'rubric': 'situational',
        'q_en': 'Workplace Scenario 9: A training participant or guest speaker angrily complains about a 2-month delay in receiving their travel reimbursement or honorarium. How will you respond?',
        'q_mr': 'कार्यालयीन प्रसंग ९: एका प्रशिक्षणार्थीने किंवा पाहुण्या वक्त्याने त्यांचे २ महिन्यांपासून प्रलंबित असलेले प्रवास भाडे किंवा मानधन न मिळाल्याबद्दल कार्यालयात येऊन संतापाने तक्रार केली. तुम्ही काय प्रतिसाद द्याल?',
        'q_hi': 'मानदेय में देरी से नाराज प्रतिभागी या वक्ता को आप कैसे शांत करेंगे और क्या कदम उठाएंगे?',
        'keyPoints': [
            'Calm, respectful, patient public dealing attitude',
            'Listen without arguing or being defensive',
            'Check the bill status in payment tracker: Was it received? Was bank detail incorrect? Was fund awaited from Head Office?',
            'Explain the exact factual status transparently and give a realistic resolution timeframe',
            'Expedite the pending voucher with the officer'
        ],
        'modelAnswer': 'सर, अशा वेळी मी स्वतः शांत राहीन आणि त्यांचा राग समजून घेईन. जनतेशी आणि पाहुण्यांशी संवाद साधताना संयम अत्यंत आवश्यक असतो.\nमाझी कृती:\n१. आदरपूर्वक ऐकून घेणे: मी त्यांना बसायला सांगेन, पाणी देईन आणि त्यांची अडचण शांतपणे ऐकून घेईन. वाद घालणार नाही.\n२. स्टेटस तपासणे: त्यांचे नाव, बॅच नंबर आणि बँक खात्याचा तपशील घेऊन माझ्या पेमेंट ट्रॅकरमध्ये तपासेन की बिल कोणत्या टप्प्यावर अडकले आहे (उदा. बँक खाते क्रमांक चुकीचा होता का, की मुख्यालयाकडून त्या बॅचचा निधी जमा व्हायचा बाकी होता).\n३. वस्तुस्थिती सांगणे: त्यांना खोटे आश्वासन न देता खरी परिस्थिती नम्रपणे समजावून सांगेन.\n४. पाठपुरावा: जर कागदपत्रांची पूर्तता असेल, तर जिल्हा प्रकल्प अधिकाऱ्यांशी बोलून तात्काळ पुढील २-३ दिवसांत त्यांचे पेमेंट बँक ट्रान्सफरने होईल याची जबाबदारी घेऊन त्यांना तसे आश्वस्त करेन.',
        'commonMistakes': [
            'Arguing back or shouting "I am busy, come later"',
            'Passing the blame vaguely without checking the records'
        ],
        'followUp': 'Why is public dealing and polite behavior equally important for an Account Assistant?',
        'followUpAnswer': 'कारण अकाउंट असिस्टंट हा कार्यालयाचा चेहरा असतो. आपल्या चुकीच्या वागण्यामुळे MCED या संस्थेची प्रतिष्ठा पणाला लागू शकते; नम्र आणि कार्यक्षम सेवेमुळे लोकांचा संस्थेवर विश्वास वाढतो.',
        'keywords': ['public dealing', 'patient listening', 'payment tracker check', 'factual explanation', 'empathy', 'expedited resolution', 'professionalism']
    },
    {
        'id': 'S10',
        'module': 'SITUATIONAL',
        'category': 'Workplace Simulation',
        'rubric': 'situational',
        'q_en': 'Workplace Scenario 10: A senior officer verbally instructs you to issue a cheque of ₹25,000 for event decorations immediately, promising to submit the quotation and approval papers tomorrow. How will you handle this respectfully without violating financial rules?',
        'q_mr': 'कार्यालयीन प्रसंग १०: वरिष्ठ अधिकाऱ्यांनी तुम्हाला कार्यक्रमाच्या डेकोरेशनसाठी ₹२५,००० चा चेक लगेच द्यायला तोंडी सांगितले आणि म्हटले की, "कोटेशन व मंजुरीची कागदपत्रे मी उद्या देतो." आर्थिक नियमांचे उल्लंघन न करता तुम्ही हे आदराने कसे हाताळाल?',
        'q_hi': 'वरिष्ठ अधिकारी द्वारा बिना कागजात के तत्काल ₹25,000 का चेक जारी करने का मौखिक आदेश मिलने पर आप क्या करेंगे?',
        'keyPoints': [
            'Rule: No cheque can be drawn without a sanctioned payment voucher and supporting bills',
            'Tone: Extremely respectful, humble, but firm on audit rules',
            'Remind senior about joint financial responsibility and audit objection risk',
            'Solution: Offer to prepare an Advance Voucher if permitted under rules with officer’s written note sheet approval, OR urgently prepare voucher as soon as basic sanction is signed'
        ],
        'modelAnswer': 'मॅडम, हा अतिशय संवेदनशील प्रसंग आहे. मी उद्धट न होता वरिष्ठांचा आदर राखून अधिकृत नियम समजावून सांगेन.\nमाझी कृती:\n१. नम्रपणे समजावणे: मी साहेबांना एकांतात आदराने सांगेन, "सर, लेखा नियमांनुसार आणि बँक नियमांनुसार मंजूर व्हाउचर आणि सपोर्टिंगशिवाय थेट चेक लिहिल्यास ऑडिटमध्ये ही थेट अनियमितता (Severe Irregularity) ठरते आणि आपणा दोघांवरही जबाबदारी येऊ शकते."\n२. व्यावहारिक पर्याय: जर कार्यक्रम आजच आहे आणि खरोखर तातडी असेल, तर मी त्यांना सांगेन, "सर, आपण व्हेंडरला पेमेंट करण्याऐवजी आपल्या नावाने अधिकृत ॲडव्हान्स (Advance Note Sheet) मंजूर करून द्या; मी ॲडव्हान्स व्हाउचर बनवून देतो. नंतर उद्या बिल आल्यावर आपण ते ॲडजस्ट करू."\n३. लेखी आदेशाशिवाय किंवा अधिकृत व्हाउचरशिवाय मी कोरा किंवा कागदपत्रांशिवाय चेक काढणार नाही.',
        'commonMistakes': [
            'Aggressively challenging the boss in front of everyone',
            'Blindly signing/issuing the cheque without any paper trail'
        ],
        'followUp': 'What is the role of a "Note Sheet" in government office decision making?',
        'followUpAnswer': 'नोटशीट हे अधिकृत निर्णयाचे लेखी पान असते, ज्यावर कारकुनापासून ते अधिकाऱ्यापर्यंत सर्वांच्या स्वाक्षऱ्या आणि नियमांचे संदर्भ नोंदवून लेखी मंजुरी घेतली जाते.',
        'keywords': ['verbal instruction', 'no cheque without voucher', 'respectful explanation', 'audit irregularity', 'note sheet', 'advance voucher', 'integrity']
    },
    {
        'id': 'S11',
        'module': 'SITUATIONAL',
        'category': 'Workplace Simulation',
        'rubric': 'situational',
        'q_en': 'Workplace Scenario 11: After emailing the quarterly expenditure statement to Head Office, you discover a formula error in Excel that under-reported expenditure by ₹10,000. What is your immediate next step?',
        'q_mr': 'कार्यालयीन प्रसंग ११: मुख्यालयाला त्रैमासिक खर्चाचा अहवाल ईमेलने पाठवल्यानंतर तुमच्या लक्षात आले की एक्सेल फॉर्म्युल्याच्या चुकीमुळे ₹१०,००० चा खर्च कमी दाखवला गेला आहे. तुमचे तत्काळ पाऊल काय असेल?',
        'q_hi': 'रिपोर्ट भेजने के बाद ₹10,000 की फॉर्मूला त्रुटि का पता चलने पर आप तुरंत क्या करेंगे?',
        'keyPoints': [
            'Never hide the mistake or wait for Head Office to catch it',
            'Inform the District Project Officer immediately with the correct figures',
            'Prepare a Revised Financial Statement highlighting the corrected formula and row',
            'Send an official revised email with DPO approval clearly explaining the inadvertent formula error'
        ],
        'modelAnswer': 'सर, चूक लपवण्याचा प्रयत्न केल्यास भविष्यात ऑडिटमध्ये जास्त अडचण येते. स्वतःहून चूक वेळेवर सुधारणे हीच खरी व्यावसायिकता आहे.\nमाझी कृती:\n१. तातडीने चूक दुरुस्त करणे: मी लगेच मूळ एक्सेल फाईलमध्ये फॉर्म्युला दुरुस्त करून योग्य आकडा असलेला सुधारित अहवाल (Revised Statement) तयार करेन.\n२. अधिकाऱ्यांच्या निदर्शनास आणणे: मी स्वतः जिल्हा प्रकल्प अधिकाऱ्यांना सांगेन की, "सर, फॉर्म्युल्यातील तांत्रिक चुकीमुळे ₹१०,००० चा फरक राहिला होता, मी तो दुरुस्त केला आहे."\n३. मुख्यालयाला ईमेल: अधिकाऱ्यांच्या मंजुरीने मुख्यालयाच्या फायनान्स विभागाला तात्काळ एक सुधारित ईमेल पाठवेन, ज्याचा विषय असेल: "Corrigendum / Revised Quarterly Statement for District X".\n४. आत्मपरीक्षण: भविष्यात अहवाल पाठवण्यापूर्वी मी मॅन्युअल क्रॉस-टोटलिंग करून फॉर्म्युले दोनदा तपासेन.',
        'commonMistakes': [
            'Staying silent and hoping nobody notices',
            'Blaming Microsoft Excel instead of taking personal responsibility'
        ],
        'followUp': 'Why is sending a prompt corrigendum appreciated by senior accounts officers?',
        'followUpAnswer': 'कारण त्यामुळे मुख्यालयाचा एकत्रित ताळेबंद वेळेत सुधारला जातो आणि कर्मचाऱ्याचा प्रामाणिकपणा व जबाबदार वृत्ती दिसून येते.',
        'keywords': ['formula error', 'immediate disclosure', 'revised statement', 'corrigendum email', 'dpo approval', 'responsibility', 'cross verification']
    },
    {
        'id': 'S12',
        'module': 'SITUATIONAL',
        'category': 'Workplace Simulation',
        'rubric': 'situational',
        'q_en': 'Workplace Scenario 12: At 4:00 PM, the District Project Officer asks you to prepare an urgent audit reply, while a visiting Regional Officer asks you to compile a batch expenditure sheet right away. How will you prioritize and communicate?',
        'q_mr': 'कार्यालयीन प्रसंग १२: दुपारी ४ वाजता जिल्हा प्रकल्प अधिकाऱ्यांनी तुम्हाला तातडीचे ऑडिट उत्तर तयार करायला सांगितले, त्याच वेळी भेटीवर आलेल्या विभागीय अधिकाऱ्यांनी (Regional Officer) लगेच बॅच खर्चाची शीट मागितली. तुम्ही प्राधान्य कसे ठरवाल आणि कसा संवाद साधाल?',
        'q_hi': 'दो वरिष्ठ अधिकारियों द्वारा एक ही समय पर आवश्यक कार्य सौंपे जाने पर आप प्राथमिकता कैसे तय करेंगे?',
        'keyPoints': [
            'Do not panic or complain about overload',
            'Assess the exact deadline and time required for both tasks',
            'Transparent communication: Bring both tasks politely to the attention of both officers',
            'Let the senior officers decide the relative priority or offer a realistic schedule (e.g. Task 1 by 4:45 PM, Task 2 by 5:30 PM)'
        ],
        'modelAnswer': 'मॅडम, अशा वेळी गोंधळून न जाता मी अत्यंत नम्र आणि पारदर्शक संवाद ठेवेन:\n१. वेळेचा अंदाज घेणे: मी पाहीन की दोन्ही कामांसाठी नेमका किती वेळ लागेल.\n२. पारदर्शक संवाद: मी विभागीय अधिकाऱ्यांना (RO) आदरपूर्वक सांगेन की, "सर, मी आत्ताच जिल्हा प्रकल्प अधिकाऱ्यांच्या सूचनेनुसार आजच्या ऑडिट उत्तरावर काम करत आहे. मी हे काम ४:४० पर्यंत पूर्ण करून लगेच आपली बॅच शीट ५:१५ पर्यंत पूर्ण करून देऊ का?"\n३. अधिकाऱ्यांमध्ये समन्वय: गरज पडल्यास मी जिल्हा प्रकल्प अधिकाऱ्यांनाही सांगून ठेवेन की विभागीय साहेबांनीही हे काम दिले आहे. अधिकारी आपापसात ठरवून मला प्राधान्य सांगतील.\n४. जबाबदारी पूर्ण करणे: थोडे जास्तीचे थांबून दोन्ही कामे अचूकतेने पूर्ण करूनच कार्यालय सोडेन.',
        'commonMistakes': [
            'Saying "No, I will not do it" to either officer',
            'Accepting both silently and failing to deliver either on time'
        ],
        'followUp': 'What is the best way to handle multiple deadlines in daily office work?',
        'followUpAnswer': 'एका छोट्या डायरीत किंवा टू-डू लिस्टवर कामांची निकड (Urgency) आणि महत्त्व (Importance) लिहून एकाग्रतेने एक-एक काम संपवणे.',
        'keywords': ['conflicting priorities', 'transparent communication', 'time estimate', 'respectful coordination', 'to-do list', 'professionalism']
    },
    {
        'id': 'S13',
        'module': 'SITUATIONAL',
        'category': 'Workplace Simulation',
        'rubric': 'situational',
        'q_en': 'Workplace Scenario 13: A colleague from another department or a friend asks you to show the confidential quotation rates of vendors who applied for a catering tender. How will you respond?',
        'q_mr': 'कार्यालयीन प्रसंग १३: दुसऱ्या विभागातील सहकाऱ्याने किंवा ओळखीच्या मित्राने केटरिंग टेंडरसाठी आलेल्या व्हेंडर्सचे गोपनीय कोट्स आणि दर पाहण्यासाठी मागितले. तुम्ही काय प्रतिसाद द्याल?',
        'q_hi': 'किसी सहकर्मी द्वारा टेंडर की गोपनीय दरें मांगने पर आप क्या प्रतिक्रिया देंगे?',
        'keyPoints': [
            'Tender rates, quotations and financial bids are strictly official and confidential before official opening and sanction',
            'Polite, respectful but firm refusal',
            'Explain official code of conduct and integrity rules',
            'Advise them to follow official procedure if information is officially required'
        ],
        'modelAnswer': 'सर, मी कोणत्याही दबावाला किंवा मैत्रीला बळी न पडता अतिशय स्पष्ट आणि नम्र शब्दात नकार देईन.\nमी त्यांना सांगेन: "मित्रा/सहकारी, टेंडरचे कोटेशन्स आणि आर्थिक दर हे टेंडर उघडेपर्यंत आणि अधिकृत मंजुरी मिळेपर्यंत अत्यंत गोपनीय (Strictly Confidential) असतात. ही माहिती अनधिकृतपणे कोणालाही दाखवणे शासकीय नियमांचा आणि माझ्या व्यावसायिक सचोटीचा (Integrity) गंभीर भंग ठरेल. त्यामुळे मी ही माहिती दाखवू शकत नाही."\nजर त्यांना काही अधिकृत काम असेल, तर त्यांनी जिल्हा प्रकल्प अधिकाऱ्यांची रीतसर लेखी परवानगी आणावी, त्यानंतरच अधिकृत प्रक्रिया केली जाईल.',
        'commonMistakes': [
            'Sharing the data because the person is an office colleague',
            'Being unnecessarily rude and creating a personal fight'
        ],
        'followUp': 'Why is maintaining secrecy of financial bids essential for public procurement?',
        'followUpAnswer': 'कारण दर आधीच बाहेर पडल्यास स्पर्धा संपते, मर्जीतील व्हेंडरला फायदा मिळवून दिला जाऊ शकतो आणि संस्थेचे मोठे आर्थिक नुकसान होऊन पारदर्शकता नष्ट होते.',
        'keywords': ['confidential quotation', 'tender secrecy', 'firm refusal', 'professional integrity', 'code of conduct', 'official permission']
    },
    {
        'id': 'S14',
        'module': 'SITUATIONAL',
        'category': 'Workplace Simulation',
        'rubric': 'situational',
        'q_en': 'Workplace Scenario 14: You are newly appointed as District Account Assistant and assigned to prepare a Utilization Certificate (UC) and Expenditure Statement for a scheme you have not handled before. How will you proceed without making mistakes?',
        'q_mr': 'कार्यालयीन प्रसंग १४: तुमची नवीनच नियुक्ती झाली आहे आणि तुम्हाला एका नवीन योजनेचे युटिलायझेशन सर्टिफिकेट (UC) आणि खर्चाचे विवरण तयार करण्याचे काम दिले आहे, जे तुम्ही आधी कधीही केलेले नाही. चुका न करता तुम्ही हे काम कसे पूर्ण कराल?',
        'q_hi': 'नए पद पर होने पर यदि कोई नया वित्तीय कार्य (जैसे UC बनाना) मिले तो आप बिना गलती किए इसे कैसे करेंगे?',
        'keyPoints': [
            'Do not pretend to know everything; ask and learn properly',
            'Refer to past approved files and previous year’s UC formats of the same scheme',
            'Study the scheme guidelines and government resolution (GR)',
            'Draft the statement carefully with supporting ledger vouchers',
            'Request the senior officer or senior assistant to review and guide before final submission'
        ],
        'modelAnswer': 'मॅडम, नवीन जबाबदारी स्वीकारताना घाबरून न जाता शिकण्याची वृत्ती ठेवणे महत्त्वाचे आहे.\nमाझी कृती:\n१. जुन्या फायलींचा अभ्यास: मी कार्यालयातील रेकॉर्ड रूममधून त्याच योजनेचे आधीचे मंजूर झालेले युटिलायझेशन सर्टिफिकेट (UC) आणि फायली काढून नमुना (Format) समजून घेईन.\n२. शासन निर्णय व मार्गदर्शक तत्त्वे: त्या योजनेचा मूळ शासन निर्णय (GR) किंवा मुख्यालयाची मार्गदर्शक तत्त्वे वाचीन, ज्यामध्ये खर्चाचे नियम दिलेले असतात.\n३. कच्चा मसुदा (Drafting): लेजर आणि व्हाउचरशी आकडे तपासून कच्चा ताळेबंद तयार करेन.\n४. वरिष्ठांचे मार्गदर्शन: मी स्वतः जिल्हा प्रकल्प अधिकाऱ्यांना किंवा सिनियर सहकाऱ्यांना मसुदा दाखवून विनंती करेन, "सर, मी नवीन असल्याने हा मसुदा तयार केला आहे, कृपया तपासून काही सुधारणा असल्यास मार्गदर्शन करावे."\n५. यामुळे काम अचूक होईल आणि मला नवीन शासकीय कार्यपद्धती शिकता येईल.',
        'commonMistakes': [
            'Pretending you know everything and submitting wrong UC',
            'Sitting idle and waiting for someone else to do your work'
        ],
        'followUp': 'Is asking for guidance from seniors considered a weakness in an office?',
        'followUpAnswer': 'मुळीच नाही सर! न समजता चुकीचा हिशेब करण्यापेक्षा वेळेवर नम्रपणे मार्गदर्शन विचारून अचूक काम करणे हे जबाबदार कर्मचाऱ्याचे लक्षण मानले जाते.',
        'keywords': ['newly appointed', 'learning attitude', 'reference to past files', 'scheme guidelines', 'drafting uc', 'senior guidance', 'accuracy']
    },
    {
        'id': 'S15',
        'module': 'SITUATIONAL',
        'category': 'Workplace Simulation',
        'rubric': 'situational',
        'q_en': 'Workplace Scenario 15: During BRS preparation at month-end, you find an unexplained debit of ₹18,500 in the bank statement that does not match any office payment voucher or cheque. What steps will you take?',
        'q_mr': 'कार्यालयीन प्रसंग १५: महिन्याअखेरीस BRS करताना तुम्हाला बँक स्टेटमेंटमध्ये ₹१८,५०० ची एक डेबिट नोंद दिसली, ज्याचा कोणताही व्हाउचर किंवा चेक कार्यालयाच्या रेकॉर्डमध्ये नाही. तुम्ही काय तपासणी कराल?',
        'q_hi': 'बैंक स्टेटमेंट में ₹18,500 की अज्ञात डेबिट एंट्री मिलने पर आप क्या जांच करेंगे?',
        'keyPoints': [
            'Step 1: Check bank statement narration / UTR / transaction details carefully',
            'Step 2: Check if any auto-debit, ECS, loan installment or annual bank charges took place',
            'Step 3: Check if any online transaction was carried out by authorized signatory',
            'Step 4: Immediately report to District Project Officer',
            'Step 5: Visit the bank branch with an official letter signed by DPO to get full transaction trail / beneficiary account',
            'Step 6: Show in BRS as "Amounts debited by Bank not entered in Cash Book" till resolved'
        ],
        'modelAnswer': 'सर, बँकेतून विनानोंद पैसे वजा होणे ही गंभीर बाब ठरू शकते. माझी कृती:\n१. नॅरेशन तपासणे: मी बँक स्टेटमेंटमधील त्या एंट्रीचे नॅरेशन, तारीख आणि ट्रान्झॅक्शन आयडी बारकाईने तपासेन (उदा. कोणताही ईसीएस, बँक चार्जेस किंवा ऑनलाइन व्यवहार आहे का).\n२. कार्यालयीन तपासणी: ऑफिसमध्ये कोणी ऑनलाइन पेमेंट किंवा अधिकृत चालान भरले आहे का आणि त्याची व्हाउचर एन्ट्री राहून गेली आहे का ते पाहीन.\n३. अधिकाऱ्यांच्या निदर्शनास आणणे: त्वरित जिल्हा प्रकल्प अधिकाऱ्यांना ही अज्ञात डेबिट नोंद दाखवेन.\n४. बँकेशी पत्रव्यवहार: DPO साहेबांच्या स्वाक्षरीचे अधिकृत पत्र घेऊन बँकेच्या शाखेत जाईन आणि तो व्यवहार कोणाच्या खात्यात आणि कोणत्या अधिकाराने झाला याचा बँक स्टेटमेंट लेजर उतारा मागेन.\n५. BRS मध्ये नोंद: जोपर्यंत तोडगा निघत नाही, तोपर्यंत BRS मध्ये "Amount debited by Bank not credited in Cash Book" या मथळ्याखाली हा फरक दाखवून ताळेबंद जुळवून ठेवेन.',
        'commonMistakes': [
            'Ignoring the entry and forcing the cash book to match by false entry',
            'Waiting for 3 months to contact the bank'
        ],
        'followUp': 'What should be done if the bank confirms that the debit was due to a clerical mistake made by the bank clerk?',
        'followUpAnswer': 'बँकेकडून लेखी पत्र घेऊन ती रक्कम तात्काळ खात्यात रिव्हर्स (Re-credit) करून घेतली जाईल आणि पासबुकमध्ये सुधारणा नोंद करून घेतली जाईल.',
        'keywords': ['unexplained bank debit', 'bank narration', 'dpo intimation', 'bank inquiry letter', 'brs timing difference', 'bank error reversal']
    },

    # =========================================================================
    # PART 3: PERSONAL INTERVIEW, HR & BEHAVIOURAL QUESTIONS (20% Weightage)
    # =========================================================================
    {
        'id': 'H1',
        'module': 'HR',
        'category': 'Personal & HR',
        'rubric': 'personality',
        'q_en': 'Please tell us about yourself, your educational background, and what motivated you to choose a career in accounts.',
        'q_mr': 'कृपया तुमचा परिचय द्या, तुमचे शिक्षण सांगा आणि अकाउंट्स क्षेत्रात करिअर करण्याचे तुम्ही का ठरवले ते सांगा.',
        'q_hi': 'कृपया अपना परिचय दीजिए और बताइए कि आपने अकाउंट्स में करियर क्यों चुना?',
        'keyPoints': [
            'Warm, professional greeting',
            'Name, hometown and commerce degree credentials',
            'Passion for accounting: precision, numbers, transparency, organization',
            'Readiness to serve in public sector organisation like MCED'
        ],
        'modelAnswer': 'Good morning/afternoon, Sir and Madam. माझं नाव [नाव] आहे. मी [गाव/शहर] येथील रहिवासी आहे. मी माझे बी.कॉम [कॉलेजचे नाव] मधून [वर्ष] मध्ये पूर्ण केले आहे, ज्यामध्ये फायनान्शियल अकाउंटिंग आणि ऑडिटिंग हे माझे मुख्य विषय होते. मला एमएस एक्सेल आणि टॅलीचे प्रॅक्टिकल ज्ञान आहे.\nमला सुरुवातीपासूनच आकड्यांची अचूक मांडणी करणे, हिशेब जुळवणे आणि आर्थिक पारदर्शकता ठेवणे यामध्ये विशेष आवड आहे. लेखी परीक्षा उत्तीर्ण झाल्यानंतर, MCED सारख्या महाराष्ट्रातील अग्रगण्य संस्थेच्या जिल्हा कार्यालयात अकाउंट असिस्टंट म्हणून काम करण्याची संधी मिळणे ही माझ्या करिअरसाठी सन्मानाची बाब असेल. धन्यवाद.',
        'commonMistakes': [
            'Speaking in a memorized, unnatural robot-like tone',
            'Talking too much about childhood or family history',
            'Forgetting to mention commerce/accounting passion'
        ],
        'followUp': 'Why did you choose commerce over other career streams?',
        'followUpAnswer': 'कारण प्रत्येक संस्था, उद्योग किंवा शासकीय उपक्रम हा आर्थिक व्यवस्थापनावर चालतो. अचूक हिशेब ठेवणे ही कोणत्याही संस्थेची खरी ताकद असते आणि मला ही जबाबदारी पार पाडणे मनापासून आवडते.',
        'keywords': ['introduction', 'b.com', 'commerce', 'accounting', 'precision', 'excel', 'hometown', 'mced career', 'transparency']
    },
    {
        'id': 'H2',
        'module': 'HR',
        'category': 'Personal & HR',
        'rubric': 'personality',
        'q_en': 'Why do you want to join MCED specifically, rather than a private corporate company or bank?',
        'q_mr': 'खाजगी कंपनी किंवा बँकेऐवजी तुम्हाला विशेषतः MCED मध्येच का काम करायचे आहे?',
        'q_hi': 'प्राइवेट कंपनी या बैंक के बजाय आप MCED में ही क्यों आना चाहते हैं?',
        'keyPoints': [
            'Meaningful developmental public mission: Empowering youth and women to become job creators',
            'Public sector financial discipline and audit exposure',
            'Stable, respectable and learning-oriented work environment'
        ],
        'modelAnswer': 'सर, खाजगी कंपनीत काम करणे हा मुख्यत्वे नफा मिळवण्यासाठीचा भाग असतो; परंतु MCED मध्ये काम करण्यामागे एक सामाजिक आणि विकासात्मक उद्दिष्ट (Social & Developmental Purpose) आहे. MCED मुळे ग्रामीण भागातील युवक, शेतकरी आणि महिला स्वतःचे उद्योग सुरू करतात आणि इतरांना रोजगार देतात. अशा संस्थेच्या जिल्हा स्तरावर आर्थिक कामकाज सांभाळताना आपल्याला प्रत्यक्ष समाजविकासात योगदान दिल्याचे समाधान मिळते. तसेच शासकीय नियमावली, बजेट व्यवस्थापन आणि ऑडिट यासारख्या बाबींचा सखोल अनुभव येथे मिळतो, जो माझ्या व्यावसायिक प्रगतीसाठी अत्यंत मोलाचा आहे.',
        'commonMistakes': [
            'Saying "Private companies make people work too hard"',
            'Saying only "Government job offers pension or job safety"'
        ],
        'followUp': 'How will your accounting work at the district level help an unemployed rural youth?',
        'followUpAnswer': 'वेळेवर निधी उपलब्ध ठेवणे, प्रशिक्षणाची साधने आणि चहापान वेळेत देणे आणि वेळेवर हिशेब पूर्ण करून योजना विनाअडथळा सुरू ठेवणे याने थेट प्रशिक्षणार्थी तरुणांना फायदा होतो.',
        'keywords': ['why mced', 'developmental mission', 'job creators', 'public finance', 'social impact', 'professional growth', 'stability']
    },
    {
        'id': 'H3',
        'module': 'HR',
        'category': 'Personal & HR',
        'rubric': 'personality',
        'q_en': 'What are your key strengths, and what is one weakness that you are actively working to improve?',
        'q_mr': 'तुमची मुख्य बलस्थाने (Strengths) काय आहेत, आणि अशी कोणती एक उणीव (Weakness) आहे जी सुधारण्यासाठी तुम्ही सक्रिय प्रयत्न करत आहात?',
        'q_hi': 'आपकी ताकत क्या है और ऐसी कौन सी कमजोरी है जिसे आप सुधार रहे हैं?',
        'keyPoints': [
            'Strengths: High numerical accuracy, patience, meticulous document checking, integrity',
            'Weakness: Realistic and professional; coupled with concrete self-improvement actions',
            'Avoid destructive weaknesses like "I get angry quickly" or fake answers like "I have no flaw"'
        ],
        'modelAnswer': 'मॅडम, माझी मुख्य ताकद म्हणजे "Attention to Detail" (सूक्ष्म तपासणी) आणि संयम. हिशेब तपासताना किंवा बिले पडताळताना मी घाई न करता प्रत्येक व्हाउचर, बिल नंबर आणि आकड्यांची क्रॉस-व्हेरीफिकेशन करते. माझे काम प्रामाणिकपणे आणि वेळेत पूर्ण करण्याची माझी सवय आहे.\nमाझी एक उणीव सांगायची तर, पूर्वी मला अनोळखी व्यक्तींसमोर किंवा वरिष्ठ अधिकाऱ्यांसमोर मोठ्या समूहात बोलताना थोडे दडपण यायचे. परंतु ही उणीव दूर करण्यासाठी मी इंग्रजी व मराठी संभाषण सराव, मॉक इंटरव्ह्यू आणि सादरीकरणाची नियमित प्रॅक्टिस सुरू केली आहे, ज्यामुळे आता माझा आत्मविश्वास खूप वाढला आहे.',
        'commonMistakes': [
            'Saying "I have no weakness"',
            'Saying a disqualifying weakness like "I am weak in math"'
        ],
        'followUp': 'How do you ensure you do not miss small errors while checking a 10-page bill?',
        'followUpAnswer': 'मी एक चेकलिस्ट वापरते आणि पेन्सिलने प्रत्येक आकडा व सपोर्टिंग तपासून झाल्यावरच अंतिम व्हाउचरवर स्वाक्षरी करते.',
        'keywords': ['strengths', 'attention to detail', 'patience', 'accuracy', 'weakness', 'communication improvement', 'confidence']
    },
    {
        'id': 'H4',
        'module': 'HR',
        'category': 'Personal & HR',
        'rubric': 'personality',
        'q_en': 'How do you respond when a senior officer criticizes your work or points out an error in your report?',
        'q_mr': 'जेव्हा वरिष्ठ अधिकारी तुमच्या कामावर टीका करतात किंवा तुमच्या अहवालातील चूक निदर्शनास आणून देतात, तेव्हा तुम्ही काय प्रतिक्रिया देता?',
        'q_hi': 'वरिष्ठ अधिकारी द्वारा काम की आलोचना या गलती बताने पर आपकी क्या प्रतिक्रिया होती है?',
        'keyPoints': [
            'Non-defensive, mature and receptive attitude',
            'Listening carefully to understand the exact feedback',
            'Acknowledge the mistake gracefully, apologize politely if needed, and rectify it immediately',
            'Viewing constructive criticism as an opportunity to learn and grow'
        ],
        'modelAnswer': 'सर, मी वरिष्ठांच्या टीकेकडे वैयक्तिक हल्ला म्हणून न पाहता कामातील सुधारणेची संधी (Learning Opportunity) म्हणून सकारात्मकतेने घेते.\nमाझी प्रतिक्रिया:\n१. शांतपणे ऐकणे: साहेब काय चूक दाखवत आहेत ते मध्ये न बोलता शांतपणे समजून घेईन.\n२. लगेच दुरुस्ती: चूक मान्य करून, कोणतीही खोटी कारणे न देता ती चूक तात्काळ दुरुस्त करेन.\n३. शिकण्याची वृत्ती: "थँक्यू सर, तुम्ही ही चूक दाखवली; मी यापुढे अशी चूक होणार नाही याची काळजी घेईन" असे नम्रपणे सांगेन.\nअकाउंट्सच्या कामात वरिष्ठांनी चूक वेळेवर दाखवली तर भविष्यातील मोठा ऑडिट आक्षेप टळतो, त्यामुळे त्यांचे मार्गदर्शन माझ्यासाठी मार्गदर्शक ठरते.',
        'commonMistakes': [
            'Arguing defensively or blaming colleagues/computer',
            'Getting upset, weeping or holding grudges'
        ],
        'followUp': 'What if you feel the officer’s criticism was based on a misunderstanding of the facts?',
        'followUpAnswer': 'मी शांतपणे संबंधित कागदपत्रे आणि नियम अधिकाऱ्यांसमोर ठेवून नम्रपणे सांगेन, "सर, वस्तुस्थिती अशी आहे; कृपया एकदा तपासून पाहावी." जर त्यांनी तरीही दुरुस्ती सांगितली, तर त्यांच्या आदेशाचे पालन करेन.',
        'keywords': ['criticism', 'learning opportunity', 'positive attitude', 'immediate rectification', 'humble', 'audit prevention', 'maturity']
    },
    {
        'id': 'H5',
        'module': 'HR',
        'category': 'Personal & HR',
        'rubric': 'personality',
        'q_en': 'What will you do during this interview if the panel asks you a question whose answer you genuinely do not know?',
        'q_mr': 'या मुलाखतीत जर पॅनेलने तुम्हाला असा प्रश्न विचारला ज्याचे उत्तर तुम्हाला अजिबात माहित नाही, तर तुम्ही काय कराल?',
        'q_hi': 'यदि साक्षात्कार में किसी प्रश्न का उत्तर आपको नहीं पता, तो आप क्या करेंगे?',
        'keyPoints': [
            'Honesty and integrity: Never bluff, guess blindly or make up false information',
            'Polite, composed admission',
            'Expression of willingness to learn',
            'Shows professional maturity under pressure'
        ],
        'modelAnswer': 'मॅडम, अशा वेळी खोटे बोलणे किंवा अंदाजे चुकीचे उत्तर देणे अत्यंत चुकीचे ठरेल, विशेषतः अकाउंट्स क्षेत्रात जिथे सत्यता सर्वात महत्त्वाची असते.\nमी पॅनेलसमोर अत्यंत नम्रपणे आणि आत्मविश्वासाने सांगेन:\n"सर/मॅडम, मला सध्या या विषयाबद्दल/नियमाबद्दल नेमकी खात्री नाही; मी चुकीचे सांगून आपला वेळ वाया घालवणार नाही. परंतु मुलाखतीनंतर मी हा नियम किंवा संदर्भ नक्की वाचीन आणि समजून घेईन."\nयामुळे पॅनेलला माझा प्रामाणिकपणा समजतो आणि मी दडपणाखाली खोटे बोलत नाही हे सिद्ध होते.',
        'commonMistakes': [
            'Bluffing or giving random irrelevant answers',
            'Panicking, sweating and losing confidence for subsequent questions'
        ],
        'followUp': 'Is it acceptable for an accountant to say "I don’t know" in an office setting?',
        'followUpAnswer': 'होय सर, चुकीची नोंद करण्यापेक्षा "नियम तपासून सांगतो" असे प्रामाणिकपणे म्हणून योग्य नियम वाचून मगच कारवाई करणे अधिक सुरक्षित असते.',
        'keywords': ['do not know', 'honesty', 'no bluffing', 'polite admission', 'willingness to learn', 'integrity', 'calm']
    },

    # =========================================================================
    # PART 4: PRACTICAL ACCOUNTING & FINANCIAL CONTROLS (15% Weightage)
    # =========================================================================
    {
        'id': 'P1',
        'module': 'PRACTICAL_ACC',
        'category': 'Practical Accounting',
        'rubric': 'practical_acc',
        'q_en': 'What essential checks do you perform on a Tax Invoice submitted by a vendor before processing payment?',
        'q_mr': 'व्हेंडरने सादर केलेल्या टॅक्स इनव्हॉईसवर (Tax Invoice) पेमेंट करण्यापूर्वी तुम्ही कोणत्या तांत्रिक व कायदेशीर बाबी तपासाल?',
        'q_hi': 'टैक्स इनवॉइस की जांच करते समय कौन-कौन सी मुख्य बातें देखी जाती हैं?',
        'keyPoints': [
            'Title: "Tax Invoice" mentioned clearly',
            'Vendor GSTIN, Name, Address, and Invoice Serial Number & Date',
            'Buyer details: MCED District Centre Name, Address, and GSTIN (State code 27)',
            'HSN/SAC Code, description of goods/services, Quantity and Unit Price',
            'CGST/SGST/IGST breakdown and arithmetical totals',
            'Signature of the vendor / authorized signatory'
        ],
        'modelAnswer': 'सर, जीएसटी कायद्यानुसार आणि लेखा नियमांनुसार टॅक्स इनव्हॉईसवर खालील बाबींची तपासणी केली जाते:\n१. इनव्हॉइसचे नाव: बिलावर स्पष्टपणे "Tax Invoice" लिहिलेले असावे.\n२. व्हेंडरचा तपशील: पुरवठादाराचे नाव, पत्ता आणि १५ अंकी वैध GSTIN क्रमांक.\n३. MCED चा तपशील: बिलावर खरेदीदार म्हणून MCED चे नाव आणि महाराष्ट्राचा GSTIN (२७ ने सुरू होणारा) बरोबर असावा.\n४. इनव्हॉइस नंबर व तारीख: सलग क्रमांक (Consecutive Serial Number) आणि चालू आर्थिक वर्षातील तारीख.\n५. माल/सेवेचा तपशील: वस्तूंचा HSN कोड किंवा सेवेचा SAC कोड, प्रमाण (Quantity) आणि दर.\n६. टॅक्सचे स्वतंत्र विभाजन: बेस रक्कम, CGST, SGST किंवा IGST चे स्वतंत्र रकाने आणि अंतिम बेरीज.\n७. स्वाक्षरी: व्हेंडरची अधिकृत स्वाक्षरी किंवा डिजिटल स्वाक्षरी असावी. या सर्व बाबी बरोबर असल्यावरच इनपुट टॅक्स क्रेडिट (ITC) सुरक्षित राहते.',
        'commonMistakes': [
            'Accepting an estimate or quotation as a tax invoice',
            'Not checking if MCED GSTIN is printed on the bill'
        ],
        'followUp': 'What is the consequence if a vendor bill has only "Proforma Invoice" written on it?',
        'followUpAnswer': 'प्रोफॉर्मा इन्व्हॉईस हे फक्त अंदाजे दरपत्रक असते, तो अधिकृत कर दस्तऐवज नसतो; त्यामुळे त्यावर प्रत्यक्ष पेमेंट किंवा ITC क्लेम करता येत नाही.',
        'keywords': ['tax invoice', 'gstin 27', 'hsn sac code', 'cgst sgst', 'serial number', 'proforma invoice', 'vendor signature']
    },
    {
        'id': 'P2',
        'module': 'PRACTICAL_ACC',
        'category': 'Practical Accounting',
        'rubric': 'practical_acc',
        'q_en': 'How do you calculate and deduct TDS under Section 194C (Contractors) and Section 194J (Professional fees) in office bills?',
        'q_mr': 'कार्यालयीन बिलांवर कंत्राटदारांसाठी कलम 194C आणि व्यावसायिक फीसाठी कलम 194J अंतर्गत टीडीएस कसा मोजला आणि कापला जातो?',
        'q_hi': 'धारा 194C और 194J के तहत TDS की गणना और कटौती कैसे की जाती है?',
        'keyPoints': [
            'Section 194C (Contractor/Advertising/Catering): 1% for Individual/HUF, 2% for Company/Firm. Threshold: Single bill > ₹30,000 or aggregate > ₹1,00,000 in FY',
            'Section 194J (Guest Speakers, CA, Legal, Technical): 10% for professional services, 2% for technical services. Threshold: ₹30,000 in FY',
            'Calculated on base value excluding GST (if GST shown separately)',
            'Remittance deadline: 7th of next month'
        ],
        'modelAnswer': 'मॅडम, TDS (Tax Deducted at Source) हा आयकर कायद्यानुसार बिलातून कापला जातो:\n१. Section 194C (कंत्राटदार - उदा. मंडप, केटरिंग, छपाई, जाहिरात):\n- जर व्हेंडर व्यक्ती/HUF असेल तर १% TDS; आणि जर कंपनी/पार्टनरशिप फर्म असेल तर २% TDS.\n- मर्यादा: एका बिलासाठी ₹३०,००० पेक्षा जास्त किंवा वर्षभरात ₹१,००,००० पेक्षा जास्त व्यवहार झाल्यास.\n२. Section 194J (व्यावसायिक व तांत्रिक फी - उदा. गेस्ट लेक्चरर्स, सीए फी, आयटी कन्सल्टंट):\n- प्रोफेशनल फीवर १०% किंवा तांत्रिक सेवेवर २% TDS.\n- मर्यादा: वर्षभरात ₹३०,००० पेक्षा जास्त रक्कम असल्यास.\nमहत्त्वाचा नियम: जर बिलावर GST स्वतंत्र दाखवला असेल, तर TDS फक्त मूळ बिलाच्या रकमेवर (Base Value) आकारला जातो, जीएसटीवर नाही.\nकापलेला TDS पुढील महिन्याच्या ७ तारखेच्या आत सरकारी खात्यात जमा करावा लागतो.',
        'commonMistakes': [
            'Calculating TDS on total amount including GST',
            'Not knowing the 7th of next month payment deadline'
        ],
        'followUp': 'What rate of TDS applies if the vendor does not submit their PAN card?',
        'followUpAnswer': 'Section 206AA नुसार जर व्हेंडरने पॅन कार्ड दिले नाही, तर थेट २०% (20%) या उच्च दराने TDS कापावा लागतो.',
        'keywords': ['tds calculation', '194c', '194j', 'guest lecturer', 'contractor', 'base value', '7th of next month', 'pan 206aa']
    },
    {
        'id': 'P3',
        'module': 'PRACTICAL_ACC',
        'category': 'Practical Accounting',
        'rubric': 'practical_acc',
        'q_en': 'Explain how a Double-Column or Triple-Column Cash Book is balanced daily and monthly in a government-supported office.',
        'q_mr': 'शासकीय अनुदानित कार्यालयात रोखवही (Cash Book) दररोज आणि महिन्याअखेरीस कशी संतुलित (Balance) केली जाते?',
        'q_hi': 'कार्यालय में Cash Book का दैनिक और मासिक संतुलन (Balancing) कैसे किया जाता है?',
        'keyPoints': [
            'Daily balancing: Debit receipts vs Credit payments',
            'Physical cash count verification at closing time every single day',
            'Cash column can NEVER have a credit balance (you cannot spend more physical cash than you have)',
            'Monthly bank column reconciliation with Bank Statement (BRS)',
            'Countersignature of Head of Office / District Officer daily'
        ],
        'modelAnswer': 'सर, कॅश बुक हे कार्यालयाचे हृदय असते. दैनंदिन आणि मासिक संतुलन खालीलप्रमाणे होते:\n१. दैनंदिन संतुलन (Daily Balancing):\n- दिवसभरात आलेल्या सर्व पावत्या डेबिट (रिसिट) बाजूला आणि झालेले खर्च क्रेडिट (पेमेंट) बाजूला नोंदवले जातात.\n- सायंकाळी दोन्ही बाजूंची बेरीज करून "Balance c/d" (क्लोजिंग बॅलन्स) काढला जातो.\n- कॅश रकान्यातील शिल्लक प्रत्यक्ष कॅश बॉक्समधील नोटा आणि नाणी मोजून तंतोतंत जुळवली जाते.\n- सुवर्ण नियम: कॅश रकान्याला कधीही क्रेडिट शिल्लक (उणे शिल्लक) असू शकत नाही, कारण जेवढी रोख आहे त्यापेक्षा जास्त खर्च करता येत नाही.\n- दररोज या नोंदीवर आणि प्रत्यक्ष शिलकेवर जिल्हा प्रकल्प अधिकाऱ्यांची स्वाक्षरी घेतली जाते.\n२. मासिक संतुलन (Monthly Balancing):\n- महिन्याच्या शेवटी बँक रकान्याची शिल्लक बँक पासबुक/स्टेटमेंटशी जुळवून बँक रिकन्सिलिएशन स्टेटमेंट (BRS) तयार केले जाते.',
        'commonMistakes': [
            'Saying Cash column can have a negative or credit balance',
            'Forgetting the daily physical cash verification'
        ],
        'followUp': 'Can the Bank column of a Cash Book have a credit balance?',
        'followUpAnswer': 'हो सर, बँकेत ओव्हरड्राफ्ट (Bank Overdraft) सुविधा असल्यास किंवा खात्यात पैसे नसताना बँकेने पेमेंट दिल्यास बँक रकान्याला क्रेडिट शिल्लक असू शकते.',
        'keywords': ['cash book balancing', 'daily cash count', 'balance c/d', 'no credit cash balance', 'bank column', 'brs', 'officer countersignature']
    },

    # =========================================================================
    # PART 5: COMPUTER, EXCEL & OFFICE KNOWLEDGE (5% Weightage)
    # =========================================================================
    {
        'id': 'C1',
        'module': 'COMPUTER',
        'category': 'Computer & Office Tools',
        'rubric': 'computer_office',
        'q_en': 'How do you practically use MS Excel to maintain batch-wise expenditure sheets and prevent duplicate entries?',
        'q_mr': 'बॅचनिहाय खर्चाचे विवरणपत्र तयार करण्यासाठी आणि डुप्लिकेट नोंदी रोखण्यासाठी तुम्ही MS Excel चा प्रॅक्टिकल वापर कसा कराल?',
        'q_hi': 'Excel में व्यय विवरण बनाने और डुप्लिकेट प्रविष्टियाँ रोकने के लिए आप क्या करेंगे?',
        'keyPoints': [
            'Using structured columns: Sl No, Date, Voucher No, Budget Head, Beneficiary, Bill No, Amount, TDS, Net Paid, Cheque/UTR No',
            'SUMIF formula: To calculate head-wise expenditure automatically (=SUMIF(D:D, "Refreshment", H:H))',
            'Data Validation: Restricting input errors and creating Dropdown lists for Budget Heads',
            'Conditional Formatting / COUNTIF: Highlighting duplicate invoice numbers in red (=COUNTIF(F:F, F2)>1)'
        ],
        'modelAnswer': 'मॅडम, एक्सेलमध्ये मी खालील पद्धतीने अचूक आणि सुरक्षित एक्सपेन्स शीट तयार करेन:\n१. सुव्यवस्थित रकाने (Columns): अनुक्रमांक, तारीख, व्हाउचर नंबर, बजेट हेड, पार्टीचे नाव, इनव्हॉईस नंबर, एकूण रक्कम, टीडीएस, निव्वळ रक्कम (Net Amount) आणि UTR नंबर.\n२. हेडनिहाय बेरीज (SUMIF): कोणत्या हेडखाली किती खर्च झाला हे आपोआप काढण्यासाठी =SUMIF(Head_Range, "Stationery", Amount_Range) हे सूत्र वापरेन.\n३. ड्रॉपडाउन लिस्ट: Budget Head च्या कॉलममध्ये स्पेलिंगच्या चुका टाळण्यासाठी Data Validation द्वारे फिक्स ड्रॉपडाउन लिस्ट तयार करेन.\n४. डुप्लिकेट रोखणे: इनव्हॉईस नंबरच्या कॉलममध्ये Conditional Formatting लावून =COUNTIF($F:$F, F2)>1 हा फॉर्म्युला लावेन; जेणेकरून तोच बिल नंबर पुन्हा टाईप होताच सेल तात्काळ लाल रंगात हायलाइट होईल आणि चूक पकडली जाईल.',
        'commonMistakes': [
            'Only mentioning basic SUM formula without mentioning Data Validation or duplicate prevention'
        ],
        'followUp': 'What shortcut key is used in Excel to format numbers as currency (₹)?',
        'followUpAnswer': 'Ctrl + Shift + 4 ($/₹ Currency Format).',
        'keywords': ['ms excel', 'batch expense sheet', 'sumif', 'data validation', 'dropdown list', 'countif duplicate', 'conditional formatting']
    },
    {
        'id': 'C2',
        'module': 'COMPUTER',
        'category': 'Computer & Office Tools',
        'rubric': 'computer_office',
        'q_en': 'What precautions do you take regarding official email communication, file naming, and financial data backup in an office computer?',
        'q_mr': 'कार्यालयीन कॉम्प्युटरवर आर्थिक अहवालांचे बॅकअप, फाईलचे नाव (File Naming) आणि अधिकृत ईमेल्स पाठवताना तुम्ही कोणती दक्षता घ्याल?',
        'q_hi': 'कार्यालयीन डेटा बैकअप, फाइल नामकरण और ईमेल संचार में आप क्या सावधानियाँ बरतेंगे?',
        'keyPoints': [
            'Standard file naming conventions: "MCED_District_Monthly_Accounts_Oct2026_v1.xlsx"',
            'Regular periodic data backups on external hard disk / official cloud drive to prevent data loss',
            'Official email etiquette: Clear subject line, polite salutation, attaching PDF reports, checking recipient email address before sending',
            'Password security: Keeping system locked when away from desk, never sharing financial login credentials'
        ],
        'modelAnswer': 'सर, डिजिटल रेकॉर्ड्सची सुरक्षा आणि शिस्त खालीलप्रमाणे पाळली जाईल:\n१. फाईलचे पद्धतशीर नामकरण (File Naming): फाईल सेव्ह करताना स्पष्ट नाव, महिना आणि व्हर्जन नंबर लिहिला जाईल, उदा. "MCED_Nashik_Exp_Statement_Oct2026_Final.xlsx". यामुळे जुनी आणि नवीन फाईल यात गोंधळ होत नाही.\n२. नियमित बॅकअप (Backup): कॉम्प्युटर खराब झाल्यास डेटा नष्ट होऊ नये म्हणून दर आठवड्याला सर्व लेजर्स आणि एक्सेल फाइल्सचा बॅकअप अधिकृत एक्सटर्नल ड्राईव्ह किंवा शासकीय क्लाउडवर ठेवला जाईल.\n३. ईमेल शिस्त: मुख्यालयाला मेल पाठवताना स्पष्ट विषय (Subject Line), वरिष्ठ अधिकाऱ्यांचे मार्क (Mark to DPO in CC), योग्य सही आणि फायली आधी PDF करून मगच जोडल्या जातील.\n४. सुरक्षितता: जागेवरून उठताना कॉम्प्युटर Win+L ने लॉक करणे आणि बँक पोर्टल्सचे पासवर्ड्स कोणाशीही शेअर न करणे.',
        'commonMistakes': [
            'Naming files as "Book1.xlsx" or "Final_Final2.xlsx"',
            'Not keeping any backup copy'
        ],
        'followUp': 'Why should financial reports be emailed in PDF format rather than raw Excel sheets to outside authorities?',
        'followUpAnswer': 'कारण PDF मधील आकडे कोणीही परस्पर बदलू शकत नाही (Read-only format), प्रिंटिंग लेआउट सुरक्षित राहतो आणि त्यावर अधिकृत डिजिटल स्वाक्षरी करता येते.',
        'keywords': ['file naming', 'backup', 'official email', 'pdf format', 'password security', 'data integrity', 'lock screen']
    }
]
