def find_student(
    cursor, name: str, second_name: str
) -> tuple[int | None, int | None]:
    query = """SELECT id, group_id FROM students 
           WHERE name = %s AND second_name = %s 
           LIMIT 1"""
    values = (name, second_name)
    cursor.execute(query, values)
    row = cursor.fetchone()
    return (row[0], row[1]) if row else (None, None)


def find_group(cursor, title: str) -> int | None:
    query = """SELECT id FROM `groups` 
               WHERE title = %s
               LIMIT 1
            """
    values = (title,)
    cursor.execute(query, values)
    row = cursor.fetchone()
    return row[0] if row else None


def find_student_book(cursor, title: str, student_id: int) -> int | None:
    query = """SELECT id FROM books 
               WHERE title = %s AND taken_by_student_id = %s
               LIMIT 1"""
    values = (title, student_id)
    cursor.execute(query, values)
    row = cursor.fetchone()
    return row[0] if row else None


def find_subject(cursor, title: str) -> int | None:
    query = """SELECT id FROM subjects 
               WHERE title = %s
               LIMIT 1"""
    values = (title,)
    cursor.execute(query, values)
    row = cursor.fetchone()
    return row[0] if row else None


def find_lesson(cursor, title: str, subject_id: int) -> int | None:
    query = """SELECT id FROM lessons
               WHERE title = %s AND subject_id = %s
               LIMIT 1"""
    values = (title, subject_id)
    cursor.execute(query, values)
    row = cursor.fetchone()
    return row[0] if row else None


def find_mark(
    cursor, value: str, lesson_id: int, student_id: int
) -> int | None:
    query = """SELECT id FROM marks 
               WHERE value = %s
               AND lesson_id = %s 
               AND student_id = %s 
               LIMIT 1"""
    values = (value, lesson_id, student_id)
    cursor.execute(query, values)
    row = cursor.fetchone()
    return row[0] if row else None
