from typing import Optional
from pydantic import BaseModel, Field, validator
from enum import Enum


class SizeEnum(str, Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


class ThemeEnum(str, Enum):
    WHITE = "white"
    SWIFT = "swift"
    DARK = "dark"
    ONEDARK = "onedark"
    GITHUB_DARK = "github-dark"


class BadgeQueryParams(BaseModel):
    user: Optional[str] = Field(None, description="사용자명")
    theme: ThemeEnum = Field(ThemeEnum.WHITE, description="테마")
    size: SizeEnum = Field(SizeEnum.SMALL, description="크기")
    common_color: Optional[str] = Field(None, description="주요 색상 (hex)")
    sub_color: Optional[str] = Field(None, description="보조 색상 (hex)")
    back_color: Optional[str] = Field(None, description="배경 색상 (hex)")
    border_color: Optional[str] = Field(None, description="테두리 색상 (hex)")
    use_shadow: bool = Field(True, description="그림자 사용 여부")
    compact: bool = Field(True, description="컴팩트 모드 여부")
    use_back_color: bool = Field(True, description="배경색 사용 여부")
    use_border: bool = Field(True, description="테두리 사용 여부")

    @validator('common_color', 'sub_color', 'back_color', 'border_color')
    def validate_hex_color(cls, v):
        if v is not None:
            import re
            if not re.match(r'^[a-fA-F0-9]{3}(?:[a-fA-F0-9]{3})?$', v):
                raise ValueError('색상은 3자리 또는 6자리 hex 코드여야 합니다')
        return v


class ErrorResponse(BaseModel):
    error: str
    message: str
    detail: Optional[str] = None


class BadgeInfoResponse(BaseModel):
    """Badge 정보 응답 모델"""
    available_sizes: list[str]
    available_themes: list[str]
    description: str = "Solved.ac Badge Generator API"