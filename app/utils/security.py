import hashlib
import hmac
import uuid
from datetime import datetime, timedelta, timezone
from jose import jwt

SECRET_KEY = "CHANGE_THIS_IN_ENV"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

PASSWORD_SALT = b"CHANGE_THIS_SALT"

ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 30


def hash_password(password: str) -> str:
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        PASSWORD_SALT,
        100_000
    ).hex()


def verify_password(password: str, password_hash: str) -> bool:
    computed = hash_password(password)
    return hmac.compare_digest(computed, password_hash)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode["exp"] = expire
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token() -> tuple[str, datetime]:
    expires_at = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    return str(uuid.uuid4()), expires_at