import math


def fibonacci_generator():
    """Бесконечный генератор чисел Фибоначчи"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def num_digits(n: int) -> int:
    """Возвращает количество цифр в числе без преобразования в строку"""
    return math.floor(math.log10(n)) + 1 if n > 0 else 1


target_positions = [5, 200, 1000, 100000]

generator = fibonacci_generator()

results = {}
for idx, num in enumerate(generator, start=1):
    if idx in target_positions:
        results[idx] = num
        if len(results) == len(target_positions):
            break

for position in target_positions:
    num = results[position]
    if position == 100000:
        print(f'{position}-е число Фибоначчи имеет {num_digits(num)} цифр')
    else:
        print(f'{position}-е число Фибоначчи: {num}')
