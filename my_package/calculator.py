"""Here is implementation of the calculator."""


def calculator(expression):
    """
     Функция калькулятор, которая принимает строку, содержащую два целых числа и один знак арифметической операции
     и возвращает результат этой операции.
     Если числа не целые, или отсутствует оператор, то бросать исключение ValueError.
    """
    allowed = '+-*/'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Выражение должно содержать хотя бы один знак {allowed}')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)

                return {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b,
                }[sign](left, right)  # поиск в словаре по значению sign,
                # далее передаем в выбранную функцию 2 значения (left, right)

            except (ValueError, TypeError):
                raise ValueError('Выражение должно содержать 2 целых числа и 1 знак!')


if __name__ == '__main__':
    print(calculator('6/7'))
