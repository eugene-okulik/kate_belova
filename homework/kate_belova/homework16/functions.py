from typing import Any


def find_one(
    cursor: Any,
    table: str,
    filters: dict[str, Any],
    fields: list[str] | None = None,
) -> int | tuple[Any, ...] | None:
    """
    Универсальный селект
    :param cursor: MySQL курсор
    :param table: название таблицы
    :param filters: словарь {колонка: значение}
    :param fields: список возвращаемых полей, если None — используется ['id']
    :return: одно значение, кортеж значений или None
    """
    if fields is None:
        fields = ['id']

    fields_sql = ', '.join([f'`{f}`' for f in fields])
    where = ' AND '.join([f'`{col}` = %s' for col in filters])
    query = f'SELECT {fields_sql} FROM `{table}` WHERE {where} LIMIT 1'
    cursor.execute(query, tuple(filters.values()))
    row = cursor.fetchone()
    if not row:
        return None if len(fields) == 1 else (None,) * len(fields)
    return row[0] if len(fields) == 1 else row


def find_student(
    cursor: Any, name: str, second_name: str
) -> tuple[int | None, ...]:
    return find_one(
        cursor,
        'students',
        {'name': name, 'second_name': second_name},
        ['id', 'group_id'],
    )


def find_group(cursor: Any, title: str) -> int | None:
    return find_one(cursor, 'groups', {'title': title})


def find_student_book(cursor: Any, title: str, student_id: int) -> int | None:
    return find_one(
        cursor,
        'books',
        {'title': title, 'taken_by_student_id': student_id},
    )


def find_subject(cursor: Any, title: str) -> int | None:
    return find_one(cursor, 'subjects', {'title': title})


def find_lesson(cursor: Any, title: str, subject_id: int) -> int | None:
    return find_one(
        cursor,
        'lessons',
        {'title': title, 'subject_id': subject_id},
    )


def find_mark(
    cursor: Any, value: str, lesson_id: int, student_id: int
) -> int | None:
    return find_one(
        cursor,
        'marks',
        {'value': value, 'lesson_id': lesson_id, 'student_id': student_id},
    )
