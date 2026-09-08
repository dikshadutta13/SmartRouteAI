import json


def generate_performance_report(results):
    report = {}

    for algorithm, result in results.items():
        report[algorithm] = {
            "route": result["route"],
            "cost": result["cost"],
            "distance": result["distance"],
            "travel_time": result["travel_time"],
            "nodes_explored": result["nodes_explored"],
            "execution_time_ms": result["execution_time"]
        }

    return report


def save_performance_report(results, filename):
    report = generate_performance_report(results)

    with open(filename, "w") as file:
        json.dump(report, file, indent=4)

    return filename


def load_performance_report(filename):
    with open(filename, "r") as file:
        return json.load(file)