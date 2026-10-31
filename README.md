# IE Portfolio

I'm an industrial engineering student at the German Jordanian University. This repo is where I learn in public and build three projects between November 2026 and October 2027.

Each project starts from a real operations problem and should end with a number and a recommendation, not just working code.

## Projects

**CHOKEPOINT** ([10-chokepoint](10-chokepoint/))
How much stock does an importer need when a shipping lane closes? I'll use real Red Sea and Suez transit data to model an importer supplying warehouses in Aqaba and Hamburg, then work out the inventory policy that keeps shelves stocked at the lowest cost.
Planned for January to April 2027.

**ANYCITY** ([20-anycity](20-anycity/))
Route planning for an electric delivery fleet in any city, built from OpenStreetMap. It handles battery range, charging and delivery windows, and tests each plan against bad traffic days. I'll compare Amman, Munich and Hamburg.
Planned for April to July 2027.

**GEMBA LENS** ([30-gemba-lens](30-gemba-lens/))
A time study from a video. It tracks my hands and posture while I do a repetitive task, times each step, scores ergonomic risk and drafts the work instructions. I'll check it against a stopwatch study I do by hand first.
Planned for July to October 2027.

## Foundations

Before the projects I'm working through Excel, Python, Lean basics and one warm-up analysis:

- [01-excel](01-excel/): formulas, pivot tables, Power Query, Solver
- [02-python-basics](02-python-basics/): CS50P problem sets
- [03-lean-time-study](03-lean-time-study/): process mapping and a 30-cycle manual time study
- [04-dataco-warmup](04-dataco-warmup/): why deliveries arrive late in the DataCo supply chain dataset

The week-by-week plan is in [00-plan/PLAN.md](00-plan/PLAN.md).

## Running the code

```bash
uv sync
uv run jupyter lab
```
