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

    from app.component.badge import CompactBadge, DefaultBadge

    if options is None:
        options = Options()

    badge = CompactBadge() if options.is_compact else DefaultBadge()

    theme = make_theme(options)
    badge.theme = theme
    badge.size = options.size
    badge.user = user

    return badge


def __is_hex(code: str) -> bool:
    _rgbstring = re.compile(r"[a-fA-F0-9]{3}(?:[a-fA-F0-9]{3})?$")
    return bool(_rgbstring.match(code))
