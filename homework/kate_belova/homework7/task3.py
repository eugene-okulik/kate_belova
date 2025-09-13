def extract_number(lines: list) -> int | None:
    for line in lines:
        num = int(line.split(':')[1].strip())
        return num
    return None


number = extract_number(input('Введите строки: ').split()) + 10
print(number)
