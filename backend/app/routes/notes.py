from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.NoteOut)
def create_note(note: schemas.NoteCreate, db: Session = Depends(database.get_db)):
    new_note = models.Note(title=note.title, content=note.content)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

@router.get("/", response_model=list[schemas.NoteOut])
def get_notes(db: Session = Depends(database.get_db)):
    return db.query(models.Note).all()

@router.get("/{note_id}", response_model=schemas.NoteOut)
def get_note(note_id: int, db: Session = Depends(database.get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.put("/{note_id}", response_model=schemas.NoteOut)
def update_note(note_id: int, note_update: schemas.NoteUpdate, db: Session = Depends(database.get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    if note_update.title is not None:
        note.title = note_update.title
    if note_update.content is not None:
        note.content = note_update.content
    if note_update.summary is not None:
        note.summary = note_update.summary
    
    db.commit()
    db.refresh(note)
    return note

@router.delete("/{note_id}")
def delete_note(note_id: int, db: Session = Depends(database.get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return {"message": "Note deleted successfully"}
