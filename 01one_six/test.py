import unittest
from one_six import triangle

class TestOneSix(unittest.TestCase):

    def test_one_six1(self):
        value1 = "5"
        value2 = "2 3 4 5 10"
        expected = 12
        actual = triangle(value1,value2)
        self.assertEqual(expected,actual)

    def test_one_six2(self):
        value1 = "4"
        value2 = "4 5 10 20"
        expected = 0
        actual = triangle(value1,value2)
        self.assertEqual(expected,actual)

if __name__ == "__main__":
    unittest.main(exit=False)
