import unittest
from simple_calculator import SimpleCalculator

class SimpleCalculatorTest(unittest.TestCase):
    def setUp(self):
        calculator = SimpleCalculator()
        self.add = calculator.add
        self.subtract = calculator.subtract
        self.multiply = calculator.multiply
        self.divide = calculator.divide
    def test_add(self):
        self.assertEqual(self.add(3, 2), 5)
    def test_subtract(self):
        self.assertEqual(1, self.subtract(5, 4))
    def test_multiply(self):
        self.assertEqual(10, self.multiply(5, 2))
    def test_divide(self):
        self.assertEqual(2, self.divide(10, 5))
    def test_divideWithZero(self):
        self.assertEqual(None, self.divide(10, 0))

if __name__ == "__main__":
    unittest.main()