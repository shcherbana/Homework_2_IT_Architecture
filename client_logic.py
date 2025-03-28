from fastapi import FastAPI, Header, HTTPException
import requests
import os
from database_service import Write

SECRET_TOKEN = os.getenv("SECRET_TOKEN", "secret-token")

app = FastAPI()

DATABASE_SERVICE_URL = "http://127.0.0.1:8001"
BUSINESS_LOGIC_SERVICE_URL = "http://127.0.0.1:8000"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Client Service orchestrates calls to Database and Business Logic services."}

def validate_token(authorization: str):
    if authorization != f"Bearer {SECRET_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.post("/process")
async def process(request: Write, authorization: str = Header(None)):
    validate_token(authorization)

    
    process_response = requests.post(f"{BUSINESS_LOGIC_SERVICE_URL}/process", json=request.data)
    
    if process_response.status_code != 200:
        raise HTTPException(status_code=process_response.status_code, detail="Failed to process data in the Business Logic service")

    processed_result = process_response.json()

    result = {"data": processed_result, "key": request.key} 
    requests.post(f"{DATABASE_SERVICE_URL}/write", json=result)

    return {"status": "success", "processed_data": processed_result}

