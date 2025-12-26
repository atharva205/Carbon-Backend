from pydantic import BaseModel

class CarbonInput(BaseModel):
    transport_mode: str
    distance_km: float
    meal_type: str
    electricity_kwh: float
    
class Benchmark(BaseModel):
    average_daily_co2: float
    difference_percent: float
    comparison: str   # ABOVE_AVERAGE / BELOW_AVERAGE
    country: str
    
class CarbonResponse(BaseModel):
    total_co2: float
    breakdown: dict
    score: str
    suggestion: str

