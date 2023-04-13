from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Power(BaseModel):
    question: str
    answer: float

@app.get("/power")
async def read_power():
    return {"question": "A 1200 W hair dryer is used for 5 minutes to dry a person's hair. How much energy does the hair dryer consume during this time?"}

@app.post("/power")
async def validate_power_answer(power: Power):
    try:
        if float(power.answer) == 360000:
            return {"result": "Correct answer!"}
        else:
            raise HTTPException(status_code=400, detail="Incorrect answer")
    except ValueError:
        raise HTTPException(status_code=400, detail="Answer must be a number")
