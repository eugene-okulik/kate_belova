import argparse
from pathlib import Path


def search_in_file(
    file_path: Path,
    text_: str,
    number_of_words_to_show_: int,
    max_results_: int | None,
):
    results = []
    with file_path.open(encoding='utf-8', errors='ignore') as f:
        for line_num, line in enumerate(f, start=1):
            if text_ in line:
                words = line.strip().split()
                for i, word in enumerate(words):
                    if text_ in word:
                        start = max(0, i - number_of_words_to_show_)
                        end = min(len(words), i + number_of_words_to_show_ + 1)
                        fragment_ = ' '.join(words[start:end])
                        results.append((file_path.name, line_num, fragment_))
                        if max_results_ and len(results) >= max_results_:
                            return results
    return results


parser = argparse.ArgumentParser(description='Анализатор логов')
parser.add_argument('folder', nargs='?', help='Папка с логами')
parser.add_argument('--text', help='Текст для поиска')
parser.add_argument(
    '--number_of_words_to_show',
    type=int,
    default=5,
    help='Сколько слов показывать вокруг найденного текста (по умолчанию 5)',
)
parser.add_argument(
    '--max_results',
    type=int,
    help='Максимальное количество совпадений (если не указано — выводим все)',
)
args = parser.parse_args()

# Если не переданы аргументы — интерактивный режим
if not args.folder or not args.text:
    folder = input('Введите полный путь к папке с логами: ').strip()
    text = input('Введите текст для поиска: ').strip()
    number_of_words_to_show = input(
        'Сколько слов показывать вокруг найденного текста (по умолчанию 5): '
    ).strip()
    number_of_words_to_show = (
        int(number_of_words_to_show) if number_of_words_to_show else 5
    )

    all_results = input('Показывать все совпадения? (Y/N): ').strip().lower()
    if all_results == 'y':
        max_results = None
    else:
        max_results = int(input('Сколько совпадений показать: ').strip() or 1)
else:
    folder = args.folder
    text = args.text
    number_of_words_to_show = args.number_of_words_to_show
    max_results = args.max_results

folder_path = Path(folder)
if not folder_path.exists() or not folder_path.is_dir():
    print(f'Папка {folder} не найдена')
else:
    print(f'\nПоиск "{text}" в папке {folder}\n')
    for file in folder_path.iterdir():
        if file.is_file():
            matches = search_in_file(
                file, text, number_of_words_to_show, max_results
            )
            for filename, line_number, fragment in matches:
                print(f'Файл: {filename}, строка {line_number}')
                print(f'Фрагмент: {fragment}\n')
