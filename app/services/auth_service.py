import uuid
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from app.models.refresh_token import RefreshToken
from app.models.user import User
from app.models.enums import UserRoleEnum
from app.schemas.auth import RefreshRequest, RegisterRequest
from app.utils.db import get_db
from app.utils.security import (
    ALGORITHM, 
    SECRET_KEY, 
    create_refresh_token, 
    hash_password, 
    verify_password, 
    create_access_token
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def register(db: Session, payload: RegisterRequest) -> User:
    if db.query(User).filter(User.username == payload.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")

    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")

    user = User(
        id=str(uuid.uuid4()),
        username=payload.username,
        email=payload.email,
        password_hash=hash_password(payload.password),
        role=payload.role,
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def login(db: Session, username: str, password: str) -> dict:
    user = db.query(User).filter(User.username == username).first()

    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    access_token = create_access_token({
        "sub": user.id,
        "role": user.role
    })

    refresh_token_value, expires_at = create_refresh_token()

    refresh_token = RefreshToken(
        id=refresh_token_value,
        user_id=user.id,
        expires_at=expires_at
    )

    db.add(refresh_token)
    db.commit()

    return {
        "access_token": access_token,
        "refresh_token": refresh_token_value
    }


def refresh_token(db: Session, payload: RefreshRequest) -> dict:
    token = (
        db.query(RefreshToken)
        .filter(RefreshToken.id == payload.refresh_token)
        .first()
    )

    if not token or token.expires_at < datetime.now(timezone.utc):
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")

    user = db.query(User).filter(User.id == token.user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    # Rotate token (invalidate old one)
    db.delete(token)

    new_refresh, expires_at = create_refresh_token()
    db.add(RefreshToken(
        id=new_refresh,
        user_id=user.id,
        expires_at=expires_at
    ))

    access_token = create_access_token({
        "sub": user.id,
        "role": user.role
    })

    db.commit()

    return {
        "access_token": access_token,
        "refresh_token": new_refresh
    }


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        sub = payload.get("sub")
        if not isinstance(sub, str):
            raise JWTError("Invalid subject")

        user_id: str = sub

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user


def require_roles(*allowed_roles: UserRoleEnum):
    """Dependency factory to require specific roles for endpoints"""
    def role_checker(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions"
            )
        return current_user

    return role_checker