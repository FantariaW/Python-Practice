# Lesson 7: with open(), split()
# try:
#     with open("students.csv") as students_file:
#         for line in students_file:
#             row = line.strip().split(",")
#             print(f"{row[0]} is in {row[1]}")
# except FileNotFoundError as e:
#     print("File Not Found!, New File Created!")

# =============================================================================

# 將文件的每行取出存入 list
# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.strip().split(",")
#         students.append(f"{name} is in {house}")
#
# for student in sorted(students):
#     print(student)

# 將文件的每行取出存入 list
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.strip().split(",")

        student = {
            "name": name,
            "house": house
        }
        students.append(student)

    def get_name(student):
        return student["name"]

    for student in sorted(students, key=get_name, reverse=True):
        print(f"{student['name']} is in {student['house']}")

# =============================================================================
