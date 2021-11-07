"""

one dark
    back_color      -   #282C34
    sub_color       -   #D96D74
    common_color    -   #E3BE79

"""


class ColorSet:
    DEFAULT = "default"
    DARK = "dark"

    def __init__(self):
        self.common_color = "#333"
        self.sub_color = "#0099EF"
        self.back_color = "#FFF"
        self.use_back_color = False


def get_colorset(color_name, *args) -> ColorSet:
    r"""테마 이름을 입력받아 `ColorSet`을 반환합니다.

    :param color_name: 테마 이름 문자열
    :param args: Optional arguments
        use_back_color: (bool): 배경 색 적용 toggle

    :return: :class: `ColorSet` 객체
    :rtype: colorset.ColorSet
    """
    a = len(args)
    color_dict = {
        ColorSet.DEFAULT: "default",
        ColorSet.DARK: "dark",
    }
    result = ColorSet()

    if color_name in color_dict:
        pass
    else:
        pass

    return result
