from pydantic import BaseModel, EmailStr
from datetime import datetime
from app.models.enums import UserRoleEnum


class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: UserRoleEnum


class LoginRequest(BaseModel):
    username: str
    password: str


class RefreshRequest(BaseModel):
    refresh_token: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str


class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr
    role: UserRoleEnum
    created_at: datetime
