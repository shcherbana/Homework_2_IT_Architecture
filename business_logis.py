from fastapi import FastAPI
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from pydantic import BaseModel

class TextInput(BaseModel):
    text: str

app = FastAPI()


model = joblib.load("automobile_or_medicine_model.pkl")



@app.get("/")
def root():
    return {"message":"This is a small description of my microservice. It returns to what the discussion is related: automobile or medicine"}

@app.get("/health")
def health():
    return {"status" : "ok"}

@app.post("/process")
async def process_data(input_data: TextInput):

    prediction = model.predict([input_data.text])[0]
    category = "Automobile" if prediction == 0 else "Medical"

    return {"text": input_data.text, "category": category}