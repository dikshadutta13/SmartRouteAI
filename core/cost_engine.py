TRAFFIC_MULTIPLIERS = {
    "low": 1.0,
    "medium": 1.5,
    "high": 2.0
}


def calculate_road_cost(distance, travel_time, traffic):
    traffic = traffic.lower()

    if traffic not in TRAFFIC_MULTIPLIERS:
        raise ValueError("Invalid traffic level")

    traffic_penalty = distance * (
        TRAFFIC_MULTIPLIERS[traffic] - 1
    )

    time_cost = travel_time * 0.2

    total_cost = distance + traffic_penalty + time_cost

    return round(total_cost, 2)


def get_traffic_multiplier(traffic):
    traffic = traffic.lower()

    if traffic not in TRAFFIC_MULTIPLIERS:
        raise ValueError("Invalid traffic level")

    return TRAFFIC_MULTIPLIERS[traffic]


def get_traffic_score(traffic):
    scores = {
        "low": 1,
        "medium": 2,
        "high": 3
    }

    traffic = traffic.lower()

    if traffic not in scores:
        raise ValueError("Invalid traffic level")

    return scores[traffic]