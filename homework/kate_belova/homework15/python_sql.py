import mysql.connector

from homework.kate_belova.homework15.config import DB_CONFIG

with mysql.connector.connect(**DB_CONFIG) as conn:

    # -------------------------------
    # 1. Создание студента
    with conn.cursor() as cursor:
        query = """
            INSERT INTO students (name, second_name)
            VALUES (%s, %s)
        """
        values = ('Kate', 'Belova')
        cursor.execute(query, values)
        student_id = cursor.lastrowid
        print('Student ID:', student_id)
    conn.commit()

    # -------------------------------
    # 2. Создание группы
    with conn.cursor() as cursor:
        query = """
                INSERT INTO `groups` (title, start_date, end_date)
                VALUES (%s, %s, %s)
                """
        values = ('QA Automation', '2025-09-01', '2025-10-31')
        cursor.execute(query, values)
        group_id = cursor.lastrowid
        print('Group ID:', group_id)
    conn.commit()

    # -------------------------------
    # 3. Привязка студента к группе
    with conn.cursor() as cursor:
        query = """
                UPDATE students
                SET group_id = %s
                WHERE id = %s
                """
        values = (group_id, student_id)
        cursor.execute(query, values)
    conn.commit()

    # -------------------------------
    # 4. Создание книг
    books = [
        'Mastering Selenium',
        'Playwright in Action',
        'Python Requests Essentials',
    ]
    with conn.cursor() as cursor:
        query = """
                INSERT INTO books (title, taken_by_student_id)
                VALUES (%s, %s)
                """
        values = [(title, student_id) for title in books]
        cursor.executemany(query, values)
    conn.commit()

    # -------------------------------
    # 5. Создание предметов
    subjects = [
        'Python Basics',
        'Database Fundamentals',
        'REST API Automated Testing',
        'UI Automation',
    ]
    subject_ids = []
    with conn.cursor() as cursor:
        for title in subjects:
            query = """INSERT INTO subjects (title) VALUES (%s)"""
            values = (title,)
            cursor.execute(query, values)
            subject_ids.append(cursor.lastrowid)
        print('Subject IDs:', *subject_ids)
    conn.commit()

    # -------------------------------
    # 6. Создание 2х занятий для каждого предмета
    lesson_ids = []
    with conn.cursor() as cursor:
        for i, subject_id in enumerate(subject_ids):
            lesson_titles = [
                f'{subjects[i]} - Lesson 1',
                f'{subjects[i]} - Lesson 2',
            ]
            for title in lesson_titles:
                query = """INSERT INTO lessons (title, subject_id)
                           VALUES (%s, %s)"""
                values = (title, subject_id)
                cursor.execute(query, values)
                lesson_ids.append(cursor.lastrowid)
        print('Lesson IDs:', lesson_ids)
    conn.commit()

    # -------------------------------
    # 7. Проставление студенту оценок
    marks = ['9', '8', '10', '9', '8', '10', '9', '10']
    mark_values = [
        (mark, lesson_id, student_id)
        for lesson_id, mark in zip(lesson_ids, marks)
    ]
    with conn.cursor() as cursor:
        query = """INSERT INTO marks (value, lesson_id, student_id)
                   VALUES (%s, %s, %s)"""
        cursor.executemany(query, mark_values)
    conn.commit()

    # -------------------------------
    # 8. Получение всех оценок студента
    with conn.cursor() as cursor:
        query = """
                SELECT m.value, l.title
                FROM marks m
                         JOIN lessons l ON m.lesson_id = l.id
                WHERE m.student_id = %s
                """
        values = (student_id,)
        cursor.execute(query, values)
        print('\nMarks:')
        for value, lesson in cursor.fetchall():
            print(f'{lesson} - {value}')

    # -------------------------------
    # 9. Получение всех книг студента
    with conn.cursor() as cursor:
        query = """SELECT title FROM books WHERE taken_by_student_id = %s"""
        values = (student_id,)
        cursor.execute(query, values)
        print('\nBooks:')
        for (title,) in cursor.fetchall():
            print(title)

    # -------------------------------
    # 10. Получение полной информации о студенте
    with conn.cursor() as cursor:
        query = """
                SELECT s.name, s.second_name, g.title, b.title, l.title,
                       sub.title, m.value
                FROM students s
                         LEFT JOIN `groups` g ON s.group_id = g.id
                         LEFT JOIN books b ON b.taken_by_student_id = s.id
                         LEFT JOIN marks m ON m.student_id = s.id
                         LEFT JOIN lessons l ON m.lesson_id = l.id
                         LEFT JOIN subjects sub ON l.subject_id = sub.id
                WHERE s.id = %s
                """
        values = (student_id,)
        cursor.execute(query, values)
        print('\nFull student info:')
        for row in cursor.fetchall():
            print(row)
