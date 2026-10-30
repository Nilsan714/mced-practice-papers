# -*- coding: utf-8 -*-
"""Generate redesigned oral interview dataset matching exact priorities:
- 30% MCED Organisation & Job Role Awareness (6 Marks)
- 30% Real-Life Workplace Simulations (6 Marks)
- 20% Personal Interview, HR & Behavioural (4 Marks)
- 15% Practical Accounting & Controls (3 Marks)
- 5% Computer & Office Knowledge (1 Mark)
Total: 20 Marks
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
WEB_JS = os.path.join(os.path.dirname(HERE), 'docs', 'js')
OUT_FILE = os.path.join(WEB_JS, 'interview_data.js')

MODULES = {
    'MCED': {
        'name': 'MCED संस्था व पदाची कर्तव्ये (30%)',
        'desc': 'MCED पार्श्वभूमी, ध्येय, EDP प्रशिक्षण, जिल्हा केंद्र व Account Assistant ची खरी भूमिका',
        'icon': '🏛️',
        'rubric': 'mced_org',
        'weight': 30
    },
    'SITUATIONAL': {
        'name': 'प्रत्यक्ष कार्यालयीन प्रसंग व निर्णयक्षमता (30%)',
        'desc': '१५ वास्तववादी कार्यालयीन प्रसंग: बिले, अपूर्ण पुरावे, कॅश तूट, दुहेरी पेमेंट व समन्वय',
        'icon': '🏢',
        'rubric': 'situational',
        'weight': 30
    },
    'HR': {
        'name': 'व्यक्तिमत्व, HR व व्यावसायिक वर्तणूक (20%)',
        'desc': 'परिचय, प्रेरणा, बलस्थाने, दडपण हाताळणे, टीका स्वीकारणे व प्रामाणिकपणा',
        'icon': '👤',
        'rubric': 'personality',
        'weight': 20
    },
    'PRACTICAL_ACC': {
        'name': 'प्रॅक्टिकल अकाउंट्स व वित्तीय नियंत्रण (15%)',
        'desc': 'टॅक्स इनव्हॉईस पडताळणी, TDS कलमे (194C/J), कॅश बुक संतुलन व BRS',
        'icon': '📊',
        'rubric': 'practical_acc',
        'weight': 15
    },
    'COMPUTER': {
        'name': 'कॉम्प्युटर, एक्सेल व कार्यालयीन कौशल्ये (5%)',
        'desc': 'एक्सेल खर्च पत्रक, SUMIF, डेटा व्हॅलिडेशन, ईमेल शिस्त व बॅकअप',
        'icon': '💻',
        'rubric': 'computer_office',
        'weight': 5
    }
}

RUBRIC_CONFIG = {
    'mced_org': {
        'name': 'MCED Organisation & Job Role Awareness',
        'marks': 6,
        'pct': 30,
        'desc': 'संस्थेची उद्दिष्टे, EDPs, जिल्हा केंद्राचे कार्य आणि Account Assistant ची खरी कर्तव्ये व मर्यादा'
    },
    'situational': {
        'name': 'Workplace Situations & Practical Judgement',
        'marks': 6,
        'pct': 30,
        'desc': 'अपूर्ण बिले, तफावत, तातडीची डेडलाईन, कॅश शॉर्टेज आणि प्रत्यक्ष कार्यालयीन निर्णयक्षमता'
    },
    'personality': {
        'name': 'Personality, HR & Behavioural Maturity',
        'marks': 4,
        'pct': 20,
        'desc': 'आत्मविश्वास, प्रामाणिकपणा, टीमवर्क, टीका स्वीकारणे व व्यावसायिक संभाषण'
    },
    'practical_acc': {
        'name': 'Practical Accounting & Financial Controls',
        'marks': 3,
        'pct': 15,
        'desc': 'टॅक्स इनव्हॉईस, टीडीएस कपात, कॅश बुक संतुलन, बँक रिकन्सिलिएशन'
    },
    'computer_office': {
        'name': 'Computer & Office Management',
        'marks': 1,
        'pct': 5,
        'desc': 'MS Excel चा व्यावहारिक वापर, फाईल नेमिंग, ईमेल व डिजिटल डेटा सुरक्षा'
    },
    'total': 20
}

PLAN_14_DAYS = [
    {
        'day': 1,
        'title': 'MCED संस्थेची ओळख व पायाभूत माहिती (30% Priority)',
        'desc': 'MCED ची स्थापना (1988), मुख्यालय (छत्रपती संभाजीनगर), स्वायत्त स्वरूप आणि उद्योजकता ध्येय.',
        'module': 'MCED',
        'targetQ': ['M1', 'M2'],
        'tips': 'MCED ही बँक नसून उद्योग विभागांतर्गत उद्योजकता प्रशिक्षण देणारी स्वायत्त संस्था आहे हे स्पष्ट सांगा.'
    },
    {
        'day': 2,
        'title': 'EDPs व जिल्हा केंद्राचे कार्य',
        'desc': 'उद्योजकता विकास कार्यक्रम (EDPs), कौशल्य प्रशिक्षण आणि जिल्हा केंद्राचे स्थानिक महत्त्व.',
        'module': 'MCED',
        'targetQ': ['M3', 'M4'],
        'tips': 'जिल्हा स्तरावर DIC आणि बँकांशी समन्वय कसा होतो ते उदाहरणासह सांगा.'
    },
    {
        'day': 3,
        'title': 'District Account Assistant ची खरी भूमिका व मर्यादा',
        'desc': 'तयार करणे, तपासणे, नोंदवणे आणि अहवाल देणे यातील फरक. Account Assistant चे अधिकार व मर्यादा.',
        'module': 'MCED',
        'targetQ': ['M5', 'M6'],
        'tips': 'लक्षात ठेवा: Account Assistant कडे बिल मंजूर (Sanction) करण्याचे अधिकार नसतात; फक्त तपासणे व शिफारस करणे असते.'
    },
    {
        'day': 4,
        'title': 'आर्थिक शिस्त, वेळेवर अहवाल व समन्वय',
        'desc': 'युटिलायझेशन सर्टिफिकेट्स (UCs), वेळेवर अहवाल पाठवणे आणि DPO व मुख्यालयाशी समन्वय.',
        'module': 'MCED',
        'targetQ': ['M7', 'M8'],
        'tips': 'वेळेवर अहवाल गेला नाही तर जिल्ह्याचे पुढील अनुदान रखडते हे स्पष्ट करा.'
    },
    {
        'day': 5,
        'title': 'प्रशिक्षण बॅचचे खर्च रेकॉर्ड व अपूर्ण बिले (Simulation 1 & 2)',
        'desc': '१५ दिवसांच्या EDP बॅचचे संपूर्ण खर्च रेकॉर्ड फाईल करणे आणि अपूर्ण बिलांची पडताळणी.',
        'module': 'SITUATIONAL',
        'targetQ': ['S1', 'S2'],
        'tips': 'विद्यार्थ्यांची उपस्थिती पत्रके ही केटरिंग बिलासाठी सर्वात महत्त्वाचा पुरावा असतो.'
    },
    {
        'day': 6,
        'title': 'मंजूर मर्यादेपेक्षा जास्त बिल व दुहेरी पेमेंट (Simulation 3 & 4)',
        'desc': 'मंजूर रकमेपेक्षा जास्त आलेले बिल आणि आधीच पेमेंट झालेले बिल पुन्हा आल्यास करावयाची कृती.',
        'module': 'SITUATIONAL',
        'targetQ': ['S3', 'S4'],
        'tips': 'सुधारित मंजुरीशिवाय (Revised Sanction) एका रुपयाचेही जास्तीचे पेमेंट करता येत नाही.'
    },
    {
        'day': 7,
        'title': 'तातडीची डेडलाईन व कॅश बॉक्समधील तूट (Simulation 5 & 6)',
        'desc': 'संध्याकाळी ५ ची अहवाल डेडलाईन आणि कॅश बॉक्समध्ये ₹५०० कमी भरल्यास काय कराल.',
        'module': 'SITUATIONAL',
        'targetQ': ['S5', 'S6'],
        'tips': 'कधीही स्वतःच्या खिशातून पैसे टाकून तूट लपवू नका. तात्काळ वरिष्ठांना लेखी सांगा.'
    },
    {
        'day': 8,
        'title': 'संपलेले बजेट व जुन्या ऑडिट फायली (Simulation 7 & 8)',
        'desc': 'बजेट ९५% संपले असताना आलेला नवीन खर्च आणि ३ वर्षांपूर्वीच्या फर्निचर बिलांची ऑडिट तपासणी.',
        'module': 'SITUATIONAL',
        'targetQ': ['S7', 'S8'],
        'tips': 'दुसऱ्या हेडचा निधी परस्पर वळवणे (Diversion) बेकायदेशीर आहे; मुख्यालयाची मंजुरी लागते.'
    },
    {
        'day': 9,
        'title': 'तक्रारदार हाताळणे व वरिष्ठांचा तोंडी दबाव (Simulation 9 & 10)',
        'desc': 'मानधनासाठी संतापलेला प्रशिक्षणार्थी आणि पुराव्याशिवाय चेक देण्याचा वरिष्ठांचा तोंडी आग्रह.',
        'module': 'SITUATIONAL',
        'targetQ': ['S9', 'S10'],
        'tips': 'आदरपूर्वक बोला, पण आर्थिक नियमांचे उल्लंघन करू नका. नोटशीटचा पर्याय द्या.'
    },
    {
        'day': 10,
        'title': 'अहवालातील चूक, दोन अधिकाऱ्यांची कामे व गोपनीयता (Simulation 11, 12, 13)',
        'desc': 'गेलेल्या रिपोर्टमधील चूक दुरुस्त करणे, कामाचे प्राधान्य ठरवणे आणि टेंडर कोटेशनची गोपनीयता राखणे.',
        'module': 'SITUATIONAL',
        'targetQ': ['S11', 'S12', 'S13'],
        'tips': 'चूक लपवण्याऐवजी स्वतःहून तातडीने Corrigendum पाठवणे हाच योग्य मार्ग आहे.'
    },
    {
        'day': 11,
        'title': 'नवीन कार्यपद्धती व बँक स्टेटमेंटमधील अज्ञात डेबिट (Simulation 14, 15)',
        'desc': 'नवीन योजनेचे UC तयार करताना ज्येष्ठ सहकाऱ्यांचे मार्गदर्शन घेणे आणि बँक तफावत शोधणे.',
        'module': 'SITUATIONAL',
        'targetQ': ['S14', 'S15'],
        'tips': 'न समजता चुकीचा हिशेब करण्यापेक्षा वेळेवर नम्रपणे मार्गदर्शन विचारणे अधिक चांगले.'
    },
    {
        'day': 12,
        'title': 'व्यक्तिमत्व, HR व वर्तणूक प्रश्न (20% Priority)',
        'desc': 'स्वतःचा परिचय, MCED ची निवड का, बलस्थाने/उणिवा, टीका स्वीकारणे आणि उत्तर माहित नसतानाची कृती.',
        'module': 'HR',
        'targetQ': ['H1', 'H2', 'H3', 'H4', 'H5'],
        'tips': 'उत्तर माहित नसेल तर खोटे बोलू नका किंवा अंदाज लावू नका; प्रामाणिकपणे मान्य करा.'
    },
    {
        'day': 13,
        'title': 'प्रॅक्टिकल अकाउंट्स, टॅक्स इनव्हॉईस, TDS व MS Excel',
        'desc': 'टॅक्स इनव्हॉईसचे घटक, कलम 194C/J नुसार TDS कपात, कॅश बुक संतुलन आणि एक्सेल ट्रॅकर.',
        'module': 'PRACTICAL_ACC',
        'targetQ': ['P1', 'P2', 'P3', 'C1', 'C2'],
        'tips': 'टीडीएस हा मूळ बिलाच्या रकमेवर (Base Value) मोजला जातो, जीएसटीवर नाही.'
    },
    {
        'day': 14,
        'title': 'संपूर्ण अधिकृत मॉक मुलाखत (Target 20/20 Marks)',
        'desc': 'नवीन प्राधान्यांनुसार १० प्रश्नांची प्रत्यक्ष पॅनेल परीक्षा, थेट मूल्यमापन व अंतिम उजळणी.',
        'module': 'MOCK',
        'targetQ': ['ALL'],
        'tips': 'पॅनेलसमोर शांत, हसतमुख आणि ठाम राहा. ३० ते ६० सेकंदांत मुद्देसूद उत्तर संपवा.'
    }
]

from generate_questions_list import QUESTIONS

def main():
    content = "/* MCED District Account Assistant - Redesigned Strategy Dataset */\n"
    content += "window.INTERVIEW_DATA = {\n"
    content += "  modules: " + json.dumps(MODULES, ensure_ascii=False, indent=2) + ",\n"
    content += "  rubric: " + json.dumps(RUBRIC_CONFIG, ensure_ascii=False, indent=2) + ",\n"
    content += "  plan14: " + json.dumps(PLAN_14_DAYS, ensure_ascii=False, indent=2) + ",\n"
    content += "  questions: " + json.dumps(QUESTIONS, ensure_ascii=False, indent=2) + "\n"
    content += "};\n"
    
    with open(OUT_FILE, 'w', encoding='utf8') as f:
        f.write(content)
    print(f"Successfully generated {OUT_FILE} with {len(QUESTIONS)} redesigned questions!")

if __name__ == '__main__':
    main()
