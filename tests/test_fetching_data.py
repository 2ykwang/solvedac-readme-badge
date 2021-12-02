from app.solvedac import SolvedacFetcher


def test_get_user():
    fetcher = SolvedacFetcher("solved.ac")

    username = "2ykwang"
    userdata = fetcher.get_user_info(username)

    ACTUAL = userdata["handle"]
    EXPECTED = "2ykwang"

    assert ACTUAL == EXPECTED


def test_get_problems_stats():
    fetcher = SolvedacFetcher("solved.ac")

    username = "2ykwang"
    userdata = fetcher.get_user_problem_stat(username)

    take_first = userdata[0]

    ACTUAL = [x for x in take_first.keys()]
    EXPECTED = ["level", "total", "solved", "partial", "tried", "exp"]

    assert ACTUAL == EXPECTED
