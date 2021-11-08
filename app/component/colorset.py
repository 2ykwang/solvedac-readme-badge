import re


class ColorSet:
    """
    뱃지, 카드 색상을 정의하는 클래스
    """
    DEFAULT = "default"
    DARK = "dark"
    ONEDARK = "onedark"

    def __init__(self,
                 common_color: str = "#333",
                 sub_color: str = "#0099EF",
                 back_color: str = "#FFF",
                 use_back_color: bool = True,
                 border_color: str = "#EEE",
                 use_border: bool = True
                 ):
        self.common_color = common_color
        self.sub_color = sub_color
        self.back_color = back_color
        self.use_back_color = use_back_color
        self.border_color = border_color
        self.use_border = use_border


__default_color = ColorSet(
    common_color="#333",
    sub_color="#0099EF",
    back_color="#FFF",
    border_color="#EEE",
    use_back_color=True,
    use_border=True
)
__dark_color = ColorSet(
    common_color="#fff",
    sub_color="#eee",
    back_color="#333",
    border_color="#EEE",
    use_back_color=True,
    use_border=True
)
__onedark_color = ColorSet(
    common_color="#E3BE79",
    sub_color="#D96D74",
    back_color="#282C34",
    border_color="#EEE",
    use_back_color=True,
    use_border=True
)

__color_set_dict = {
    ColorSet.DEFAULT: __default_color,
    ColorSet.DARK: __dark_color,
    ColorSet.ONEDARK: __onedark_color
}


def make_colorset(theme_name, options: dict = None) -> ColorSet:
    r"""테마 이름을 입력받아 `ColorSet`을 반환합니다.

    :param theme_name: 테마 이름 문자열
    :param options: dict
        use_back_color: (bool): 배경 색 적용 여부
        back_color: (str): 배경 색 Hex
        common_color: (str): common 글씨 색 Hex
        sub_color: (str): sub 글씨 색 Hex
        border_color: (str): 테두리 글씨 색
        use_border: (bool): 테두리 적용 여부

    :return: :class: `ColorSet` 객체
    :rtype: colorset.ColorSet
    """
    if options is None:
        options = {}

    result = ColorSet()

    if theme_name in __color_set_dict:
        result = __color_set_dict[theme_name]

    if 'use_back_color' in options:
        result.use_back_color = options['use_back_color']

    if 'back_color' in options and __is_hex(options['back_color']):
        result.back_color = f"#{options['back_color']}"

    if 'common_color' in options and __is_hex(options['common_color']):
        result.common_color = f"#{options['common_color']}"

    if 'sub_color' in options and __is_hex(options['sub_color']):
        result.sub_color = f"#{options['sub_color']}"

    if 'border_color' in options and __is_hex(options['border_color']):
        result.border_color = f"#{options['border_color']}"

    if 'use_border' in options:
        result.use_border = options['use_border']

    return result


def __is_hex(code: str) -> bool:
    _rgbstring = re.compile(r'[a-fA-F0-9]{3}(?:[a-fA-F0-9]{3})?$')
    return bool(_rgbstring.match(code))
