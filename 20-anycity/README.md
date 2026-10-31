# 🚐 ANYCITY: electric last-mile fleet lab

> **Status: planned for Apr–Jul 2027.** This page states the problem. Results will replace the targets below as they arrive.

## The problem
Cities from Munich to Amman are pushing delivery fleets toward electric vans, which adds battery range and charging time to an already hard routing problem. Given *any* city, what is the smallest electric fleet that delivers on time, and how robust is that plan when traffic doesn't cooperate?

## Approach (built in rungs; each rung is shippable)
1. **Any-city routing:** OSMnx road network + generated demand → OR-Tools VRP with capacity and time windows, compared against a nearest-neighbour baseline.
2. **Electric constraints:** battery range, charging stations from OpenStreetMap, charging time.
3. **Stress test:** SimPy replays 1,000 days of random traffic and late orders.
4. **LLM dispatcher:** plain-language changes ("van 3 broke down, add 5 rush orders") → agent calls the solver, validates the result, explains trade-offs.
5. **Cross-city benchmark:** Amman vs Munich vs Hamburg. What makes the same fleet cost more in one city?

## Target headline
"Same deliveries, X% fewer vans, Y% on time under random traffic, in three cities."

## Data
- OpenStreetMap (road networks, charging stations, points of interest)
- Public population grids for demand generation
