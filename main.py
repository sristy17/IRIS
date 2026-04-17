from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "IRIS Search Engine is running"}