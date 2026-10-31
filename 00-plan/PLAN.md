# Suleiman: IE Career Build Plan, v12 (Oct 2026 to Sep 2027)

As of: 2026-10-31. Revises v11 (2026-10-20). The goal, the employer's verdict, the three flagships, the German track and the LinkedIn plan are unchanged. This version changes **how** you learn and **when** Python starts.

## What changed from v11 and why

| Change | Why |
| --- | --- |
| Excel cut from 4 weeks to 2, focused on what operations jobs actually test | Excel isn't outdated as a workplace tool. Operations, supply chain and finance teams in Jordan and Germany still run on it, and job postings list it. It is outdated as your main analysis tool, so learn it to a working level and move on. |
| Python starts in week 3, not week 13 | With an AI tutor the slow first month gets shorter. Ten extra weeks of Python is worth more than a third Excel week. |
| Warm-up project done in Python (Jupyter + pandas), summarised in Excel and Power BI | You build the skill the flagships need from day one instead of doing the analysis twice. |
| PCEP dropped | Three public GitHub repos prove Python better than an entry exam. That frees a week and the exam fee. |
| SQL learned with DuckDB on your own project data | It's the same SQL, but on data you already understand, inside the same notebook. |
| Each flagship ships with a small Streamlit web app | A recruiter can click a link and use the tool. That beats reading a README. |
| New learning method (below) replaces "watch the video, copy it" | The bottleneck isn't access to information anymore. It's understanding what you build. |

## The learning method: build first, then ask

The old way was to watch a tutorial, copy the code and end up with something that works but that you can't explain. The new loop for every skill:

1. **Read the goal, not the solution.** One short doc page or a 10-minute video at most, just to know what the tool is.
2. **Attempt it yourself first**, even badly. Set a 30-minute limit before asking for help.
3. **Ask Claude as a tutor, not a code generator.** In Claude Code, turn on the *Learning* output style. Claude then leaves key pieces for you to write and explains its choices. Ask "why", "what breaks if", "what's the alternative".
4. **Explain it back.** Before each commit, write 3 lines in the notebook on what the code does and why. Rule: **never commit code you cannot explain line by line.** Interviewers will ask.
5. **Get a review.** Ask Claude to review your notebook as a senior analyst would: wrong assumptions, weak numbers, unclear charts.
6. **Ship it.** Commit to GitHub at the end of every session, even unfinished work.

Use AI to go faster, not to skip understanding. In an interview you are on your own, so the explaining back in step 4 is what counts.

## Toolkit (all free)

| Tool | Use |
| --- | --- |
| Claude Code (this app) | Tutor, code reviewer, sets up projects, runs your code, pushes to GitHub |
| Python via `uv` + Jupyter (in VS Code) | Every analysis and every flagship |
| Git + GitHub CLI (`gh`) | Version control. Claude can create repos, commit and push for you |
| **GitHub Student Developer Pack** | Apply with your GJU email: free Copilot Pro, GitHub Pages, cloud credits and more |
| pandas, matplotlib/plotly | Analysis and charts |
| DuckDB | SQL directly on CSVs and pandas data |
| PuLP, Google OR-Tools | Optimization (Flagships 1 and 2) |
| SimPy | Discrete-event simulation |
| OpenCV, MediaPipe | Flagship 3 |
| Streamlit (+ Streamlit Community Cloud) | Free hosted demo apps for each flagship |
| Excel (with Power Query and Solver) | Workplace standard; summary layer |
| Power BI Desktop (free on Windows) | Dashboards; PL-300 |
| Kaggle | Datasets and free Kaggle Learn micro-courses |
| Anki or a similar app + Goethe materials | German, every day, 20 minutes |

## Phase 1: Foundations + Python start (weeks 1 to 12, Nov 2026 to Jan 2027)

4 to 6 hours a week. Pause during exams; don't quit.

| Week | Focus | Deliverable |
| --- | --- | --- |
| 1 | Setup: Python, VS Code, Git, GitHub account, Student Pack. Excel: formulas, absolute refs, IF, XLOOKUP, pivot tables | First repo `ie-portfolio` live; one course problem set rebuilt in Excel |
| 2 | Excel: Power Query cleaning, charts, Solver product-mix model | Working Solver model (keep it; you'll rebuild it in PuLP in Phase 3) |
| 3 to 4 | Python basics (CS50P weeks 0 to 2, problem sets), with Claude in Learning mode | Problem sets in repo |
| 5 | Lean: 8 wastes, value stream mapping, takt, cycle time, OEE | VSM of a process you know |
| 6 | Time study: hand-time a repetitive task 30 times; analyse in Python | Cycle-time histogram (baseline for Flagship 3) |
| 7 to 8 | Yellow Belt prep and exam; Python functions and files (CS50P weeks 3 to 6) | Certificate 1 |
| 9 | pandas basics (Kaggle Learn); DataCo problem statement | One-page problem statement |
| 10 | DataCo late-delivery analysis in Jupyter | Breakdown by region, mode, category, order size |
| 11 | Write a consulting-style report + one-page Excel/Power BI summary | Report with 2 to 3 recommendations and estimated impact |
| 12 | Publish; LinkedIn setup; first post | Warm-up project done |

Side tasks: one Forage simulation (operations or supply chain). German daily.

## Phase 2: Flagship 1, Amman delivery route optimizer (weeks 13 to 24, mid Jan to mid Apr 2027)

| Week | Focus | Deliverable |
| --- | --- | --- |
| 13 to 14 | Finish CS50P weeks 7 to 9 (regex, OOP, tests) | Tests running on your own code |
| 15 | Statistics essentials (StatQuest): distributions, CIs, regression | Stats section added to DataCo report |
| 16 | VRP concepts; OR-Tools routing guide | Toy 5-stop solver |
| 17 to 18 | Amman road distances via OSRM / OpenStreetMap | 30-location distance matrix |
| 19 to 20 | Capacity, time windows, shift limits | Valid routes |
| 21 | Nearest-neighbour baseline; measure savings | Headline % saved |
| 22 to 23 | Streamlit app: pick orders, see routes on a map | Live demo link |
| 24 | README as business case; LinkedIn post | Flagship 1 done |

Scope warning (unchanged): if real road distances stall for more than a week, use straight-line distance × 1.3, document it and move on. Phase 2 now has 2 spare weeks compared with v11, so absorb delays here, not in Phase 3.

## Phase 3: Flagship 2, exam timetabling (weeks 25 to 36, mid Apr to mid Jul 2027)

| Week | Focus | Deliverable |
| --- | --- | --- |
| 25 to 26 | LP: formulation, duality; rebuild Phase 1 Solver model in PuLP | 10 LP problems in PuLP |
| 27 to 28 | Integer programming: binaries, big-M, assignment | Shift-scheduling model |
| 29 | SQL with DuckDB on DataCo + Flagship 1 data | Queries notebook, including window functions |
| 30 | Define the timetabling problem; generate enrollment data | Dataset |
| 31 to 32 | Clash, room-capacity and rest constraints (OR-Tools CP-SAT) | Model |
| 33 | Solve, debug infeasibility | Valid timetable + infeasibility write-up |
| 34 | Compare with the real GJU schedule if obtainable; Streamlit viewer | Improvement claim |
| 35 | SimPy queue simulation (side exercise) | Notebook |
| 36 | README, post. Research German internship openings for 2028 | Flagship 2 done |

## Phase 4: Analytics, Flagship 3 and applications (weeks 37 to 48, Jul to Oct 2027)

| Week | Focus | Deliverable |
| --- | --- | --- |
| 37 to 38 | Power BI data model, DAX, dashboard from Flagship 1/2 outputs | Dashboard |
| 39 | PL-300 prep and exam | Certificate 2 |
| 40 to 41 | OpenCV + MediaPipe hand tracking | Hands tracked across a clip |
| 42 to 43 | Element detection and timing | Automatic cycle times |
| 44 | Validate against week 6 hand timings | Accuracy figure |
| 45 | Distribution + bottleneck; Streamlit upload-a-video demo | IE analysis layer |
| 46 | README, demo video, post | Flagship 3 done |
| 47 to 48 | Buffer | |

From week 37, in parallel: list 20 to 30 target companies, tailor your CV and apply. If you're behind, cut Flagship 3, not the applications.

## Certificates (revised)

| Certificate | When | Status |
| --- | --- | --- |
| Lean Six Sigma Yellow Belt | Phase 1 | Keep |
| ~~PCEP~~ | | Dropped: the GitHub portfolio proves it |
| Microsoft PL-300 | Phase 4 | Keep |
| Goethe B1 then B2 | Throughout | Keep: the highest return on this list |
| Green Belt | Third year, during internship | Keep |

## Priorities (unchanged)

1. Finishing one phase beats starting four.
2. German to B2.
3. The internship is the goal. When you have to choose, the application beats the project.
