# 🚀 FastAPI Starter with Templates & Static Assets

A minimal FastAPI application in Python 3.10+ featuring server-side rendered HTML with Jinja2 and a small, modern CSS card grid.

## ✨ Features

- `/` HTML page rendered with Jinja2 templates
- Responsive card grid layout with clean, modern styling
- `/health` endpoint for health checks
- Interactive Swagger UI at `/docs` and Redoc at `/redoc`
- Docker-ready

## 🗂️ Project Structure

```
app/
  main.py
  templates/
    index.html
  static/
    styles.css
Dockerfile
requirements.txt
```

## ▶️ Run locally

Prereqs: Python 3.10+

Create and activate a virtualenv (recommended), then install dependencies:

```bash
pip install -r requirements.txt
```

Start the dev server:

```bash
uvicorn app.main:app --reload
```

Open in your browser:

- Home page: http://127.0.0.1:8000/
- Health check: http://127.0.0.1:8000/health
- Swagger docs: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc
