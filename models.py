from pydantic import BaseModel

class CarbonInput(BaseModel):
    transport_mode: str
    distance_km: float
    meal_type: str
    electricity_kwh: float

class CarbonResponse(BaseModel):
    total_co2: float
    breakdown: dict
    score: str
    suggestion: str
