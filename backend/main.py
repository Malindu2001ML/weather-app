from datetime import datetime 
from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

@app.get("/")
def home():
    return {"message": "Weather API is running!"}

@app.get("/weather")
def get_weather(city: str):
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"
    response = requests.get(url)
    return response.json()

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "api_key_configured": bool(WEATHER_API_KEY),
        "service": "Weather API",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)