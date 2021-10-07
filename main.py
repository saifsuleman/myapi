from fastapi import FastAPI
import binomial
import uvicorn

app = FastAPI()

d = {}

@app.get("/api/binomial/expand/{query}")
async def root(query):
    try:
        return {query:binomial.expand(query)}
    except ValueError:
        return {"error":"Invalid query string!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9001)