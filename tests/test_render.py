from app.component.badge import Badge, CompactBadge, DefaultBadge
from app.component.utils import get_tier_icon, get_tier_text
from app.solvedac.user import User
from bs4 import BeautifulSoup


def element_content(element):
    if element:
        return "".join([str(x) for x in element.contents]).strip()


def test_render_no_user_error():
    for target in [CompactBadge, DefaultBadge]:
        badge = target()

        bs = BeautifulSoup(badge.render())
        ACTUAL = bs.find(id="error_message").text.strip()
        EXPECTED = Badge.USER_NOT_FOUND

        assert EXPECTED in ACTUAL


def test_badge_render():
    user = User(
        username="2ykwang",
        bio="biography",
        tier=8,
        user_class=1,
        user_class_decoration="",
        rating=400,
        exp=0,
        rank=19250,
    )

    for target in [CompactBadge, DefaultBadge]:
        badge = target()
        badge.user = user

        tier_icon = get_tier_icon(user.tier)
        tier_text = get_tier_text(user.tier)

        bs = BeautifulSoup(badge.render())

        render_tier_icon = element_content(bs.find("tier_badge"))
        render_tier_text = element_content(bs.find("tier_text"))
        render_username = bs.find(id="username").text.strip()

        if render_tier_icon:
            assert render_tier_icon == tier_icon
        if render_tier_text:
            assert render_tier_text == tier_text

        assert render_username == user.username
