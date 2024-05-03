from crewai import Task
from textwrap import dedent


class WeatherTasks:
    def research_local_weather(self, agent, location):
        return Task(
            description=dedent(
                f"""Find 5-year historical weather conditions for {location}"""
            ),
            agent=agent,
            expected_output="A JSON string",
            async_execution=True,
        )

    def provide_weather_tips(self, agent, context):
        return Task(
            description=dedent(f"""Give safety tips"""),
            agent=agent,
            context=context,
            expected_output="A JSON string",
            async_execution=True,
        )
