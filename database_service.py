from fastapi import FastAPI
from typing import Dict, Any
from pydantic import BaseModel

app = FastAPI()

db: Dict[int, Any] = {}

class Write(BaseModel):
    data: dict
    key: int

@app.get("/")
def root():
    return{"message" : "Database handles storage of results and texts"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/write")
def write(request: Write):
    db[request.key] = request.data
    return {"message" : "Data saved"}

@app.get("/read")
def read(key : int):
    if key not in db.keys():
        return {"message" : "Key not found"}
    return {"Data" : db[key]}
    