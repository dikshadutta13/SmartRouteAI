import heapq
from core.cost_engine import calculate_road_cost


def ucs(graph, start, goal):
    priority_queue = [(0, start, [start])]
    visited = set()
    nodes_explored = 0

    while priority_queue:
        cost, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)
        nodes_explored += 1

        if current == goal:
            return {
                "route": path,
                "cost": round(cost, 2),
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

                new_cost = cost + road_cost

                heapq.heappush(
                    priority_queue,
                    (new_cost, neighbor, path + [neighbor])
                )

    return {
        "route": [],
        "cost": float("inf"),
        "nodes_explored": nodes_explored,
        "status": "no_path"
    }