from fastapi import FastAPI
from manager import Manager



app = FastAPI()

# Create a Manager object
manager = Manager()
manager.full_data()
manager.to_df()
manager.process()
manager.to_json()

# Get the prompt from the request and return the classification.
@app.get("/")
def send():
    return manager.get_json()