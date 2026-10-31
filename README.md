<div align="center">

# Suleiman Qaryouti

**Industrial Engineering · Operations Research · AI for Operations**

German Jordanian University · building in public, Nov 2026 to Oct 2027

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![OR-Tools](https://img.shields.io/badge/OR--Tools-optimization-4285F4?logo=google&logoColor=white)
![SimPy](https://img.shields.io/badge/SimPy-simulation-6E4C9E)
![DuckDB](https://img.shields.io/badge/DuckDB-SQL-FFF000?logo=duckdb&logoColor=black)
![MediaPipe](https://img.shields.io/badge/MediaPipe-vision-0097A7)
![Streamlit](https://img.shields.io/badge/Streamlit-apps-FF4B4B?logo=streamlit&logoColor=white)

</div>

> Classic industrial engineering methods (optimization, simulation, time study, inventory theory) with AI as the interface and the sensor. Every project ends in a number and a recommendation.

---

## Flagship projects

### 🚢 [CHOKEPOINT](10-chokepoint/): supply chain shock digital twin
*What happens to a company's shelves when a shipping lane closes?*

Real Red Sea / Suez transit data drives a digital twin of an importer supplying **Aqaba 🇯🇴 and Hamburg 🇩🇪** from Asia. It measures how disruptions stretch lead times, forecasts demand, and optimizes the inventory policy that holds service level at the lowest cost. An LLM scenario analyst answers "what if" questions by running the twin.

`DuckDB` `pandas` `LightGBM` `SimPy` `PuLP` `inventory theory` `LLM tool use` · **Status: planned (Jan–Apr 2027)**

### 🚐 [ANYCITY](20-anycity/): electric last-mile fleet lab
*Type any city. Get an optimized electric delivery fleet, stress-tested.*

It pulls any city's road network from OpenStreetMap, generates realistic demand, and routes an **electric** van fleet with battery range, charging stops and time windows. Plans are stress-tested against 1,000 random traffic days, and a dispatcher can change them in plain language. Benchmarked on **Amman, Munich and Hamburg**.

`OR-Tools` `OSMnx` `E-VRP` `SimPy` `LLM agents` `geospatial` · **Status: planned (Apr–Jul 2027)**

### 🎥 [GEMBA LENS](30-gemba-lens/): AI time study and auto-written standard work
*Point a camera at a manual task. Get the time study, ergonomic risk and work instructions.*

Hand and pose tracking split a video into work elements, time every cycle and find the bottleneck. It scores **REBA ergonomic risk** frame by frame, balances the task across stations to meet a takt time, and has a vision-language model write the standard work instructions.

`OpenCV` `MediaPipe` `time study` `REBA` `line balancing` `multimodal AI` · **Status: planned (Jul–Oct 2027)**

---

## Skills map

| | CHOKEPOINT | ANYCITY | GEMBA LENS |
| --- | :-: | :-: | :-: |
| Optimization (LP / IP / VRP) | ● | ● | ● |
| Discrete-event simulation | ● | ● | |
| Statistics & ML forecasting | ● | ● | ● |
| SQL | ● | | |
| Geospatial | | ● | |
| Computer vision | | | ● |
| Lean, time study, ergonomics | | | ● |
| LLM agents / multimodal AI | ● | ● | ● |
| Apps & dashboards | ● | ● | ● |

## Foundations log

| | Folder | Status |
| --- | --- | --- |
| Excel: formulas, pivots, Power Query, Solver | [01-excel](01-excel/) | 🔄 in progress |
| Python (CS50P problem sets) | [02-python-basics](02-python-basics/) | ⏳ |
| Lean & manual time study (30 cycles) | [03-lean-time-study](03-lean-time-study/) | ⏳ |
| DataCo late-delivery analysis (warm-up) | [04-dataco-warmup](04-dataco-warmup/) | ⏳ |

Full roadmap: [00-plan/PLAN.md](00-plan/PLAN.md)

## Run it

```bash
uv sync
uv run jupyter lab
```

---

<div align="center">

📫 [LinkedIn](#) · Open to operations, supply chain and OR internships for 2028 · Deutsch: learning toward B2

</div>
