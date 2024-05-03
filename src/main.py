from fastapi import FastAPI
from src.crew import DottedCrew

app = FastAPI()


@app.post("/generate")
def generate_itinerary():
    dotted_crew = DottedCrew()
    result = dotted_crew.run()
    return result
