from typing import Final, Dict, Optional
from dataclasses import dataclass
from enum import Enum


class ThemeName(str, Enum):
    """사용 가능한 테마 이름들"""
    WHITE = "white"
    SWIFT = "swift"
    DARK = "dark"
    ONEDARK = "onedark"
    GITHUB_DARK = "github-dark"


@dataclass
class ThemeConfig:
    """테마 설정을 담는 데이터 클래스"""
    common_color: str
    sub_color: str
    back_color: str
    border_color: str
    use_back_color: bool = True
    use_border: bool = True
    use_shadow: bool = True


class Theme:
    """
    뱃지, 카드 색상을 정의하는 클래스
    """

    WHITE: Final = "white"
    SWIFT: Final = "swift"
    DARK: Final = "dark"
    ONEDARK: Final = "onedark"
    GITHUB_DARK: Final = "github-dark"

    def __init__(
        self,
        common_color: str = "#333",
        sub_color: str = "#0099EF",
        back_color: str = "#FFF",
        use_back_color: bool = True,
        border_color: str = "#EEE",
        use_border: bool = True,
        use_shadow: bool = True,
    ):
        self.common_color = common_color
        self.sub_color = sub_color
        self.back_color = back_color
        self.border_color = border_color
        self.use_back_color = use_back_color
        self.use_border = use_border
        self.use_shadow = use_shadow

    @classmethod
    def from_config(cls, config: ThemeConfig) -> 'Theme':
        """ThemeConfig로부터 Theme을 생성합니다."""
        return cls(
            common_color=config.common_color,
            sub_color=config.sub_color,
            back_color=config.back_color,
            border_color=config.border_color,
            use_back_color=config.use_back_color,
            use_border=config.use_border,
            use_shadow=config.use_shadow,
        )

    @staticmethod
    def get_theme_list():
        return THEME_DICT.keys()

    @staticmethod
    def get_available_themes() -> Dict[str, ThemeConfig]:
        """사용 가능한 테마 목록을 반환합니다."""
        return THEME_CONFIGS


# 테마 설정들
THEME_CONFIGS = {
    ThemeName.WHITE: ThemeConfig(
        common_color="#333",
        sub_color="#0099EF",
        back_color="#FFF",
        border_color="#E4E2E2",
    ),
    ThemeName.SWIFT: ThemeConfig(
        common_color="#000",
        sub_color="#E44D35",
        back_color="#FFF",
        border_color="#E4E2E2",
    ),
    ThemeName.DARK: ThemeConfig(
        common_color="#fff",
        sub_color="#599552",
        back_color="#121619",
        border_color="#2D373F",
    ),
    ThemeName.ONEDARK: ThemeConfig(
        common_color="#E3BE79",
        sub_color="#D96D74",
        back_color="#282C34",
        border_color="#E4E2E2",
    ),
    ThemeName.GITHUB_DARK: ThemeConfig(
        common_color="#a2d2fb",
        sub_color="#cea5fb",
        back_color="#21262d",
        border_color="#E4E2E2",
    ),
}

# 레거시 호환성을 위한 테마 객체들
THEME_WHITE = Theme.from_config(THEME_CONFIGS[ThemeName.WHITE])
THEME_SWIFT = Theme.from_config(THEME_CONFIGS[ThemeName.SWIFT])
THEME_DARK = Theme.from_config(THEME_CONFIGS[ThemeName.DARK])
THEME_ONEDARK = Theme.from_config(THEME_CONFIGS[ThemeName.ONEDARK])
THEME_GITHUB_DARK = Theme.from_config(THEME_CONFIGS[ThemeName.GITHUB_DARK])

THEME_DICT = {
    Theme.WHITE: THEME_WHITE,
    Theme.SWIFT: THEME_SWIFT,
    Theme.DARK: THEME_DARK,
    Theme.ONEDARK: THEME_ONEDARK,
    Theme.GITHUB_DARK: THEME_GITHUB_DARK,
}
