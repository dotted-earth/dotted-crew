from fastapi import FastAPI
from src.crew import DottedCrew
from src.models.generate_itinerary_request_body import GenerateItineraryRequestBody


app = FastAPI()


@app.post("/generate")
def generate_itinerary(data: GenerateItineraryRequestBody):

    dotted_crew = DottedCrew(data)
    result = dotted_crew.run()
    return result
