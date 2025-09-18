# Lesson 7: lambda, sorted(), import csv
import csv

name = input("Name: ")
house = input("House: ")

try:
    with open("students_3.csv", "a", newline="", encoding="utf-8") as s_file:
        # s_file.write(f"{name},{house}\n")

        # writer = csv.writer(s_file)
        # writer.writerow([name, house])

        writer = csv.DictWriter(s_file, fieldnames=["name", "house"])
        writer.writeheader()
        writer.writerow({"name": name, "house": house})
except FileNotFoundError:
    print("File Not Found, New File Created!")

with open("students_3.csv", "r", encoding="utf-8") as s_file:
    lines = s_file.readlines()
    for line in lines:
        print(line, end="")
