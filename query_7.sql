SELECT student_id, grade
FROM grades
JOIN students ON grades.student_id = students.student_id
WHERE students.group_id = your_value AND grades.subject_id = your_condition;
