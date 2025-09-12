lines = [
    'результат операции: 42',
    'результат операции: 514',
    'результат работы программы: 9',
]

for line in lines:
    colon_pos = line.index(':')
    start = colon_pos + 1
    num_str = line[start:].strip()
    num = int(num_str) + 10
    print(num)
