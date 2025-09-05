from fastapi import FastAPI
from .routes import notes, ai
from .database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Notes API")

# Routers
app.include_router(notes.router, prefix="/notes", tags=["Notes"])
app.include_router(ai.router, prefix="/ai", tags=["AI"])
