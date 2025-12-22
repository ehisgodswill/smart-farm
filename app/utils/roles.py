from fastapi import Depends, HTTPException, status
from app.models.user import User
from app.models.enums import UserRoleEnum
from app.services.auth_service import get_current_user

def require_admin(
    current_user: User = Depends(get_current_user),
) -> User:
    if current_user.role != UserRoleEnum.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required",
        )
    return current_user

def require_admin_or_manager(
    current_user: User = Depends(get_current_user),
) -> User:
    if current_user.role not in {
        UserRoleEnum.ADMIN,
        UserRoleEnum.FARM_MANAGER,
    }:
        raise HTTPException(status_code=403, detail="Access denied")
    return current_user
