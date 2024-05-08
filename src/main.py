from typing import List
from fastapi import FastAPI
from src.crew import DottedCrew
from src.models.itinerary_data import ItineraryData


app = FastAPI()


@app.get("/ping")
def ping_pong():
    return "pong"


@app.post("/generate")
async def generate_itinerary(data: ItineraryData):

    dotted_crew = DottedCrew()
    result = dotted_crew.run(data)
    return result
