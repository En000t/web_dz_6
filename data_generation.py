from faker import Faker
import psycopg2
import random
from datetime import date

fake = Faker()

# Підключення до бази даних
conn = psycopg2.connect(dbname="your_database_name", user="your_username", password="your_password", host="your_host")
cursor = conn.cursor()

# Генерація груп
for _ in range(3):
    cursor.execute("INSERT INTO groups (group_name) VALUES (%s)", (fake.word(),))

# Генерація студентів
for _ in range(30):
    cursor.execute("INSERT INTO students (student_name, group_id) VALUES (%s, %s)", (fake.name(), random.randint(1, 3)))

# Генерація викладачів
for _ in range(5):
    cursor.execute("INSERT INTO teachers (teacher_name) VALUES (%s)", (fake.name(),))

# Генерація предметів
for _ in range(8):
    cursor.execute("INSERT INTO subjects (subject_name, teacher_id) VALUES (%s, %s)", (fake.word(), random.randint(1, 5)))

# Генерація оцінок
for student_id in range(1, 31):
    for subject_id in range(1, 9):
        cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (%s, %s, %s, %s)",
                       (student_id, subject_id, random.randint(60, 100), fake.date_this_year().isoformat()))

# Збереження змін
conn.commit()

# Закриття з'єднання
cursor.close()
conn.close()
