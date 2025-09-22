DESCRIBE books;

INSERT INTO books
    (title, taken_by_student_id)
VALUES ('Selenium Automation Testing with Python', 21358),
       ('Playwright Python Automation Testing', 21358),
       ('Python API Test Automation Framework', 21358);

SELECT *
FROM books
WHERE taken_by_student_id = 21358;


