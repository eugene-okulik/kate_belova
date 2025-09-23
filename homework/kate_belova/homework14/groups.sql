DESCRIBE `groups`;

INSERT INTO `groups` (title, start_date, end_date)
SELECT 'QA Automation', '2025-09-01', '2025-10-31'
WHERE NOT EXISTS (SELECT 1 FROM `groups` WHERE title = 'QA Automation');

SELECT *
FROM `groups`
WHERE title = 'QA AUTOMATION';

