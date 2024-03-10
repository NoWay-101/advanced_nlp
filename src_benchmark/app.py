from fastapi import FastAPI
from pydantic import BaseModel
from pipeline import get_ai_feedback

class Prompt(BaseModel):
    mathToCheck: str

app = FastAPI()


@app.post("/check-math")
async def check_math(prompt: Prompt):
    
    feedbacks = get_ai_feedback(prompt.mathToCheck)
    
    return {
        "feedbacks": feedbacks
    }