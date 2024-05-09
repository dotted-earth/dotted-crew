from typing import List
from pydantic import BaseModel
from src.models.cuisine import Cuisine
from src.models.diet import Diet
from src.models.food_allergy import FoodAllergy
from src.models.recreation import Recreation
from src.models.itinerary_request_body import ItineraryRequestBody


class GenerateItineraryRequestBody(BaseModel):
    itinerary: ItineraryRequestBody
    recreations: List[Recreation]
    cuisines: List[Cuisine]
    diets: List[Diet]
    food_allergies: List[FoodAllergy]
