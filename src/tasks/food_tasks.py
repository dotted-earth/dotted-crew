from crewai import Task
from textwrap import dedent


class FoodTasks:
    def research_local_restaurants(self, agent, location):
        return Task(
            description=dedent(
                f"""Find a list of local restaurants in the area of {location}"""
            ),
            agent=agent,
            expected_output="A JSON string",
            output_json="",
            async_execution=True,
        )
