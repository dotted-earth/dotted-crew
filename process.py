import os
from crewai import Crew
from decouple import config

from agents import CustomAgents
from tasks import CustomTasks


os.environ['GROQ_API_KEY'] = config("GROQ_API_KEY")

class DottedCrew:
    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        expert_travel_agent = agents.expert_travel_agent()
       

        task_generate_itinerary = tasks.generate_itinerary(
            expert_travel_agent
        )

        crew = Crew(
            agents=[expert_travel_agent],
            tasks=[task_generate_itinerary],
            verbose=2,
            max_rpm=2 # prevent rate limiting on Groq's API
        )

        result = crew.kickoff()
        return result
