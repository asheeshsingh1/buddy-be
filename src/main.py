### Directory: src/buddy/main.py

from fastapi import FastAPI
from src.api.v1.endpoints import talk
import os
os.makedirs("storage/uploads", exist_ok=True)


app = FastAPI(title="Buddy AI Assistant")

# Include V1 API Routes
app.include_router(talk.router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"message": "Buddy AI Assistant is running"}
