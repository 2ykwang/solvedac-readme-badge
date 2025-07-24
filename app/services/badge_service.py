from typing import Optional
from fastapi import HTTPException
from app.schemas import BadgeQueryParams
from app.factories.badge_factory import BadgeFactory
from app.services.user_service import UserService
from app.component.badge import Badge


class BadgeService:
    """Badge 생성을 관리하는 서비스 클래스"""
    
    def __init__(self, user_service: UserService):
        self.user_service = user_service
    
    def generate_badge(self, params: BadgeQueryParams) -> Badge:
        """Badge를 생성합니다."""
        # 사용자 정보 가져오기
        user = None
        if params.user:
            user = self.user_service.get_user(params.user)
        
        # Badge 생성
        badge = BadgeFactory.create_badge(user, params)
        
        return badge
    
    def generate_badge_svg(self, params: BadgeQueryParams) -> str:
        """Badge SVG를 생성합니다."""
        badge = self.generate_badge(params)
        return badge.render()