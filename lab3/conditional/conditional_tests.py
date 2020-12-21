import unittest
from conditional import *

class TestCases(unittest.TestCase):
    def test_function_names(self):
        max_101(0, 0)
        self.assertEquals(max_101(3,4),4)
        self.assertEquals(max_101(3.5,4.5),4.5)
        self.assertEquals(max_101(4,4),"Equal")
        max_of_three(0, 0, 0)
        self.assertEquals(max_of_three(5.5,6.3,7.9),7.9)
        self.assertEquals(max_of_three(6.8,7.0,5.5),7.0)
        self.assertEquals(max_of_three(7.9,6.6,5.4),7.9)
        self.assertEquals(max_of_three(15.0,15.0,15.0),"Equal")
        rental_late_fee(0)
        self.assertEquals(rental_late_fee(0),0)
        self.assertEquals(rental_late_fee(8),5)
        self.assertEquals(rental_late_fee(13),7)
        self.assertEquals(rental_late_fee(15),7)
        self.assertEquals(rental_late_fee(22),19)
        self.assertEquals(rental_late_fee(24),19)
        self.assertEquals(rental_late_fee(48),100)

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

