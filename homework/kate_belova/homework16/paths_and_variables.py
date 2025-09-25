import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSW = os.getenv('DB_PASSW')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

if not all([DB_USER, DB_PASSW, DB_HOST, DB_PORT, DB_NAME]):
    raise SystemExit(
        'Не найдены все переменные окружения DB_USER, DB_PASSW, '
        'DB_HOST, DB_PORT, DB_NAME. Проверьте файл .env.'
    )

DB_CONFIG = {
    'user': DB_USER,
    'password': DB_PASSW,
    'host': DB_HOST,
    'port': DB_PORT,
    'database': DB_NAME,
}

current_file = Path(__file__).resolve()
homework_path = current_file.parents[2]
csv_path = (
    homework_path / 'eugene_okulik' / 'Lesson_16' / 'hw_data' / 'data.csv'
)

if not csv_path.exists():
    raise SystemExit(f'CSV файл не найден по пути: {csv_path}')
