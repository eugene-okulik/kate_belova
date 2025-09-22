def extract_numbers(str_lines: list) -> list[int]:
    numbers_lst = []
    for line in str_lines:
        num = int(line.split(':')[1].strip())
        numbers_lst.append(num)
    return numbers_lst


lines = [
    'результат операции: 42',
    'результат операции: 54',
    'результат работы программы: 209',
    'результат: 2',
]
numbers = [num + 10 for num in extract_numbers(lines)]
print(*numbers)
