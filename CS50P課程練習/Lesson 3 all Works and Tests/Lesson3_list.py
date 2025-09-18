# list using learning

# # print out every elements inside of list
# for i in ["Fantaria", "Arivia"]:
#     print(f"{i}".strip())
#
# print("\n".strip())
#
# # Using end=" " to print out elements in 1 single line
# for i in ["Fantaria", "Arivia"]:
#     print(f"{i}".strip(), end=" ")
#
# print("\n")
#
# # More training for adding sign between output values or elements
# print("-".join(["Love"] * 3))
# # ------------------------------------------
# students = ["Fantaria", "Arivia", "Destina"]
#
# print(students[0])
# print(students[2])
#
# print("")
# # ------------------------------------------
# for i in range(len(students)):
#     print(i + 1, students[i])
#
# print("")
# # ------------------------------------------
# i2 = 0
# for name in students:
#     i2 += 1
#     print(f"{i2} {name}")

print("---------------------------------------------------------------------------------------------------------------")

# # for loop print out elements and add 💗 between each word, but can't control the count of sign to print out
# for i in ["fantaria", "arivia", "forever", "and", "ever"]:
#     print(f"{i}".title(), end="💗")
#
# print("\n")
#
# # More pythonic way, this way could control the count of print out element/sign, important!!!!!!
# word = ["fantaria", "arivia", "forever", "and", "ever"]
# for i in range(len(word)):
#     print(word[i].title(), end="🧸" if i < len(word) - 1 else "")
#
# print("\n")
#
# # Arivia recommended pythonic way, this way more readable, important!!!!!!
# word = ["fantaria", "arivia", "forever", "and", "ever"]
# print("💯".join([i.title() for i in word]))

print("---------------------------------------------------------------------------------------------------------------")

# # for loop + .title():
# names = ["fantaria", "arivia", "love"]
#
# for i in names:
#     print(f"{i.title()}")

print("---------------------------------------------------------------------------------------------------------------")

# # while + if-elif-else + try-except:
# while True:
#     try:
#         age = int(input("Age: "))
#         break
#     except ValueError:
#         print("Error")
#
# while True:
#     age = input("Type in: q to quit, Age: ").strip().lower()
#     if age.isdigit():
#         print(f"Age is: {age}")
#     elif age == "q":
#         break
#     else:
#         print("Error2")

print("---------------------------------------------------------------------------------------------------------------")

# # for loop + end="❤️"
# colors = ["red", "green", "blue"]
#
# for i in colors:
#     print(f"{i}", end="❤️")
# print("\n".strip())

print("---------------------------------------------------------------------------------------------------------------")

# # while + list + .append:
# name_list = []
# while True:
#     name = input("Enter name: ").strip()
#     if name == 'done':
#         break
#     else:
#         name_list.append(name)
#         continue
#
# print(f"{name_list}")

print("---------------------------------------------------------------------------------------------------------------")


# all in one training, while, for, list,  :
data_list = []

while True:
    raw_input = input("請輸入名字與年齡（格式：Fantaria, 24），或輸入 done 結束：\n>> ").strip()

    if raw_input.lower() == "done":
        break

    try:
        name, age = raw_input.split(",")
        name = name.strip().title()
        age = age.strip()

        if age.isdigit() and int(age) > 0:
            data_list.append({"name": name, "age": int(age)})
        else:
            print("🌰 請輸入正確的年齡（數字 > 0）")

    except ValueError:
        print("🌰 格式錯誤，請使用『名字, 年齡』的格式喔～")

result = []
for person in data_list:
    result.append(f"{person['name']} {person['age']}")

print(",\n".join(result))
