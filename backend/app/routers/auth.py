from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User

router = APIRouter(prefix="/auth", tags=["auth"])

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

@router.post("/signup", response_model=Token)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    # In a real app, hash password and save to DB
    # db_user = User(username=user.username, hashed_password=fake_hash(user.password))
    # db.add(db_user)
    # db.commit()
    return {"access_token": "fake-jwt-token", "token_type": "bearer"}

@router.post("/login", response_model=Token)
def login(user: UserCreate, db: Session = Depends(get_db)):
    # Verify user
    return {"access_token": "fake-jwt-token", "token_type": "bearer"}
