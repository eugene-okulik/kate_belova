a, b = map(int, input('Введите 2 числа через пробел: ').split())

sum_ = a + b
diff_ = a - b
product = a * b

print(
    f'Сумма чисел {a} и {b}: {sum_}\n'
    f'Разность чисел {a} и {b}: {diff_}\n'
    f'Произведение чисел {a} и {b}: {product}'
)
