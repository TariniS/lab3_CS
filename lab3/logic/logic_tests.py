import unittest
from logic import *

class TestCases(unittest.TestCase):
    def test_function_names(self):
        is_even(0)
        self.assertEquals(is_even(2), True)
        self.assertEquals(is_even(-2), True)
        self.assertEquals(is_even(3), False)
        self.assertEquals(is_even(-3), False)
        self.assertEquals(is_even(0), True)
        in_an_interval(0)
        self.assertEquals(in_an_interval(2),True)
        self.assertEquals(in_an_interval(9), False)
        self.assertEquals(in_an_interval(47), False)
        self.assertEquals(in_an_interval(92), False)
        self.assertEquals(in_an_interval(12), False)
        self.assertEquals(in_an_interval(19), True)
        self.assertEquals(in_an_interval(101), True)
        self.assertEquals(in_an_interval(103), True)
        self.assertEquals(in_an_interval(4), True)
        self.assertEquals(in_an_interval(55), True)
        self.assertEquals(in_an_interval(17),True)
        self.assertEquals(in_an_interval(102), True)
        self.assertEquals(in_an_interval(900),False)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

