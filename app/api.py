from fastapi import APIRouter, HTTPException
from app.models import (
    TextRequest,
    SummaryResponse,
    SentimentResponse,
    ParaphraseResponse,
    KeywordsResponse
)
from app import services

router = APIRouter()

MAX_LENGTH = 3000  # Limit text length to prevent memory issues
MIN_LENGTH = 3     # Ignore text that is too short to process


def validate_text(text: str):
    cleaned = text.strip()
    
    if not cleaned:
        raise HTTPException(status_code=400, detail="Text cannot be empty or only whitespace.")
    
    if len(cleaned) < MIN_LENGTH:
        raise HTTPException(status_code=400, detail="Text is too short to process.")
    
    if len(cleaned) > MAX_LENGTH:
        raise HTTPException(status_code=400, detail=f"Text is too long (max {MAX_LENGTH} characters).")
    
    return cleaned


@router.get("/")
def wake_me_up():
    return {"message": "I'm awake!"}


@router.post("/summarize", response_model=SummaryResponse)
def api_summarize(request: TextRequest):
    try:
        text = validate_text(request.text)
        summary = services.summarize(text)
        return {"summary": summary}
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/sentiment", response_model=SentimentResponse)
def api_sentiment(request: TextRequest):
    try:
        text = validate_text(request.text)
        label, score = services.sentiment(text)
        return {"label": label, "score": score}
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/paraphrase", response_model=ParaphraseResponse)
def api_paraphrase(request: TextRequest):
    try:
        text = validate_text(request.text)
        paraphrased = services.paraphrase(text)
        return {"paraphrase": paraphrased}
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/keywords", response_model=KeywordsResponse)
def api_keywords(request: TextRequest):
    try:
        text = validate_text(request.text)
        keywords = services.extract_keywords(text)
        return {"keywords": keywords}
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
