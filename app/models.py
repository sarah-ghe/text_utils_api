from pydantic import BaseModel, Field
from typing import List

class TextRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Text to analyze")

class SummaryResponse(BaseModel):
    summary: str

class SentimentResponse(BaseModel):
    label: str
    score: float

class ParaphraseResponse(BaseModel):
    paraphrase: str

class KeywordsResponse(BaseModel):
    keywords: List[str]
