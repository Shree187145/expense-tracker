
from fastapi import FastAPI

from app.database import Base, engine
from app import models
from app.routers.expenses import router as expense_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker API")

app.include_router(expense_router)


@app.get("/")
def home():
    return {"message": "Welcome to Expense Tracker API"}
