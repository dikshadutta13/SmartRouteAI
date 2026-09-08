class Graph:
    def __init__(self):
        self.graph = {}

    def add_location(self, location):
        if location not in self.graph:
            self.graph[location] = []

    def add_road(
        self,
        source,
        destination,
        distance,
        travel_time=0,
        traffic="low"
    ):
        self.add_location(source)
        self.add_location(destination)

        road = {
            "destination": destination,
            "distance": distance,
            "travel_time": travel_time,
            "traffic": traffic
        }

        reverse_road = {
            "destination": source,
            "distance": distance,
            "travel_time": travel_time,
            "traffic": traffic
        }

        self.graph[source].append(road)
        self.graph[destination].append(reverse_road)

    def get_neighbors(self, location):
        return self.graph.get(location, [])

    def display(self):
        for location, roads in self.graph.items():
            print(f"\n{location}:")
            for road in roads:
                print(
                    f"  -> {road['destination']} | "
                    f"Distance: {road['distance']} km | "
                    f"Time: {road['travel_time']} min | "
                    f"Traffic: {road['traffic']}"
                )