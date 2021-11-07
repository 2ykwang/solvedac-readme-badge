from .user import User
from .tier import (
    get_tier_text,
    get_tier_icon,
)
from ..component import *


def make_badge(user: User, is_compact: bool = False, _test=False) -> str:
    comp = Badge()

    tier_icon = get_tier_icon(user.tier)
    tier_text = get_tier_text(user.tier)
    username = user.username
    comp.use_back_color = False
    comp.back_color = "transparent"
    res = ""
    if not is_compact:
        comp.styles = """
    #username {
        font-size: 0.960em;
        font-weight: 600;
    }
    .description { 
        overflow: hidden;
        text-overflow: ellipsis;
        text-align: center;
        display: inline-block;
        white-space: nowrap;
        width: 140px;
        height: 30px; 
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
    <svg y="115" >
      <title>닉네임</title>
      <foreignObject width="140" height="30">
        <xhtml:span xmlns:xhtml="http://www.w3.org/1999/xhtml" id = "username" class="text description sub_color">
          {username}
        </xhtml:span>
      </foreignObject>
    </svg>
        """
        res = comp.render(body)
    else:
        comp.width = 170
        comp.height = 45
        comp.use_back_color = True
        comp.back_color = "#fff"
        if _test:
            comp.common_color = "#E3BE79"
            comp.sub_color = "#D96D74"
            comp.use_back_color = True
            comp.back_color = "#282C34"
        comp.styles = """
        #tier_text {
            font-size: 0.72em;
            font-weight: 600;
            letter-spacing: 0.15em;
        }
        #username {
            font-size: 0.735em;
            font-weight: 600;
        }
        .description { 
            overflow: hidden;
            text-overflow: ellipsis;
            text-align: center;
            display: inline-block;
            width: 120px;
            height: 30px;
            white-space: nowrap;
        }
        """

        body = f"""
        <title>badge compact</title>
        <svg width ="20%" height="80%" x="5%" y="10%">
        {tier_icon}
        </svg>
        <svg x="50" y="7">
          <title>랭크</title>
          <foreignObject width="120" height="30">
            <xhtml:span xmlns:xhtml="http://www.w3.org/1999/xhtml" id="tier_text" class="text description common_color">
              {tier_text}
            </xhtml:span>
          </foreignObject>
        </svg>
    
        <svg x="50" y="22" >
          <title>닉네임</title>
          <foreignObject width="120" height="30">
            <xhtml:span xmlns:xhtml="http://www.w3.org/1999/xhtml" id = "username" class="text description sub_color">
              {username}
            </xhtml:span>
          </foreignObject>
        </svg>
            """
        res = comp.render(body)
    return res
