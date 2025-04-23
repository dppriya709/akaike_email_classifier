from fastapi import FastAPI
from pydantic import BaseModel
from app import process_email_pipeline
import uvicorn

app = FastAPI()

class EmailRequest(BaseModel):
    input_email_body: str

@app.post("/classify")
def classify_email(email: EmailRequest):
    result = process_email_pipeline(email.input_email_body)
    return result

# For local testing
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
