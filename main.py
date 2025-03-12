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

