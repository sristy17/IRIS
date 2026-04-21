from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from query.query_engine import QueryEngine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = QueryEngine()


@app.get("/")
def root():
    return {"message": "IRIS Search API is running"}


@app.get("/search")
def search(q: str = Query(..., min_length=1)):
    q = q.strip()

    results = engine.search(q)

    return {
        "query": q,
        "count": len(results),
        "results": results
    }