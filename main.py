from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import CarbonInput, CarbonResponse
from calculator import calculate_emissions

app = FastAPI(title="Carbon Footprint API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # safe for demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "API is running"}

@app.post("/calculate", response_model=CarbonResponse)
def calculate(data: CarbonInput):
    return calculate_emissions(data)
