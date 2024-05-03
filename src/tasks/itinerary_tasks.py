from crewai import Task
from textwrap import dedent


class ItineraryTasks:
    def generate_itinerary(self, agent):
        return Task(
            description=dedent(
                f"""Generate a 2 day itinerary for a trip to Tokyo, Japan. The budget is $200. The itinerary must include breakfast, lunch, and dinner and at least 2 activities. Also include mode of transportation, distance from point ot point, and duration of each activity, and commuting. Make sure to use the most recent data as possible."""
            ),
            agent=agent,
            expected_output="A JSON string",
            output_json="",
            async_execution=True,
        )
