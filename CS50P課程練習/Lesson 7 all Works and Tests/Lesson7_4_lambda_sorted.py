# Lesson 7: lambda, sorted(), csv.reader()
import csv

students = []

with open("students_2.csv") as s_file:
    f_reader = csv.reader(s_file)
    for row in f_reader:
        students.append({"name": row[0], "house": row[1]})
    # for name, house in f_reader:
    #     students.append({'name': name, 'house': house})

print(students)

for student in sorted(students, key=lambda s: s["name"]):
    print(f"{student['name']} is in {student['house']}")
