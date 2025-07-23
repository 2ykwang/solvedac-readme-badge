import pytest
from app.component.badge import Badge, CompactBadge, DefaultBadge
from app.solvedac.user import User


class TestBadge:
    @pytest.fixture(autouse=True)
    def _setup(self):
        self.user = User(
            username="tester",
            bio="biography",
            tier=8,
            user_class=1,
            user_class_decoration="",
            rating=400,
            exp=0,
            rank=19250,
        )

    def test_render_error(self):

        compact_badge = CompactBadge()
        assert Badge.USER_NOT_FOUND in compact_badge.render()

        default_badge = DefaultBadge()
        assert Badge.USER_NOT_FOUND in default_badge.render()

    def test_render(self):

        compact_badge = CompactBadge()
        compact_badge.user = self.user
        assert self.user.username in compact_badge.render()

        default_badge = CompactBadge()
        default_badge.user = self.user
        assert self.user.username in default_badge.render()
