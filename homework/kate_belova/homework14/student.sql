DESCRIBE students;

INSERT INTO students (name, second_name)
SELECT 'Kate', 'Belova'
WHERE NOT EXISTS (SELECT 1
                  FROM students
                  WHERE name = 'Kate'
                    AND second_name = 'Belova');

SELECT *
FROM students
WHERE name = 'Kate'
  AND second_name = 'Belova';

UPDATE students
SET group_id = 21325
WHERE name = 'Kate'
  AND second_name = 'Belova';


