import unittest
from src.fieldgrep import matches


class TestNone(unittest.TestCase):
    def test_no_match(self):
        self.assertEqual(matches(["aaa"], "zzz"), [])


if __name__ == "__main__":
    unittest.main()
