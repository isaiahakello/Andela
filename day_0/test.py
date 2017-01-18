
import unittest


class Calculator(object):
    def add(self, x, y):
        return x + y

    def Subtract(self, x, y):
        return x - y

    def Multiply(self, x, y):
        return x * y

    def Divide(self, x, y):
        return x / y

class tddexample(unittest.TestCase):
    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.add(2, 2)
        self.assertEqual(4, result)

    def test_calculator_Subtract_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.Subtract(5, 2)
        self.assertEqual(3, result)

    def test_calculator_Multiply_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.Multiply(5, 2)
        self.assertEqual(10, result)

    def test_calculator_Divide_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.Divide(8, 2)
        self.assertEqual(4, result)


if __name__ == '__main__':
unittest.main()
