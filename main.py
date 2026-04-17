from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()

@app.get("/")
def root():
    return {"message": "IRIS Search Engine is running"}

@app.get("/favicon.ico")
def favicon():
    return Response(status_code=204)