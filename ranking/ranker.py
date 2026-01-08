def rank_vehicles(vehicles, preference="balanced"):
    """
    Rank vehicles based on user preference:
    - fastest
    - cheapest
    - balanced
    """
    if preference == "fastest":
        return sorted(vehicles, key=lambda x: x["eta"])

    if preference == "cheapest":
        return sorted(vehicles, key=lambda x: x["cost"])

    return sorted(vehicles, key=lambda x: x["eta"] + x["cost"])
