from crewai import Agent
from textwrap import dedent


class LocalFoodExpertAgent:
    def __init__(self, llm):
        self.llm = llm

    def create(self):
        return Agent(
            role="Local Food Expert",
            backstory=dedent(
                f"""I've tasted my way through every corner, from hidden gems to famous spots. With my passion and knowledge, I guide both locals and visitors to the best dining experiences."""
            ),
            goal=dedent(
                f"""To ensure everyone enjoys unforgettable meals in our vibrant city."""
            ),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )
