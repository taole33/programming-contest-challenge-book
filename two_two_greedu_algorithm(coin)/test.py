import unittest
from two_two_greedy_algorithm_coin import main_method


class TestOneSix(unittest.TestCase):

    def test1(self):
        coins = [3,2,1,3,0,2]
        A = 620
        expected = 6
        actual = main_method(coins,A)
        self.assertEqual(expected,actual)

    def test2(self):
        coins = [100,2,2,3,5,2]
        A = 1021
        expected = 5
        actual = main_method(coins,A)
        self.assertEqual(expected,actual)


if __name__ == "__main__":
    unittest.main(exit=False)