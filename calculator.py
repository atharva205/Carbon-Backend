TRANSPORT_FACTORS = {
    "car": 0.21,
    "bus": 0.089,
    "bike": 0.0,
    "walk": 0.0
}

COUNTRY_DAILY_CO2 = {
    "GLOBAL": 11.0,
    "USA": 39.0,
    "INDIA": 5.0,
    "EU": 18.0,
    "CHINA": 22.0
}

FOOD_FACTORS = {
    "veg": 1.5,
    "non-veg": 3.3
}

ELECTRICITY_FACTOR = 0.82

def get_country_average(country: str):
    return COUNTRY_DAILY_CO2.get(country.upper(), COUNTRY_DAILY_CO2["GLOBAL"])

def calculate_emissions(data):
    transport = TRANSPORT_FACTORS[data.transport_mode] * data.distance_km
    food = FOOD_FACTORS[data.meal_type]
    electricity = ELECTRICITY_FACTOR * data.electricity_kwh

    total = round(transport + food + electricity, 2)


    if total < 3:
        score = "LOW"
    elif total < 6:
        score = "MEDIUM"
    else:
        score = "HIGH"

    max_source = max(
        [("transport", transport), ("food", food), ("electricity", electricity)],
        key=lambda x: x[1]
    )[0]

    if max_source == "transport":
        suggestion = "Transport is your biggest contributor. Try public transport or carpooling."
    elif max_source == "food":
        suggestion = "Food choices contribute most. Consider more plant-based meals."
    else:
        suggestion = "Electricity usage is high. Switch off unused appliances or use LEDs."

    avg_co2 = get_country_average(data.country)

    diff_percent = round(((total - avg_co2) / avg_co2) * 100, 1)

    if diff_percent <= -15:
            comparison = "BELOW_AVERAGE"
    elif -15 < diff_percent < 15:
            comparison = "AVERAGE"
    else:
            comparison = "ABOVE_AVERAGE"

    return {
        "total_co2": total,
        "breakdown": {
            "transport": round(transport, 2),
            "food": round(food, 2),
            "electricity": round(electricity, 2)
        },
        "score": score,
        "suggestion": suggestion,
        "benchmark": {
            "average_daily_co2": avg_co2,
            "difference_percent": diff_percent,
            "comparison": comparison,
            "country": data.country
        }

    }
