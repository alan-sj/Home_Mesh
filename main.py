from fastapi import FastAPI
from database import engine,Base
from models import user
from routers import users, categories

app=FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(users.router)
app.include_router(categories.router)