def update_traffic(graph):

    print("\nTRAFFIC UPDATE")
    print("-" * 40)

    roads = []

    for source, neighbors in graph.graph.items():
        for road in neighbors:
            destination = road["destination"]

            if source < destination:
                roads.append((source, destination, road))

    for index, (source, destination, road) in enumerate(roads, 1):
        print(
            f"{index}. {source} -> {destination} "
            f"[{road['traffic']}]"
        )

    print(f"{len(roads) + 1}. Cancel")

    while True:
        try:
            choice = int(input("\nSelect road: "))

            if choice == len(roads) + 1:
                return

            if 1 <= choice <= len(roads):
                break

        except ValueError:
            pass

        print("Invalid selection.")

    source, destination, road = roads[choice - 1]

    print("\nTraffic Levels")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    traffic_map = {
        "1": "low",
        "2": "medium",
        "3": "high"
    }

    while True:
        traffic_choice = input(
            "Select traffic level: "
        ).strip()

        if traffic_choice in traffic_map:
            break

        print("Invalid choice.")

    new_traffic = traffic_map[traffic_choice]

    for item in graph.graph[source]:
        if item["destination"] == destination:
            item["traffic"] = new_traffic

    for item in graph.graph[destination]:
        if item["destination"] == source:
            item["traffic"] = new_traffic

    print(
        f"\nTraffic updated: "
        f"{source} -> {destination} = {new_traffic}"
    )