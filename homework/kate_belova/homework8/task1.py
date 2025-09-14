import random

salary = int(input('Введите ваши зарплатные ожидания (целое число): '))

bonus = random.choice([True, False])
final_salary = salary + random.randint(5000, 20000) if bonus else salary

print(f"{salary}, {bonus} - '${final_salary}'")
