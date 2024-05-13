from crewai import Task
from textwrap import dedent

from src.agents.weather_expert import WeatherExpertAgent
from src.models.weather import Weather


class WeatherTasks:
    def research_local_weather(
        self,
        agent: WeatherExpertAgent,
        location: str,
    ) -> Task:
        return Task(
            description=dedent(
                f"""Find 5-year historical weather conditions for {location}"""
            ),
            agent=agent,
            expected_output="A JSON output",
            output_json=Weather,
            async_execution=False,
        )

    def provide_weather_tips(self, agent: WeatherExpertAgent) -> Task:
        return Task(
            description=dedent(f"""Give safety tips"""),
            agent=agent,
            expected_output="A list of tips",
            async_execution=False,
        )
