from typing import Final

from app.component.options import Options


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


THEME_WHITE = Theme(
    common_color="#333",
    sub_color="#0099EF",
    back_color="#FFF",
    border_color="#E4E2E2",
)
THEME_SWIFT = Theme(
    common_color="#000",
    sub_color="#E44D35",
    back_color="#FFF",
    border_color="#E4E2E2",
)
THEME_DARK = Theme(
    common_color="#fff",
    sub_color="#599552",
    back_color="#121619",
    border_color="#2D373F",
)
THEME_ONEDARK = Theme(
    common_color="#E3BE79",
    sub_color="#D96D74",
    back_color="#282C34",
    border_color="#E4E2E2",
)
THEME_GITHUB_DARK = Theme(
    common_color="#a2d2fb",
    sub_color="#cea5fb",
    back_color="#21262d",
    border_color="#E4E2E2",
)

THEME_DICT = {
    Theme.WHITE: THEME_WHITE,
    Theme.SWIFT: THEME_SWIFT,
    Theme.DARK: THEME_DARK,
    Theme.ONEDARK: THEME_ONEDARK,
    Theme.GITHUB_DARK: THEME_GITHUB_DARK,
}
