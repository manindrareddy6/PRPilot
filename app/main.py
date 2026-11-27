from fastapi import FastAPI

app = FastAPI(
    title="PRPilot",
    description="AI-Powered GitHub Pull Request Reviewer",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to PRPilot",
        "status": "running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }