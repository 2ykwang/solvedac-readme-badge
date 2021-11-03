from .user import User
from .tier import (
    get_tier_text,
    get_tier_icon,
)
from ..component import *


def make_badge(user: User, is_compact: bool = False) -> str:
    comp = Badge()

    tier_icon = get_tier_icon(user.tier)
    tier_text = get_tier_text(user.tier)
    username = user.username

    res = ""
    if not is_compact:
        comp.styles = """
    #username {
        font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji";
        font-size: 75%;
        font-weight: 600;
        text-align:center;
    }
    """

        body = f"""
    <title>badge small</title>
    <svg 
        x="15%" 
        y="9%" 
        height="70%" 
        width="70%" 
        id="tier_icon">{tier_icon}</svg>
    <text
        x="50%"
        y="90%"
        dominant-baseline="middle"
        text-anchor="middle"
        font-size="14"
        class="sub_color"
        id="username">{username}</text>
        """
        res = comp.render(body)
    else:
        comp.width = 150
        comp.height = 45
        comp.back_color = "#FFF"

        comp.styles = """
        #username {
            font-size: 0.815em;
            font-weight: 600;
        }
        #tier_text {
            font-size: 0.72em;
            font-weight: 600;
            letter-spacing: 0.15em;
        }
        """

        body = f"""
        <title>badge compact</title>
        <svg width ="20%" height="80%" x="5%" y="10%">
        {tier_icon}
        </svg>
        <text
            x="65%"
            y="40%"
            dominant-baseline="middle"
            text-anchor="middle"
            id="tier_text"
            class="common_color">{tier_text}</text>
        <text
            x="65%"
            y="75%"
            dominant-baseline="middle"
            text-anchor="middle"
            class="sub_color"
            id="username">{username}</text>
            """
        res = comp.render(body)
    return res
