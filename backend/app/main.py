from fastapi import FastAPI
from .routes import notes, ai
from .database import engine, Base

# This creates the notes table automatically if not exists
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Notes API")

# Root endpoint
@app.get("/")
def root():
    return {"message": "Smart Notes API is running 🚀"}

app.include_router(notes.router, prefix="/notes", tags=["Notes"])
app.include_router(ai.router, prefix="/ai", tags=["AI"])
