import heapq
from core.cost_engine import calculate_road_cost


def a_star(graph, start, goal, heuristic):
    priority_queue = [(heuristic[start], 0, start, [start])]
    visited = set()
    nodes_explored = 0

    while priority_queue:
        f_cost, g_cost, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)
        nodes_explored += 1

        if current == goal:
            return {
                "route": path,
                "cost": round(g_cost, 2),
                "nodes_explored": nodes_explored,
                "status": "success"
            }

        for road in graph.get_neighbors(current):
            neighbor = road["destination"]

            if neighbor not in visited:
                road_cost = calculate_road_cost(
                    road["distance"],
                    road["travel_time"],
                    road["traffic"]
                )

                new_g_cost = g_cost + road_cost
                new_f_cost = new_g_cost + heuristic[neighbor]

                heapq.heappush(
                    priority_queue,
                    (
                        new_f_cost,
                        new_g_cost,
                        neighbor,
                        path + [neighbor]
                    )
                )

    return {
        "route": [],
        "cost": float("inf"),
        "nodes_explored": nodes_explored,
        "status": "no_path"
    }