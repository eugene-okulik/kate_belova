DESCRIBE marks;

INSERT INTO marks (value, lesson_id, student_id)
SELECT '9', lessons.id, 21358
FROM lessons
WHERE lessons.title = 'Python Start';

INSERT INTO marks (value, lesson_id, student_id)
SELECT '8', lessons.id, 21358
FROM lessons
WHERE lessons.title = 'Python OOP';

INSERT INTO marks (value, lesson_id, student_id)
SELECT '8', lessons.id, 21358
FROM lessons
WHERE lessons.title = 'SQL Basics';

INSERT INTO marks (value, lesson_id, student_id)
SELECT '8', lessons.id, 21358
FROM lessons
WHERE lessons.title = 'SQL with Python';

INSERT INTO marks (value, lesson_id, student_id)
SELECT '9', lessons.id, 21358
FROM lessons
WHERE lessons.title = 'REST API Basics';

INSERT INTO marks (value, lesson_id, student_id)
SELECT '9', lessons.id, 21358
FROM lessons
WHERE lessons.title = 'Requests Library';

INSERT INTO marks (value, lesson_id, student_id)
SELECT '10', lessons.id, 21358
FROM lessons
WHERE lessons.title = 'Selenium Library';

INSERT INTO marks (value, lesson_id, student_id)
SELECT '7', lessons.id, 21358
FROM lessons
WHERE lessons.title = 'Playwright library';

SELECT *
FROM marks
ORDER BY id DESC
LIMIT 20;
