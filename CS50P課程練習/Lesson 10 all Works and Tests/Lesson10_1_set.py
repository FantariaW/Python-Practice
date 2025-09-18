# Lesson 10 Training: set()
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Lesson 10 Training
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]

# houses = []
# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])

# 1
houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)
    if "Slytherin" in house:
        print("\n" + house)

print("")

# 2
houses_2 = {student["house"] for student in students}
for item in sorted(houses_2):
    if "Gryffindor" in item:
        print(item)
