from datetime import datetime, timedelta
from pathlib import Path

from homework.kate_belova.homework13.weekdays_translations import weekdays

current_file = Path(__file__).resolve()
homework_path = current_file.parents[2]
file_path = homework_path / 'eugene_okulik' / 'hw_13' / 'data.txt'


with open(file_path, encoding='utf-8') as dates_file:
    lines = dates_file.readlines()

for line in lines:
    number, rest = line.split('.', 1)
    date_str, action = rest.split(' - ', 1)
    date_str = date_str.strip()
    action = action.strip()

    date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')

    if 'неделю позже' in action:
        result = date + timedelta(weeks=1)
        print(f'{number}. {result}')

    elif 'день недели' in action:
        weekday_en = date.strftime('%A')
        translations = weekdays[weekday_en]
        print(
            f'{number}. День недели:\n'
            f'   EN: {weekday_en}\n'
            f'   RU: {translations["ru"]}\n'
            f'   UK: {translations["uk"]}\n'
            f'   DE: {translations["de"]}\n'
            f'   BE: {translations["be"]}\n'
            f'   ES: {translations["es"]}'
        )

    elif 'сколько дней назад' in action:
        delta = datetime.now() - date
        print(f'{number}. {delta.days} дней назад')

    else:
        print(f'{number}. Неизвестное действие: {action}')
