from fastapi import APIRouter
from ..services.summarizer import generate_summary
from ..services.title_generator import generate_title

router = APIRouter()

@router.post("/summarize")
def summarize_text(content: dict):
    text = content.get("text", "")
    summary = generate_summary(text)
    return {"summary": summary}

@router.post("/title")
def smart_title(content: dict):
    text = content.get("text", "")
    title = generate_title(text)
    return {"title": title}
