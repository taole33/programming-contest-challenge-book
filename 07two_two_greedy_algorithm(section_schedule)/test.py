import unittest
from two_two_greedy_algorithm_section_schedule import main_method


class TestOneSix(unittest.TestCase):

    def test1(self):
        n = 5
        start_time = [1,2,4,6,8]
        end_time = [3,5,7,9,10]
        expected = 3
        actual = main_method(n,start_time,end_time)
        self.assertEqual(expected,actual)

    def test2(self):
        n = 5
        start_time = [11,2,4,6,8]
        end_time = [13,25,7,9,10]
        expected = 3
        actual = main_method(n,start_time,end_time)
        self.assertEqual(expected,actual)    



if __name__ == "__main__":
    unittest.main(exit=False)
