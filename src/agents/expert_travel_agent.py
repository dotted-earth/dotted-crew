from crewai import Agent
from textwrap import dedent


class ExpertTravelAgent:
    def __init__(self, llm):
        self.llm = llm

    def create(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(
                f"""Seasoned travel agent with years of experience in crafting unforgettable journeys. With a passion for exploration and a knack for logistics, I specialize in curating seamless travel experiences tailored to each client's desires. From exotic adventures to luxurious getaways, I handle every detail to ensure a stress-free and memorable trip."""
            ),
            goal=dedent(
                f"""Create a num-day itinerary with detailed per-day plans, include budget, packing suggestions, and safety tips.
                        """
            ),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )
