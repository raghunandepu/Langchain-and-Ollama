# Run as: uvicorn main_fastapi:app --reload

import os
from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from ollama import Client

load_dotenv()
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
client = Client(host=OLLAMA_HOST)
app = FastAPI(title="Ollama FastAPI Example")

#Schema for the request body
Role = Literal["system", "user", "assistant"]
class Message(BaseModel):
    role: Role
    content: str

class ChatRequest(BaseModel):
    model: str = "qwen3:latest"
    messages: list[Message]

class ChatResponse(BaseModel):
    response: str
    model: str

# API Route
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        result = client.chat(
            model=request.model,
            messages=[m.model_dump() for m in request.messages],
            stream=False
        )
        return ChatResponse(
            response=result["message"]["content"],
            model=result.get("model", request.model),
        )
    except Exception as e:
        return ChatResponse(response=f"[error] {e}", model=request.model)
    

"""Sample request body:

{
  "model": "gemma2:2b",
  "messages": [
    {
      "role": "system",
      "content": "You are an helpful assistant"
    },
    {
      "role": "user",
      "content": "What is Machine Learning? Explain in short."
    }

  ]
}"""