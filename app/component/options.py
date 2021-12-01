class Options:
    DEFAULT_THEME = "white"
    DEFAULT_SIZE = "small"

    def __init__(
        self,
        theme: str = DEFAULT_THEME,
        size: str = DEFAULT_SIZE,
        back_color: str = "",
        common_color: str = "",
        sub_color: str = "",
        border_color: str = "",
        use_back_color: bool = True,
        use_border: bool = True,
        use_shadow: bool = True,
        is_compact: bool = True,
    ) -> None:
        self.theme = theme
        self.size = size
        self.back_color = back_color
        self.common_color = common_color
        self.sub_color = sub_color
        self.border_color = border_color
        self.use_back_color = use_back_color
        self.use_border = use_border
        self.use_shadow = use_shadow
        self.is_compact = is_compact
