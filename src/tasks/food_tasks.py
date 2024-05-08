from crewai import Task
from textwrap import dedent
from src.agents.local_food_expert import LocalFoodExpertAgent


class FoodTasks:
    def research_local_restaurants(
        self, agent: LocalFoodExpertAgent, location: str
    ) -> Task:
        return Task(
            description=dedent(
                f"""Find a list of local restaurants in the area of {location}. There should be at least 10 different restaurants for each category: breakfast, lunch, and dinner"""
            ),
            agent=agent,
            expected_output="A JSON string",
            async_execution=True,
        )
