# MCED District Account Assistant — Practice Paper Series + Study App

For the written exam on **27 October 2026, 11:00 AM** (venue and documents in the app's "Exam Day" page). Syllabus (from the call letter): Book keeping & Basic Accounting & Modern tools, Taxation, Budget & Financial discipline, Banking, Current Affairs, Computer Knowledge.
**These are practice materials, not official MCED papers, patterns, marks schemes or predictions.** Scoring (1 mark per correct answer, no negative marking) is a transparent practice rule only.

## 1. The Study App (what Aishwarya uses on the phone)

Live link: **https://nilsan714.github.io/mced-practice-papers/** (works on any network). Local copy: `online_practice\server.py` (same app + auto-sync of progress on the same Wi-Fi).

| Section | What it does |
|---|---|
| Home | Countdown to the exam, personal message from Nilesh, next task, XP / level / streak, topic progress, badges |
| Plan | 8-day plan (19–27 Oct); tasks tick automatically when the work is done |
| Learn | 11 lessons (concepts → worked examples → interactive practice). A lesson is "understood" only after a **Concept Check** (5 questions, ≥4 right) |
| Practice | Practice mode (instant explanation), Exam mode (timed), Weak-questions quiz, **Revision** (re-tests earlier topics after ~20 hours) |
| More | Flashcards (74), Cheat sheet, Exam-day checklist, My progress (topic-wise Mastered/Learning/Weak), Report to Tutor, Tutor Dashboard, language switch (मराठी / English) |

### Tracking (for Nilesh)
* **Anywhere:** Aishwarya taps *More → Report to Tutor* → WhatsApp (or Copy). The message contains a readable summary + a code. Nilesh opens the app → *More → Tutor Dashboard* → pastes it. The dashboard shows plan %, streak, XP, per-paper scores, weak subtopics with the lesson to re-teach, recent attempts, idle warning, notes, CSV export, and one-tap WhatsApp messages (praise / nudge / weak-topic). Set Nilesh's WhatsApp number in *More* so reports go straight to him.
* **Same Wi-Fi:** run the local server; progress is saved automatically in `online_practice\progress\` and appears in the Tutor Dashboard (`/progress.csv` on the PC too).
* Progress is stored on her phone's browser; clearing browser data erases it (use *Report* regularly).

### Editing the personal messages / plan
Edit `_build\content\extras.py` (Marathi) and `_build\content\en\extras_en.py` (English: `PERSONAL`, `QUOTES`, `PLAN_TXT`, `TASK_TXT`, flashcards, cheat sheet), then run `python _build\rebuild_app.py`, commit and push. (`git add -A`, `git commit`, `git push`.)

## 2. Printable papers (for the tutor)

Order of use: Baseline (original 40-question file, untouched) → Paper 1 → Papers 2–5 (accounting core) → 6 Tax → 7 Budget → 8 Banking → 9 Computer/Excel → 10 Current Affairs → 11 Mixed mock.
Each folder `01_…`–`11_…` has: Student Question Paper (.docx + .pdf), Teacher Answer Key (.docx, tutor only), Remediation Notes (.docx).
Loop for each paper: question-only paper → solve without key → record answers → open key after submission → topic-wise analysis → explain mistakes → teach from Remediation Notes → short remedial quiz (≥4/5) → next topic.
`MCED_Practice_Performance_Tracker.xlsx` (tutor only; contains the key): Attempts (auto score/%), Topic_Accuracy (weakest subtopic + lesson), Error_Log (Conceptual / Calculation / Terminology / Careless), Retest, Baseline_40.

## 3. Files

| Item | Notes |
|---|---|
| `docs\` | The study app (static; served by GitHub Pages) + data in `docs\data` (Marathi) and `docs\data\en` (English) |
| `online_practice\server.py` | Local server for the same app; stores progress snapshots |
| `Question_Paper_Manifest.md/.json` | Every file with size + SHA-256, per-paper statistics, sources and verification status |
| `_build\` | Generators, question data (`content\p01–p11.py`, English in `content\en`), validators, `rebuild_app.py` |

## 4. Validation performed
Automated (`_build\validate.py`): numbering, 4 options, duplicates, invalid letters, near-duplicate questions across all papers, progressive difficulty, arithmetic re-computation of numerical questions, key-file consistency, no answer leaks in student DOCX/PDF, source references. English data (`_build\build_en.py`): same questions/answers/numbers/structure as the Marathi data. Excel formulas were tested in desktop Excel. The app was tested end-to-end in a browser (both languages, all screens, concept check, revision, report encode/decode, tutor import, live sync).

## 5. Limitations (please read)
* **No official pattern, question count or marks distribution is known.** The call letter gives only topics.
* Questions, answers and Marathi/English text were written by the AI and checked by automated arithmetic and self-review. **No independent subject-expert or native-language review was done** — have a commerce teacher skim the keys.
* **Changing facts are "as of 2026-10-19".** GST 2.0 (5/18/40% from 22 Sep 2025; PIB pages returned HTTP 403 to my tool, so it rests on search listings and several secondary sources), TDS rates/thresholds, Income-tax Act 2025/Tax Year, new-regime slabs, Union Budget capex ₹12.2 lakh crore, Census 2027 dates and the RBI Governor/CM are **secondary-sourced** and labelled in each key. Union and Maharashtra Budget figures were read from PRS. Static GK was not re-checked online. Recheck current-affairs items before the exam.
* Deliberately not asked: current repo rate and UPI limits (no official figure confirmed).
* The *Executive Summary* file mentions GST 12%/28% slabs, which were replaced from 22 Sep 2025; treat it as outdated.
* Baseline Q1 contains Gujarati text (original file, untouched).
* The public GitHub Pages site exposes all answers and explanations in its data files (it is a static site). It is meant for self-practice.
* The app has no login. Progress lives in the phone's browser; reports are shared by WhatsApp or the local network.
