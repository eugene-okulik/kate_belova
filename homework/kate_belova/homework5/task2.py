lines = [
    'результат операции: 42',
    'результат операции: 514',
    'результат работы программы: 9',
]

for line in lines:
    print(int(line[line.index(':') + 1 :].strip()) + 10)
