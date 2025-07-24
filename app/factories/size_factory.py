from typing import Dict, Any
from dataclasses import dataclass
from app.schemas import SizeEnum


@dataclass
class SizeConfig:
    width: int
    height: int
    font_size: float
    big_font_size: float = None
    small_font_size: float = None


class SizeFactory:
    """크기 설정을 관리하는 팩토리 클래스"""
    
    DEFAULT_SIZES = {
        SizeEnum.SMALL: {
            "default": SizeConfig(180, 180, 1.0),
            "compact": SizeConfig(240, 70, 1.0, 1.1, 0.85)
        },
        SizeEnum.MEDIUM: {
            "default": SizeConfig(270, 270, 1.5),
            "compact": SizeConfig(360, 105, 1.5, 1.65, 1.275)
        },
        SizeEnum.LARGE: {
            "default": SizeConfig(410, 410, 2.25),
            "compact": SizeConfig(540, 158, 2.25, 2.475, 1.915)
        }
    }

    @classmethod
    def get_size_config(cls, size: SizeEnum, is_compact: bool = True) -> SizeConfig:
        """크기 설정을 반환합니다."""
        badge_type = "compact" if is_compact else "default"
        return cls.DEFAULT_SIZES[size][badge_type]

    @classmethod
    def get_available_sizes(cls) -> list:
        """사용 가능한 크기 목록을 반환합니다."""
        return list(cls.DEFAULT_SIZES.keys())