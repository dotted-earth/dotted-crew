from enum import Enum


class ScheduleIntensityEnum(str, Enum):
    relaxed = "relaxed"
    moderate = "moderate"
    active = "active"


class ScheduleLineItemEnum(str, Enum):
    accommodation = "accommodation"
    transportation = "transportation"
    meal = "meal"
    activity = "activity"


class ScheduleLengthEnum(str, Enum):
    quarter_day = "quarter_day"  # 2-4 hours
    half_day = "half_day"  # 4-6 hours
    full_day = "full_day"  # 6-8 hours
    whole_day = "whole_day"  # 8+ hours
