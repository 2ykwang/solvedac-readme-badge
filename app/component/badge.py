class Badge:

    def __init__(self):
        self.width = 140
        self.height = 140
        self.styles = ""
        self.common_color = "#333"
        self.sub_color = "#0099EF"
        self.back_color = "transparent"

    def render(self, body: str) -> str:
        # <rect x="0" y="0" width="100%" height="100%" style=" stroke:pink; stroke-width:1; fill-opacity:0; stroke-opacity:1;" />
        return f"""
<svg
    style="background-color: {self.back_color}"
    width="{self.width}"
    height="{self.height}"
    xmlns="http://www.w3.org/2000/svg">
    <style>
        .common_color{{ fill: {self.common_color}; }}
        .sub_color{{ fill: {self.sub_color}; }}
        text{{ font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji";}}
        {self.styles}
    </style>
     
    <g>
        {body}
    </g>
</svg>
"""


def error_render(message: str) -> str:
    badge = Badge()
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
    return badge.render(error_text)
