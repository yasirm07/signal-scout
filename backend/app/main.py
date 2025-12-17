from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import AnalyzeRequest, AnalysisResult
from app.services.pipeline import run_analysis
from app.config import get_settings

settings = get_settings()

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    return {"status": "ok", "app": settings.app_name}


@app.post("/analyze", response_model=AnalysisResult)
async def analyze(payload: AnalyzeRequest):
    if not payload.business_name or not payload.city:
        raise HTTPException(status_code=400, detail="business_name and city are required")
    result = await run_analysis(payload.business_name, payload.city, payload.website)
    return result

