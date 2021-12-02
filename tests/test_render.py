import pytest
from app.component.badge import Badge, CompactBadge, DefaultBadge
from app.solvedac.user import User


def test_func():
    a = 4
    assert a == 5


class TestBadge:
    @pytest.fixture
    def setUp(self) -> None:

        test_user = User(
            username="2ykwang",
            bio="biography",
            tier=8,
            user_class=1,
            user_class_decoration="",
            rating=400,
            exp=0,
            rank=19250,
        )

        self.test_user = test_user

    def test_render_error(self):

        compact_badge = CompactBadge()

        ACTUAL = compact_badge.render()
        EXPECTED = Badge.USER_NOT_FOUND

        assert EXPECTED in ACTUAL

        default_badge = DefaultBadge()

        ACTUAL = default_badge.render()
        EXPECTED = Badge.USER_NOT_FOUND

        assert EXPECTED in ACTUAL

    def test_render(self):

        compact_badge = CompactBadge()
        compact_badge.user = self.user

        ACTUAL = compact_badge.render()
        EXPECTED = self.user.username

        assert EXPECTED in ACTUAL

        default_badge = CompactBadge()
        default_badge.user = self.user

        ACTUAL = default_badge.render()
        EXPECTED = self.user.username

        assert EXPECTED in ACTUAL
