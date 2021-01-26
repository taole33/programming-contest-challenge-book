import unittest
from two_one_DFS import main_method


class TestOneSix(unittest.TestCase):

    def test1(self):
        value1 = "4"
        value2 = "1 2 4 7"
        value3 = "13"
        expected = True
        actual = main_method(value1,value2,value3)
        self.assertEqual(expected,actual)

    def test2(self):
        value1 = "4"
        value2 = "1 2 4 7"
        value3 = "15"
        expected = False
        actual = main_method(value1,value2,value3)
        self.assertEqual(expected,actual)

    def test_mytest(self):
        value1 = "6"
        value2 = "1 5 6 10 89"
        value3 = "100"
        expected = True
        actual = main_method(value1,value2,value3)
        self.assertEqual(expected,actual)



if __name__ == "__main__":
    unittest.main(exit=False)