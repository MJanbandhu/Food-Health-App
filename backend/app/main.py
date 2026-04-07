from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.v1.router import api_router
from app.db.session import engine, Base
import os

# Create tables if not using migrations right away for ease of testing
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Food & Health Smart App Modular")

# Allows CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

# Ensure static files exist (to avoid crash during local dev if dist not built)
dist_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "dist")
if not os.path.exists(dist_dir):
    os.makedirs(dist_dir, exist_ok=True)

# Catch-all to serve index.html for React Router and static files
@app.get("/{full_path:path}")
def serve_react_app(full_path: str):
    # If the user is requesting a static asset (e.g. .css, .js, .svg)
    file_path = os.path.join(dist_dir, full_path)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return FileResponse(file_path)
        
    # Otherwise, fallback to serving index.html so React Router takes over
    index_path = os.path.join(dist_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "Frontend not built yet. Run npm run build."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)

