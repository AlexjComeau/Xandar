import openai
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()
openai.api_key = "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"

class MessageInput(BaseModel):
    message: str

class MessageOutput(BaseModel):
    response: str

@app.post("/chat", response_model=MessageOutput)
async def chat(input_message: MessageInput):
    prompt = f"Xandar, the helpful AI assistant: {input_message.message}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return {"response": response.choices[0].text.strip()}