from fastapi import APIRouter
from app.database import SessionLocal
from app.models.bird import Bird

router = APIRouter()

@router.post("/")
def create_bird(pen_id: str):
    db = SessionLocal()
    bird = Bird(pen_id=pen_id)
    db.add(bird)
    db.commit()
    return {"bird_id": bird.id}
