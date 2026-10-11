import unittest
from src.fieldgrep import matches


class TestMatch(unittest.TestCase):
    def test_matches(self):
        self.assertEqual(matches(["abc", "xbcx"], "bc"), ["abc", "xbcx"])


if __name__ == "__main__":
    unittest.main()
