# 🚢 CHOKEPOINT: supply chain shock digital twin

> **Status: planned for Jan–Apr 2027.** This page states the problem. Results will replace the targets below as they arrive.

## The problem
Since 2024, attacks in the Red Sea have pushed container ships around the Cape of Good Hope, adding weeks to Asia–Europe and Asia–Middle East voyages. A fictional importer supplies two warehouses, **Aqaba (Jordan)** and **Hamburg (Germany)**, from Asian suppliers. How much buffer stock does it need, where, and when should it switch routes?

## Approach (built in rungs; each rung is shippable)
1. **Lead-time shock:** real chokepoint transit data (IMF PortWatch) in DuckDB → lead-time distributions before and during disruption → safety stock that holds 95% service.
2. **Forecasting:** statistical baselines vs LightGBM, backtested.
3. **Digital twin:** SimPy model of ships, ports and warehouses; replay historic and hypothetical closures.
4. **Optimization:** sourcing split, route mix and buffer stock that minimise cost across scenarios.
5. **Scenario analyst:** a Streamlit app where an LLM runs the twin to answer "what if" questions.

## Target headline
"Under a 12-week closure, the recommended policy holds 95% service at X% lower cost than a static policy."

## Data
- IMF PortWatch: daily chokepoint transits and port calls
- M5 retail demand (Kaggle), mapped to the importer's catalogue
