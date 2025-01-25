import unittest
from src.math_operations import add, subtract, multiply, divide

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-2, 7), 5)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-3, -7), 4)

    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(-4, 6), -24)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-9, 3), -3)
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == "__main__":
    unittest.main()
