from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "system",
                "content": """당신은 신입사원을 위한 사내규정 안내 챗봇입니다.
반드시 한국어로만 답변하세요. 한자, 일본어, 영어, 독일어 등 다른 언어는 절대 사용하지 마세요.
반드시 아래 JSON 형식으로만 응답하세요. 다른 텍스트는 절대 포함하지 마세요:
{
    "answer": "한국어 답변",
    "suggested_questions": ["한국어 질문1", "한국어 질문2", "한국어 질문3"]
}"""
            },
            {
                "role": "user",
                "content": request.message
            }
        ]
    )

    text = response.choices[0].message.content

    try:
        json_match = re.search(r'\{.*\}', text, re.DOTALL)
        if json_match:
            parsed = json.loads(json_match.group())
            return parsed
    except:
        pass

    return {"answer": text, "suggested_questions": []}

@app.get("/")
async def root():
    return {"message": "ChatbotForZin API 실행중"}