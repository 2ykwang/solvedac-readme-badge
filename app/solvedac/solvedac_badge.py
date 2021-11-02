from . import User
from ..component import *
from ..solvedac import (
    tier
)


def make_badge(user: User, is_compact: bool = False) -> str:
    badge = Badge.Badge()

    tier_icon = tier.tier_icon[user.tier]
    tier_text = tier.tier_text[user.tier]
    username = user.username

    res = ""
    if not is_compact:
        badge.styles = """
    #username {
        font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji";
        font-size: 75%;
        font-weight: 600;
        text-align:center;
    }
    #tier_icon {
        width:50px;
        height:50px;
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
        res = badge.render(body)
    else:
        badge.width = 150
        badge.height = 45
        badge.back_color = "#FFF"

        badge.styles = """
        #username {
            font-size: 80%;
            font-weight: 600; 
        }
        #tier_text { 
            font-size: 70%;
            font-weight: 600; 
        }
        """

        body = f"""
        <title>badge compact</title>
        <svg 
            x="5%" 
            y="10%" 
            height="80%" 
            width="25%">{tier_icon}</svg>
        <text
            x="67%"
            y="35%"
            dominant-baseline="middle"
            text-anchor="middle"
            id="tier_text"
            class="common_color">{tier_text}</text>
        <text
            x="67%"
            y="70%"
            dominant-baseline="middle"
            text-anchor="middle"
            font-size="12"
            class="sub_color"
            id="username">{username}</text>
            """
        res = badge.render(body)
    return res
