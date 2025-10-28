from fastapi import FastAPI
from app.database import init_db
app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()


@app.get("/")
def read_root():
    return {"message": "Smart Task Manager API is running"}
