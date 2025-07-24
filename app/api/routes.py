from fastapi import APIRouter
from fastapi.responses import Response

from . import views
from app.schemas import BadgeInfoResponse

router = APIRouter()

# API 정보 엔드포인트
router.add_api_route(
    "/info", 
    views.get_badge_info, 
    methods=["GET"], 
    response_model=BadgeInfoResponse,
    summary="Get Badge Info",
    description="사용 가능한 Badge 옵션 정보를 반환합니다."
)

# 새로운 API 엔드포인트 (Pydantic 모델 사용)
router.add_api_route(
    "/badge", 
    views.generate_badge_by_username, 
    methods=["GET"], 
    response_class=Response,
    summary="Generate Badge",
    description="사용자명으로 Badge를 생성합니다."
)

# 레거시 엔드포인트 (하위 호환성)
router.add_api_route(
    "/badge/legacy", 
    views.generate_badge_by_username_legacy, 
    methods=["GET"], 
    response_class=Response
)

# 기존 레거시 URL
router.add_api_route(
    "/generate/api", 
    views.generate_badge_by_username_legacy, 
    methods=["GET"], 
    response_class=Response
)
