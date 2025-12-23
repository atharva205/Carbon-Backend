from fastapi import FastAPI
from models import CarbonInput, CarbonResponse
from calculator import calculate_emissions

app = FastAPI(title="Carbon Footprint API")

@app.get("/")
def health_check():
    return {"status": "API is running"}

@app.post("/calculate", response_model=CarbonResponse)
def calculate(data: CarbonInput):
    return calculate_emissions(data)
