from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# TODO: Import API routers here
# from .api.v1.router import api_router as api_v1_router

app = FastAPI(title="My Client Product API", version="0.1.0")

# --- CORS Middleware ---
# TODO: Restrict origins in production
origins = [
    "http://localhost",
    "http://localhost:5173",  # Default Vite dev server port
    "http://127.0.0.1:5173",
    # Add your frontend production domain here later
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- API Routers ---
# TODO: Include API routers here
# app.include_router(api_v1_router, prefix="/api/v1")

# --- Basic Health Check Endpoint ---
@app.get("/health", tags=["Health"])
async def health_check():
    """
    Simple health check endpoint.
    """
    return {"status": "ok"}

# --- Root Endpoint (Optional) ---
@app.get("/", tags=["Root"])
async def read_root():
    """
    Root endpoint providing basic info.
    """
    return {"message": "Welcome to the API!"}