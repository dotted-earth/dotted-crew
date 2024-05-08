from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from src.crew import DottedCrew
from src.models.cuisine import Cuisine
from src.models.diet import Diet
from src.models.food_allergy import FoodAllergy
from src.models.itinerary import Itinerary
from src.models.recreation import Recreation


app = FastAPI()


class ItineraryData(BaseModel):
    itinerary: Itinerary
    recreations: List[Recreation]
    cuisines: List[Cuisine]
    diets: List[Diet]
    food_allergies: List[FoodAllergy]


@app.get("/ping")
def ping_pong():
    return "pong"


@app.post("/generate")
async def generate_itinerary(data: ItineraryData):

    dotted_crew = DottedCrew(data)
    result = dotted_crew.run()
    return result
