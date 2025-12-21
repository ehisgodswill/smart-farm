from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.utils.db import get_db
from app.schemas.auth import (
    RefreshRequest,
    RegisterRequest,
    LoginRequest,
    TokenResponse,
    UserResponse
)
from app.services.auth_service import get_current_user, login, refresh_token, register
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserResponse)
def api_register(payload: RegisterRequest, db: Session = Depends(get_db)):
    return register(db, payload)


@router.post("/login", response_model=TokenResponse)
def api_login(payload: LoginRequest, db: Session = Depends(get_db)):
    token = login(db, payload.username, payload.password)
    return {"access_token": token}


@router.get("/me", response_model=UserResponse)
def api_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.post("/refresh", response_model=TokenResponse)
def api_refresh_token(payload: RefreshRequest, db: Session = Depends(get_db)):
  return refresh_token(db, payload)