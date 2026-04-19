from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from Weather App!"}

@app.get("/test")
def test():
    return {"status": "ok", "message": "GitHub connection test"}