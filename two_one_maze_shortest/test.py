import unittest
from two_one_maze_shortest import main_method


class TestOneSix(unittest.TestCase):

    def test1(self):
        value1 = "10"
        value2 = "10"
        value3 = [['#','S','#','#','#','#','#','#','.','#'],
                  ['.','.','.','.','.','.','#','.','.','#'],
                  ['.','#','.','#','#','.','#','#','.','#'],
                  ['.','#','.','.','.','.','.','.','.','.'],
                  ['#','#','.','#','#','.','#','#','#','#'],
                  ['.','.','.','.','#','.','.','.','.','#'],
                  ['.','#','#','#','#','#','#','#','.','#'],
                  ['.','.','.','.','#','.','.','.','.','.'],
                  ['.','#','#','#','#','.','#','#','#','.'],
                  ['.','.','#','.','.','.','.','.','G','#']]
        expected = 22
        actual = main_method(value1,value2,value3)
        self.assertEqual(expected,actual)

    def test2_mytest(self):
        value1 = "4"
        value2 = "4"
        value3 = [['#','#','#','#'],
                  ['.','.','.','.'],
                  ['.','#','.','#'],
                  ['S','#','.','G']]
        expected = 7
        actual = main_method(value1,value2,value3)
        self.assertEqual(expected,actual)


if __name__ == "__main__":
    unittest.main(exit=False)