from fastapi import FastAPI
from database import test_db

app=FastAPI()

@app.get("/")
def read_root():
    print("FastAPI Running")
    return{"status": "FastAPI Running"}

@app.get("/db-test")
def db_test():
    return test_db()
