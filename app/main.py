
from fastapi import FastAPI

app = FastAPI(
    title="DevOps Deployment Pipeline",
    description="A demo application for my DevOps portfolio",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Hello from my DevOps portfolio!",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }
