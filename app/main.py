from fastapi import FastAPI
from app.models import (
    TextRequest,
    SummaryResponse,
    SentimentResponse,
    ParaphraseResponse,
    KeywordsResponse
)
from app.services import summarize, sentiment, paraphrase, extract_keywords
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Text Utilities API",
    description="Summarize, analyze, paraphrase, and extract keywords from text.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # URL de frontend Vite
    allow_credentials=True,
    allow_methods=["*"],  # Autoriser toutes les méthodes HTTP
    allow_headers=["*"],  # Autoriser tous les en-têtes HTTP
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/summarize", response_model=SummaryResponse)
def api_summarize(request: TextRequest):
    summary = summarize(request.text)
    return {"summary": summary}

@app.post("/sentiment", response_model=SentimentResponse)
def api_sentiment(request: TextRequest):
    label, score = sentiment(request.text)
    return {"label": label, "score": score}

@app.post("/paraphrase", response_model=ParaphraseResponse)
def api_paraphrase(request: TextRequest):
    paraphrased = paraphrase(request.text)
    return {"paraphrase": paraphrased}

@app.post("/keywords", response_model=KeywordsResponse)
def api_keywords(request: TextRequest):
    keywords = extract_keywords(request.text)
    return {"keywords": keywords}
