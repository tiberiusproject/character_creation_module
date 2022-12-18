from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления '
' квадратного корня из заданного числа '


def calculate_square_root(number) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Вычисляет квадратный корень."""
    if your_number <= 0:
        return 'Please give a number that is bigger than 0'
    root = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: '
          f'{root}')
    return 'Something wrong'


print(message)
calc(25.5)
