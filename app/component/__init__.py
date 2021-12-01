from typing import Final

BADGE_SMALL_SIZE: Final = "small"
BADGE_MEDIUM_SIZE: Final = "medium"
BADGE_LARGE_SIZE: Final = "large"
BADGE_DEFAULT_SIZE: Final = BADGE_SMALL_SIZE

USER_NOT_FOUND: Final = "사용자를 불러오지 못했습니다."

from .badge import Badge as Badge
from .badge import CompactBadge as CompactBadge
from .badge import DefaultBadge as DefaultBadge
from .badge import make_badge as make_badge
from .colorset import ColorSet as ColorSet
from .colorset import make_colorset
from .options import Options
