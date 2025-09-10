# Day All Training 1: All 1-10 Practice
# new code: # type: ignore  -  line: 185-195
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Day All Training:
import re
import os
import csv
import json
import pandas


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Name: {self.name} - Age: {self.age}"

    def get_person(self) -> tuple[str, int]:
        return self.name, self.age

    def to_dict(self) -> dict:
        return {
            "name": "",
            "age": "",
            "subject": "",
            "id": "",
            "grade": ""
        }


class Teacher(Person):
    def __init__(self, name, age, subject_list: list[str]):
        super().__init__(name, age)
        self.subject_list = subject_list

    def __str__(self) -> str:
        return f"{super().__str__()} - Subject: {self.subject_list}."

    def to_dict(self):
        updated_dict = super().to_dict()
        updated_dict.update({
            "name": self.name,
            "age": self.age,
            "subject": self.subject_list
        })
        return updated_dict

    def get_subject(self) -> list[str]:
        return self.subject_list


class Student(Person):
    def __init__(self, name, age, id, grade):
        super().__init__(name, age)
        self.id = id
        self.grade = grade

    def __str__(self) -> str:
        return f"{super().__str__()} - ID: {self.id} - Grade: {self.grade}."

    def to_dict(self):
        updated_dict = super().to_dict()
        updated_dict.update({
            "name": self.name,
            "age": self.age,
            "id": self.id,
            "grade": self.grade
        })
        return updated_dict

    def get_student(self) -> tuple[int, int]:
        return self.id, self.grade


class GetPerson:
    def __init__(self, people_list: list[dict]):
        self.people_list = people_list

    def __str__(self):
        result = []
        for index, row in enumerate(self.people_list, 1):
            result.append(f"{index}.{row}")
        return "\n".join(result)

    @staticmethod
    def get_prompt(prompt_msg, assert_msg, error_msg, allow_stop=False):
        while True:
            try:
                user_input = input(prompt_msg).strip()
                if allow_stop is True and user_input.lower() == "exit":
                    return None
                assert assert_msg(user_input), error_msg
                return user_input
            except AssertionError as e:
                print(e)

    @classmethod
    def get_information(cls):
        people_list = []
        while True:
            try:
                print("📝【考核】學生管理與報表系統")
                info_type = input("T = Teacher, S = Student, stop = exit: ").strip()
                if info_type.lower() == "exit":
                    print("Exit From Program.")
                    break
                elif info_type.lower() not in ["t", "s"]:
                    print("Invalid Type...")
                    continue

                name = cls.get_prompt(
                    "Enter Name: ",
                    lambda n: re.fullmatch(r"^[a-z]+ *[a-z]*$", n, re.IGNORECASE),
                    "Invalid Name..."
                )

                min_age, max_age = (20, 50) if info_type.lower() == "t" else (10, 20)
                age_prompt_msg = "20 - 50" if info_type.lower() == "t" else "10 - 20"
                age = cls.get_prompt(
                    f"Enter Age({age_prompt_msg}): ",
                    lambda a: a.isdigit() and min_age <= int(a) <= max_age,
                    "Invalid Age..."
                )

                match info_type.lower():
                    case "t":
                        subject_list: list[str] = []
                        while True:
                            try:
                                subject = cls.get_prompt(
                                    "Enter Subject('exit' to stop): ",
                                    lambda s: re.fullmatch(r"^[a-z]{2,20}$", s, re.IGNORECASE),
                                    "Invalid Subject...",
                                    allow_stop=True
                                )
                                if subject is None:
                                    break
                                subject_list.append(subject)
                            except AssertionError as e:
                                print(e)
                        teacher = Teacher(name, int(age), subject_list)
                        people_list.append(Teacher.to_dict(teacher))

                    case "s":
                        id = cls.get_prompt(
                            "Enter ID(10XX): ",
                            lambda i: re.fullmatch(r"^10[0-9]{2}$", i),
                            "Invalid ID..."
                        )
                        grade = cls.get_prompt(
                            "Enter Grade(0-100): ",
                            lambda g: g.isdigit() and 0 <= int(g) <= 100,
                            "Invalid Grade..."
                        )
                        student = Student(name, int(age), id, grade)
                        people_list.append(Student.to_dict(student))
                    case _:
                        print("Invalid Type...")
            except AssertionError as e:
                print(e)
        print(type(people_list))
        people_list_obj = cls(people_list)
        print(people_list_obj.__str__())
        return people_list


# print(GetPerson.get_information())


class WriteCSV:
    @staticmethod
    def read_file():
        try:
            with open("people.csv", "r", encoding="utf-8") as people_f:
                # ❗❤ pythonic 高級寫法，我不太記得住，暫時不打算使用
                # DictReader 不要使用 fieldnames=["name", "age", "subject", "id", "grade"]
                # 這行等於強制告訴 DictReader：「不要把第一行當表頭，把它也當成一條普通資料」。
                # 於是首行（name,age,subject,id,grade）就被讀成了字典：
                # {"name": "name", "age": "age", "subject": "subject", "id": "id", "grade": "grade"}
                # return list(csv.DictReader(people_f))
                csv_reader = csv.DictReader(people_f)

                csv_set = set()
                csv_list = []

                for row in csv_reader:
                    # ❗關於 type:ignore 的使用和解釋 (詳細可以翻翻python筆記)：
                    # Expected type 'SupportsIndex | slice', got 'str' instead
                    #
                    # csv.DictReader 的每一行 → 應該是一個 dict：
                    # {"name": "teacher one", "age": "20", "id": "1001", "grade": "90"}
                    # 但靜態型別檢查器（PyCharm/VSCode + Pylance/mypy）對 row 的推斷不總是那麼精準。
                    # 它有時候會把 row 判斷成「list 或 str」，而不是「dict」。
                    # 當它認為 row 可能是 list 時，row['name'] 就被當成「拿字串做索引」，所以 IDE 提示：
                    # Expected type 'SupportsIndex | slice', got 'str' instead

                    identifier = f"{row['name']}_{row['id']}"  # type:ignore

                    if identifier not in csv_set:
                        csv_set.add(identifier)
                        csv_list.append(row)

                return csv_list
        except FileNotFoundError:
            print("📂File Not Found...")
            return []

    @staticmethod
    def append_file(people_list):
        with open("people.csv", "a", newline="", encoding="utf-8") as people_f:
            csv_writer = csv.DictWriter(people_f, fieldnames=["name", "age", "subject", "id", "grade"])
            if not os.path.exists("people.csv") or os.stat("people.csv").st_size == 0:
                csv_writer.writeheader()
            csv_writer.writerows(people_list)


class WriteJSON:
    @staticmethod
    def write_json(read_csv_list):
        with open("people.json", "w", encoding="utf-8") as people_f:
            json.dump(read_csv_list, people_f, indent=4, ensure_ascii=False)


class WriteExcel:
    @staticmethod
    def write_excel(read_csv_list):
        people_xlsx = pandas.DataFrame(read_csv_list)
        people_xlsx.to_excel("people.xlsx", index=False)


class MainPage:
    @staticmethod
    def main():
        # 首先詢問獲取用戶信息 -> list[dict]
        people_list = GetPerson.get_information()

        # 將 list[dict] 存入CSV文件
        WriteCSV.append_file(people_list)

        # 讀取csv文件内容，存入json文件
        read_csv_list = WriteCSV.read_file()
        WriteJSON.write_json(read_csv_list)

        # 使用已經讀取的list内容，寫入excel
        WriteExcel.write_excel(read_csv_list)

    if __name__ == "__main__":
        main()
