import csv
import mysql.connector

from homework.kate_belova.homework15.config import DB_CONFIG
# fmt: off
from homework.kate_belova.homework16.functions import (
    find_student, find_group, find_student_book,
    find_subject, find_lesson, find_mark,
)
# fmt: on
from homework.kate_belova.homework16.paths_and_variables import csv_path

results = {
    'full': [],  # полностью совпавшие строки
    'partial': [],  # частично совпавшие
    'none': [],  # вообще не совпавшие
}

rows_checked = 0

with mysql.connector.connect(**DB_CONFIG) as conn:
    with conn.cursor() as cursor:
        with open(csv_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row_num, row in enumerate(reader, start=1):
                rows_checked += 1
                name = row.get('name', '').strip()
                second_name = row.get('second_name', '').strip()
                group_title = row.get('group_title', '').strip()
                book_title = row.get('book_title', '').strip()
                subject_title = row.get('subject_title', '').strip()
                lesson_title = row.get('lesson_title', '').strip()
                mark_value = row.get('mark_value', '').strip()

                missing = []
                found_any = False

                # 1) студент
                student_id, student_group_id = find_student(
                    cursor, name, second_name
                )
                if student_id:
                    found_any = True
                    # 2) группа
                    group_id = find_group(cursor, group_title)
                    if not group_id:
                        missing.append(f'group (title={group_title})')
                    else:
                        if student_group_id != group_id:
                            missing.append(
                                f'student not in group '
                                f'(student.group_id={student_group_id} '
                                f'!= group.id={group_id})'
                            )

                    # 3) книга
                    book_id = find_student_book(cursor, book_title, student_id)
                    if not book_id:
                        missing.append(
                            f'book (title={book_title} '
                            f'taken_by_student_id={student_id})'
                        )

                else:
                    missing.append(
                        f'student (name={name} second_name={second_name})'
                    )

                # 4) предмет
                subject_id = find_subject(cursor, subject_title)
                if subject_id:
                    found_any = True
                    # 5) урок
                    lesson_id = find_lesson(cursor, lesson_title, subject_id)
                    if lesson_id:
                        # 6) оценка
                        if student_id:
                            mark_id = find_mark(
                                cursor, mark_value, lesson_id, student_id
                            )
                            if not mark_id:
                                missing.append(
                                    f'mark (value={mark_value} '
                                    f'lesson_id={lesson_id} '
                                    f'student_id={student_id})'
                                )
                        else:
                            missing.append(
                                'mark (cannot check without student)'
                            )
                    else:
                        missing.append(
                            f'lesson (title={lesson_title} '
                            f'subject_id={subject_id})'
                        )
                else:
                    missing.append(f'subject (title={subject_title})')

                if not missing:
                    results['full'].append((row_num, row))
                elif found_any:
                    results['partial'].append((row_num, row, missing))
                else:
                    results['none'].append((row_num, row))

print('-' * 60)
print(f'CSV: {csv_path}')
print(f'Проверено строк: {rows_checked}')
print(f'Полностью совпало: {len(results["full"])}')
print(f'Частично совпало: {len(results["partial"])}')
print(f'Не совпало совсем: {len(results["none"])}')
print('-' * 60)

if results['full']:
    print('\n✅ Полное совпадение:')
    for row_num, row in results['full']:
        print(f'  Row #{row_num}: {row}')

if results['partial']:
    print('\n⚠️ Частичное совпадение:')
    for row_num, row, missing in results['partial']:
        print(f'  Row #{row_num}: {row}')
        print('    Недостающие элементы:')
        for m in missing:
            print(f'     - {m}')

if results['none']:
    print('\n❌ Нет совпадений:')
    for row_num, row in results['none']:
        print(f'  Row #{row_num}: {row}')
