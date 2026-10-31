# Suleiman: IE Career Build Plan, v13 (Nov 2026 to Oct 2027)

As of: 2026-10-31. Revises v12. The employer's verdict, Phase 1, German, certificates and LinkedIn are unchanged. **v13 replaces all three flagships** with international, AI-era projects that each combine a hard industrial engineering method with modern tooling.

## The employer's verdict (unchanged)

What gets you hired, in order: a real internship → evidence you turn messy data into decisions → English and German → GPA → certificates. Projects are the second item. They have to be finished, defensible and led by a number.

## Design rules for every flagship

1. **International by default.** Any city, any port, any task. Amman appears as one demo next to German cities, because those are the employers your degree feeds into.
2. **The IE core decides; AI is the interface or the sensor.** Solvers optimize, simulations test, statistics prove. LLMs translate, explain and label. Never let an LLM make the decision itself.
3. **Every project ends in a number and a recommendation.**
4. **Laptop only, public data, zero interviews.**
5. **Ladder scope.** Each project has an MVP rung that is publishable on its own. Upgrades come after the MVP ships. If time runs out, you stop on a finished rung, never halfway between two.

## Flagship 1: CHOKEPOINT, a supply chain shock digital twin

*What happens to a company's shelves when a shipping lane closes?*

Since 2024 the Red Sea crisis has rerouted global shipping around Africa. Aqaba, Jordan's only port, sits at the end of the same lane. CHOKEPOINT models a fictional importer with two warehouses (Aqaba, Jordan and Hamburg, Germany) sourcing from Asia. It uses real chokepoint transit data to measure how disruptions stretch lead times, then finds the inventory policy that keeps service level up at the lowest cost.

| Rung | What it adds | Skills |
| --- | --- | --- |
| MVP | Real Suez / Bab el-Mandeb / Cape transit data (IMF PortWatch) queried with DuckDB → lead-time distributions before and during disruption → safety stock and reorder points that hold 95% service under each scenario | SQL, pandas, statistics, inventory theory |
| 2 | Demand forecasting (statsforecast baselines vs LightGBM on M5 retail data mapped to the importer's catalogue) | Machine learning, time series, backtesting |
| 3 | SimPy digital twin of the network: ships, ports, warehouses; replay 2023, 2024 and "Suez closed 12 weeks" scenarios | Discrete-event simulation |
| 4 | Optimization: choose sourcing split, route mix and buffer stock to minimise total cost across scenarios (PuLP) | Stochastic / scenario optimization |
| 5 | Streamlit dashboard + an LLM "scenario analyst": ask "what if Bab el-Mandeb closes in March?" and it runs the twin and writes the briefing | LLM tool use, app deployment |

Headline target: "Under a 12-week closure, policy X holds 95% service at Y% lower cost than the static policy."

## Flagship 2: ANYCITY, an electric last-mile fleet lab

*Type any city. Get an optimized electric delivery fleet, stress-tested.*

ANYCITY downloads any city's road network from OpenStreetMap and generates realistic delivery demand from population and point-of-interest data. It then plans routes for an **electric** van fleet with battery range, charging stops, time windows and shift limits. The routes are stress-tested under random traffic, and a dispatcher can change the plan in plain language. It runs on Amman, Munich and Hamburg side by side.

| Rung | What it adds | Skills |
| --- | --- | --- |
| MVP | OSMnx road network for any city → capacitated VRP with time windows in OR-Tools → savings vs nearest-neighbour baseline | Optimization, geospatial Python |
| 2 | EV constraints: battery range, charging stations from OSM, charging time | Advanced routing (E-VRP) |
| 3 | SimPy stress test: 1,000 days of random traffic and late orders; report on-time % and the robust plan | Simulation, robustness |
| 4 | LLM dispatcher: "van 3 broke down, add 5 rush orders in Schwabing" → agent calls the solver, validates the output, explains trade-offs | LLM agents with tool calls and guardrails |
| 5 | Cross-city benchmark: why does the same fleet cost more in Amman than in Munich? (street layout, hills, density) | Comparative analysis, storytelling |

Headline target: "Same deliveries, X% fewer vans, on-time Y% under random traffic, in three cities."

## Flagship 3: GEMBA LENS, AI time study and auto-written standard work

*Point a laptop camera at a manual task. Get the time study, ergonomic risk and the work instructions written for you.*

Record yourself doing a repetitive assembly task (LEGO kits, packing, cable assembly). GEMBA LENS tracks hands and body, splits the video into work elements, times every cycle, scores ergonomic risk on every frame and identifies the bottleneck element. A vision-language model then writes **standard work instructions** with screenshots: the document a factory engineer spends days producing by hand.

| Rung | What it adds | Skills |
| --- | --- | --- |
| MVP | MediaPipe hand tracking → element boundaries → cycle-time distribution and bottleneck; validated against your week 6 stopwatch study | Computer vision, time study, validation |
| 2 | REBA ergonomic risk score from body pose, frame by frame, with the riskiest moments flagged | Ergonomics, pose estimation |
| 3 | Vision-language model labels elements and drafts standard work instructions with keyframes | Multimodal AI |
| 4 | Line balancing: split the task across 2 to 4 stations to meet a takt time; show the balance efficiency | Line balancing, Lean |
| 5 | Streamlit app: upload a video, get the full report as a PDF | Productising |

Headline target: "Within X% of manual timing across 30 cycles; instructions generated in minutes instead of days."

## Skill coverage

| Skill | Phase 1 | CHOKEPOINT | ANYCITY | GEMBA LENS |
| --- | --- | --- | --- | --- |
| Excel / Solver | ● | | | |
| Lean, time study | ● | | | ● |
| Python, pandas | ● | ● | ● | ● |
| SQL (DuckDB) | | ● | | |
| Statistics | ● | ● | ● | ● |
| ML forecasting | | ● | | |
| Inventory theory | | ● | | |
| Linear / integer programming | | ● | ● | ● |
| Vehicle routing | | | ● | |
| Discrete-event simulation | | ● | ● | |
| Geospatial | | | ● | |
| Computer vision | | | | ● |
| Ergonomics | | | | ● |
| LLM agents / multimodal AI | | ● | ● | ● |
| Dashboards & apps (Streamlit, Power BI) | ● | ● | ● | ● |

## Phase 1: Foundations + Python start (weeks 1 to 12, Nov 2026 to Jan 2027)

4 to 6 hours a week. Pause during exams; don't quit.

| Week | Focus | Deliverable |
| --- | --- | --- |
| 1 | Setup (done). Excel: formulas, absolute refs, IF, XLOOKUP, pivot tables | One course problem set rebuilt in Excel |
| 2 | Excel: Power Query cleaning, charts, Solver product-mix model | Working Solver model |
| 3 to 4 | Python basics (CS50P weeks 0 to 2), Claude in Learning mode | Problem sets in repo |
| 5 | Lean: 8 wastes, value stream mapping, takt, cycle time, OEE | VSM of a process you know |
| 6 | Time study: hand-time a repetitive task 30 times; analyse in Python. **Film it too**; this is GEMBA LENS's validation data | Histogram + video saved |
| 7 to 8 | Yellow Belt prep and exam; CS50P weeks 3 to 6 | Certificate 1 |
| 9 | pandas (Kaggle Learn); DataCo problem statement | One-page problem statement |
| 10 | DataCo late-delivery analysis in Jupyter | Breakdown by region, mode, category, order size |
| 11 | Consulting-style report + one-page Excel / Power BI summary | 2 to 3 recommendations with impact |
| 12 | Publish; LinkedIn setup; first post | Warm-up done |

## Phase 2: CHOKEPOINT (weeks 13 to 24, mid Jan to mid Apr 2027)

| Week | Focus | Deliverable |
| --- | --- | --- |
| 13 to 14 | Finish CS50P (regex, OOP, tests); SQL basics in DuckDB | Tests on own code; SQL notebook |
| 15 | Statistics: distributions, CIs, bootstrapping | Stats added to DataCo report |
| 16 | PortWatch data in DuckDB; disruption timeline | Transit-count charts per chokepoint |
| 17 | Lead-time distributions per scenario | Fitted distributions |
| 18 | Safety stock / reorder point under variable lead time | **MVP shipped**: README + post |
| 19 to 20 | Forecasting: baselines vs LightGBM, backtesting | Rung 2 |
| 21 | SimPy network twin | Rung 3 |
| 22 | Scenario optimization in PuLP | Rung 4 |
| 23 | Streamlit + LLM scenario analyst | Rung 5 |
| 24 | Final write-up, demo GIF, LinkedIn post | Flagship 1 done |

## Phase 3: ANYCITY (weeks 25 to 36, mid Apr to mid Jul 2027)

Weeks 25 to 28 overlap spring exams. The timeline is a guide.

| Week | Focus | Deliverable |
| --- | --- | --- |
| 25 to 26 | LP / IP fundamentals in PuLP: formulation, binaries, big-M | 10 practice models |
| 27 | OSMnx: road networks, distance matrices for any city | Matrix for 3 cities |
| 28 | Demand generation from population + POI data | Realistic order sets |
| 29 to 30 | OR-Tools CVRPTW + nearest-neighbour baseline | **MVP shipped** |
| 31 | EV range + charging constraints | Rung 2 |
| 32 | SimPy traffic stress test | Rung 3 |
| 33 | LLM dispatcher with tool calls + output validation | Rung 4 |
| 34 | Amman vs Munich vs Hamburg benchmark | Rung 5 |
| 35 | Streamlit deploy | Live demo |
| 36 | Write-up + post. Research German internships for 2028 | Flagship 2 done |

## Phase 4: GEMBA LENS + applications (weeks 37 to 48, Jul to Oct 2027)

| Week | Focus | Deliverable |
| --- | --- | --- |
| 37 to 38 | Power BI: dashboard over CHOKEPOINT outputs | Dashboard |
| 39 | PL-300 exam | Certificate 2 |
| 40 to 41 | OpenCV + MediaPipe hands and pose | Tracked clip |
| 42 to 43 | Element segmentation, cycle timing, validation vs week 6 | **MVP shipped** |
| 44 | REBA ergonomic scoring | Rung 2 |
| 45 | VLM element labels + standard work instructions | Rung 3 |
| 46 | Line balancing to a takt time | Rung 4 |
| 47 | Streamlit upload-a-video app, demo video | Rung 5 |
| 48 | Buffer | |

From week 37, in parallel: list 20 to 30 target companies and apply. **If you're behind, cut rungs, never the applications.**

## Certificates

| Certificate | When |
| --- | --- |
| Lean Six Sigma Yellow Belt | Phase 1 |
| Microsoft PL-300 | Phase 4 |
| Goethe B1 → B2 | Throughout: highest return on this list |
| Green Belt | Third year, during internship |

## Running costs

Everything is free except LLM calls: under $10 for the whole year with Claude Haiku, or $0 with a local model through Ollama.

## Priorities (unchanged)

1. Finish a rung before starting the next. Finish a flagship before starting the next.
2. German to B2.
3. The internship is the goal.
