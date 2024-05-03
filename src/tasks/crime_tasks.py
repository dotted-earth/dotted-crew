from crewai import Task
from textwrap import dedent


class CrimeTasks:
    def research_local_crime(self, agent, location):
        return Task(
            description=dedent(f"""Research crime near {location}"""),
            agent=agent,
            expected_output="A JSON string",
            async_execution=True,
        )

    def provide_safety_tips(self, agent, context):
        return Task(
            description=dedent(f"""Give safety tips"""),
            agent=agent,
            context=context,
            expected_output="A JSON string",
            async_execution=True,
        )
