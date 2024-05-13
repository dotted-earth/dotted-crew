from crewai import Task
from textwrap import dedent

from src.agents.local_crime_expert import LocalCrimeExpertAgent
from src.models.crime import Crime


class CrimeTasks:
    def research_local_crime(self, agent: LocalCrimeExpertAgent, location: str) -> Task:
        return Task(
            description=dedent(f"""Research crime near {location}"""),
            agent=agent,
            expected_output="A JSON object",
            output_json=Crime,
            async_execution=False,
        )

    def provide_safety_tips(self, agent: LocalCrimeExpertAgent):
        return Task(
            description=dedent(f"""Give safety tips"""),
            agent=agent,
            expected_output="A JSON object",
            output_json=Crime,
            async_execution=False,
        )
