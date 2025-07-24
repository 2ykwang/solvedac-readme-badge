import logging
from typing import Optional, Union

from fastapi import Depends, HTTPException, Request, Response
from fastapi.responses import Response

from app.schemas import BadgeQueryParams, ErrorResponse, BadgeInfoResponse
from app.services.badge_service import BadgeService
from app.services.user_service import UserService
from app.dependencies import get_user_service, get_badge_service
from app.factories.size_factory import SizeFactory
from app.component.theme import Theme
from app import cache


async def get_badge_info() -> BadgeInfoResponse:
    """사용 가능한 Badge 옵션 정보를 반환합니다."""
    available_sizes = [size.value for size in SizeFactory.get_available_sizes()]
    available_themes = [theme.value for theme in Theme.get_available_themes().keys()]
    
    return BadgeInfoResponse(
        available_sizes=available_sizes,
        available_themes=available_themes,
        description="Solved.ac Badge Generator API"
    )


async def generate_badge_by_username(
    params: BadgeQueryParams = Depends(),
    badge_service: BadgeService = Depends(get_badge_service),
    request: Request = None
) -> Response:
    """사용자명으로 Badge를 생성합니다."""
    try:
        # Badge SVG 생성
        svg_content = badge_service.generate_badge_svg(params)
        
        # 캐시 헤더 설정
        config = request.app.state.config
        cache_max_age = config.CACHE_CONTROL
        headers = {"Cache-Control": f"public, max-age={cache_max_age}"}
        
        return Response(
            content=svg_content, 
            media_type="image/svg+xml", 
            headers=headers
        )
    except Exception as e:
        # 에러 응답
        error_response = ErrorResponse(
            error="Badge generation failed",
            message="Badge 생성 중 오류가 발생했습니다.",
            detail=str(e)
        )
        raise HTTPException(status_code=500, detail=error_response.dict())


# Legacy 함수 (하위 호환성을 위해 유지)
def generate_badge_by_username_legacy(request: Request) -> Response:
    """레거시 API를 위한 함수 (하위 호환성)"""
    # 쿼리 파라미터를 Pydantic 모델로 변환
    params = BadgeQueryParams(
        user=request.query_params.get("user"),
        theme=request.query_params.get("theme", "white"),
        size=request.query_params.get("size", "small"),
        common_color=request.query_params.get("common_color"),
        sub_color=request.query_params.get("sub_color"),
        back_color=request.query_params.get("back_color"),
        border_color=request.query_params.get("border_color"),
        use_shadow=_bool_parse(request.query_params.get("use_shadow", "true")),
        compact=_bool_parse(request.query_params.get("compact", "true")),
        use_back_color=_bool_parse(request.query_params.get("use_back_color", "true")),
        use_border=_bool_parse(request.query_params.get("use_border", "true")),
    )
    
    # 새로운 서비스 사용
    user_service = get_user_service(request)
    badge_service = BadgeService(user_service)
    
    try:
        svg_content = badge_service.generate_badge_svg(params)
        
        config = request.app.state.config
        cache_max_age = config.CACHE_CONTROL
        headers = {"Cache-Control": f"public, max-age={cache_max_age}"}
        
        return Response(
            content=svg_content, 
            media_type="image/svg+xml", 
            headers=headers
        )
    except Exception as e:
        import logging
        logging.getLogger("uvicorn.error").error(f"generate_badge_by_username - {e}")
        return Response(
            content="<svg>Error</svg>",
            media_type="image/svg+xml"
        )


def _bool_parse(text) -> bool:
    """문자열을 불린으로 파싱합니다."""
    if isinstance(text, bool):
        return text
    return str(text).lower() in ["yes", "true", "1", "t"]
