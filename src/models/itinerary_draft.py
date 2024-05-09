from typing import List
from pydantic import BaseModel

from src.models.schedule import Schedule


class ItineraryDraft(BaseModel):
    schedule: List[Schedule]
