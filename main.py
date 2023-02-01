from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

ENV = os.getenv('ENV')

print(f"Server started.... {ENV}")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": f"Hello World {ENV}"}