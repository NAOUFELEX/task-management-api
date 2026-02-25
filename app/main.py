from fastapi import FastAPI

app = FastAPI(title="Task Management API")

@app.get("/")
def root():
    return {"message": "API is running"}