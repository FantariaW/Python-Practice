# Day All Training 2: All 1-10 Practice
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Day All Training:
import re
import os
import csv
import json
import pandas


class StaffForm:
    def __init__(self, staff_list):
        self.staff_list = staff_list

    def __str__(self):
        result = []

        for index, row in enumerate(self.staff_list, 1):
            name = row["name"]
            age = row["age"]
            department = row["department"]
            id = row["id"]
            password = row["password"]

            masked_pw = "*" * len(password)

            result.append(f"{index}."
                          f"{name} | "
                          f"{age} | "
                          f"{department} | "
                          f"{id} | "
                          f"{masked_pw}.")

        return "\n".join(result)


class GetStaffForm:
    def __init__(self, name, age, department, id, password):
        self.name = name
        self.age = age
        self.department = department
        self.id = id
        self.password = password

    @staticmethod
    def get_prompt_input(prompt_msg, assert_msg, error_msg, allow_stop=False):
        while True:
            try:
                user_input = input(prompt_msg).strip()
                if allow_stop is True and user_input.lower() == "stop":
                    return None
                assert assert_msg(user_input), error_msg
                return user_input
            except AssertionError as e:
                print(e)

    @classmethod
    def get_staff_form(cls):
        staff_list = []
        print("==Staff Form==")
        while True:
            try:
                name = cls.get_prompt_input(
                    "Enter Name: ",
                    lambda n: re.fullmatch(r"^[a-z]+ *[a-z]*$", n, re.IGNORECASE),
                    "Invalid Name...",
                    allow_stop=True
                )
                if name is None:
                    print("End of Program...")
                    break

                age = cls.get_prompt_input(
                    "Enter Age: ",
                    lambda a: a.isdigit() and 18 <= int(a) <= 60,
                    "Invalid Age..."
                )

                department = cls.get_prompt_input(
                    "Enter Department: ",
                    lambda d: re.fullmatch(r"^[a-z]{2,}$", d, re.IGNORECASE),
                    "Invalid Department..."
                )

                id = cls.get_prompt_input(
                    "Enter ID: ",
                    lambda i: i.isdigit() and 1000 <= int(i) <= 9999,
                    "Invalid ID..."
                )

                password = cls.get_prompt_input(
                    "Enter Password: ",
                    lambda p: re.fullmatch(r"^[A-Za-z0-9]{6,10}$", p),
                    "Invalid Password..."
                )

                staff_dict = {
                    "name": name,
                    "age": age,
                    "department": department,
                    "id": id,
                    "password": password
                }

                staff_list.append(staff_dict)

            except ValueError as e:
                print(e)

        cls_staff_list = StaffForm(staff_list)
        print(cls_staff_list.__str__())
        return staff_list


class WriteCSV:
    @staticmethod
    def read_csv():
        try:
            with open("staff.csv", "r", encoding="utf-8") as read_file:
                # ❗使用 set() 檢測重複 id 然後去重！
                csv_set = set()
                csv_list = []

                csv_reader = csv.DictReader(read_file)
                for row in sorted(csv_reader):
                    row_id = row["id"]  # type: ignore
                    if row_id not in csv_set:
                        csv_set.add(row_id)
                        csv_list.append(row)
                return csv_list
        except FileNotFoundError:
            print("📂File Not Found...")
            return []

    @staticmethod
    def append_file(csv_list):
        with open("staff.csv", "a", newline="", encoding="utf-8") as append_file:
            csv_writer = csv.DictWriter(append_file, fieldnames=["name", "age", "department", "id", "password"])
            if not os.path.exists("staff.csv") or os.stat("staff.csv").st_size == 0:
                csv_writer.writeheader()
            csv_writer.writerows(csv_list)

    @staticmethod
    def write_file(staff_list):
        with open("staff.csv", "w", newline="", encoding="utf-8") as write_file:
            csv_writer = csv.DictWriter(write_file, fieldnames=["name", "age", "department", "id", "password"])
            if not os.path.exists("staff.csv") or os.stat("staff.csv").st_size == 0:
                csv_writer.writeheader()
            csv_writer.writerows(staff_list)


# 完善json和excel寫入，寫入更新密碼的程式，sorted所有員工id的順序
class WriteJSON:
    @staticmethod
    def write_json(csv_list):
        with open("staff.json", "w", encoding="utf-8") as write_file:
            json.dump(csv_list, write_file, indent=4, ensure_ascii=False)


class WriteExcel:
    @staticmethod
    def write_excel(csv_list):
        excel_writer = pandas.DataFrame(csv_list)
        excel_writer.to_excel("staff.xlsx", index=False)


class PasswordUpdate:
    @staticmethod
    def password_update(csv_list):
        while True:
            try:
                staff_num = GetStaffForm.get_prompt_input(
                    "Please Select an Staff by Number: ",
                    lambda staff_n: 1 <= int(staff_n) <= len(csv_list),
                    "Num Not Found...",
                    allow_stop=True
                )
                if staff_num is None:
                    return

                new_pw = GetStaffForm.get_prompt_input(
                    "Update New Password: ",
                    lambda new_p: re.fullmatch(r"^[A-Za-z0-9]{6,10}$", new_p),
                    "Invalid Password..."
                )

                csv_list[int(staff_num) - 1]["password"] = new_pw
                WriteCSV.write_file(csv_list)
                print("Password Updated Successfully!")
            except FileNotFoundError:
                print("📂File Not Found...")
                return []


class MainPage:
    @staticmethod
    def function_choice():
        while True:
            try:
                print("Select a Function to Run Program: ")
                user_choice = input(
                    "1.Add New Staff\n"
                    "2.Read CSV File\n"
                    "3.Write into JSON\n"
                    "4.Write into Excel\n"
                    "5.Change Password\n"
                    "6.Exit\n"
                    "- "
                )
                csv_list = WriteCSV.read_csv()

                match user_choice.lower():
                    case "1":
                        staff_list = GetStaffForm.get_staff_form()
                        WriteCSV.append_file(staff_list)
                        print("Staff Added!")
                    case "2":
                        # print(type(csv_list))
                        print(StaffForm(csv_list).__str__())
                    case "3":
                        WriteJSON.write_json(csv_list)
                        print("JSON File Updated!")
                    case "4":
                        WriteExcel.write_excel(csv_list)
                        print("Excel File Updated!")
                    case "5":
                        new_csv_list = PasswordUpdate.password_update(csv_list)
                        if new_csv_list:
                            WriteCSV.write_file(new_csv_list)
                    case "6":
                        print("Exit...")
                        break
                    case _:
                        print("Invalid Choice...")
            except ValueError as e:
                print(e)

    if __name__ == "__main__":
        function_choice()
