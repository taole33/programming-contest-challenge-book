import unittest
from two_one_LakeCounting import main_method


class TestOneSix(unittest.TestCase):

    def test1(self):
        value1 = "10"
        value2 = "12"
        value3 = [['W','.','.','.','.','.','.','.','.','W','W','.'],
                  ['.','W','W','W','.','.','.','.','.','W','W','W'],
                  ['.','.','.','.','W','W','.','.','.','W','W','.'],
                  ['.','.','.','.','.','.','.','.','.','W','W','.'],
                  ['.','.','.','.','.','.','.','.','.','W','.','.'],
                  ['.','.','W','.','.','.','.','.','.','W','.','.'],
                  ['.','W','.','W','.','.','.','.','.','W','W','.'],
                  ['W','.','W','.','W','.','.','.','.','.','W','.'],
                  ['.','W','.','W','.','.','.','.','.','.','W','.'],
                  ['.','.','W','.','.','.','.','.','.','.','W','.']]
        expected = 3
        actual = main_method(value1,value2,value3)
        self.assertEqual(expected,actual)


if __name__ == "__main__":
    unittest.main(exit=False)