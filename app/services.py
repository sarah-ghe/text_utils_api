from transformers import pipeline
import spacy
from keybert import KeyBERT

# Load models only once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
sentiment_analyzer = pipeline("sentiment-analysis")
paraphraser = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws")
nlp = spacy.load("en_core_web_sm")
kb = KeyBERT()

def summarize(text: str) -> str:
    output = summarizer(
        text,
        max_length=130,
        min_length=30,
        do_sample=False
    )
    return output[0]['summary_text']

def sentiment(text: str) -> (str, float):
    output = sentiment_analyzer(text)[0]
    return output['label'], float(output['score'])

def paraphrase(text: str) -> str:
    output = paraphraser(
        f"paraphrase: {text}",
        max_length=256,
        num_return_sequences=1
    )
    return output[0]['generated_text']

def extract_keywords(text: str) -> list:
    return kb.extract_keywords(text, top_n=5, stop_words='english')
