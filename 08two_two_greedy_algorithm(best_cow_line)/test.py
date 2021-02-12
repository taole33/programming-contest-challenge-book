import unittest
from two_two_greedy_algorithm_bestcowline import main_method


class TestTwoTwo(unittest.TestCase):

    def test1(self):
        N = 6
        S = "ACDBCB"
        expected = "ABCBCD"
        actual = main_method(N,S)
        self.assertEqual(expected,actual)

    def test2(self):
        N = 5
        S = "46153"
        expected = "34516"
        actual = main_method(N,S)
        self.assertEqual(expected,actual)

    def test3(self):
        N = 4
        S = "4649"
        expected = "4649"
        actual = main_method(N,S)
        self.assertEqual(expected,actual)




if __name__ == "__main__":
    unittest.main(exit=False)
