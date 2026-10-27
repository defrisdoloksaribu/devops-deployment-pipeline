
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(
    title="DevOps Deployment Pipeline",
    description="A demo application for my DevOps portfolio",
    version="1.0.0",
)

Instrumentator().instrument(app).expose(app)


@app.get("/")
def home():
    return {
        "message": "Hello from my DevOps portfolio!",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
