import json
from fastapi import FastAPI
from src.crew import DottedCrew
from src.models.generate_itinerary_request_body import GenerateItineraryRequestBody


app = FastAPI()


@app.post("/generate")
async def generate_itinerary(data: GenerateItineraryRequestBody):

    dotted_crew = DottedCrew()
    result = await dotted_crew.run(data)
    return json.loads(result)
