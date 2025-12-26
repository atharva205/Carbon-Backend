TRANSPORT_FACTORS = {
    "car": 0.21,
    "bus": 0.089,
    "bike": 0.0,
    "walk": 0.0
}

FOOD_FACTORS = {
    "veg": 1.5,
    "non-veg": 3.3
}

ELECTRICITY_FACTOR = 0.82


def calculate_emissions(data):
    # Calculate individual emissions
    transport = TRANSPORT_FACTORS[data.transport_mode] * data.distance_km
    food = FOOD_FACTORS[data.meal_type]
    electricity = ELECTRICITY_FACTOR * data.electricity_kwh

    total = round(transport + food + electricity, 2)

    # Find biggest contributor
    breakdown = {
        "transport": transport,
        "food": food,
        "electricity": electricity
    }
    max_source = max(breakdown, key=breakdown.get)

    # Score based on total emissions
    if total < 3:
        score = "LOW"
    elif total < 6:
        score = "MEDIUM"
    else:
        score = "HIGH"

    # Suggestion based on biggest contributor
    if max_source == "transport":
        suggestion = "Transport is your biggest contributor. Try public transport, cycling, or carpooling."
    elif max_source == "food":
        suggestion = "Food contributes most. Consider more plant-based meals."
    else:
        suggestion = "Electricity usage is high. Switch off unused appliances or use energy-efficient devices."

    return {
        "total_co2": total,
        "breakdown": {
            "transport": round(transport, 2),
            "food": food,
            "electricity": round(electricity, 2)
        },
        "score": score,
        "suggestion": suggestion
    }
