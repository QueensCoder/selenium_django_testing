import unittest
from calc import add


class TestMath(unittest.TestCase):

    def test_addition(self):
        result = add(1, 2)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main(warnings='ignore')
