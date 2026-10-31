# CHOKEPOINT

Status: not started. Planned for January to April 2027.

## The question

Since 2024 many container ships have avoided the Red Sea and gone around Africa instead, which adds weeks to the trip from Asia. Take an importer with one warehouse in Aqaba and one in Hamburg, both supplied from Asia. How much safety stock does it need in each, and when is it worth paying for a different route?

## How I plan to build it

I'll build it in steps, and each step should be usable on its own:

1. Load daily ship transit counts for Suez, Bab el-Mandeb and the Cape (IMF PortWatch) into DuckDB and turn them into lead-time distributions before and during the disruption. Set reorder points and safety stock that keep a 95% service level.
2. Forecast demand, comparing simple baselines with LightGBM on the M5 retail dataset.
3. Simulate ships, ports and warehouses in SimPy, and replay past and made-up closures.
4. Choose the sourcing split and buffer stock that minimise cost across those scenarios (PuLP).
5. Put it in a small Streamlit app where you can ask "what if the strait closes for 12 weeks?" and get the simulation's answer.

## Data

- IMF PortWatch: chokepoint transits and port calls
- M5 forecasting dataset (Kaggle)
