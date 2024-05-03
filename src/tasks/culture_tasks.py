from crewai import Task
from textwrap import dedent


class CultureTasks:
    def research_local_culture(self, agent, location):
        return Task(
            description=dedent(f"""Research local culture for {location}"""),
            agent=agent,
            expected_output="A JSON string",
            async_execution=True,
        )
