from abc import abstractmethod
from typing import Final

from app.component.options import Options
from app.component.theme import Theme
from app.component.utils import (
    get_tier_hex_color,
    get_tier_icon,
    get_tier_text,
    make_theme,
)
from app.solvedac import User


class Badge:
    USER_NOT_FOUND: Final = "사용자를 불러오지 못했습니다."

    def __init__(self):
        """ """
        self.width = 180
        self.height = 180
        self.styles = ""
        self._styles = ""
        self.user: User = None
        self.theme: Theme = None
        self.size = Options.DEFAULT_SIZE

    @abstractmethod
    def _set_size(self) -> None:
        pass

    @abstractmethod
    def error_render(self, message: str) -> str:
        pass

    def _render(self, body: str) -> str:

        if self.theme is None:
            self.theme = make_theme(Options())

        border = (
            f'stroke="{self.theme.border_color}" stroke-opacity="1" stroke-width="0.5"'
        )
        drop_shadow = (
            f"filter: drop-shadow({get_tier_hex_color(self.user.tier)} 0px 1px 6px);"
            if self.theme.use_shadow and self.user is not None
            else ""
        )

        back_ground = f"<rect x=\"0\" y=\"0\" width=\"99%\" height=\"99%\" rx=\"2.5\" ry=\"2.5\" fill=\"{self.theme.back_color}\" {border if self.theme.use_border else ''}/> "
        return f"""
        <svg
            width="{self.width}"
            height="{self.height}"
            xmlns="http://www.w3.org/2000/svg"> 
            <style>
            #tier_badge {{ {drop_shadow} }}
            .common_color{{ fill: {self.theme.common_color}; color: {self.theme.common_color}; }}
            .sub_color{{ fill: {self.theme.sub_color}; color: {self.theme.sub_color};}}
            .text{{ font-family: -apple-system,BlinkMacSystemFont,'Segoe UI', Ubuntu, Sans-Serif;}}
            {self.styles}
            {self._styles}
            </style>
            {back_ground if self.theme.use_back_color else ""}
            <g>
                {body}
            </g>
        </svg>"""

    def render(self, body: str) -> str:

        self._set_size()

        if self.user is None:
            return self.error_render(self.USER_NOT_FOUND)

        return self._render(body)


class DefaultBadge(Badge):
    def __init__(self):
        super(DefaultBadge, self).__init__()

        self.__sizes = {
            Options.SMALL_SIZE: {"width": 180, "height": 180, "font_size": 1},
            Options.MEDIUM_SIZE: {"width": 270, "height": 270, "font_size": 1.5},
            Options.LARGE_SIZE: {"width": 410, "height": 410, "font_size": 2.25},
        }
        self.width = self.__sizes[Options.DEFAULT_SIZE]["width"]
        self.height = self.__sizes[Options.DEFAULT_SIZE]["height"]
        self.font_size = self.__sizes[Options.DEFAULT_SIZE]["font_size"]

    def _set_size(self):
        if self.size in self.__sizes:
            size = self.__sizes[self.size]
            self.width = size["width"]
            self.height = size["height"]
            self.font_size = size["font_size"]

    def error_render(self, message: str) -> str:
        self._set_size()

        self._styles = f"""
        #error_message {{ font-size: {self.font_size}em; font-weight: 600; }}
        .description {{ text-align: center; display: inline-block; width: 100%; height: 100%; white-space:normal; }}
        """
        error_text = f"""
        <title>badge {self.size}</title>
        <svg y="50%">
          <title>Error message</title>
            <foreignObject width="100%" height="100%">
            <xhtml:span xmlns:xhtml="http://www.w3.org/1999/xhtml" id = "error_message" class="text description sub_color">
              {message}
            </xhtml:span>
          </foreignObject>
        </svg>
            """
        return super(DefaultBadge, self)._render(error_text)

    def render(self) -> str:
        self._set_size()

        if self.user is None:
            return self.error_render(self.USER_NOT_FOUND)

        tier_icon = get_tier_icon(self.user.tier)

        """
            <!-- small 180, 180 1-->
            <!-- medium 270, 270 1.5-->
            <!-- large 410, 410 2.25-->
        """
        self._styles = f"""
        #username {{ font-size: {self.font_size}em; font-weight: 600; }}
        .description {{ overflow: hidden; text-overflow: ellipsis; text-align: center; display: inline-block; width: 100%; height: 100%; white-space: nowrap; }}
        """
        body = f"""
        <title>badge {self.size}</title>
        <svg
            x="15%"
            y="9%"
            height="70%"
            width="70%"
            id="tier_icon">{tier_icon}</svg>
        <svg y="85%" >
          <title>닉네임</title>
            <foreignObject width="100%" height="100%">
            <xhtml:span xmlns:xhtml="http://www.w3.org/1999/xhtml" id = "username" class="text description sub_color">
              {self.user.username}
            </xhtml:span>
          </foreignObject>
        </svg>
            """
        return super(DefaultBadge, self).render(body)


class CompactBadge(Badge):
    def __init__(self):
        super(CompactBadge, self).__init__()

        self.__sizes = {
            Options.SMALL_SIZE: {
                "width": 240,
                "height": 70,
                "big_font_size": 1.1,
                "small_font_size": 0.85,
            },
            Options.MEDIUM_SIZE: {
                "width": 360,
                "height": 105,
                "big_font_size": 1.65,
                "small_font_size": 1.275,
            },
            Options.LARGE_SIZE: {
                "width": 540,
                "height": 158,
                "big_font_size": 2.475,
                "small_font_size": 1.915,
            },
        }
        self.width = self.__sizes[Options.DEFAULT_SIZE]["width"]
        self.height = self.__sizes[Options.DEFAULT_SIZE]["height"]
        self.big_font_size = self.__sizes[Options.DEFAULT_SIZE]["big_font_size"]
        self.small_font_size = self.__sizes[Options.DEFAULT_SIZE]["small_font_size"]

    def _set_size(self):
        if self.size in self.__sizes:
            size = self.__sizes[self.size]
            self.width = size["width"]
            self.height = size["height"]
            self.big_font_size = size["big_font_size"]
            self.small_font_size = size["small_font_size"]

    def error_render(self, message: str) -> str:
        self._set_size()

        self._styles = f"""
        #error_title {{  font-size: {self.big_font_size}em; font-weight: 600; letter-spacing: 0.15em; }}
        #error_message {{ font-size: {self.small_font_size}em; font-weight: 600; }}
        .description {{ overflow: hidden; text-overflow: ellipsis; text-align: center; display: inline-block; width: 100%; height: 100%; white-space: nowrap; }}
        """
        error_text = f"""
        <title>badge compact {self.size}</title>
        <svg y="15%">
          <title>Error title</title>
          <foreignObject width="100%" height="100%">
            <xhtml:span xmlns:xhtml="http://www.w3.org/1999/xhtml" id="error_title" class="text description common_color">
              ERROR
            </xhtml:span>
          </foreignObject>
        </svg>
        <svg y="48%" >
          <title>Error message</title>
          <foreignObject width="100%" height="100%">
            <xhtml:span xmlns:xhtml="http://www.w3.org/1999/xhtml" id = "error_message" class="text description sub_color">
              {message}
            </xhtml:span>
          </foreignObject>
        </svg>
        """
        return super(CompactBadge, self)._render(error_text)

    def render(self) -> str:
        self._set_size()

        if self.user is None:
            return self.error_render(self.USER_NOT_FOUND)

        tier_icon = get_tier_icon(self.user.tier)
        tier_text = get_tier_text(self.user.tier)

        """
            <!-- small 240, 70  1.1, 0.85-->
            <!-- medium 360, 105 1.65, 1.275-->
            <!-- large 540, 158 2.475 1.915-->
        """
        self._styles = f"""
        #tier_text {{  font-size: {self.big_font_size}em; font-weight: 600; letter-spacing: 0.15em;   }}
        #username {{ font-size: {self.small_font_size}em; font-weight: 600; }}
        .description {{ overflow: hidden; text-overflow: ellipsis; text-align: center; display: inline-block; width: 70%; height: 100%; white-space: nowrap; }}
        """
        body = f"""
        <title>badge compact</title>
        <svg width ="20%" height="80%" x="5%" y="10%" id="tier_badge">
            {tier_icon}
        </svg>
        <svg x="29%" y="15%">
          <title>랭크</title>
          <foreignObject width="100%" height="100%">
            <xhtml:span xmlns:xhtml="http://www.w3.org/1999/xhtml" id="tier_text" class="text description common_color">
              {tier_text}
            </xhtml:span>
          </foreignObject>
        </svg>
        <svg x="29%" y="48%" >
          <title>닉네임</title>
          <foreignObject width="100%" height="100%">
            <xhtml:span xmlns:xhtml="http://www.w3.org/1999/xhtml" id = "username" class="text description sub_color">
              {self.user.username}
            </xhtml:span>
          </foreignObject>
        </svg>
        """
        return super(CompactBadge, self).render(body)
