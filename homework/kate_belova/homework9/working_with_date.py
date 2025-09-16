from datetime import datetime

date_str = 'Jan 15, 2023 - 12:05:33'
date = datetime.strptime(date_str, '%b %d, %Y - %H:%M:%S')

month = date.strftime('%B')
print(f'Month: {month}')

formatted_date = date.strftime('%d.%m.%Y, %H:%M')
print(f'Date in East European format: {formatted_date}')
