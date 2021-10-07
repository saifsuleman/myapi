from fastapi import FastAPI
import binomial

app = FastAPI()

d = {}

@app.get("/api/binomial/expand/{query}")
async def root(query):
    try:
        return {query:binomial.expand(query)}
    except ValueError:
        return {"error":"Invalid query string!"}