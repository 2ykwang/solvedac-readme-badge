import os
import unittest

from app.solvedac.solvedacfetcher import SolvedacFetcher


class TestFetchingData(unittest.TestCase):
    def setUp(self) -> None:
        host = os.getenv("API_HOST", "solved.ac")
        self.fetcher = SolvedacFetcher(host)

    def test_get_user(self):
        username = "2ykwang"
        userdata = self.fetcher.get_user_info(username)

        ACTUAL = userdata["handle"]
        EXPECTED = "2ykwang"

        self.assertEqual(ACTUAL, EXPECTED)

    def test_get_problems_stats(self):
        username = "2ykwang"
        userdata = self.fetcher.get_user_problem_stat(username)

        take_first = userdata[0]

        ACTUAL = [x for x in take_first.keys()]
        EXPECTED = ["level", "total", "solved", "partial", "tried", "exp"]

        self.assertEqual(ACTUAL, EXPECTED)


if __name__ == "__main__":
    unittest.main()
