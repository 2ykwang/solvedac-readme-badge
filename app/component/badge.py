from typing import Dict
from . import BADGE_DEFAULT_SIZE, BADGE_LARGE_SIZE, BADGE_MEDIUM_SIZE, BADGE_SMALL_SIZE
from .colorset import ColorSet, make_colorset
from ..solvedac import (
    User,
    get_tier_text,
    get_tier_icon
)


class Badge:

    def __init__(self):
        """
        """
        self.width = 140
        self.height = 140
        self.styles = ""
        self._styles = ""
        self.user = None
        self.colorset: ColorSet = make_colorset(ColorSet.DEFAULT)
        self.size = BADGE_DEFAULT_SIZE

    def render(self):
        pass

    def _render(self, body: str) -> str:
        # 기본 뼈대

        border = f"stroke=\"{self.colorset.border_color}\" stroke-opacity=\"1\" stroke-width=\"0.5\""
        back_ground = f"<rect x=\"0\" y=\"0\" width=\"99%\" height=\"99%\" rx=\"2.5\" ry=\"2.5\" fill=\"{self.colorset.back_color}\" {border if self.colorset.use_border else ''}/> "
        return f"""
        <svg
            width="{self.width}"
            height="{self.height}"
            xmlns="http://www.w3.org/2000/svg"> 
            <style>
            .common_color{{ fill: {self.colorset.common_color}; color: {self.colorset.common_color}; }}
            .sub_color{{ fill: {self.colorset.sub_color}; color: {self.colorset.sub_color};}}
            .text{{ font-family: -apple-system,BlinkMacSystemFont,'Segoe UI', Ubuntu, Sans-Serif;}}
            {self.styles}
            {self._styles}
            </style>
            {back_ground if self.colorset.use_back_color else ""}
            <g>
                {body}
            </g>
        </svg>"""

    def error_render(self, message: str) -> str:
        error_text = f""" 
            <text
            fill="#000000"
            stroke="#000"
            x="50%"
            y="50%"
            dominant-baseline="middle"
            text-anchor="middle"
            stroke-width="0"
            font-size="14"
            class="common_color"
            id="username">{message}</text> 
        """
        return self._render(error_text)


class DefaultBadge(Badge):
    def __init__(self):
        super(DefaultBadge, self).__init__()
        self.width = 180
        self.height = 180
        self.font_size = 1

    def render(self) -> str:
        tier_icon = get_tier_icon(self.user.tier)

        """
            <!-- small 180, 180 1-->
            <!-- medium 270, 270 1.5-->
            <!-- large 410, 410 2.25-->
        """
        if self.size == BADGE_SMALL_SIZE:
            self.width = 180
            self.height = 180
            self.font_size = 1
        elif self.size == BADGE_MEDIUM_SIZE:
            self.width = 270
            self.height = 270
            self.font_size = 1.5
        elif self.size == BADGE_LARGE_SIZE:
            self.width = 410
            self.height = 410
            self.font_size = 2.25

        self._styles = f"""
        #username {{
            font-size: {self.font_size}em;
            font-weight: 600;
        }}
        .description {{
            overflow: hidden;
            text-overflow: ellipsis;
            text-align: center;
            display: inline-block;
            width: 100%;
            height: 100%;
            white-space: nowrap;
        }}
        """
        body = f"""
        <title>badge small</title>
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
        return super(DefaultBadge, self)._render(body)


class CompactBadge(Badge):
    def __init__(self):
        super(CompactBadge, self).__init__()
        self.width = 240
        self.height = 70
        self.big_font_size = 1.1
        self.small_font_size = 0.85

    def render(self) -> str:
        tier_icon = get_tier_icon(self.user.tier)
        tier_text = get_tier_text(self.user.tier)

        """
            <!-- small 240, 70  1.1, 0.85-->
            <!-- medium 360, 105 1.65, 1.275-->
            <!-- large 540, 158 2.475 1.915--> 
        """

        if self.size == BADGE_SMALL_SIZE:
            self.width = 240
            self.height = 70
            self.big_font_size = 1.1
            self.small_font_size = 0.85
        elif self.size == BADGE_MEDIUM_SIZE:
            self.width = 360
            self.height = 105
            self.big_font_size = 1.65
            self.small_font_size = 1.275
        elif self.size == BADGE_LARGE_SIZE:
            self.width = 540
            self.height = 158
            self.big_font_size = 2.475
            self.small_font_size = 1.915

        self._styles = f"""
        #tier_text {{ 
            font-size: {self.big_font_size}em;
            font-weight: 600;
            letter-spacing: 0.15em;
        }}
        #username {{
            font-size: {self.small_font_size}em;
            font-weight: 600;
        }}
        .description {{ 
            overflow: hidden;
            text-overflow: ellipsis;
            text-align: center;
            display: inline-block;
            width: 70%;
            height: 100%;
            white-space: nowrap;
        }}
        """
        body = f"""
        <title>badge compact</title>
        <svg width ="20%" height="80%" x="5%" y="10%">
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
        return super(CompactBadge, self)._render(body)


def make_badge(theme: str, is_compact: bool, user: User = None, options: Dict[str, str] = None) -> Badge:
    if options is None:
        options = {}

    if is_compact:
        badge = CompactBadge()
    else:
        badge = DefaultBadge()

    colorset = make_colorset(theme, options)
    badge.colorset = colorset
    badge.size = options["component_size"]
    badge.user = user

    return badge
