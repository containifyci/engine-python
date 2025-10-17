# app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello(name: str = "world"):
    return {"message": f"hello {name}."}
