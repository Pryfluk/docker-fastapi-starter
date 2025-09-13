from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="My FastAPI App",
    description="A simple FastAPI app with health check and Swagger UI",
    version="1.0.0"
)

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/health", tags=["Health"])
async def health_check():
    return JSONResponse(content={"status": "ok"})


@app.get("/", tags=["Pages"])
async def read_root(request: Request):
    sample_cards = [
        {"name": "Wichy", "description": "Software Engineer"},
        {"name": "Ai", "description": "Software Engineer"},
        {"name": "Bank", "description": "Software Engineer"},
    ]
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "cards": sample_cards},
    )
