SELECT subjects.subject_name
FROM subjects
JOIN grades ON subjects.subject_id = grades.subject_id
JOIN teachers ON subjects.teacher_id = teachers.teacher_id
JOIN students ON grades.student_id = students.student_id
WHERE students.student_id = your_value AND teachers.teacher_id = your_condition;
