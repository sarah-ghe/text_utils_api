from transformers import pipeline, Pipeline
from keybert import KeyBERT
from typing import Tuple, List

# Lazy-loaded models as singletons
_summarizer: Pipeline = None
_sentiment_analyzer: Pipeline = None
_paraphraser: Pipeline = None
_keybert: KeyBERT = None

def get_summarizer() -> Pipeline:
    global _summarizer
    if _summarizer is None:
        _summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return _summarizer

def get_sentiment_analyzer() -> Pipeline:
    global _sentiment_analyzer
    if _sentiment_analyzer is None:
        _sentiment_analyzer = pipeline("sentiment-analysis")
    return _sentiment_analyzer

def get_paraphraser() -> Pipeline:
    global _paraphraser
    if _paraphraser is None:
        _paraphraser = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws")
    return _paraphraser

def get_keybert() -> KeyBERT:
    global _keybert
    if _keybert is None:
        _keybert = KeyBERT()
    return _keybert

def summarize(text: str) -> str:
    summarizer = get_summarizer()
    try:
        output = summarizer(
            text,
            max_length=130,
            min_length=30,
            do_sample=False
        )
        return output[0]['summary_text']
    except Exception as e:
        raise RuntimeError(f"Summarization failed: {e}")

def sentiment(text: str) -> Tuple[str, float]:
    analyzer = get_sentiment_analyzer()
    try:
        output = analyzer(text)[0]
        return output['label'], float(output['score'])
    except Exception as e:
        raise RuntimeError(f"Sentiment analysis failed: {e}")

def paraphrase(text: str) -> str:
    paraphraser = get_paraphraser()
    try:
        output = paraphraser(
            f"paraphrase: {text}",
            max_length=256,
            num_return_sequences=1
        )
        return output[0]['generated_text']
    except Exception as e:
        raise RuntimeError(f"Paraphrasing failed: {e}")

def extract_keywords(text: str) -> List[str]:
    kb = get_keybert()
    try:
        keywords = kb.extract_keywords(text, top_n=5, stop_words='english')
        return [kw[0] for kw in keywords]
    except Exception as e:
        raise RuntimeError(f"Keyword extraction failed: {e}")
