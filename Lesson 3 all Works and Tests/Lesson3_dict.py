# list + dict training

# first element is 'KEY', print the KEY, out put result
students = {
    "Student 1": "Fantaria",
    "Student 2": "Arivia",
    "Student 3": "Destina"
}

print(students["Student 1"])

for student in students:
    print(student)

for student in students:
    print(student, students[student], sep=": ")


print("---------------------------------------------------------------------------------------------------------------")


players = [
    {"name": "AAA", "name2": "BBB", "name3": "CCC"},
    {"name": "DDD", "name2": "EEE", "name3": "FFF"},
    {"name": "GGG", "name2": "HHH", "name3": "III"},
    {"name": None, "name2": None, "name3": None}
]

# Arivia_Test_dict.py 裏的例子更清晰易懂
for player in players:
    print("-----".join([
        value if value is not None else ""
        for value in [player["name"], player["name2"], player["name3"]]
    ]), end=", ")

# This will print out None if elements contains 'None' value:
for player in players:
    print(player["name"], player["name2"], player["name3"], sep="-----", end=", ")
