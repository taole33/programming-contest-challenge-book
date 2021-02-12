import unittest
from one_six_Ants import main_method


class TestOneSix(unittest.TestCase):

    def test_one_six_ants(self):
        value1 = "10"
        value2 = "3"
        value3 = "2 6 7"
        expected = (4,8)
        actual = main_method(value1,value2,value3)
        self.assertEqual(expected,actual)

    def test_one_six_ants_mytest(self):
        value1 = "100"
        value2 = "4"
        value3 = "3 6 40 10"
        expected = (40,97)
        actual = main_method(value1,value2,value3)
        self.assertEqual(expected,actual)



if __name__ == "__main__":
    unittest.main(exit=False)
