import time


def run_algorithm(algorithm, graph, start, goal, heuristic=None):
    start_time = time.perf_counter()

    if heuristic is not None:
        result = algorithm(graph, start, goal, heuristic)
    else:
        result = algorithm(graph, start, goal)

    end_time = time.perf_counter()

    result["execution_time"] = round(
        (end_time - start_time) * 1000,
        4
    )

    return result


def calculate_route_metrics(graph, route):
    distance = 0
    travel_time = 0
    traffic_score = 0

    for i in range(len(route) - 1):
        current = route[i]
        next_node = route[i + 1]

        for road in graph.get_neighbors(current):
            if road["destination"] == next_node:
                distance += road["distance"]
                travel_time += road["travel_time"]

                traffic_values = {
                    "low": 1,
                    "medium": 2,
                    "high": 3
                }

                traffic_score += traffic_values[
                    road["traffic"].lower()
                ]

                break

    return {
        "distance": distance,
        "travel_time": travel_time,
        "traffic_score": traffic_score
    }


def select_recommended_algorithm(
    results,
    optimization_mode
):
    successful_results = {
        name: result
        for name, result in results.items()
        if result["status"] == "success"
    }

    if not successful_results:
        return None

    if optimization_mode == "1":
        return min(
            successful_results,
            key=lambda x: successful_results[x]["distance"]
        )

    if optimization_mode == "2":
        return min(
            successful_results,
            key=lambda x: successful_results[x]["travel_time"]
        )

    if optimization_mode == "3":
        return min(
            successful_results,
            key=lambda x: successful_results[x]["traffic_score"]
        )

    return min(
        successful_results,
        key=lambda x: (
            successful_results[x]["cost"],
            successful_results[x]["execution_time"]
        )
    )


def display_comparison(results):
    print("\n")
    print("=" * 85)
    print("                    ALGORITHM COMPARISON")
    print("=" * 85)

    print(
        f"{'Algorithm':<28}"
        f"{'Cost':<12}"
        f"{'Distance':<12}"
        f"{'Time':<12}"
        f"{'Nodes':<10}"
    )

    print("-" * 85)

    for name, result in results.items():
        print(
            f"{name:<28}"
            f"{result['cost']:<12}"
            f"{result['distance']:<12}"
            f"{result['travel_time']:<12}"
            f"{result['nodes_explored']:<10}"
        )

    print("=" * 85)