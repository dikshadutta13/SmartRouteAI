import matplotlib.pyplot as plt


def plot_algorithm_comparison(results):

    algorithms = list(results.keys())

    costs = [
        results[algorithm]["cost"]
        for algorithm in algorithms
    ]

    nodes = [
        results[algorithm]["nodes_explored"]
        for algorithm in algorithms
    ]

    execution_times = [
        results[algorithm]["execution_time"]
        for algorithm in algorithms
    ]

    distances = [
        results[algorithm]["distance"]
        for algorithm in algorithms
    ]

    travel_times = [
        results[algorithm]["travel_time"]
        for algorithm in algorithms
    ]

    plt.figure(figsize=(10, 6))
    plt.bar(algorithms, costs)
    plt.title("Route Cost Comparison")
    plt.xlabel("Algorithm")
    plt.ylabel("Cost")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig("route_cost_comparison.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.bar(algorithms, nodes)
    plt.title("Nodes Explored Comparison")
    plt.xlabel("Algorithm")
    plt.ylabel("Nodes Explored")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig("nodes_explored_comparison.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.bar(algorithms, execution_times)
    plt.title("Execution Time Comparison")
    plt.xlabel("Algorithm")
    plt.ylabel("Execution Time (ms)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig("execution_time_comparison.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.bar(algorithms, distances)
    plt.title("Distance Comparison")
    plt.xlabel("Algorithm")
    plt.ylabel("Distance (km)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig("distance_comparison.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.bar(algorithms, travel_times)
    plt.title("Travel Time Comparison")
    plt.xlabel("Algorithm")
    plt.ylabel("Travel Time (minutes)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig("travel_time_comparison.png")
    plt.close()