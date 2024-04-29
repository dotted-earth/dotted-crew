import os;
from crewai import Agent
from textwrap import dedent
from langchain_groq import ChatGroq

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:
    def __init__(self):
        self.llm = ChatGroq(
            api_key=os.environ.get('GROQ_API_KEY'),
            model="llama3-8b-8192",
            temperature=0
        )
            

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in travel planning and logistics. I have decades of making travel itineraries."""),
            goal=dedent(f"""Create a 2-day itinerary with detailed per-day plans, include budget, packing suggestions, and safety tips.
                        """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )
