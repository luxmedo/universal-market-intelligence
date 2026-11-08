import unittest
from scripts.unit_economics import calculate

class TestEconomics(unittest.TestCase):
    def test_example(self):
        self.assertEqual(calculate(50, 10, 5, 2, 15)["profit_per_order"], 20.5)
    def test_invalid(self):
        with self.assertRaises(ValueError):
            calculate(50, 10, 5, 2, 15, 2)

if __name__ == "__main__":
    unittest.main()
