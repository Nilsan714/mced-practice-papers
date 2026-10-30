"""Build comprehensive question bank and syllabus data for MCED District Account Assistant Interview Coach"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
WEB_JS = os.path.join(os.path.dirname(HERE), 'docs', 'js')
OUT_FILE = os.path.join(WEB_JS, 'interview_data.js')

MODULES = {
    'A': {'name': 'Module A: Personality & HR', 'desc': 'Self introduction, motivation, strengths, goals & communication', 'icon': '👤', 'rubric': 'communication'},
    'B': {'name': 'Module B: Accounting Fundamentals', 'desc': 'Concepts, Golden Rules, Journal, Ledger, BRS, Final Accounts', 'icon': '📚', 'rubric': 'accounting'},
    'C': {'name': 'Module C: Practical Accounting & Office Work', 'desc': 'Bills, vouchers, cash/bank records, advances, audit & filing', 'icon': '🏢', 'rubric': 'practical'},
    'D': {'name': 'Module D: Taxation & Banking', 'desc': 'GST, ITC, TDS (194C/J/I), NEFT/RTGS, cheques & digital safety', 'icon': '💳', 'rubric': 'practical'},
    'E': {'name': 'Module E: Computer & MS Excel', 'desc': 'Excel formulas (SUM, IF, COUNTIF), sorting, billing, Tally & Word', 'icon': '💻', 'rubric': 'practical'},
    'F': {'name': 'Module F: MCED & Government Awareness', 'desc': 'MCED background, EDPs, District centres, schemes & discipline', 'icon': '🏛️', 'rubric': 'mced'},
    'G': {'name': 'Module G: Situational & Ethical Questions', 'desc': 'Disagreements, errors, cash mismatch, duplicate bills & integrity', 'icon': '⚖️', 'rubric': 'confidence'}
}

PLAN_14_DAYS = [
    {
        'day': 1,
        'title': 'Personal Introduction & Communication Assessment',
        'desc': 'मराठी आणि इंग्रजीत स्वतःचा प्रभावी व नैसर्गिक परिचय देणे. First impression आणि आवाज तपासणी.',
        'module': 'A',
        'targetQ': ['A1', 'A2', 'A3', 'A4'],
        'tips': 'रट्टा मारू नका. आत्मविश्वासाने आणि हसतमुखाने बोला. शिक्षण, कॉमर्स बॅकग्राउंड आणि कौशल्यांवर भर द्या.'
    },
    {
        'day': 2,
        'title': 'HR Questions & Confidence Building',
        'desc': 'Why MCED, Strengths/Weaknesses, handling pressure आणि करिअर उद्दिष्टे.',
        'module': 'A',
        'targetQ': ['A5', 'A6', 'A7', 'A8', 'A9', 'A10'],
        'tips': 'प्रामाणिक राहा. अशक्तता सांगताना ती सुधारण्यासाठी काय करताय ते सांगा.'
    },
    {
        'day': 3,
        'title': 'Accounting Fundamentals & Golden Rules',
        'desc': 'लेखांकनाची उद्दिष्टे, मूलभूत संकल्पना (Accrual, Going Concern), Types of Accounts आणि Golden Rules.',
        'module': 'B',
        'targetQ': ['B1', 'B2', 'B3', 'B4', 'B5'],
        'tips': 'Golden Rules चे उदाहरण स्वतःच्या शब्दांत आणि व्यवहारासह सांगा.'
    },
    {
        'day': 4,
        'title': 'Journal, Ledger & Trial Balance',
        'desc': 'Journal Entries, Ledger Posting, Balancing आणि Trial Balance चे महत्व व मर्यादा.',
        'module': 'B',
        'targetQ': ['B6', 'B7', 'B8', 'B9'],
        'tips': 'Trial Balance tally असणे म्हणजे हिशेब १००% बिनचूक असा अर्थ होत नाही, हे स्पष्ट करा.'
    },
    {
        'day': 5,
        'title': 'Cash Book, Vouchers & Practical Entries',
        'desc': 'Single, Double, Triple column Cash Book, Contra Entry, Petty Cash व Imprest System.',
        'module': 'B',
        'targetQ': ['B10', 'B11', 'B12'],
        'tips': 'Imprest System मध्ये दर महिन्याला सुरुवातीला ठराविक रक्कम का ठेवली जाते हे सांगा.'
    },
    {
        'day': 6,
        'title': 'Bank Reconciliation & Financial Statements',
        'desc': 'BRS ची गरज, फरक येण्याची कारणे, Trading, P&L Account आणि Balance Sheet.',
        'module': 'B',
        'targetQ': ['B13', 'B14', 'B15', 'B16', 'B17'],
        'tips': 'Cheques issued but not presented चा Cash book आणि Pass book वर काय परिणाम होतो ते समजवा.'
    },
    {
        'day': 7,
        'title': 'Depreciation, Adjustments & Rectification of Errors',
        'desc': 'SLM vs WDV Depreciation, Outstanding/Prepaid Expenses, Suspense Account आणि चुकांची दुरुस्ती.',
        'module': 'B',
        'targetQ': ['B18', 'B19', 'B20', 'B21', 'B22'],
        'tips': 'Office equipment वर Depreciation का आकारले जाते आणि Suspense Account कधी वापरतात ते स्पष्ट करा.'
    },
    {
        'day': 8,
        'title': 'Practical Accounts Office Situations',
        'desc': 'Bills तपासणी, Supporting Documents, Vouchers, Cheque Register, Advances आणि Audit तयारी.',
        'module': 'C',
        'targetQ': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'],
        'tips': 'सरकारी कार्यालयात प्रत्येक खर्चाला सँक्शन ऑर्डर आणि मूळ बिल का लागते यावर भर द्या.'
    },
    {
        'day': 9,
        'title': 'GST, TDS & Banking Fundamentals',
        'desc': 'GST (CGST/SGST/IGST), Input Tax Credit, TDS कलमे (194C, 194J), NEFT/RTGS आणि Cheque सुरक्षा.',
        'module': 'D',
        'targetQ': ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7'],
        'tips': 'Contractor बिलातून TDS कापणे आणि 15 अंकी GSTIN चा अर्थ स्पष्ट सांगा.'
    },
    {
        'day': 10,
        'title': 'Excel & Computer Knowledge in Accounts',
        'desc': 'SUM, AVERAGE, IF, SUMIF, COUNTIF, VLOOKUP, Payment sheets, Tally vouchers व Email drafting.',
        'module': 'E',
        'targetQ': ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7'],
        'tips': 'एक्सेलमध्ये एरर टाळण्यासाठी Data Validation आणि बॅकअप पद्धती सांगा.'
    },
    {
        'day': 11,
        'title': 'MCED Organisation & Government Awareness',
        'desc': 'MCED चे कार्य, उद्दिष्टे, EDPs, जिल्हा केंद्र, CMEGP, PMEGP आणि वित्तीय शिस्त.',
        'module': 'F',
        'targetQ': ['F1', 'F2', 'F3', 'F4', 'F5', 'F6'],
        'tips': 'MCED चे पूर्ण नाव, मुख्यालय (छत्रपती संभाजीनगर) आणि उद्योग विभागाशी संबंध लक्षात ठेवा.'
    },
    {
        'day': 12,
        'title': 'Situational & Ethical Scenarios',
        'desc': 'वरिष्ठांची अयोग्य सूचना, Cash mismatch, बँक फरक, दुहेरी पेमेंट आणि गोपनीयता.',
        'module': 'G',
        'targetQ': ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7'],
        'tips': 'पारदर्शकता, नम्रता, नियम आणि अधिकृत परवानगी या तत्वांना नेहमी प्राधान्य द्या.'
    },
    {
        'day': 13,
        'title': 'Full Mock Interview – Diagnostic Assessment (20 Marks)',
        'desc': 'पहिली संपूर्ण २० गुणांची प्रत्यक्ष मुलाखत. पॅनेल समोर १०-१२ प्रश्न, टायमर आणि थेट मूल्यमापन.',
        'module': 'MOCK',
        'targetQ': ['ALL'],
        'tips': 'घाबरू नका. जणू आपण प्रत्यक्ष पॅनेलसमोर बसलो आहोत अशा पद्धतीने शांतपणे उत्तर द्या.'
    },
    {
        'day': 14,
        'title': 'Weak-Area Revision & Final Mock Interview',
        'desc': 'कमकुवत मुद्यांची उजळणी, उच्चारण व देहबोली सुधारणा आणि अंतिम २०/२० टार्गेट मॉक.',
        'module': 'FINAL',
        'targetQ': ['WEAK'],
        'tips': 'शेवटची उजळणी! आत्मविश्वास, चेहऱ्यावर शांतता आणि स्पष्ट शब्दोच्चार ठेवा.'
    }
]

RUBRIC_CONFIG = {
    'accounting': {'name': 'Accounting Knowledge', 'marks': 6, 'desc': 'Golden rules, entries, BRS, final accounts & concepts'},
    'practical': {'name': 'Practical Accounting Skills', 'marks': 5, 'desc': 'Vouchers, bills, cash book, Excel, TDS, GST & office filing'},
    'mced': {'name': 'MCED & Govt Awareness', 'marks': 3, 'desc': 'MCED role, EDPs, district centres, government schemes & discipline'},
    'communication': {'name': 'Communication & Clarity', 'marks': 3, 'desc': 'Fluency, technical terminology, sentence clarity & listening'},
    'confidence': {'name': 'Confidence & Professional Behaviour', 'marks': 3, 'desc': 'Honesty, ethical judgement, calm demeanor & handling pressure'},
    'total': 20
}

# Let's verify python code runs and exports
print("Module builder configured")
