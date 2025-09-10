leg1, leg2 = map(int, input('Введите длины 2х катетов чере пробел: ').split())

hypotenuse = (leg1**2 + leg2**2) ** 0.5
area = leg1 * leg2 / 2

print(
    f'Гипотенуза прямоугольного треугольника с катетами {leg1} и {leg2}: '
    f'{hypotenuse}'
)
print(
    f'Площадь прямоугольного треугольника с катетами {leg1} и {leg2}: '
    f'{area}'
)
