from fastapi import FastAPI
from app.api.upload import router as upload_router

app = FastAPI(
    title="Sentinel Drift AI",
    version="1.0.0",
    description="AI-Powered Security Control Drift & Misconfiguration Detection"
)

app.include_router(upload_router)


@app.get("/")
def root():
    return {
        "status": "running",
        "project": "Sentinel Drift AI",
        "version": "1.0.0"
    }