from crewai import Crew

from src.agents.expert_travel_agent import ExpertTravelAgent
from src.tasks.itinerary_tasks import ItineraryTasks
from src.utils.chat_groq import groqLLM


class DottedCrew:
    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = ExpertTravelAgent(groqLLM)
        tasks = ItineraryTasks()

        expert_travel_agent = agents.expert_travel_agent()

        task_generate_itinerary = tasks.generate_itinerary(expert_travel_agent)

        crew = Crew(
            agents=[expert_travel_agent],
            tasks=[task_generate_itinerary],
            verbose=2,
            max_rpm=2,  # prevent rate limiting on Groq's API
        )

        result = crew.kickoff()
        return result
