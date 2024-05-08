from crewai import Task
from textwrap import dedent

from src.agents.local_culture_expert import LocalCultureExpertAgent


class CultureTasks:
    def research_local_culture(
        self, agent: LocalCultureExpertAgent, location: str
    ) -> Task:
        return Task(
            description=dedent(f"""Research local culture for {location}"""),
            agent=agent,
            expected_output="A JSON string",
            async_execution=True,
        )
