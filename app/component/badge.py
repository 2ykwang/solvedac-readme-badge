# flake8: noqa
from abc import abstractmethod
from typing import Final, Optional
from dataclasses import dataclass

from app.component.options import Options
from app.component.theme import Theme
from app.component.utils import (
    get_tier_hex_color,
    get_tier_icon,
    get_tier_text,
    make_theme,
)
from app.solvedac import User
from app.factories.size_factory import SizeConfig


@dataclass
class BadgeConfig:
    """Badge 설정을 담는 데이터 클래스"""
    width: int
    height: int
    font_size: float
    big_font_size: Optional[float] = None
    small_font_size: Optional[float] = None


class Badge:
    USER_NOT_FOUND: Final = "사용자를 불러오지 못했습니다."

    def __init__(self):
        """Badge 기본 초기화"""
        self.width = 180
        self.height = 180
        self.styles = ""
        self._styles = ""
        self.user: Optional[User] = None
        self.theme: Optional[Theme] = None
        self.size = Options.DEFAULT_SIZE
        self._config: Optional[BadgeConfig] = None

    def _apply_size_config(self, config: BadgeConfig) -> None:
        """크기 설정을 적용합니다."""
        self._config = config
        self.width = config.width
        self.height = config.height

    @abstractmethod
    def error_render(self, message: str) -> str:
        """에러 메시지를 렌더링합니다."""
        pass

    def _render(self, body: str) -> str:
        """SVG를 렌더링합니다."""
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

    def render(self, body: str = None) -> str:
        """Badge를 렌더링합니다."""
        if self.user is None:
            return self.error_render(self.USER_NOT_FOUND)

        if body is None:
            body = self._generate_body()
        
        return self._render(body)

    @abstractmethod
    def _generate_body(self) -> str:
        """Badge 본문을 생성합니다."""
        pass


class DefaultBadge(Badge):
    def __init__(self):
        super(DefaultBadge, self).__init__()

    def error_render(self, message: str) -> str:
        """에러 메시지를 렌더링합니다."""
        if not self._config:
            return super().error_render(message)

        self._styles = f"""
        #error_message {{ font-size: {self._config.font_size}em; font-weight: 600; }}
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

    def _generate_body(self) -> str:
        """Default Badge 본문을 생성합니다."""
        if not self._config:
            return ""
            
        tier_icon = get_tier_icon(self.user.tier)

        self._styles = f"""
        #username {{ font-size: {self._config.font_size}em; font-weight: 600; }}
        .description {{ overflow: hidden; text-overflow: ellipsis; text-align: center; display: inline-block; width: 100%; height: 100%; white-space: nowrap; }}
        """
        return f"""
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


class CompactBadge(Badge):
    def __init__(self):
        super(CompactBadge, self).__init__()

    def error_render(self, message: str) -> str:
        """에러 메시지를 렌더링합니다."""
        if not self._config:
            return super().error_render(message)

        self._styles = f"""
        #error_title {{  font-size: {self._config.big_font_size}em; font-weight: 600; letter-spacing: 0.15em; }}
        #error_message {{ font-size: {self._config.small_font_size}em; font-weight: 600; }}
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

    def _generate_body(self) -> str:
        """Compact Badge 본문을 생성합니다."""
        if not self._config:
            return ""
            
        tier_icon = get_tier_icon(self.user.tier)
        tier_text = get_tier_text(self.user.tier)

        self._styles = f"""
        #tier_text {{  font-size: {self._config.big_font_size}em; font-weight: 600; letter-spacing: 0.15em;   }}
        #username {{ font-size: {self._config.small_font_size}em; font-weight: 600; }}
        .description {{ overflow: hidden; text-overflow: ellipsis; text-align: center; display: inline-block; width: 70%; height: 100%; white-space: nowrap; }}
        """
        return f"""
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
