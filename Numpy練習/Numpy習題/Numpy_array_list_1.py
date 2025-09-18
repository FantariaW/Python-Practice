# Numpy Practice: array, list
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
import numpy as np


students_list = []

student_count = input("Enter Number of Student: ").strip()
subject_grade = input("Enter Number of Subject: ").strip()

for row in range(int(student_count)):
    grade_list = []
    print(f"Student - {row + 1}: ")
    for num in range(int(subject_grade)):
        grade = int(input(f"Student {row + 1} Subject {num + 1}: "))
        grade_list.append(grade)

    students_list.append(grade_list)

np_list = np.array(students_list)

print(np_list)

print(np_list.sum())
print(f"按竪列(每科成績)計算成績: {np_list.sum(axis=0)}")
print(f"按橫行(每人)計算成績: {np_list.sum(axis=1)}")
print(f"按橫行(每人)平均成績: {np_list.mean(axis=1)}")
