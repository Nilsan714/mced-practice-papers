"""Study-app content: daily plan, flashcards, cheat sheet, mnemonics, motivation. Facts reuse the verified paper content."""

EXAM = dict(date='2026-10-27T11:00:00+05:30', venue='M.C.E.D., A-38, Opp. MIDC Quarters, MIDC Area, Near Railway Station, Ch. Sambhajinagar',
            carry=['Original ओळखपत्र (PAN Card / Driving License / Aadhaar Card / Election Card)', '2 passport size photo', 'Pen', 'Admit/call letter ची प्रत किंवा फोटो'],
            note='पत्रानुसार: कोणताही प्रवास/इतर भत्ता मिळणार नाही. Syllabus: Book keeping & Basic Accounting & Modern tools, Taxation, Budget & Financial discipline, Banking, Current Affairs, Computer Knowledge.')

# day plan: date, title, tasks [ (id, type, ref, label) ] type: lesson|cards|quiz|practice|weak|cheat|exam
PLAN = [
    dict(date='2026-10-19', title='Day 1 — सुरुवात: Basics ओळख', goal='Accounting का गरजेचे ते समजून घ्या: A = L + C', tasks=[
        ('d1a', 'quiz', 0, 'Baseline test (40 प्रश्न) — आत्ता कुठे आहात ते पाहा (अंदाज लावला तरी चालेल)'),
        ('d1b', 'lesson', 2, 'Lesson 2: Accounting Fundamentals वाचा + Concept check पास करा'), ('d1c', 'cards', 'Accounting', 'Flashcards: Accounting (10 मिनिटे)'),
        ('d1d', 'practice', 2, 'Paper 2 Practice mode सोडवा'), ('d1e', 'quiz', 2, 'Paper 2 Exam (वेळेसह) — किमान 80% मिळवा')]),
    dict(date='2026-10-20', title='Day 2 — Debit/Credit आणि Journal', goal='3 Golden Rules पक्के करा', tasks=[
        ('d2a', 'lesson', 3, 'Lesson 3: Debit, Credit, Journal वाचा + Concept check पास करा'), ('d2b', 'cards', 'Accounting', 'Flashcards: Accounting'),
        ('d2c', 'practice', 3, 'Paper 3 Practice mode'), ('d2d', 'weak', 0, 'Weak-topic quiz (चुकलेल्या प्रश्नांची उजळणी)'), ('d2e', 'quiz', 3, 'Paper 3 Exam (वेळेसह) — किमान 80% मिळवा')]),
    dict(date='2026-10-21', title='Day 3 — Ledger, Cash Book, Trial Balance', goal='Posting, balancing आणि TB समजून घ्या', tasks=[
        ('d3a', 'lesson', 4, 'Lesson 4: Ledger/Cash Book/TB वाचा + Concept check पास करा'), ('d3b', 'practice', 4, 'Paper 4 Practice mode'),
        ('d3c', 'cards', 'Accounting', 'Flashcards: Accounting'), ('d3d', 'weak', 0, 'Weak-topic quiz'), ('d3e', 'revise', 0, 'उजळणी: आधी शिकलेले (Revision quiz)'), ('d3f', 'quiz', 4, 'Paper 4 Exam (वेळेसह) — किमान 80% मिळवा')]),
    dict(date='2026-10-22', title='Day 4 — BRS, Depreciation, Final Accounts', goal='Gross/Net Profit आणि Balance Sheet जमवा', tasks=[
        ('d4a', 'lesson', 5, 'Lesson 5: BRS/Depreciation/Final Accounts वाचा + Concept check पास करा'), ('d4b', 'practice', 5, 'Paper 5 Practice mode'),
        ('d4c', 'cheat', 0, 'Cheat sheet वाचा (सूत्रे)'), ('d4d', 'weak', 0, 'Weak-topic quiz'), ('d4e', 'revise', 0, 'उजळणी: आधी शिकलेले (Revision quiz)'), ('d4f', 'quiz', 5, 'Paper 5 Exam (वेळेसह) — किमान 80% मिळवा')]),
    dict(date='2026-10-23', title='Day 5 — Taxation आणि Budget', goal='GST, ITC, TDS आणि Deficits', tasks=[
        ('d5a', 'lesson', 6, 'Lesson 6: Taxation वाचा + Concept check पास करा'), ('d5b', 'practice', 6, 'Paper 6 Practice'),
        ('d5c', 'lesson', 7, 'Lesson 7: Budget वाचा + Concept check पास करा'), ('d5d', 'practice', 7, 'Paper 7 Practice'), ('d5e', 'cards', 'Taxation', 'Flashcards: Taxation + Budget'), ('d5f', 'revise', 0, 'उजळणी: आधी शिकलेले (Revision quiz)'), ('d5g', 'quiz', 6, 'Paper 6 Exam (वेळेसह) — किमान 80% मिळवा'), ('d5h', 'quiz', 7, 'Paper 7 Exam (वेळेसह) — किमान 80% मिळवा')]),
    dict(date='2026-10-24', title='Day 6 — Banking आणि Computer', goal='Full forms, NEFT/RTGS/UPI आणि Excel formulas', tasks=[
        ('d6a', 'lesson', 8, 'Lesson 8: Banking वाचा + Concept check पास करा'), ('d6b', 'practice', 8, 'Paper 8 Practice'),
        ('d6c', 'lesson', 9, 'Lesson 9: Computer/Excel वाचा + Concept check पास करा'), ('d6d', 'practice', 9, 'Paper 9 Practice'), ('d6e', 'cards', 'Banking', 'Flashcards: Banking + Computer'), ('d6f', 'revise', 0, 'उजळणी: आधी शिकलेले (Revision quiz)'), ('d6g', 'quiz', 8, 'Paper 8 Exam (वेळेसह) — किमान 80% मिळवा'), ('d6h', 'quiz', 9, 'Paper 9 Exam (वेळेसह) — किमान 80% मिळवा')]),
    dict(date='2026-10-25', title='Day 7 — Current Affairs + कमकुवत भाग', goal='Budget 2026-27 चे आकडे आणि कमी गुणांचे topics', tasks=[
        ('d7a', 'lesson', 10, 'Lesson 10: Current Affairs वाचा + Concept check पास करा'), ('d7b', 'practice', 10, 'Paper 10 Practice'),
        ('d7c', 'quiz', 1, 'Paper 1 Re-test (Exam mode) — किमान 80% मिळवा'), ('d7d', 'weak', 0, 'Weak-topic quiz'), ('d7e', 'cards', 'Current Affairs', 'Flashcards: Current Affairs'), ('d7f', 'revise', 0, 'उजळणी: सर्व शिकलेले (Revision quiz)'), ('d7g', 'quiz', 10, 'Paper 10 Exam (वेळेसह) — किमान 80% मिळवा')]),
    dict(date='2026-10-26', title='Day 8 — Mock आणि विश्रांती', goal='Paper 11 वेळ लावून; नवीन काही शिकू नका', tasks=[
        ('d8a', 'quiz', 11, 'Paper 11 Mock (Exam mode, 40 मिनिटे) — किमान 80% मिळवा'), ('d8b', 'weak', 0, 'चुकलेल्या प्रश्नांची उजळणी'),
        ('d8c', 'cheat', 0, 'Cheat sheet शेवटचे वाचन'), ('d8d', 'exam', 0, 'उद्याची तयारी (ID, photo, venue) तपासा'), ('d8e', 'revise', 0, 'शेवटची उजळणी (Revision quiz)')]),
    dict(date='2026-10-27', title='परीक्षेचा दिवस — 11:00 AM', goal='शांत रहा. सोपे प्रश्न आधी. तुम्ही तयार आहात.', tasks=[
        ('d9a', 'exam', 0, 'Checklist: ID, 2 photo, pen, 10:30 पर्यंत पोहोचा'), ('d9b', 'cheat', 0, 'निघण्यापूर्वी Cheat sheet 5 मिनिटे')]),
]

# flashcards: (topic, front, back)
FLASH = [
    ('Accounting', 'Personal Account चा नियम?', 'Debit the Receiver, Credit the Giver (जो घेतो Dr, जो देतो Cr)'),
    ('Accounting', 'Real Account चा नियम?', 'Debit what comes in, Credit what goes out (आत येते Dr, बाहेर जाते Cr)'),
    ('Accounting', 'Nominal Account चा नियम?', 'Debit all Expenses & Losses, Credit all Incomes & Gains'),
    ('Accounting', 'Accounting Equation?', 'Assets = Liabilities + Capital'),
    ('Accounting', 'Capital कसे काढतात?', 'Capital = Assets − Liabilities'),
    ('Accounting', 'Closing Capital?', 'Opening Capital + Profit − Drawings'),
    ('Accounting', 'Drawings म्हणजे?', 'Owner ने personal कामासाठी काढलेले पैसे/माल. हा Expense नाही; Capital कमी करतो.'),
    ('Accounting', 'Debtors आणि Creditors फरक?', 'Debtors = आपल्याला पैसे येणे (Asset). Creditors = आपण द्यायचे (Liability).'),
    ('Accounting', 'Cash purchase ची entry?', 'Purchases A/c Dr; To Cash A/c'),
    ('Accounting', 'उधार विक्री (credit sale) ची entry?', 'Debtor A/c Dr; To Sales A/c'),
    ('Accounting', 'Debtor कडून cash मिळाले — entry?', 'Cash A/c Dr; To Debtor A/c'),
    ('Accounting', 'Creditor ला payment — entry?', 'Creditor A/c Dr; To Cash A/c'),
    ('Accounting', 'Discount Allowed vs Discount Received?', 'Allowed = खर्च/नुकसान (Debit). Received = उत्पन्न (Credit). Trade discount नोंदवत नाहीत.'),
    ('Accounting', 'Trial Balance चा उद्देश?', 'Ledger चे Dr आणि Cr totals जुळतात का ते तपासणे. सर्व चुका पकडत नाही (Omission, Principle).'),
    ('Accounting', 'TB मध्ये Debit balance कोणाचा?', 'Assets, Expenses, Drawings. Credit: Liabilities, Capital, Incomes.'),
    ('Accounting', 'SLM Depreciation सूत्र?', '(Cost − Scrap value) ÷ Life  → दरवर्षी समान'),
    ('Accounting', 'WDV Depreciation?', 'Book Value × % → दरवर्षी कमी होते'),
    ('Accounting', 'Gross Profit काढा', 'Net Sales − COGS;  COGS = Opening Stock + Purchases − Closing Stock'),
    ('Accounting', 'Net Profit काढा', 'Gross Profit + Other Incomes − Indirect Expenses'),
    ('Accounting', 'Outstanding Expense?', 'या वर्षाचा पण देणे बाकी. Expense = Paid + Outstanding. Balance Sheet मध्ये Liability.'),
    ('Accounting', 'Prepaid Expense?', 'पुढील कालावधीचा आधी भरलेला खर्च. Expense = Paid − Prepaid. Asset.'),
    ('Accounting', 'BRS: Unpresented cheque चा परिणाम?', 'आपण दिला पण bank मध्ये नाही → Passbook balance जास्त (CB + unpresented).'),
    ('Accounting', 'Contra Entry म्हणजे?', 'Cash ↔ Bank व्यवहार; दोन्ही Cash Book मध्ये; दोन्ही बाजूला "C".'),
    ('Accounting', 'Imprest System?', 'ठराविक रक्कम Petty Cashier ला; महिनाअखेरीस खर्च झालेली रक्कम reimburse.'),
    ('Accounting', 'Closing Stock Balance Sheet मध्ये?', 'Current Asset'),
    ('Taxation', 'GST full form आणि प्रकार?', 'Goods and Services Tax — Indirect tax'),
    ('Taxation', 'Intra-state supply वर GST?', 'CGST + SGST (प्रत्येकी अर्धा दर, उदा. 18% = 9% + 9%)'),
    ('Taxation', 'Inter-state supply वर GST?', 'IGST (पूर्ण दर)'),
    ('Taxation', 'GST दर (22 Sep 2025 पासून)?', 'मुख्य 5% आणि 18%; निवडक sin/luxury वर 40%. (12%/28% आता नाहीत)'),
    ('Taxation', 'Net GST किती भरायचा?', 'Output GST − Input GST (ITC)'),
    ('Taxation', 'GSTIN?', '15-अंकी GST Identification Number'),
    ('Taxation', 'TDS म्हणजे?', 'Tax Deducted at Source — पैसे देणारा कर कापतो आणि सरकारला भरतो'),
    ('Taxation', 'PAN?', 'Permanent Account Number (Income Tax)'),
    ('Taxation', 'नवीन Income-tax Act?', 'Income-tax Act, 2025 — 1 एप्रिल 2026 पासून; "Tax Year" संकल्पना'),
    ('Taxation', 'Direct vs Indirect tax?', 'Income Tax = Direct. GST/Customs/Excise = Indirect.'),
    ('Budget', 'Financial Year?', '1 एप्रिल ते 31 मार्च'),
    ('Budget', 'Revenue vs Capital Expenditure?', 'Revenue = नियमित खर्च (Salary, वीज). Capital = Asset निर्मिती (Land, Machinery).'),
    ('Budget', 'Revenue Deficit?', 'Revenue Expenditure − Revenue Receipts'),
    ('Budget', 'Fiscal Deficit?', 'Total Expenditure − Total Receipts (Borrowings वगळून)'),
    ('Budget', 'Primary Deficit?', 'Fiscal Deficit − Interest Payments'),
    ('Budget', 'Variance: Adverse/Favourable?', 'खर्च Budget पेक्षा जास्त = Adverse. कमी = Favourable.'),
    ('Budget', 'Article 112 / 114 / 266 / 267?', '112 = Budget (Annual Financial Statement); 114 = Appropriation Bill; 266 = Consolidated Fund; 267 = Contingency Fund'),
    ('Budget', 'Segregation of Duties?', 'मंजुरी, नोंद आणि cash हाताळणी वेगवेगळ्या व्यक्तींकडे'),
    ('Budget', 'Voucher म्हणजे?', 'Payment/receipt चा लेखी पुरावा. Voucher शिवाय payment नको.'),
    ('Banking', 'NEFT?', 'National Electronic Funds Transfer — 24x7, half-hourly batches (RBI FAQ)'),
    ('Banking', 'RTGS?', 'Real Time Gross Settlement — किमान ₹2,00,000, कमाल मर्यादा नाही, 24x7 (RBI FAQ)'),
    ('Banking', 'UPI?', 'Unified Payments Interface (NPCI). पैसे मिळवायला PIN लागत नाही.'),
    ('Banking', 'IMPS?', 'Immediate Payment Service — instant 24x7 (NPCI: ₹5 लाख/व्यवहार, SMS/IVR वगळता)'),
    ('Banking', 'IFSC?', '11 characters: पहिली 4 अक्षरे bank, 5 वे 0, शेवटची 6 branch'),
    ('Banking', 'Cheque ची वैधता?', '3 महिने (नंतर stale cheque)'),
    ('Banking', 'A/c Payee crossing?', 'रक्कम फक्त payee च्या खात्यातच जमा; cash मिळत नाही'),
    ('Banking', 'Repo Rate / CRR?', 'Repo = RBI कडून banks ना कर्ज दर. CRR = ठेवींचा भाग RBI कडे cash ठेवणे.'),
    ('Banking', 'KYC?', 'Know Your Customer'),
    ('Banking', 'Simple Interest / Compound Interest?', 'SI = P×R×T ÷ 100;  A = P(1 + r)ⁿ'),
    ('Banking', 'RBI स्थापना / HQ?', '1 एप्रिल 1935; मुख्यालय मुंबई'),
    ('Computer', 'Excel मध्ये बेरीज, सरासरी, मोठे, लहान?', '=SUM(), =AVERAGE(), =MAX(), =MIN()'),
    ('Computer', 'IF आणि COUNTIF/SUMIF?', '=IF(अट, खरे, खोटे);  COUNTIF = अटीनुसार मोजा;  SUMIF = अटीनुसार बेरीज'),
    ('Computer', 'VLOOKUP/XLOOKUP?', 'Key (उदा. ID) वरून table मधील माहिती शोधतो'),
    ('Computer', '$B$2 म्हणजे?', 'Absolute reference — formula copy केला तरी B2 बदलत नाही'),
    ('Computer', 'Ctrl+C / X / V / Z / Y / S?', 'Copy / Cut / Paste / Undo / Redo / Save'),
    ('Computer', 'Excel formula कशाने सुरू?', '= (बरोबर चिन्ह)'),
    ('Computer', 'CC आणि BCC?', 'CC = Carbon Copy. BCC = Blind (इतरांना दिसत नाही).'),
    ('Computer', 'OTP/PIN/Link चा नियम?', 'OTP/PIN कोणालाही देऊ नका; अनोळखी link उघडू नका; official channel ने तपासा. Cyber helpline 1930.'),
    ('Computer', 'File extensions?', '.docx Word | .xlsx Excel | .pptx PowerPoint | .pdf PDF | .txt Notepad'),
    ('Computer', 'RAM vs Hard disk?', 'RAM = तात्पुरती working memory. Hard disk/SSD = कायमस्वरूपी storage.'),
    ('Current Affairs', 'Union Budget 2026-27 तारीख?', '1 फेब्रुवारी 2026 (PRS)'),
    ('Current Affairs', 'Union Budget 2026-27 मुख्य आकडे (PRS)?', 'खर्च ₹53,47,315 कोटी; Fiscal Deficit GDP च्या 4.3%; Revenue Deficit 1.5%; Receipts (borrowing वगळून) ₹36,51,547 कोटी'),
    ('Current Affairs', 'Maharashtra Budget 2026-27 (PRS)?', '6 मार्च 2026; Fiscal Deficit ₹1,50,491 कोटी = GSDP चे 2.8%; Revenue Deficit ₹40,552 कोटी = 0.7%'),
    ('Current Affairs', 'MGNREGA ची जागा?', 'VB-G RAM G (PRS नुसार)'),
    ('Current Affairs', 'Census 2027?', 'पहिली पूर्ण digital जनगणना. Phase I: 1 Apr–30 Sep 2026. Phase II: Feb 2027; reference date 1 मार्च 2027'),
    ('Current Affairs', 'RBI Governor / Maharashtra CM (Oct 2026)?', 'Sanjay Malhotra / Devendra Fadnavis (as of 2026-10-19; पुन्हा तपासा)'),
    ('Current Affairs', 'संविधान लागू / Maharashtra Day / GST सुरू?', '26 जाने 1950 / 1 मे 1960 / 1 जुलै 2017'),
    ('Current Affairs', 'Article 148 / 280 आणि NITI Aayog?', '148 = CAG; 280 = Finance Commission; NITI Aayog = Planning Commission ची जागा (2015)'),
    ('Current Affairs', 'GST 2.0 कधी?', '56th GST Council 3 Sep 2025; दर 22 Sep 2025 पासून (5% / 18% / 40%)'),
]

CHEAT = [
    dict(title='1) Golden Rules', rows=[['Personal', 'Receiver Dr, Giver Cr'], ['Real', 'आत येते Dr, बाहेर जाते Cr'], ['Nominal', 'खर्च/नुकसान Dr, उत्पन्न/नफा Cr']]),
    dict(title='2) मुख्य सूत्रे', rows=[['Accounting Equation', 'A = L + C'], ['Capital', 'A − L'], ['Closing Capital', 'Opening + Profit − Drawings'], ['SLM Depreciation', '(Cost − Scrap) ÷ Life'], ['WDV', 'Book Value × %'],
        ['Gross Profit', 'Net Sales − (Op. Stock + Purchases − Cl. Stock)'], ['Net Profit', 'GP + Incomes − Indirect Exp.'], ['Cash Book closing', 'Opening + Receipts − Payments'], ['Variance %', 'Variance ÷ Budget × 100'],
        ['Simple Interest', 'P × R × T ÷ 100'], ['Net GST', 'Output GST − Input GST'], ['GST (exclusive)', 'Value × rate'], ['GST (inclusive)', 'Total ÷ (1 + rate)'], ['TDS net payment', 'Payment − (Payment × TDS%)']]),
    dict(title='3) Entries (पटापट)', rows=[['Cash purchase', 'Purchases Dr / Cash Cr'], ['Cash sale', 'Cash Dr / Sales Cr'], ['Credit purchase', 'Purchases Dr / Supplier Cr'], ['Credit sale', 'Debtor Dr / Sales Cr'],
        ['Asset खरेदी', 'Asset Dr / Cash-Bank Cr'], ['Expense paid', 'Expense Dr / Cash Cr'], ['Outstanding exp.', 'Expense Dr / Outstanding Cr'], ['Prepaid', 'Prepaid Dr / Expense Cr'], ['Bad debt', 'Bad Debts Dr / Debtor Cr'], ['Drawings', 'Drawings Dr / Cash-Purchases Cr']]),
    dict(title='4) Tax आणि Budget', rows=[['Intra-state', 'CGST + SGST'], ['Inter-state', 'IGST'], ['GST दर (22 Sep 2025 पासून)', '5% / 18% / 40% विशेष'], ['Revenue Deficit', 'Rev. Exp − Rev. Receipts'], ['Fiscal Deficit', 'Total Exp − Receipts (borrowing वगळून)'], ['Primary Deficit', 'FD − Interest'], ['Articles', '112 Budget | 114 Appropriation | 266 Consolidated | 267 Contingency | 280 Finance Comm. | 148 CAG']]),
    dict(title='5) Banking आणि Computer', rows=[['NEFT', '24x7, batches'], ['RTGS', 'किमान ₹2,00,000, real-time, 24x7'], ['IMPS', 'instant 24x7'], ['UPI', 'NPCI; पैसे मिळवायला PIN नको'], ['IFSC', '11 characters'], ['Cheque', 'वैधता 3 महिने'],
        ['Excel', 'SUM AVERAGE MAX MIN IF COUNTIF SUMIF VLOOKUP, $B$2 fixed'], ['Safety', 'PIN/OTP शेअर नको; Cyber helpline 1930']]),
    dict(title='6) Current Affairs आकडे (as of 2026-10-19)', rows=[['Union Budget 2026-27', '1 Feb 2026 | खर्च ₹53,47,315 cr | FD 4.3% GDP | RD 1.5%'], ['Maharashtra Budget 2026-27', '6 Mar 2026 | FD ₹1,50,491 cr (2.8% GSDP) | RD 0.7%'], ['Census 2027', 'पहिली digital; ref. date 1 Mar 2027'],
        ['RBI Governor / CM', 'Sanjay Malhotra / Devendra Fadnavis']]),
]

MNEMONICS = {
    2: ['A = L + C: जे आपल्याकडे आहे (Assets) ते एकतर इतरांचे (Liabilities) किंवा आपले (Capital).', 'Capital काढायचे? नेहमी Assets − Liabilities.'],
    3: ['"घेणारा Debit, देणारा Credit" (Personal). "आत Debit, बाहेर Credit" (Real). "खर्च Debit, कमाई Credit" (Nominal).', 'प्रत्येक entry मध्ये Total Dr = Total Cr तपासा.'],
    4: ['Ledger = खाते; Posting मध्ये बाजू बदलत नाही.', 'Balance c/d लहान बाजूला; पुढच्या कालावधीला b/d उलट बाजूला.'],
    5: ['BRS: "आधी Cash Book adjust, मग Passbook गाठा."', 'Outstanding = देणे (Liability); Prepaid = आधी दिलेले (Asset).'],
    6: ['"एकाच राज्यात CGST+SGST, दोन राज्यात IGST."', 'Output − Input = भरायचा GST. दर 5% / 18% (विशेष 40%).'],
    7: ['Revenue = रोजचा खर्च; Capital = Asset बनवणारा.', 'Deficit सूत्रे: Revenue → Rev.Exp−Rev.Rec; Fiscal → Exp−Receipts(no borrowing); Primary → FD−Interest.'],
    8: ['NEFT = batches, RTGS = ₹2 लाख+ real-time, IMPS = instant.', 'OTP/PIN कोणालाही नाही — बँक कधीही मागत नाही.'],
    9: ['Formula = सुरू "="; Range B2:B10; $ म्हणजे fixed.', 'SUM बेरीज, AVERAGE सरासरी, MAX मोठे, MIN लहान, COUNTIF अट मोजा.'],
    10: ['आकडे पाठ करू नका: कोण-केव्हा-किती, 3 मुद्दे लिहा.', 'पद/दर बदलू शकतात — "as of तारीख" लक्षात ठेवा.'],
    11: ['सोपे प्रश्न आधी, गणित नंतर. प्रत्येक गणित options शी तपासा.'],
    1: ['प्रत्येक विभाग (A–F) ची टक्केवारी पाहा; सर्वात कमी भाग आधी शिका.'],
}

QUOTES = [
    '{name}, प्रत्येक दिवशी थोडे शिकणे हेच मोठे यश आहे. आज एक पाऊल पुढे!',
    'चुका म्हणजे शिकण्याची संधी. जे चुकले ते आज शिकले, म्हणजे परीक्षेत बरोबर येईल.',
    'Basics पक्के केले की अर्धी लढाई जिंकली. A = L + C — हे लक्षात असू द्या.',
    '{name}, तुम्ही करू शकता! रोज 2–3 तास, मन लावून.',
    'एकाच दिवसात सगळे येणार नाही, पण रोज थोडे थोडे येते. सातत्य ठेवा.',
    'आज जितके कठीण वाटते, उद्या तितके सोपे होईल. हार मानू नका.',
    'Flashcards 10 मिनिटे — रोज केले तर लक्षात राहते. आज केले का?',
    'तयारी करणारा नेहमी पुढे असतो. {name}, आजचा प्लॅन पूर्ण करा!',
    'शांत मनाने सोपे प्रश्न आधी सोडवा. आत्मविश्वास ठेवा.',
    'एक टक्का सुधारणा रोज केली तरी 8 दिवसांत फरक दिसतो. पाहा!',
]
PRAISE = ['शाब्बास!', 'उत्तम!', 'छान काम!', 'अप्रतिम!', 'असेच चालू ठेवा!']
LEVELS = [(0, 'Beginner 🌱'), (100, 'Learner 📘'), (300, 'Achiever ⭐'), (600, 'Pro 🚀'), (1000, 'Topper 🏆')]

# personal messages from the tutor/partner (editable). {name}=student, {from}=sender, {pct}=score
PERSONAL = dict(
    sender='Nilshi',
    daily=[
        'गुड मॉर्निंग {name} ☀️ आज थोडं थोडं शिकूया. मी तुझ्यासोबत आहे.',
        '{name}, माझा तुझ्यावर पूर्ण विश्वास आहे. आज जमेल तेवढं कर, बाकी आपण बघू 💪',
        'चुकलं तरी चालेल, शिकत राहा. तू पास होणारच!',
        'आज एक paper सोडव आणि मला सांग किती आले. मी वाट बघतोय',
        'तू जे करतेयस त्याचा मला खूप अभिमान आहे 🌟 असंच चालू ठेव!',
        'थोडा ब्रेक घे, पाणी पी, मग पुन्हा सुरू कर. तू करू शकतेस!',
        'रोज थोडं थोडं — बस इतकंच. बाकी सगळं आपोआप जमतं. 🍀',
    ],
    high='वाह {name}! {pct}% — मला माहीतच होतं तू करशील! 🎉',
    mid='छान {name}! {pct}% आले. चुका बघूया, पुढच्या वेळी अजून चांगलं होईल 👍',
    low='काळजी करू नकोस {name}, मी आहे ना. {pct}% हरकत नाही — आपण मिळून हे topic पक्कं करू 💪',
    day='आजचा प्लॅन पूर्ण! तू ग्रेट आहेस. आता थोडा आराम कर.',
    streak='{n} दिवस सलग! मला खूप अभिमान आहे तुझा 🔥',
    eve='उद्या तुझा दिवस आहे {name}. आज लवकर झोप, काही नवीन शिकू नकोस. मी तुझ्यासोबत आहे. All the best! 🍀',
    exam='आज सगळं छान होईल. शांत राहा, सोपे प्रश्न आधी. तुझं बेस्ट दे!',
    wa_praise='{name}, तुझं {what} बघितलं — खूप छान! असंच चालू ठेव 💪',
    wa_nudge='{name}, आज अजून काही सोडवलंस का? एखादा paper करूया का?',
    wa_weak='{name}, "{topic}" थोडा कमकुवत दिसतोय ({v}%). आज आपण हा एकत्र पक्का करूया',
)
