def calculate(num1, num2):
    result = (num1 - num2) / 1 + num1 * num2
    print(result)


x, y = map(int, input('Введите два числа через пробел: ').split())
calculate(x, y)
