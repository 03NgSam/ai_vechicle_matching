def surge_multiplier(hour):
    """
    Returns surge multiplier based on peak hours.
    """
    if 8 <= hour <= 10 or 17 <= hour <= 20:
        return 1.5
    return 1.0
