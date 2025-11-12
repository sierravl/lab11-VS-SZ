import unittest
import unittest
import math
from calculator import add, sub, div, log

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 9), 5)
        self.assertAlmostEqual(add(2.5, 0.1), 2.6, 12)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(10, 3), 7)
        self.assertEqual(sub(-2, -8), 6)
        self.assertAlmostEqual(sub(5.5, 2.2), 3.3, 12)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self): # 3 assertions

        self.assertAlmostEqual(log(10, 100), 2.0, 12)

        self.assertAlmostEqual(log(2, 8), 3.0, 12)

        self.assertAlmostEqual(log(3, 27), math.log(27, 3), 12)

    def test_log_invalid_base(self): # 1 assertion

        with self.assertRaises(ValueError):
            log(0, 10)
        with self.assertRaises(ValueError):
            log(-2, 10)

        with self.assertRaises(ValueError):
            log(1, 10)

        with self.assertRaises(ValueError):
            log(10, 0)
        with self.assertRaises(ValueError):
            log(10, -5)

    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()