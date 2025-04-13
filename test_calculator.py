import unittest
import calculator


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(7, 8), 15)

    def test_subtract(self): # 3 assertions
        self.assertEqual(calculator.subtract(1, 2), 2)
        self.assertEqual(calculator.subtract(2, 3), 1)
        self.assertEqual(calculator.subtract(7, 8), 0)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
            with self.assertRaises(ZeroDivisionError):
                calculator.div(0, 10)
    def test_logarithm(self):
        self.assertEqual(calculator.logarithm(1), 2)



    def test_log_invalid_base(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.logarithm(-1)
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
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