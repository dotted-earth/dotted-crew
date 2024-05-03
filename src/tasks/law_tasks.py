from crewai import Task
from textwrap import dedent


class LocalLawTasks:
    def research_local_laws(self, agent, location):
        return Task(
            description=dedent(
                f"""Research important local laws for travelers {location}"""
            ),
            agent=agent,
            expected_output="A JSON string",
            async_execution=True,
        )
