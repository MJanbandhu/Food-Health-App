from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserResponse

router = APIRouter()

@router.get("/me", response_model=UserResponse)
def get_current_user(db: Session = Depends(get_db)):
    # Standard MVP: Dummer user fetch
    user = db.query(User).filter(User.id == 1).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
