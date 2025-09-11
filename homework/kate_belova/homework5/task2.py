lines = [
    'результат операции: 42',
    'результат операции: 514',
    'результат работы программы: 9',
]

for line in lines:
    num = int(line.split(':')[1].strip()) + 10
    print(num)
