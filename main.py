import os

from core.map_loader import load_city_map
from core.menu import display_menu, get_menu_choice
from core.input_handler import (
    get_location,
    get_optimization_mode
)
from core.traffic import update_traffic

from algorithms.bfs import bfs
from algorithms.ucs import ucs
from algorithms.greedy import greedy_best_first_search
from algorithms.astar import a_star

from core.comparator import (
    run_algorithm,
    calculate_route_metrics,
    select_recommended_algorithm,
    display_comparison
)

from core.performance import save_performance_report
from core.visualization import plot_algorithm_comparison
from core.performance import (
    save_performance_report,
    load_performance_report
)

from core.visualization import plot_algorithm_comparison

HEURISTIC = {
    "A": 8,
    "B": 6,
    "C": 7,
    "D": 4,
    "E": 5,
    "F": 2,
    "G": 0
}


def calculate_results(city, source, destination):

    results = {}

    results["BFS"] = run_algorithm(
        bfs,
        city,
        source,
        destination
    )

    results["Uniform Cost Search"] = run_algorithm(
        ucs,
        city,
        source,
        destination
    )

    results["Greedy Best-First Search"] = run_algorithm(
        greedy_best_first_search,
        city,
        source,
        destination,
        HEURISTIC
    )

    results["A* Search"] = run_algorithm(
        a_star,
        city,
        source,
        destination,
        HEURISTIC
    )

    for result in results.values():

        if result["status"] == "success":

            metrics = calculate_route_metrics(
                city,
                result["route"]
            )

            result.update(metrics)

        else:

            result["distance"] = float("inf")
            result["travel_time"] = float("inf")
            result["traffic_score"] = float("inf")

    return results


def find_route(city):

    locations = city.graph.keys()

    print("\nAVAILABLE LOCATIONS")
    print("-" * 40)
    print(", ".join(sorted(locations)))

    source = get_location(
        "\nEnter source location: ",
        locations
    )

    destination = get_location(
        "Enter destination location: ",
        locations
    )

    while destination == source:
        print("Destination cannot be the same as source.")

        destination = get_location(
            "Enter destination location: ",
            locations
        )

    optimization_mode = get_optimization_mode()

    results = calculate_results(
        city,
        source,
        destination
    )

    recommended_algorithm = select_recommended_algorithm(
        results,
        optimization_mode
    )

    if recommended_algorithm is None:
        print("\nNo route available.")
        return

    recommended = results[recommended_algorithm]

    print("\n")
    print("=" * 65)
    print("                    RECOMMENDED ROUTE")
    print("=" * 65)

    print(f"Algorithm      : {recommended_algorithm}")

    print(
        f"Route          : "
        f"{' -> '.join(recommended['route'])}"
    )

    print(f"Total Cost     : {recommended['cost']}")
    print(f"Distance       : {recommended['distance']} km")

    print(
        f"Travel Time    : "
        f"{recommended['travel_time']} minutes"
    )

    print(
        f"Nodes Explored : "
        f"{recommended['nodes_explored']}"
    )

    print(
        f"Execution Time : "
        f"{recommended['execution_time']} ms"
    )

    print("=" * 65)


def compare_algorithms(city):

    locations = city.graph.keys()

    print("\nAVAILABLE LOCATIONS")
    print("-" * 40)
    print(", ".join(sorted(locations)))

    source = get_location(
        "\nEnter source location: ",
        locations
    )

    destination = get_location(
        "Enter destination location: ",
        locations
    )

    while destination == source:
        print("Destination cannot be the same as source.")

        destination = get_location(
            "Enter destination location: ",
            locations
        )

    results = calculate_results(
        city,
        source,
        destination
    )

    display_comparison(results)

    save_performance_report(
        results,
        "performance_report.json"
    )

    plot_algorithm_comparison(results)

    recommended = select_recommended_algorithm(
        results,
        "4"
    )

    if recommended:

        print("\n" + "=" * 65)
        print("              BEST BALANCED ROUTE")
        print("=" * 65)

        print(
            f"Algorithm : {recommended}"
        )

        print(
            f"Route     : "
            f"{' -> '.join(results[recommended]['route'])}"
        )

        print(
            f"Cost      : "
            f"{results[recommended]['cost']}"
        )

        print("=" * 65)

    print("\nPerformance files generated successfully.")

def show_performance():

    filename = "performance_report.json"

    if not os.path.exists(filename):

        print("\nNo performance report available.")

        print(
            "Please use option 3 "
            "(Compare Algorithms) first."
        )

        return

    report = load_performance_report(filename)

    print("\n")
    print("=" * 75)
    print("                    PERFORMANCE REPORT")
    print("=" * 75)

    for algorithm, data in report.items():

        print(f"\n{algorithm}")
        print("-" * 50)

        print(
            f"Route          : "
            f"{' -> '.join(data['route'])}"
        )

        print(
            f"Cost           : "
            f"{data['cost']}"
        )

        print(
            f"Distance       : "
            f"{data['distance']} km"
        )

        print(
            f"Travel Time    : "
            f"{data['travel_time']} minutes"
        )

        print(
            f"Nodes Explored : "
            f"{data['nodes_explored']}"
        )

        print(
            f"Execution Time : "
            f"{data['execution_time_ms']} ms"
        )

    print("\n" + "=" * 75)
def main():

    city = load_city_map("data/city_map.json")

    while True:

        display_menu()

        choice = get_menu_choice()

        if choice == "1":

            print("\nCITY MAP")
            print("=" * 60)
            city.display()

        elif choice == "2":

            find_route(city)

        elif choice == "3":

            compare_algorithms(city)

        elif choice == "4":

            update_traffic(city)

        elif choice == "5":

            show_performance()

        elif choice == "6":

            print("\nThank you for using SmartRoute AI.")
            break


if __name__ == "__main__":
    main()