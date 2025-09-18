# Day 9 Training: super, csv, excel, json
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Day 9 Training:
import re
import csv
import json
import pandas


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def __str__(self):
        return f"Name: {self.name} - Age: {self.age}"


class Teacher(Person):
    def __init__(self, name, age, subject):
        super(Teacher, self).__init__(name, age)
        self.subject = subject

    def __str__(self):
        return f"{super().__str__()} - Subject: {self.subject}."


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = int(grade)

    def __str__(self):
        return f"{super().__str__()} - Grade: {self.grade}."


class PromptInput:
    @staticmethod
    def prompt_input(prompt_msg, assert_msg, error_msg):
        while True:
            try:
                user_input = input(prompt_msg).strip()
                assert assert_msg(user_input), error_msg
                return user_input
            except AssertionError as e:
                print(e)

    @classmethod
    def get_input(cls):
        person_list = []

        while True:
            try:
                user_type = input("Type (T=Teacher / S=Student / stop=quit from program):").strip()
                if user_type.lower() == "stop":
                    print("Exit Program...")
                    break
                elif user_type.lower() not in ["t", "s"]:
                    print("Invalid Type...")
                    continue

                name = cls.prompt_input(
                    "Enter Name: ",
                    lambda n: re.fullmatch(r"^[a-z]+ *[a-z]*$", n, re.IGNORECASE),
                    "Invalid Name..."
                )

                min_age, max_age = (20, 50) if user_type.lower() == "t" else (10, 20)
                age = cls.prompt_input(
                    "Enter Age: ",
                    lambda a: a.isdigit() and min_age <= int(a) <= max_age,
                    "Invalid Age..."
                )

                if user_type.lower() == "t":
                    subject = cls.prompt_input(
                        "Enter Subject: ",
                        lambda s: re.fullmatch(r"^[a-z]{2,20}$", s, re.IGNORECASE),
                        "Invalid Subject..."
                    )
                    person_list.append(Teacher(name, age, subject))
                elif user_type.lower() == "s":
                    grade = cls.prompt_input(
                        "Enter Grade: ",
                        lambda g: g.isdigit() and 0 <= int(g) <= 100,
                        "Invalid Grade..."
                    )
                    person_list.append(Student(name, age, grade))
            except ValueError as e:
                print(e)

            # 呼叫 WriteCSV, 把 list 存入 WriteCSV
            WriteCSV(person_list)
            CountGrade(person_list)

        return person_list


class CountGrade:
    def __init__(self, person_list):
        self.person_list = person_list

    @staticmethod
    def count_grade(person_list):
        student_grade = 0
        for row in person_list:
            # isinstance(object, Type)
            # 十分强大的判斷方法
            # 如果对象是这个类（或它的子类）的实例 → ✅ True
            # 否则 → ❌ False
            if isinstance(row, Student):
                student_grade += row.grade

        return student_grade


class WriteCSV:
    def __init__(self, person_list):
        self.person_list = person_list

    @staticmethod
    def read_csv():
        try:
            with open("person.csv", "r", encoding="utf-8") as person_f:
                return list(csv.reader(person_f))
        except FileNotFoundError:
            print("File Not Found...")
            return []

    @staticmethod
    def append_csv(person_list):
        with open("person.csv", "a", newline="", encoding="utf-8") as person_f:
            csv_writer = csv.writer(person_f)
            for row in person_list:
                # ❌row → 可能會被當成「很多欄位」（字母一個個分開）。
                # ✔️[row] → 明確告訴 CSV：「這是一行，只有一個欄位」。
                csv_writer.writerow([row])


class WriteJSON:
    def __init__(self, read_person_list):
        self.read_person_list = read_person_list

    @staticmethod
    def write_json(read_person_list):
        with open("person.json", "w", encoding="utf-8") as person_f:
            json.dump(read_person_list, person_f, indent=4, ensure_ascii=False)


class WriteExcel:
    def __init__(self, read_person_list):
        self.read_person_list = read_person_list

    @staticmethod
    def write_excel(read_person_list):
        person_xlsx = pandas.DataFrame(read_person_list)
        person_xlsx.to_excel("person.xlsx", index=False)


class PrintList:
    def __init__(self, person_list):
        self.person_list = person_list

    def __str__(self):
        result = []

        for index, row in enumerate(self.person_list, 1):
            result.append(f"{index}.{row}")

        return "\n".join(result)


def main():
    person_list = PromptInput.get_input()
    read_person_list = WriteCSV.read_csv()

    WriteCSV.append_csv(person_list)
    WriteJSON.write_json(read_person_list)
    WriteExcel.write_excel(read_person_list)

    print(PrintList(person_list))
    print("All Student Grade:", CountGrade.count_grade(person_list))


if __name__ == "__main__":
    main()
