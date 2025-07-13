from pydantic import BaseModel
from typing import List

class TextRequest(BaseModel):
    text: str

class SummaryResponse(BaseModel):
    summary: str

class SentimentResponse(BaseModel):
    label: str
    score: float

class ParaphraseResponse(BaseModel):
    paraphrase: str

class KeywordsResponse(BaseModel):
    keywords: List[str]
