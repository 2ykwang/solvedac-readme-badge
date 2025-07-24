from typing import Optional
from app.schemas import BadgeQueryParams
from app.component.badge import Badge, DefaultBadge, CompactBadge
from app.component.theme import Theme
from app.component.utils import make_theme
from app.solvedac import User
from app.factories.size_factory import SizeFactory


class BadgeFactory:
    """Badge 생성을 관리하는 팩토리 클래스"""
    
    @classmethod
    def create_badge(cls, user: Optional[User], params: BadgeQueryParams) -> Badge:
        """파라미터에 따라 적절한 Badge를 생성합니다."""
        # 크기 설정 가져오기
        size_config = SizeFactory.get_size_config(params.size, params.compact)
        
        # 테마 생성
        theme = cls._create_theme(params)
        
        # Badge 타입에 따라 생성
        if params.compact:
            badge = CompactBadge()
        else:
            badge = DefaultBadge()
        
        # 설정 적용
        badge.user = user
        badge.theme = theme
        badge.size = params.size
        badge._apply_size_config(size_config)
        
        return badge
    
    @classmethod
    def _create_theme(cls, params: BadgeQueryParams) -> Theme:
        """파라미터로부터 테마를 생성합니다."""
        from app.component.options import Options
        
        options = Options(
            theme=params.theme.value,
            size=params.size.value,
            back_color=params.back_color or "",
            common_color=params.common_color or "",
            sub_color=params.sub_color or "",
            border_color=params.border_color or "",
            use_back_color=params.use_back_color,
            use_border=params.use_border,
            use_shadow=params.use_shadow,
            is_compact=params.compact,
        )
        
        return make_theme(options)