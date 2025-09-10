from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import notes, ai
from .database import engine, Base
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    print("Initializing database...")
    Base.metadata.create_all(bind=engine)
    print("Database initialized ✅")
    yield
    # Shutdown code (if any)
    print("Shutting down...")

app = FastAPI(title="Smart Notes API", lifespan=lifespan)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # local dev
        # add frontend URL later
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
