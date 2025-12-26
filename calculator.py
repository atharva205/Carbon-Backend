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
    transport = TRANSPORT_FACTORS[data.transport_mode] * data.distance_km
    food = FOOD_FACTORS[data.meal_type]
    electricity = ELECTRICITY_FACTOR * data.electricity_kwh

    total = round(transport + food + electricity, 2)

    if total < 3:
        score = "LOW"
        suggestion = "Great job! Keep using sustainable options."
    elif total < 6:
        score = "MEDIUM"
        suggestion = "Consider reducing non-essential travel."
    else:
        score = "HIGH"
        suggestion = "Switch to public transport or reduce meat intake."

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
