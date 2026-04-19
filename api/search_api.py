from fastapi import FastAPI
from query.query_engine import QueryEngine

app = FastAPI()

engine = QueryEngine()


@app.get("/")
def root():
    return {"message": "IRIS Search API is running"}


@app.get("/search")
def search(q: str):
    if not q.strip():
        return {"results": [], "message": "Empty query"}

    results = engine.search(q)

    return {"results": results}
    