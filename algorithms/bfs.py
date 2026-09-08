from collections import deque


def bfs(graph, start, goal):

    if start not in graph.graph:
        raise KeyError(f"Unknown source location: {start}")

    if goal not in graph.graph:
        raise KeyError(f"Unknown destination location: {goal}")

    queue = deque([(start, [start])])
    visited = set()
    nodes_explored = 0

    while queue:

        current, path = queue.popleft()

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
                queue.append(
                    (neighbor, path + [neighbor])
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
                total_cost += road["distance"]
                break

    return total_cost