from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.core.ai_engine import AICore

app = FastAPI(title="Zaid AI API")
ai = AICore(model_name="gpt2")

class QueryRequest(BaseModel):
    prompt: str
    max_length: int = 100

@app.post("/query")
async def query_ai(request: QueryRequest):
    response = ai.generate_response(request.prompt, max_length=request.max_length)
    return {"response": response}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}