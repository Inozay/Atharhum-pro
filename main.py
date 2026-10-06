from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

ROOT = Path(__file__).resolve().parent.parent
FRONTEND = ROOT / "frontend"

app = FastAPI(title="أَثَرُهُم", version="2.0.0")

# Lightweight demo API: intentionally dependency-free beyond FastAPI.
@app.get("/api/health")
def health():
    return {"status": "ok", "service": "atharhum", "version": "2.0.0"}

@app.get("/api/stats")
def stats():
    return {
        "verified": 1284,
        "sources": 367,
        "learners": 942,
        "trust_score": 96
    }

# Serve the complete frontend from the same service.
app.mount("/assets", StaticFiles(directory=FRONTEND / "assets"), name="assets")

@app.get("/{full_path:path}")
def frontend(full_path: str):
    # API routes are handled above; every remaining route gets the SPA.
    return FileResponse(FRONTEND / "index.html")
