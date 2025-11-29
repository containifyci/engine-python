# app.py
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello(name: str = "world"):
    return {"message": f"hello {name}."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)