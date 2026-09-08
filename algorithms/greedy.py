import heapq
from core.cost_engine import calculate_road_cost


def greedy_best_first_search(graph, start, goal, heuristic):
    priority_queue = [(heuristic[start], start, [start])]
    visited = set()
    nodes_explored = 0

    while priority_queue:
        _, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)
        nodes_explored += 1

        if current == goal:
            return {
                "route": path,
                "cost": calculate_path_cost(graph, path),
                "nodes_explored": nodes_explored,
                "status": "success"
            }

        for road in graph.get_neighbors(current):
            neighbor = road["destination"]

            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (
                        heuristic[neighbor],
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


def calculate_path_cost(graph, path):
    total_cost = 0

    for i in range(len(path) - 1):
        current = path[i]
        next_node = path[i + 1]

        for road in graph.get_neighbors(current):
            if road["destination"] == next_node:
                total_cost += calculate_road_cost(
                    road["distance"],
                    road["travel_time"],
                    road["traffic"]
                )
                break

    return round(total_cost, 2)