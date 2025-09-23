DESCRIBE lessons;

INSERT INTO lessons (title, subject_id)
VALUES ('Python Start', 12358),
       ('Python OOP', 12358),
       ('SQL Basics', 12359),
       ('SQL with Python', 12359),
       ('REST API Basics', 12360),
       ('Requests library', 12360),
       ('Selenium library', 12361),
       ('Playwright library', 12361);

SELECT *
FROM lessons
ORDER BY id DESC
LIMIT 20;