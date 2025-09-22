DESCRIBE subjects;

INSERT INTO subjects (title)
VALUES ('Python Basics'),
       ('Database Fundamentals'),
       ('REST API Automated Testing'),
       ('UI Automation');

SELECT *
FROM subjects
ORDER BY id DESC
LIMIT 10;
