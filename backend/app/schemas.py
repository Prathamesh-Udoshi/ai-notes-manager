from pydantic import BaseModel

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    summary: str | None = None

class NoteOut(NoteBase):
    id: int
    summary: str | None

    class Config:
        from_attributes = True
