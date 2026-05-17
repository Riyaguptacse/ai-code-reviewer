from fastapi import FastAPI
from pydantic import BaseModel
from llm_service import review_code
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    language: str
    code: str

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/review")
def review(req: CodeRequest):
    try:
        return review_code(req.language, req.code)
    except Exception as e:
        return {"error": str(e)}