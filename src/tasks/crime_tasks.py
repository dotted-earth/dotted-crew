from crewai import Task
from textwrap import dedent

from src.agents.local_crime_expert import LocalCrimeExpertAgent


class CrimeTasks:
    def research_local_crime(self, agent: LocalCrimeExpertAgent, location: str) -> Task:
        return Task(
            description=dedent(f"""Research crime near {location}"""),
            agent=agent,
            expected_output="A JSON string",
            async_execution=False,
        )

    def provide_safety_tips(self, agent: LocalCrimeExpertAgent, context: str):
        return Task(
            description=dedent(f"""Give safety tips"""),
            agent=agent,
            context=context,
            expected_output="A JSON string",
            async_execution=False,
        )
