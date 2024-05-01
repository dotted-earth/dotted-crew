
from fastapi import FastAPI
from .process import DottedCrew

app = FastAPI()

@app.post("/generate")
def generate_itinerary():
    dotted_crew = DottedCrew()
    result = dotted_crew.run()   
    return  result
