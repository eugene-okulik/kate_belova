SELECT m.value AS mark, l.title AS lesson
FROM marks m
         JOIN lessons l ON m.lesson_id = l.id
WHERE m.student_id = 21358;

SELECT b.title AS book
FROM books b
WHERE b.taken_by_student_id = 21358;

SELECT s.name        AS first_name,
       s.second_name AS last_name,
       g.title       AS group_name,
       b.title       AS book_title,
       l.title       AS lesson_title,
       sub.title     AS subject_title,
       m.value       AS mark
FROM students as s
         LEFT JOIN `groups` g ON s.group_id = g.id
         LEFT JOIN books b ON b.taken_by_student_id = s.id
         LEFT JOIN marks m ON m.student_id = s.id
         LEFT JOIN lessons l ON m.lesson_id = l.id
         LEFT JOIN subjects sub ON l.subject_id = sub.id
WHERE s.id = 21358;
