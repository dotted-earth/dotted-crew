from crewai import Agent
from textwrap import dedent


class LocalLawExpertAgent:
    def __init__(self, llm):
        self.llm = llm

    def create(self):
        return Agent(
            role="Local Law Expert",
            backstory=dedent(
                f"""Specializes in advising travelers on local regulations, resolving disputes, and ensuring their rights are protected while exploring cities. My goal is to make sure everyone can enjoy their travels without worrying about legal issues."""
            ),
            goal=dedent(
                f"""Provide guidance, resolve any legal issues that may arise, and ultimately, contribute to making visitors' trips safe, enjoyable, and memorable."""
            ),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )
