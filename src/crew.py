from crewai import Crew
from crewai.process import Process

from src.agents.expert_travel_agent import ExpertTravelAgent
from src.agents.local_crime_expert import LocalCrimeExpertAgent
from src.agents.local_culture_expert import LocalCultureExpertAgent
from src.agents.local_food_expert import LocalFoodExpertAgent
from src.agents.local_law_expert import LocalLawExpertAgent
from src.agents.weather_expert import WeatherExpertAgent

from src.models.generate_itinerary_request_body import GenerateItineraryRequestBody
from src.tasks.crime_tasks import CrimeTasks
from src.tasks.culture_tasks import CultureTasks
from src.tasks.food_tasks import FoodTasks
from src.tasks.itinerary_tasks import ItineraryTasks
from src.tasks.law_tasks import LocalLawTasks
from src.tasks.weather_tasks import WeatherTasks


from src.utils.chat_groq import groqLLM


class DottedCrew:
    def run(self, data: GenerateItineraryRequestBody):
        itinerary = data.itinerary
        destination = itinerary.destination
        start_date = itinerary.start_date
        end_date = itinerary.end_date
        length_of_stay = itinerary.length_of_stay

        user_recreations = data.recreations
        user_diets = data.diets
        user_cuisines = data.cuisines
        user_food_allergies = data.food_allergies

        expert_travel_agent = ExpertTravelAgent(groqLLM).create()
        weather_expert_agent = WeatherExpertAgent(groqLLM).create()
        local_crime_expert = LocalCrimeExpertAgent(groqLLM).create()
        local_culture_expert = LocalCultureExpertAgent(groqLLM).create()
        local_food_expert = LocalFoodExpertAgent(groqLLM).create()
        local_law_expert = LocalLawExpertAgent(groqLLM).create()

        food_tasks = FoodTasks().research_local_restaurants(
            local_food_expert, destination
        )
        culture_tasks = CultureTasks().research_local_culture(
            local_culture_expert, destination
        )
        weather_tasks = WeatherTasks().research_local_weather(
            weather_expert_agent, destination, start_date, end_date, length_of_stay
        )
        crime_tasks = CrimeTasks().research_local_crime(local_crime_expert, destination)
        local_law_tasks = LocalLawTasks().research_local_laws(
            local_law_expert, destination
        )

        itinerary_tasks = ItineraryTasks().generate_itinerary(
            agent=expert_travel_agent,
            itinerary=itinerary,
            context=[
                food_tasks,
                culture_tasks,
                weather_tasks,
                crime_tasks,
                local_law_tasks,
            ],
        )

        crew = Crew(
            agents=[
                expert_travel_agent,
                weather_expert_agent,
                local_crime_expert,
                local_culture_expert,
                local_law_expert,
                local_food_expert,
            ],
            tasks=[
                itinerary_tasks,
            ],
            process=Process.hierarchical,
            manager_llm=groqLLM,
            # memory=True,
            verbose=True,
            max_rpm=25,  # prevent rate limiting on Groq's API
        )

        result = crew.kickoff()

        return result
