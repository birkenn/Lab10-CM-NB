import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(calculator.mul(2,3),6)
        self.assertEqual(calculator.mul(2,4),8)
        self.assertEqual(calculator.mul(2, 5), 10)
    def test_divide(self):
        self.assertEqual(calculator.div(1,5),5)
        self.assertEqual(calculator.div(2, 10), 5)
        self.assertEqual(calculator.div(3, 15), 5)
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(0,10)
    def test_hypotenuse(self):
        self.assertEqual(calculator.hypotenuse(3, 4), 5)
        self.assertEqual(calculator.hypotenuse(6, 8), 10)
        self.assertEqual(calculator.hypotenuse(5, 12), 13)
    def test_sqrt(self):
        with self.assertRaises(ValueError):
            calculator.square_root(-33)
        self.assertEqual(calculator.square_root(9), 3)
        self.assertEqual(calculator.square_root(4), 2)
# Do not touch this
if __name__ == "__main__":
    unittest.main()