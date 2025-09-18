# Day 9 Training: super, csv

# Day 9 Training:
import re
import csv


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
        return f"{super(Teacher, self).__str__()} - Subject: {self.subject}."


class Student(Person):
    def __init__(self, name, age, grade):
        super(Student, self).__init__(name, age)
        self.grade = int(grade)

    def __str__(self):
        return f"{super(Student, self).__str__()} - Grade: {self.grade}"


class PromptInput:
    @staticmethod
    def prompt_validation(prompt_msg, validate_msg, error_msg):
        while True:
            try:
                user_input = input(prompt_msg).strip()
                assert validate_msg(user_input), error_msg
                return user_input
            except AssertionError as e:
                print(e)

    @classmethod
    def prompt_input(cls):
        print("📝學校人員管理📝")
        people_list = []

        while True:
            try:
                user_type = input("Type (T=Teacher / S=Student / stop=quit): ").strip()
                if user_type.lower() == "stop":
                    print("Exit From Program...Bye Bye!")
                    break
                elif user_type.lower() not in ["t", "s"]:
                    print("Invalid Choice...")
                    continue

                name = cls.prompt_validation(
                    "Name: ",
                    lambda n: re.search(r"^[a-z]+ *[a-z]*$", n, re.IGNORECASE),
                    "Invalid Name..."
                )

                min_age, max_age = (20, 50) if user_type.lower() == "t" else (10, 20)
                age = cls.prompt_validation(
                    "Age: ",
                    lambda a: a.isdigit() and min_age <= int(a) <= max_age,
                    f"Invalid Age...(Please Enter {min_age} - {max_age})"
                )

                if user_type.lower() == "t":
                    subject = cls.prompt_validation(
                        "Subject: ",
                        lambda s: re.search(r"^[a-z]+$", s, re.IGNORECASE),
                        "Invalid Subject..."
                    )
                    people_list.append(Teacher(name, age, subject))
                elif user_type.lower() == "s":
                    grade = cls.prompt_validation(
                        "Grade: ",
                        lambda s: re.search(r"^\d+$", s),
                        "Invalid Grade..."
                    )
                    people_list.append(Student(name, age, grade))
                else:
                    print("Invalid Choice...")
            except ValueError as e:
                print(e)
            AppendFile(people_list)
        return people_list


class AppendFile:
    def __init__(self, people_list):
        self.people_list = people_list

    @classmethod
    def append_file(cls, people_list):
        with open("people.csv", "a", newline="", encoding="utf-8") as people_file:
            csv_writer = csv.writer(people_file)
            csv_writer.writerow(people_list)


class PrintResult:
    def __init__(self, people_list: list):
        self.people_list = people_list

    def __str__(self):
        lines = []

        for index, line in enumerate(self.people_list, 1):
            lines.append(f"{index}.{line}")

        return "\n".join(lines)


def main():
    people_list = PromptInput.prompt_input()
    AppendFile.append_file(people_list)
    print(PrintResult(people_list))


if __name__ == "__main__":
    main()
