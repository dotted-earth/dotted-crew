from typing import List
from crewai import Task
from textwrap import dedent

from src.agents.expert_travel_agent import ExpertTravelAgent
from src.models.itinerary_request_body import ItineraryRequestBody
from src.models.itinerary_draft import ItineraryDraft


class ItineraryTasks:
    def generate_itinerary(
        self,
        agent: ExpertTravelAgent,
        itinerary: ItineraryRequestBody,
        context: List[Task],
    ) -> Task:
        return Task(
            description=dedent(
                f"""Generate a {itinerary.length_of_stay}-day itinerary for a trip to {itinerary.destination} starting {itinerary.start_date} to {itinerary.end_date}. The itinerary must include breakfast, lunch, and dinner and at least 2 activities. Also include mode of transportation, distance from point ot point, and duration of each activity, and commuting. Make sure to use the most recent data as possible. When working with your co-workers, give them the context all the itinerary {itinerary.model_dump_json()}"""
            ),
            agent=agent,
            expected_output="Output in only JSON format. Each day should be in an array.",
            # output_json=ItineraryDraft,
            context=context,
            async_execution=False,
        )
