from typing import Annotated
from fastapi import Depends, Request

from app.services.user_service import UserService
from app.services.badge_service import BadgeService


def get_user_service(request: Request) -> UserService:
    """UserService 의존성을 제공합니다."""
    config = request.app.state.config
    return UserService(config.API_HOST, config.TIMEOUT)


def get_badge_service(user_service: Annotated[UserService, Depends(get_user_service)]) -> BadgeService:
    """BadgeService 의존성을 제공합니다."""
    return BadgeService(user_service)