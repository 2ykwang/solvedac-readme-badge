import unittest

from app.component.badge import USER_NOT_FOUND, CompactBadge, DefaultBadge
from app.solvedac.user import User


class TestBadge(unittest.TestCase):
    def setUp(self) -> None:

        user = User()
        user.username = "2ykwang"
        user.bio = "biography"
        user.tier = 8
        user.user_class = 1
        user.user_class_decoration = ""
        user.rating = 400
        user.exp = 0
        user.rank = 19250

        self.user = user

    def test_render_error(self):

        compact_badge = CompactBadge()

        ACTUAL = compact_badge.render()
        EXPECTED = USER_NOT_FOUND

        self.assertIn(EXPECTED, ACTUAL)

        default_badge = DefaultBadge()

        ACTUAL = default_badge.render()
        EXPECTED = USER_NOT_FOUND

        self.assertIn(EXPECTED, ACTUAL)

    def test_render(self):

        compact_badge = CompactBadge()
        compact_badge.user = self.user

        ACTUAL = compact_badge.render()
        EXPECTED = self.user.username

        self.assertIn(EXPECTED, ACTUAL)

        default_badge = CompactBadge()
        default_badge.user = self.user

        ACTUAL = default_badge.render()
        EXPECTED = self.user.username

        self.assertIn(EXPECTED, ACTUAL)


if __name__ == "__main__":
    unittest.main()
