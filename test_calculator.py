#GITHUB LINK: https://github.com/birkenn/Lab10-CM-NB
import unittest
import calculator

class TestCalculator(unittest.TestCase):

    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(7, 8), 15)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(calculator.subtract(1, 2), -1)
        self.assertEqual(calculator.subtract(2, 3), -1)
        self.assertEqual(calculator.subtract(7, 8), -1)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(10, 0)

    def test_logarithm(self):
        self.assertEqual(calculator.logarithm(1), 0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-1)

    def test_multiply(self):
        self.assertEqual(calculator.mul(2, 3), 6)
        self.assertEqual(calculator.mul(2, 4), 8)
        self.assertEqual(calculator.mul(2, 5), 10)

    def test_divide(self):
        self.assertAlmostEqual(calculator.div(1, 5), 0.2)
        self.assertAlmostEqual(calculator.div(2, 10), 0.2)
        self.assertAlmostEqual(calculator.div(3, 15), 0.2)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 10)

    def test_hypotenuse(self):
        self.assertEqual(calculator.hypotenuse(3, 4), 5)
        self.assertEqual(calculator.hypotenuse(6, 8), 10)
        self.assertEqual(calculator.hypotenuse(5, 12), 13)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            calculator.square_root(-33)
        self.assertEqual(calculator.square_root(9), 3)
        self.assertEqual(calculator.square_root(4), 2)

if __name__ == "__main__":
    unittest.main()