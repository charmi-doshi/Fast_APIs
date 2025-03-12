from fast_api import FastAPI
from fastapi import Body
from pydantic import BaseModel
from datetime import datetime
from typing import Annotated

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

#heartbeat post api

heartbeats = []
class Heartbeat(BaseModel):
    heartbeat:str
    # timestamp:str = datetime.now().isoformat()
    
@app.post("/heartbeat")
def create_heartbeat(heartbeat:Heartbeat):
    timestamp = datetime.now().isoformat()
    heartbeats.append(heartbeat.heartbeat)
    print(heartbeats)
    return {
        "heartbeats":heartbeat.heartbeat,
        "timestamp" : timestamp    }

