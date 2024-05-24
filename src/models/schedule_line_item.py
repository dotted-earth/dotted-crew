import datetime
from typing import List, Union
from pydantic import BaseModel, Field

from src.models.enums import ScheduleLineItemEnum
from src.models.location import Location


class ScheduleLineItem(BaseModel):
    name: str = Field(description="The name of the scheduled activity", examples="Zip-lining, Dinner at Rodis', Ice Skating")
    description: str = Field(description="A description of the activity")
    schedule_type: ScheduleLineItemEnum
    start_location: Location
    end_location: Union[Location | None] = None
    start_time: datetime.time = Field(description="The activity start time in HH:MM format")
    end_time: datetime.time = Field(description="The activity end time in HH:MM format")
    duration: datetime.time = Field(description="The duration of the activity in minutes", examples="90 minutes")
    estimated_price: Union[float | None] = Field(description="The estimated cost of the activity", default=None)
    alternatives: List["ScheduleLineItem"] = []


ScheduleLineItem.model_rebuild()
