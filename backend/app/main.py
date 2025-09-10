from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import notes, ai
from .database import engine, Base

# Create tables automatically if not exists
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Notes API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",       # local dev
        "https://your-frontend.vercel.app"  # deployed frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Smart Notes API is running 🚀"}

# Routers
app.include_router(notes.router, prefix="/notes", tags=["Notes"])
app.include_router(ai.router, prefix="/ai", tags=["AI"])
