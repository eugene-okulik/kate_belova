num1, num2 = map(int, input('Введите два числа через пробел: ').split())

arithmetic_average = (num1 + num2) / 2
geometric_average = (num1 * num2) ** 0.5

print(
    f'Среднее арифметическое {num1} и {num2}: {arithmetic_average}\n'
    f'Среднее геометрическое {num1} и {num2}: {geometric_average}'
)
