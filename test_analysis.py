import unittest
from EC601_Project_Main import tweets


class TestInput(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(tweets, [])

if __name__ == "__main__":
    unittest.main()