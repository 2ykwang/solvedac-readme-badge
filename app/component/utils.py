import copy
import re

from app.component.options import Options
from app.component.theme import THEME_DICT, Theme
from app.component.tier import (
    BRONZE,
    DIAMOND,
    GOLD,
    MASTER,
    PLATINUM,
    RUBY,
    SILVER,
    TIER_BADGE_COLORS,
    TIER_ICONS,
    TIER_TEXT,
    UNKNOWN,
)
from app.solvedac import User


def get_tier_text(level: int) -> str:
    if level in TIER_TEXT:
        return TIER_TEXT[level]
    else:
        return TIER_TEXT[0]


def get_tier_icon(level: int) -> str:
    if level in TIER_ICONS:
        return TIER_ICONS[level]
    else:
        return TIER_ICONS[0]


def get_tier_section(level: int) -> int:
    if level <= 0:
        return UNKNOWN
    elif level <= 5:
        return BRONZE
    elif level <= 10:
        return SILVER
    elif level <= 15:
        return GOLD
    elif level <= 20:
        return PLATINUM
    elif level <= 25:
        return DIAMOND
    elif level <= 30:
        return RUBY
    elif level <= 31:
        return MASTER
    else:
        return UNKNOWN


def get_tier_hex_color(level: int) -> str:
    section = get_tier_section(level)
    return TIER_BADGE_COLORS[section]


def make_theme(options: Options) -> Theme:
    r"""옵션을 입력받아 `Theme`을 반환합니다.

    :param options: 옵션 객체

    :return: :class: `theme` 객체
    :rtype: Theme
    """
    if options is None:
        options = {}

    theme = Theme()

    if options.theme in THEME_DICT:
        theme = copy.deepcopy(THEME_DICT[options.theme])

    if __is_hex(options.back_color):
        theme.back_color = f"#{options.back_color}"

    if __is_hex(options.common_color):
        theme.common_color = f"#{options.common_color}"

    if __is_hex(options.sub_color):
        theme.sub_color = f"#{options.sub_color}"

    if __is_hex(options.border_color):
        theme.border_color = f"#{options.border_color}"

    theme.use_back_color = options.use_back_color
    theme.use_border = options.use_border
    theme.use_shadow = options.use_shadow

    return theme


def make_badge(user: User = None, options: Options = None):
    """레거시 호환성을 위한 함수입니다. 새로운 코드에서는 BadgeFactory를 사용하세요."""
    from app.component.badge import CompactBadge, DefaultBadge
    from app.factories.size_factory import SizeFactory

    if options is None:
        options = Options()

    # 새로운 팩토리 패턴 사용
    from app.schemas import BadgeQueryParams, SizeEnum, ThemeEnum
    
    params = BadgeQueryParams(
        user=None,  # user는 별도로 설정
        theme=ThemeEnum(options.theme),
        size=SizeEnum(options.size),
        common_color=options.common_color or None,
        sub_color=options.sub_color or None,
        back_color=options.back_color or None,
        border_color=options.border_color or None,
        use_shadow=options.use_shadow,
        compact=options.is_compact,
        use_back_color=options.use_back_color,
        use_border=options.use_border,
    )
    
    from app.factories.badge_factory import BadgeFactory
    badge = BadgeFactory.create_badge(user, params)
    
    return badge


def __is_hex(code: str) -> bool:
    _rgbstring = re.compile(r"[a-fA-F0-9]{3}(?:[a-fA-F0-9]{3})?$")
    return bool(_rgbstring.match(code))
