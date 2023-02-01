from fastapi import FastAPI

print("Server started...")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}