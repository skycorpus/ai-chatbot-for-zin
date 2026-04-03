import json
import os
import re
import shutil
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from groq import Groq
from pydantic import BaseModel

from rag import DOCS_DIR, init_vectordb, search

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise RuntimeError(f"GROQ_API_KEY is not set. Add it to {ENV_PATH}")

client = Groq(api_key=groq_api_key)

SYSTEM_PROMPT_TEMPLATE = """You are an internal HR policy chatbot for new employees.
Answer in natural Korean only.
Do not use Japanese, Chinese, or English unless the user explicitly asks for it.
Use only the policy context below. If the context is insufficient, say that the policy document does not clearly specify it.
Keep the answer concise and practical.

Policy context:
{context}

Return only valid JSON with this schema:
{{
  "answer": "short Korean answer",
  "suggested_questions": ["follow-up question 1", "follow-up question 2", "follow-up question 3"]
}}
"""

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str
    document: str | None = None


def ensure_docs_dir():
    os.makedirs(DOCS_DIR, exist_ok=True)


ensure_docs_dir()
app.mount("/docs", StaticFiles(directory=DOCS_DIR), name="docs")


def sanitize_pdf_filename(filename: str) -> str:
    safe_name = os.path.basename((filename or "").strip())
    if not safe_name:
        raise HTTPException(status_code=400, detail="Invalid filename")
    if not safe_name.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    return safe_name


@app.post("/chat")
async def chat(request: ChatRequest):
    selected_document = sanitize_pdf_filename(request.document) if request.document else None
    full_context, context_by_file = search(request.message, source_filename=selected_document)
    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(
        context=full_context if full_context else "No relevant policy context was found."
    )

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": request.message,
            },
        ],
    )

    text = response.choices[0].message.content

    try:
        json_match = re.search(r"\{.*\}", text, re.DOTALL)
        if json_match:
            parsed = json.loads(json_match.group())
            parsed["sources"] = context_by_file
            parsed["document"] = selected_document
            return parsed
    except Exception:
        pass

    return {"answer": text, "suggested_questions": [], "sources": context_by_file, "document": selected_document}


@app.get("/")
async def root():
    return {"message": "ChatbotForZin API running"}


@app.get("/admin/files")
async def list_files():
    ensure_docs_dir()
    files = [f for f in os.listdir(DOCS_DIR) if f.lower().endswith(".pdf")]
    return {"files": sorted(files)}


@app.post("/admin/upload")
async def upload_file(file: UploadFile = File(...)):
    ensure_docs_dir()
    safe_name = sanitize_pdf_filename(file.filename)
    file_path = os.path.join(DOCS_DIR, safe_name)

    try:
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
        init_vectordb()
    except Exception as exc:
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(status_code=500, detail=f"Upload failed: {exc}") from exc
    finally:
        file.file.close()

    return {"message": f"{safe_name} uploaded", "filename": safe_name}


@app.delete("/admin/files/{filename}")
async def delete_file(filename: str):
    ensure_docs_dir()
    safe_name = sanitize_pdf_filename(filename)
    file_path = os.path.join(DOCS_DIR, safe_name)

    if os.path.exists(file_path):
        os.remove(file_path)
        init_vectordb()
        return {"message": f"{safe_name} deleted"}

    raise HTTPException(status_code=404, detail="File not found")


@app.post("/admin/reload")
async def reload_db():
    ensure_docs_dir()
    init_vectordb()
    return {"message": "DB reloaded"}
