import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(7, 8), 15)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(1, 2), -1)
        self.assertEqual(calculator.subtract(2, 3), -1)
        self.assertEqual(calculator.subtract(7, 8), -1)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(10, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(100, 10), 2)
        self.assertAlmostEqual(calculator.logarithm(8, 2), 3)
        self.assertAlmostEqual(calculator.logarithm(27, 3), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(10, -1)

    def test_multiply(self):
        self.assertEqual(calculator.mul(2, 3), 6)
        self.assertEqual(calculator.mul(2, 4), 8)
        self.assertEqual(calculator.mul(2, 5), 10)

    def test_divide(self):
        self.assertAlmostEqual(calculator.div(1, 5), 5)
        self.assertAlmostEqual(calculator.div(2, 10), 5)
        self.assertAlmostEqual(calculator.div(5, 20), 4)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(6, 8), 10)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            calculator.square_root(-33)
        self.assertEqual(calculator.square_root(9), 3)
        self.assertEqual(calculator.square_root(4), 2)

if __name__ == "__main__":
    unittest.main()