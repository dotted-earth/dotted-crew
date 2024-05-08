from crewai import Task
from textwrap import dedent

from src.agents.expert_travel_agent import ExpertTravelAgent
from src.models.itinerary import Itinerary


class ItineraryTasks:
    def generate_itinerary(
        self, agent: ExpertTravelAgent, itinerary: Itinerary
    ) -> Task:
        return Task(
            description=dedent(
                f"""Generate a {itinerary.length_of_stay}-day itinerary for a trip to {itinerary.destination} starting {itinerary.start_date} to {itinerary.end_date}. The itinerary must include breakfast, lunch, and dinner and at least 2 activities. Also include mode of transportation, distance from point ot point, and duration of each activity, and commuting. Make sure to use the most recent data as possible."""
            ),
            agent=agent,
            expected_output="A JSON string",
            async_execution=True,
        )
