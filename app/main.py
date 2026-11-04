"""
Virtual Doctor Core FastAPI Application
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.config import settings
from app.api.routes import router as api_router

app = FastAPI(
    title=settings.APP_NAME,
    description="Clinical-grade Virtual Doctor Copilot with Red-Flag Triage, Vector RAG, and Embeddable Web Widget",
    version="0.1.0",
)

# CORS middleware for hospital websites & portals embedding
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Router
app.include_router(api_router)

# Mount embeddable static widget
widget_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "widget")
if os.path.exists(widget_dir):
    app.mount("/widget", StaticFiles(directory=widget_dir, html=True), name="widget")


@app.get("/")
async def root():
    return {
        "service": settings.APP_NAME,
        "api_docs": "/docs",
        "health": "/api/v1/health",
        "embed_demo": "/widget/demo.html"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG)
