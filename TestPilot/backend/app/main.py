
from fastapi import FastAPI

from .schemas import AnalyzeRequest
from .analyzer import analyze_test


app = FastAPI(
    title="TestPilot API",
    description="Explainable AI-Based Flaky Test Root Cause Analysis",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "application": "TestPilot",
        "message": "TestPilot backend is running successfully!"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": False,
        "supported_languages": ["java", "python"]
    }


@app.post("/api/analyze")
def analyze(request: AnalyzeRequest):
    return analyze_test(request)
