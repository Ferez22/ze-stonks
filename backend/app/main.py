from fastapi import FastAPI, Depends
from app.router import api

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from ze-backend"}

app.include_router(api.router)