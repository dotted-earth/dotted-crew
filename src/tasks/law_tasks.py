from crewai import Task
from textwrap import dedent

from src.agents.local_law_expert import LocalLawExpertAgent


class LocalLawTasks:
    def research_local_laws(self, agent: LocalLawExpertAgent, location: str) -> Task:
        return Task(
            description=dedent(
                f"""Research important local laws for travelers {location}"""
            ),
            agent=agent,
            expected_output="A JSON string",
            async_execution=False,
        )
