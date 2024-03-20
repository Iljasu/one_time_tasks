from math import sqrt
from typing import Optional, Union


def add_numbers(x1: int, y1: int) -> int:
    return x1 + y1


def calculate_square_root(number: Union[float, int]) -> float:
    return sqrt(number)


def calc(your_number: float) -> Optional[str]:
    if your_number >= 0:
        zed = calculate_square_root(your_number)
    return (
        f'Мы вычислили квадратный корень из введённого вами числа. '
        f'Это будет: {zed}'
    )


x1 = 10
y1 = 5
print('Сумма чисел: ', add_numbers(x1, y1))
print(calc(25.5))
