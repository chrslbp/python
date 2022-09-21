from unittest import TestCase, main
from my_package.calculator import *


class CalculatorTest(TestCase):
    def test_plus(self):
        # Утверждается равенство результата функции с данными параметрами и числа 4.
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('6-1'), 5)

    def test_mult(self):
        self.assertEqual(calculator('6*1'), 6)

    def test_div(self):
        self.assertEqual(calculator('6/2'), 3)

    def test_no_signs(self):
        # Утверждается, что будет падать данное исключение при данном исключении.
        with self.assertRaises(ValueError) as e:
            calculator('abrakadabra')
        self.assertEqual('Выражение должно содержать хотя бы один знак +-*/', e.exception.args[0])

    def test_two_signs(self):
        # Утверждается, что будет падать данное исключение при данном исключении.
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак!', e.exception.args[0])

    def test_many_signs(self):
        # Утверждается, что будет падать данное исключение при данном исключении.
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак!', e.exception.args[0])

    def test_no_ints(self):
        # Утверждается, что будет падать данное исключение при данном исключении.
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2+2.3')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак!', e.exception.args[0])

    def test_strs(self):
        # Утверждается, что будет падать данное исключение при данном исключении.
        with self.assertRaises(ValueError) as e:
            calculator('a+b')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак!', e.exception.args[0])


if __name__ == '__main__':
    main()
