from typing import List
from pydantic import BaseModel
from src.models.cuisine import Cuisine
from src.models.diet import Diet
from src.models.food_allergy import FoodAllergy
from src.models.itinerary import Itinerary
from src.models.recreation import Recreation


class ItineraryData(BaseModel):
    itinerary: Itinerary
    recreations: List[Recreation]
    cuisines: List[Cuisine]
    diets: List[Diet]
    food_allergies: List[FoodAllergy]
