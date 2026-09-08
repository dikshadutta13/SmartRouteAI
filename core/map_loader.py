import json
from core.graph import Graph


def load_city_map(filename):
    city = Graph()

    with open(filename, "r") as file:
        data = json.load(file)

    for road in data["roads"]:
        city.add_road(
            road["source"],
            road["destination"],
            road["distance"],
            road["travel_time"],
            road["traffic"]
        )

    return city