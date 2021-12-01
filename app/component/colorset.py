import copy
import re
from typing import Final

from app.component.options import Options


class ColorSet:
    """
    뱃지, 카드 색상을 정의하는 클래스
    """

    WHITE: Final = "WHITE"
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


__white_color = ColorSet(
    common_color="#333",
    sub_color="#0099EF",
    back_color="#FFF",
    border_color="#E4E2E2",
)
__swift_color = ColorSet(
    common_color="#000",
    sub_color="#E44D35",
    back_color="#FFF",
    border_color="#E4E2E2",
)
__dark_color = ColorSet(
    common_color="#fff",
    sub_color="#599552",
    back_color="#121619",
    border_color="#2D373F",
)
__onedark_color = ColorSet(
    common_color="#E3BE79",
    sub_color="#D96D74",
    back_color="#282C34",
    border_color="#E4E2E2",
)
__github_dark_color = ColorSet(
    common_color="#a2d2fb",
    sub_color="#cea5fb",
    back_color="#21262d",
    border_color="#E4E2E2",
)

__color_set_dict = {
    ColorSet.WHITE: __white_color,
    ColorSet.SWIFT: __swift_color,
    ColorSet.DARK: __dark_color,
    ColorSet.ONEDARK: __onedark_color,
    ColorSet.GITHUB_DARK: __github_dark_color,
}


def make_colorset(options: Options) -> ColorSet:
    r"""옵션을 입력받아 `ColorSet`을 반환합니다.

    :param options: 옵션 객체

    :return: :class: `ColorSet` 객체
    :rtype: colorset.ColorSet
    """
    if options is None:
        options = {}

    colorset = ColorSet()

    if options.theme in __color_set_dict:
        colorset = copy.deepcopy(__color_set_dict[options.theme])

    if __is_hex(options.back_color):
        colorset.back_color = f"#{options.back_color}"

    if __is_hex(options.common_color):
        colorset.common_color = f"#{options.common_color}"

    if __is_hex(options.sub_color):
        colorset.sub_color = f"#{options.sub_color}"

    if __is_hex(options.border_color):
        colorset.border_color = f"#{options.border_color}"

    colorset.use_back_color = options.use_back_color
    colorset.use_border = options.use_border
    colorset.use_shadow = options.use_shadow

    return colorset


def __is_hex(code: str) -> bool:
    _rgbstring = re.compile(r"[a-fA-F0-9]{3}(?:[a-fA-F0-9]{3})?$")
    return bool(_rgbstring.match(code))
