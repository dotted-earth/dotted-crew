from crewai import Task
from textwrap import dedent
from src.agents.local_food_expert import LocalFoodExpertAgent
from src.models.meal import Meal


class FoodTasks:
    def research_local_restaurants(
        self, agent: LocalFoodExpertAgent, location: str
    ) -> Task:
        return Task(
            description=dedent(
                f"""Find a list of local restaurants in the area of {location}. There should be at least 10 different restaurants for each category: breakfast, lunch, and dinner"""
            ),
            agent=agent,
            expected_output="A JSON object",
            output_json=Meal,
            async_execution=False,
        )
