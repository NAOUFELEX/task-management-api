from fastapi import FastAPI
from .database import engine, Base
from . import models

app = FastAPI(title="Task Management API")

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")

def read_root():
    return {"message": "tables created successfully!"}