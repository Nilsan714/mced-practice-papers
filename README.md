# MCED District Account Assistant — Practice Paper Series

Practice papers for the written exam on **27 October 2026**. Hindi–Marathi mix with English accounting/banking/tax/computer terms.
**These are practice papers, not official MCED papers, patterns, marks schemes or predictions.** The scoring rule (1 mark per correct answer, no negative marking) is a transparent practice rule only.

## Order of use

1. **Baseline** — the original 40-question test is unchanged in `..\MCED_District_Account_Assistant_Baseline_MCQ_Test.docx`. Record the candidate's answers in the tracker sheet `Baseline_40` (or online paper "Baseline").
2. Read `01_Baseline_Analysis_Remediation\…_Remediation_Notes.docx` to map weak sections to papers; use Paper 1 as a re-test.
3. For each paper **2 → 11**, follow this loop:
   1. Candidate gets **only** `…_Student_Question_Paper` (DOCX/PDF, or the online link) and solves without the key.
   2. Tutor records answers in `MCED_Practice_Performance_Tracker.xlsx` → `Attempts`.
   3. Open `…_Teacher_Answer_Key.docx` only **after** submission. Tracker shows total + topic-wise accuracy + weakest subtopic + suggested lesson.
   4. Explain every wrong answer; tag the error type in `Error_Log` (Conceptual / Calculation / Terminology / Careless).
   5. Teach from `…_Remediation_Notes.docx` (basics → worked examples → practice), then a short 5-question remedial quiz.
   6. Move on only when the remedial quiz is ≥4/5; record the retest in `Retest`.
4. Paper 11 is the mixed mock; finish with it. Re-check all current-affairs facts close to the exam date.

Suggested sequence: 1 → 2 → 3 → 4 → 5 (accounting core), 6 (tax), 7 (budget), 8 (banking), 9 (computer/Excel), 10 (current affairs), 11 (mock).

## Folder contents

| Item | Notes |
|---|---|
| `01_…` to `11_…` | One folder per paper: Student Question Paper (.docx + .pdf), Teacher Answer Key (.docx), Remediation Notes (.docx) |
| `MCED_Practice_Performance_Tracker.xlsx` | Tutor-only (contains the key). Sheets: Attempts, Topic_Accuracy, Error_Log, Retest, Baseline_40, Papers, Key, SubMap |
| `online_practice\` | Local-network quiz for all papers (phone link). Run `python server.py` there |
| `Question_Paper_Manifest.md/.json` | Every file with size + SHA-256, per-paper statistics, sources and verification status |
| `_build\` | Generator scripts, question data (`content\p01–p11.py`), validators, `validation_report.json` |

## Online (phone) practice

```bash
cd "C:/Users/NILESH/Downloads/Accounting Paper/MCED_Practice_Paper_Series/online_practice" && python server.py
```

Phone and PC must be on the same Wi-Fi; open the `http://<PC-IP>:8000` address printed by the server. Results (host PC only): `http://localhost:8000/results` (+ `/results.csv`). The IP changes when the PC joins another network. Answers are scored on the server; correct answers and explanations are shown only after a candidate submits.

## Validation performed

Automated (`_build\validate.py`): numbering and 4 options per question, duplicate options, invalid answer letters, near-duplicate questions across all papers, progressive difficulty order, arithmetic re-computation for numerical questions (each result must match the marked option), answer/key-file consistency, student files not leaking answers or explanations (DOCX and PDF), source references resolving to a listed source. Excel formulas were tested in desktop Excel with sample responses (results matched an independent Python score; zero formula errors). The online scoring was tested end-to-end in a browser against an independent calculation.

## Limitations (please read)

* **No syllabus/notification was in the folder.** Topics follow the six sections of the baseline paper and the *Executive Summary* day plan. Nothing here claims an official pattern, count, weightage or cutoff.
* Questions, answers and Hindi–Marathi explanations were written by the AI and checked by automated arithmetic and a self-review. **No independent human subject-expert or native-language review was done** — please have a commerce teacher skim the keys, especially Marathi wording.
* **Changing facts are as of 2026-10-19.** PIB pages returned HTTP 403 to the fetch tool, so GST 2.0 (5/18/40%, 22 Sep 2025) rests on search listings plus multiple secondary sources. TDS rates/thresholds, Income-tax Act 2025 ("Tax Year", 1 Apr 2026), new-regime slabs, Union Budget capex ₹12.2 lakh crore, Census 2027 dates and the RBI Governor/CM office-holders come from **secondary sources** and are labelled so in each key. Union Budget and Maharashtra Budget figures were read from PRS documents. Static GK (Articles, dates, IFSC, cheque validity, etc.) was not re-checked online.
* Deliberately **not** asked: current repo rate (only secondary reports found) and UPI transaction limits (no official figure confirmed).
* The *Executive Summary* file mentions GST slabs 12%/28%; these were replaced from 22 Sep 2025. Treat that file's tax examples as outdated.
* Baseline Q1 contains Gujarati text; this is in the original file and was left untouched.
* PDFs were produced by Word; layout was inspected on sample pages (not every page of every PDF).
* The online quiz has no login and stores results in `online_practice\results.jsonl` on the PC; it is meant for a trusted home/classroom network only.
