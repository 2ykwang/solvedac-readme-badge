import unittest


class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_right(self):
        value = 5+5
        EXPECTED = 10
        self.assertEqual(EXPECTED, value)


if __name__ == '__main__':
    unittest.main()
