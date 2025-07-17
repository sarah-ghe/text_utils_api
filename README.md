# 🧠 AI Text Utilities API

A FastAPI-based web service that lets you:
- ✂️ Summarize text
- 😊 Analyze sentiment
- 🔁 Paraphrase content
- 🏷️ Extract keywords

Built with 💡 FastAPI, HuggingFace Transformers, and PyTorch.

---

## 🚀 Live Demo

Check out the live API at:  
**https://text-utils-api-a4ub.onrender.com/docs**

---

## 📦 Features

- Fast and scalable REST API
- Modern async backend (FastAPI + Uvicorn)
- Clean, modular structure
- CORS enabled
- Easily extendable

---

## 🧪 Endpoints

| Method | Endpoint       | Description         |
|--------|----------------|---------------------|
| GET    | `/`            | Health check        |
| POST   | `/summarize`   | Summarize text      |
| POST   | `/sentiment`   | Sentiment analysis  |
| POST   | `/paraphrase`  | Paraphrase content  |
| POST   | `/keywords`    | Extract keywords    |

---

## 🧰 Example Request

```bash
POST /summarize
Content-Type: application/json

{
  "text": "FastAPI is a modern, fast web framework for building APIs with Python 3.6+ based on standard Python type hints."
}
