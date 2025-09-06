from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
from openai import OpenAI
from groq import Groq
from pypdf import PdfReader
from io import BytesIO

load_dotenv()

app = FastAPI(title="AI Career Coach API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    question: str
    history: Optional[List[dict]] = None

class CoverLetterRequest(BaseModel):
    job_description: str
    resume_text: Optional[str] = None

class RoadmapRequest(BaseModel):
    target_role: str
    experience_level: str

class HistoryItem(BaseModel):
    tool: str
    summary: str

# In-memory placeholder store (replace with DB later)
HISTORY: List[HistoryItem] = []

# Model providers and defaults
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY") or os.getenv("gsk")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "auto")  # openai | groq | auto

def _pick_provider() -> str:
    if MODEL_PROVIDER == "openai" and OPENAI_API_KEY:
        return "openai"
    if MODEL_PROVIDER == "groq" and GROQ_API_KEY:
        return "groq"
    # auto fallback order
    if OPENAI_API_KEY:
        return "openai"
    if GROQ_API_KEY:
        return "groq"
    return "stub"

def chat_complete(prompt: str) -> dict:
    provider = _pick_provider()
    try:
        if provider == "openai":
            mapped = {
                "openai/gpt-oss-120b": "gpt-4o-mini",
                "openai/gpt-oss-20b": "gpt-4o-mini",
            }.get(MODEL_NAME, MODEL_NAME)
            client = OpenAI(api_key=OPENAI_API_KEY)
            resp = client.chat.completions.create(
                model=mapped,
                messages=[{"role": "user", "content": prompt}],
            )
            text = resp.choices[0].message.content or ""
            return {"provider": provider, "model": mapped, "text": text}
        if provider == "groq":
            # If user supplied an explicit llama model name keep it, else default
            llama_default = "llama3-70b-8192"
            mapped = MODEL_NAME if any(k in MODEL_NAME.lower() for k in ["llama", "mixtral", "whisper"]) else llama_default
            client = Groq(api_key=GROQ_API_KEY)
            resp = client.chat.completions.create(
                model=mapped,
                messages=[{"role": "user", "content": prompt}],
            )
            text = resp.choices[0].message.content or ""
            return {"provider": provider, "model": mapped, "text": text}
        # stub fallback
        return {"provider": provider, "model": "stub", "text": f"Stub: {prompt}"}
    except Exception as e:
        return {"provider": provider, "model": MODEL_NAME, "text": f"Error from model: {e}"}

@app.get("/health")
async def health():
    return {"ok": True}

@app.post("/chat")
async def chat(req: ChatRequest):
    result = chat_complete(f"Answer the career question concisely: {req.question}")
    HISTORY.append(HistoryItem(tool="AI Career Q&A", summary=req.question[:80]))
    return {"answer": result["text"], "provider": result["provider"], "model": result["model"]}

@app.post("/resume/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    content = await file.read()
    text = ""
    if file.filename.lower().endswith('.pdf'):
        # Parse PDF in-memory to avoid filesystem/path issues on Windows
        try:
            reader = PdfReader(BytesIO(content))
            for page in reader.pages:
                text += page.extract_text() or ""
        except Exception:
            text = ""
    else:
        try:
            text = content.decode('utf-8', errors='ignore')
        except Exception:
            text = ""
    prompt = (
        "Provide actionable resume feedback in bullet points. "
        "Focus on impact, clarity, ATS, and quantification. Resume text:" + text[:6000]
    )
    feedback_dict = chat_complete(prompt)
    feedback = feedback_dict["text"]
    HISTORY.append(HistoryItem(tool="AI Resume Analyzer", summary=f"Analyzed {file.filename}"))
    return {"filename": file.filename, "feedback": feedback}

@app.post("/roadmap")
async def roadmap(req: RoadmapRequest):
    prompt = (
        f"Create a 6-step learning roadmap for a {req.target_role} at {req.experience_level} level. "
        "Each step should have a title and 2-3 bullet tasks."
    )
    reply_dict = chat_complete(prompt)
    reply_text = reply_dict["text"]
    plan = [s.strip("- ") for s in reply_text.split("\n") if s.strip()][:6] or [
        "Learn core skills", "Build projects", "Contribute to OSS", "Prepare for interviews"
    ]
    HISTORY.append(HistoryItem(tool="Career Roadmap Generator", summary=req.target_role))
    return {"steps": plan}

@app.post("/cover-letter")
async def cover_letter(req: CoverLetterRequest):
    prompt = (
        "Write a tailored, one-page cover letter. Use a confident tone, quantify achievements.\n"
        f"Job Description: {req.job_description}\nResume: {req.resume_text or ''}"
    )
    letter_dict = chat_complete(prompt)
    letter = letter_dict["text"]
    HISTORY.append(HistoryItem(tool="Cover Letter Generator", summary=req.job_description[:80]))
    return {"letter": letter}

@app.get("/history")
async def history():
    return {"items": [h.model_dump() for h in HISTORY]}

@app.get("/config")
async def config():
    return {
        "provider": _pick_provider(),
        "model_name": MODEL_NAME,
        "has_openai_key": bool(OPENAI_API_KEY),
        "has_groq_key": bool(GROQ_API_KEY),
        "history_items": len(HISTORY),
    }
