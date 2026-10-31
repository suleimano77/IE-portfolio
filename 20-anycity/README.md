# ANYCITY

Status: not started. Planned for April to July 2027.

## The question

Delivery companies are switching to electric vans, which adds battery range and charging time to an already hard routing problem. For a given city, what's the smallest electric fleet that still delivers on time, and does the plan hold up when traffic is bad?

## How I plan to build it

1. Download the road network for any city with OSMnx, generate realistic orders, and solve the routing with capacity and time windows in OR-Tools. Compare against a simple nearest-neighbour plan.
2. Add battery range, charging stations from OpenStreetMap, and charging time.
3. Replay 1,000 days of random traffic and late orders in SimPy to see how often the plan breaks.
4. Let a dispatcher change the plan in plain language ("van 3 broke down, add 5 rush orders"). A language model turns the request into solver inputs; the solver does the routing, and the result is checked before it's shown.
5. Compare Amman, Munich and Hamburg and explain why the same fleet costs more in some cities than others.

## Data

- OpenStreetMap: roads, charging stations, points of interest
- Public population grids for placing orders
