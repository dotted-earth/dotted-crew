import datetime
from typing import List, Union
from pydantic import BaseModel, Field

from src.models.enums import ScheduleLengthEnum, ScheduleIntensityEnum
from src.models.schedule_line_item import ScheduleLineItem


class Schedule(BaseModel):
    name: str = Field(description="The name of the date", examples="Monday, Jan 12, 2024")
    description: str = Field(description="A description of today's activities")
    start_date: datetime.datetime = Field(description="The start date and time of the schedule in YYYY-MM-DD HH:MM format")
    end_date: datetime.datetime = Field(description="The end date and time of the schedule in YYYY-MM-DD HH:MM format")
    schedule_intensity: ScheduleIntensityEnum = Field(description="How vigorous the day will be")
    schedule_length: ScheduleLengthEnum
    schedule_line_items: List[ScheduleLineItem] = []
    estimated_cost: Union[float | None] = Field(description="The total estimated costs for the entire schedule")


Schedule.model_rebuild()
