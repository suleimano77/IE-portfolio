# Suleiman: IE Career Build Plan (Oct 2026 to Sep 2027)

As of: 2026-10-20 (revision 11 of the source doc)

Goal: go from zero Excel/Python and one C course to a credible industrial engineering candidate with three defensible portfolio projects, two to three certificates, and a strong internship application by late 2027.

## The employer's verdict

Projects and certificates are tiebreakers. They separate candidates who already cleared the bar. They do not get you to the bar.

What gets you to the bar, in order of weight:

1. A real internship at a recognized company. Nothing on this list substitutes for it.
2. Evidence you can turn messy data into a decision. This is what the projects are for.
3. Language and communication. English for global firms, German for the firms your university feeds into.
4. GPA, roughly. Many graduate schemes filter at a threshold and then stop looking.
5. Certificates. Last. A Green Belt shows you sat an exam, not that you can run a project.

Current position: second year, one C course, no portfolio. That is a normal starting point with roughly two years of runway.

Two risks matter more than the empty portfolio:

- **Starting more than finishing.** Several past ideas (content clipping, burger kiosk, supercar importing, swing trading, a four-week Python plan) were opened and dropped. Three finished projects beat twelve explored ideas. Finish Phase 1 before reading Phase 3.
- **Discounting the German track.** A mandatory internship in Germany, with German built into the degree, is a structural advantage. B2 German would do more for employability than every project here combined.

Fit note: classic IE roles are floor-facing. If low social interaction is a real constraint, target operations analytics, supply chain analytics, or operations research. These are quantitative, screen-based, and well paid.

## Flagship projects

Three finished projects, built in this order.

### Flagship 1: Amman delivery route optimizer

Vehicle routing model for a food delivery fleet in Amman. Real road distances from OpenStreetMap, time windows, vehicle capacity, driver shift limits. Solve with Google OR-Tools. Compare against naive nearest-neighbour routing and report distance, time and fuel saved.

- Why employers care: vehicle routing is high-value applied optimization used across logistics and e-commerce.
- Proves: optimization modeling, Python, geospatial data, baseline benchmarking.

### Flagship 2: University exam timetabling

Model that schedules a GJU exam period with no student clashes, limited rooms, and minimum rest between a student's exams. Integer programming. Generate realistic enrollment data if the real data is unavailable.

- Why employers care: constraint satisfaction with a hard combinatorial core. Scheduling under constraints maps directly to production planning and workforce management.
- Proves: integer programming, constraint modeling, handling problems with no clean solution.

### Flagship 3: Automated time study from video

Record a repetitive manual task. Use Python with OpenCV or MediaPipe hand tracking to detect where each work element starts and ends, time them automatically, and output cycle time distribution and the bottleneck element.

- Why employers care: time study is the oldest IE tool and is still done with a stopwatch in most plants. Automating it shows fundamentals plus modern tooling.
- Proves: computer vision, Python, command of core IE method.

All three run on a laptop. None requires approaching a business or interviewing anyone.

**Framing rule:** present each project as a business case. State the problem, constraint, method, result as a number, and recommendation. A README that opens with "this reduces fleet distance 23%" reads like work. One that opens with "in this project I used OR-Tools" reads like homework.

## Skill stack (dependency order)

Each layer needs the one above it.

| # | Skill | Why it comes here | Free resource |
| --- | --- | --- | --- |
| 1 | Excel: formulas, pivot tables, lookups, charts | Operations teams run on it; first analysis tool | ExcelIsFun, Leila Gharani (YouTube) |
| 2 | Lean fundamentals: 8 wastes, process mapping, time study, takt time | Vocabulary of the discipline | Gemba Academy, Lean Enterprise Institute |
| 3 | Python: syntax, data structures, files, functions | C background speeds the start; everything below depends on it | CS50P (Harvard, free) |
| 4 | pandas: loading, cleaning, grouping, merging | Working layer of any analytics job | Kaggle Learn, Python for Data Analysis |
| 5 | Statistics: distributions, confidence intervals, regression basics | Needed to defend any number | StatQuest, Khan Academy |
| 6 | Optimization: linear and integer programming | Core of operations research; flagships 1 and 2 | PuLP docs, OR-Tools guides |
| 7 | Simulation: discrete event modeling | "What if we add a server" questions | SimPy documentation |
| 8 | SQL | How data is stored at any employer | SQLBolt, Mode SQL tutorial |
| 9 | Power BI or Tableau | How analysis reaches decision-makers | Microsoft Learn |

Outside the stack, two skills matter more than most of it:

- German to B2. Highest return for this specific situation.
- Clear written English. Recommendations are read before they are approved.

## Certificates

Buy a certificate only if it teaches something needed or passes an automated CV filter.

**Worth it**

| Certificate | When | Rough cost | Why |
| --- | --- | --- | --- |
| Lean Six Sigma Yellow Belt | Phase 1 | Low; varies by provider | Teaches the method behind every project. Compare CSSC, IASSC, ASQ |
| PCEP (Python Entry) | Phase 2 | Low | Confirms Python was learned, not just watched |
| Microsoft PL-300 (Power BI) | Phase 4 | Moderate | Proctored; appears in job postings |
| Lean Six Sigma Green Belt | Third year | Moderate to high | Only with a real project, ideally during internship |
| Goethe B1 then B2 (German) | Throughout | Moderate | Changes which companies will interview you |

**Skip for now**

- CSWA (SolidWorks): strong for mechanical engineers, marginal for IE.
- MATLAB certifications: free Onramp is fine; no employer hires an IE for MATLAB.
- PMP and CAPM: PMP needs documented experience; CAPM is expensive for a student.
- APICS CPIM and CSCP: valuable in supply chain but expensive; better paid for by an employer later.
- Most Coursera specializations: do them for learning, never pay for the certificate alone.
- Weekend certificates for about $15: recognized and slightly counted against you.

Forage simulations are free and useful for interview material. Pick operations, supply chain or analytics programs. List them under courses or projects, never under work experience.

## Phase 1: Foundations (weeks 1 to 12, late Oct 2026 to mid Jan 2027)

Budget 4 to 6 hours a week. Pause during exam weeks; do not quit.

| Week | Focus | Deliverable |
| --- | --- | --- |
| 1 | Excel: formulas, absolute references, IF logic | Rebuild a course problem set entirely in Excel |
| 2 | Excel: pivot tables and charts | Pivot a public dataset three ways |
| 3 | Excel: XLOOKUP, data cleaning, conditional formatting | Cleaned dataset from a messy source |
| 4 | Excel: Solver, simple product mix problem | Working profit-maximization model |
| 5 | Lean: 8 wastes, value stream mapping | Map a process you know, start to finish |
| 6 | Lean: time study, takt time, cycle time, OEE | Hand-time a repetitive task 30 times; chart distribution |
| 7 | Yellow Belt exam prep | Book the exam |
| 8 | Sit Yellow Belt exam | Certificate 1 done |
| 9 | Pick a supply chain dataset; define the question | One-page problem statement |
| 10 | Clean and analyze in Excel | Pivot tables, charts, finding |
| 11 | Write consulting-style report | 5 to 8 pages: problem, method, findings, recommendations |
| 12 | Publish; set up LinkedIn and GitHub | Warm-up project done; first LinkedIn post live |

**Warm-up project:** DataCo Smart Supply Chain on Kaggle. Question: why are deliveries late, and what should the company change? Break late deliveries down by region, shipping mode, category and order size. Recommend two or three actions with estimated impact.

**Side tasks:** one Forage simulation (operations or supply chain). Start German properly, not just to pass.

## Phase 2: Python and Flagship 1 (weeks 13 to 24, mid Jan to mid Apr 2027)

Expect the first four weeks of Python to feel slow. Push through.

| Week | Focus | Deliverable |
| --- | --- | --- |
| 13 to 14 | CS50P weeks 0 to 2: syntax, conditionals, loops | Problem sets, not just videos |
| 15 to 16 | CS50P weeks 3 to 5: functions, exceptions, libraries, tests | Working through problem sets |
| 17 | CS50P weeks 6 to 7: file I/O, regular expressions | Read and write CSVs |
| 18 | pandas: load, filter, group, merge | Redo Phase 1 Excel analysis in pandas |
| 19 | PCEP exam prep and sit it | Certificate 2 done |
| 20 | Vehicle routing problem; OR-Tools routing guides | Toy 5-stop solver that runs |
| 21 | Real Amman road distances via OpenStreetMap / OSRM | Distance matrix for 30 locations |
| 22 | Full model: capacity, time windows, shift limits | Solver returns valid routes |
| 23 | Naive baseline; measure the difference | Headline % distance saved |
| 24 | README, repo, route map visualization | Flagship 1 done, posted |

**Scope warning:** week 21 is where this project can eat the semester. If real road distances stall for more than a week, use straight-line distance times a 1.3 road factor, document it in the README, and move on.

Keep running in background: German. Do not start Flagship 2 early.

## Phase 3: Optimization and Flagship 2 (weeks 25 to 36, mid Apr to mid Jul 2027)

Weeks 25 to 28 overlap spring exams. The timeline is a guide, not a contract.

| Week | Focus | Deliverable |
| --- | --- | --- |
| 25 to 26 | Linear programming: formulation, constraints, duality basics | 10 LP problems by hand, then in PuLP |
| 27 to 28 | Integer programming: binary variables, big-M, assignment | Working shift-scheduling model |
| 29 | Statistics refresher | Defensible numbers |
| 30 | Define timetabling problem; generate enrollment data | Students, courses, rooms dataset |
| 31 to 32 | Formulate: clash, room capacity, rest constraints | Model in PuLP or OR-Tools |
| 33 | Solve, debug infeasibility, tune objectives | Valid timetable |
| 34 | Compare against real GJU schedule if obtainable | Measurable improvement claim |
| 35 | SimPy discrete-event queue simulation | Side exercise |
| 36 | Write-up, repo, README explaining constraints | Flagship 2 done, posted |

**Key lesson:** infeasibility is the point. Write about working out which constraint is impossible and whether to relax it. Interviewers probe there.

**Summer note:** weeks 33 to 36 fall in summer break, the highest-capacity window. German applications often open 9 to 12 months ahead, so research openings for the following year.

## Phase 4: Analytics, Flagship 3 and applications (weeks 37 to 48, Jul to Oct 2027)

| Week | Focus | Deliverable |
| --- | --- | --- |
| 37 to 38 | SQL: SELECT, JOIN, GROUP BY, subqueries, window functions | Query a sample database fluently |
| 39 to 40 | Power BI: data model, DAX basics, dashboard design | Dashboard from Phase 1 dataset |
| 41 | PL-300 prep and sit it | Certificate 3 done |
| 42 | OpenCV basics: video capture, frames, motion detection | Detect movement in test footage |
| 43 | MediaPipe hand tracking; define work elements | Hands tracked across a clip |
| 44 to 45 | Element-detection logic and timing output | Automatic cycle times from video |
| 46 | Validate against Phase 1 week 6 hand timings | Accuracy figure |
| 47 | Cycle time distribution, bottleneck element | IE analysis layer |
| 48 | README, demo video, write-up | Flagship 3 done, posted |

**In parallel from week 37:** internship applications. Build a list of 20 to 30 companies (German manufacturers, logistics operators, regional offices of global firms). Tailor the CV per application. Expect low response rates.

**Validation matters:** "My tool is within 4% of manual timing across 30 cycles" is the kind of sentence that gets hired.

**If behind schedule:** cut Flagship 3, not the applications.

## LinkedIn

Set up in Phase 1 week 12. Update at milestones, not weekly.

**Profile**

- Headline: "Industrial Engineering student | Operations Research & Supply Chain Analytics"
- About: three or four sentences on what you are learning, built, and seeking.
- Projects: each flagship, linked to its GitHub repo.
- Skills: only what you can defend under questioning.
- Photo: plain, well-lit, neutral background.

**Posting schedule**

| When | Post |
| --- | --- |
| Phase 1, week 8 | Yellow Belt earned, with what the method taught |
| Phase 1, week 12 | Warm-up analysis: question, finding, recommendation |
| Phase 2, week 24 | Flagship 1, lead with the number |
| Phase 3, week 36 | Flagship 2, lead with the constraint problem |
| Phase 4, week 41 | PL-300 passed, alongside the dashboard |
| Phase 4, week 48 | Flagship 3, with a short demo video |

**Post format:** four or five sentences. Problem, what you did, result as a number, what you learned, link. One clear visual. No hashtag walls, no "excited to share".

**Engagement:** connect with everyone from your program and any company you interact with. Comment substantively on operations-role posts. About 15 minutes a week.

## Priorities

1. Finishing one phase beats starting four.
2. German is the highest-return skill available. B2 changes which companies can hire you at all.
3. The internship is the actual goal. When choosing between finishing a project and preparing an application, choose the application.

Realistic target by October 2027: competent with real tools, three portfolio pieces you can defend, and a credible internship application. Being "highly sought after" comes from what you do during and after the placement.

## Sources

- Phase timing and certificate costs are approximate; verify current prices with each provider.
- No external pages were opened to build this plan beyond general knowledge of the named courses and tools.
