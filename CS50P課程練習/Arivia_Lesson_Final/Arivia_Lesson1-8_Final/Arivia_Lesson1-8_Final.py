# Lesson 1 - 8 Final: 1 - 8 Test
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Lesson 1 - 8 Final:
import sys
import re
import csv
import os
import json


class EmployeeDataSystem:
    def __init__(self, employee_lst: list):
        self.employee_lst = employee_lst

    def __str__(self):
        result = []

        for index, row in enumerate(self.employee_lst, 1):
            name = row["name"]
            age = row["age"]
            department = row["department"]
            year = row["year"]
            password = row["password"]

            pw_mask = "*" * len(password)

            result.append(f"{index}."
                          f"{name} | "
                          f"{age} | "
                          f"{department} | "
                          f"{year} | "
                          f"{pw_mask}.")

        return "Name | Age | Department | Year | Password\n" + "\n".join(result)

    @staticmethod
    def prompt_validation(prompt_msg, validate_msg, error_msg, allow_exit=False):
        while True:
            try:
                user_input = input(prompt_msg).strip()
                if allow_exit is True and user_input.lower() == "exit":
                    return None
                assert validate_msg(user_input), error_msg
                return user_input
            except AssertionError as e:
                print(e)

    @staticmethod
    def append_file(employee_dict):
        with open("employees.csv", "a", newline="", encoding="utf-8") as employees_f:
            csv_writer = csv.DictWriter(employees_f, fieldnames=["name", "age", "department", "year", "password"])
            if not os.path.exists("employees.csv") or os.stat("employees.csv").st_size == 0:
                csv_writer.writeheader()
            csv_writer.writerow(employee_dict)

    @staticmethod
    def write_file(employee_lst):
        with open("employees.csv", "w", newline="", encoding="utf-8") as employees_f:
            csv_writer = csv.DictWriter(employees_f, fieldnames=["name", "age", "department", "year", "password"])
            if not os.path.exists("employees.csv") or os.stat("employees.csv").st_size == 0:
                csv_writer.writeheader()
            csv_writer.writerows(employee_lst)

    @staticmethod
    def read_file():
        try:
            with open("employees.csv", "r", encoding="utf-8") as employees_f:
                return list(csv.DictReader(employees_f))
        except FileNotFoundError:
            print("📂File Not Found...")
            return []

    @staticmethod
    def write_json_dump(employee_lst):
        with open("employees.json", "w", encoding="utf-8") as employees_f:
            json.dump(employee_lst, employees_f, indent=4, ensure_ascii=False)

    # ========================================================================

    @classmethod
    def main_page(cls, prompt_choice="-> "):
        while True:
            print("📖=Employee Data Manage System=📖")
            print("1.Add Employee\n"
                  "2.View Employee.csv\n"
                  "3.View Summary of Employee\n"
                  "4.Change Password\n"
                  "5.Exit")
            try:
                user_choice = input(prompt_choice).strip()
                match user_choice.lower():
                    case "1":
                        cls.add_employee()
                    case "2":
                        cls.view_employee_csv()
                    case "3":
                        cls.summary_employee()
                    case "4":
                        cls.password_update()
                    case "5":
                        print("Bye Bye~")
                        sys.exit()
                    case _:
                        raise ValueError("Please choose 1 - 5")
            except ValueError as e:
                print(e)

    @classmethod
    def add_employee(cls,
                     prompt_name="Employee Name: ",
                     prompt_age="Employee Age(18-60): ",
                     prompt_department="Employee Department(IT/HR/Marketing): ",
                     prompt_joining_year="Date of Join(2000-2023): ",
                     prompt_password="Employee Account Password(6-10 characters): "):
        print("📖=Add New Employee=📖")

        emp_name = cls.prompt_validation(
            prompt_name,
            lambda n: n != "" and re.search(r"^[a-z]+\s*[a-z]*$", n, re.IGNORECASE),
            "Invalid Name, 1 Character at Least.",
            allow_exit=True
        )
        if emp_name is None:
            return

        emp_age = cls.prompt_validation(
            prompt_age,
            lambda a: a.isdigit() and 18 <= int(a) <= 60,
            "Invalid Age, Should be Around 18 - 60."
        )

        emp_department = cls.prompt_validation(
            prompt_department,
            lambda d: d.lower() in ["it", "hr", "marketing"],
            "Invalid Department, Please choose 1 of 3 Types."
        )
        if emp_department.lower() == "it" or emp_department.lower() == "hr":
            emp_department = emp_department.upper()
        else:
            emp_department = emp_department.title()

        emp_joining_year = cls.prompt_validation(
            prompt_joining_year,
            lambda y: re.search(r"^20[0-2]+[0-3]+$", y),
            "Invalid Year, Should be Around 2000 - 2023."
        )

        emp_password = cls.prompt_validation(
            prompt_password,
            lambda p: re.search(r"^[A-Za-z0-9]{6,10}$", p),
            "Invalid Password, Should be Around 6 - 10 characters."
        )

        employee_dict = {
            "name": emp_name.title(),
            "age": int(emp_age),
            "department": emp_department,
            "year": emp_joining_year,
            "password": emp_password
        }

        if os.path.exists("employees.csv") or os.stat("employees.csv").st_size != 0:
            user_choice = cls.prompt_validation(
                "❗You have a 'employees.csv' file already, would you like to update it?\n(Y/N)",
                lambda c: c.lower() in ["y", "n"],
                "Please enter Y or N."
            )
            match user_choice.lower():
                case "y":
                    cls.append_file(employee_dict)
                    employee_lst = cls.read_file()
                    cls.write_json_dump(employee_lst)  # ❗將全新的csv文件内容存入json
                    cls(employee_lst)
                    print("✅Saved Successfully!")
                case "n":
                    print("❌Employee Not Saving...")
                    return
        # print(cls_employee_lst.__str__())

    @classmethod
    def view_employee_csv(cls):
        employee_lst = cls.read_file()
        cls_employee_lst = cls(employee_lst)
        print(cls_employee_lst.__str__())

    # ❗全新邏輯和程式碼知識
    @classmethod
    def summary_employee(cls):
        employee_lst = cls.read_file()
        summary_dict = {}

        for row in employee_lst:
            if row["department"] in summary_dict:
                summary_dict[row["department"]]["count"] += 1
                summary_dict[row["department"]]["sum_age"] += int(row["age"])
            if row["department"] not in summary_dict:
                summary_dict[row["department"]] = {
                    "count": 1,
                    "sum_age": int(row["age"])
                }

        for department in summary_dict:
            count = summary_dict[department]["count"]
            total_age = summary_dict[department]["sum_age"]
            summary_dict[department]["avg_age"] = round(total_age / count, 1)
            del summary_dict[department]["sum_age"]

        print(summary_dict)

    @classmethod
    def password_update(cls,
                        prompt_employee_id="Please Enter an ID Which You want to Update the Password: ",
                        prompt_new_pw="Please Enter a New Password: "):
        employee_lst = cls.read_file()
        while True:
            try:
                employee_id = cls.prompt_validation(
                    prompt_employee_id,
                    lambda i: 1 <= int(i) <= len(employee_lst),
                    "❓Employee ID Not Exists...",
                    allow_exit=True
                )
                if employee_id is None:
                    return

                new_pw = cls.prompt_validation(
                    prompt_new_pw,
                    lambda n_pw: re.search(r"^[A-Za-z0-9]{6,10}$", n_pw),
                    "Invalid Password, Should be Around 6 - 10 characters."
                )
                employee_lst[int(employee_id) - 1]["password"] = new_pw
                cls.write_file(employee_lst)
                new_employee_lst = cls.read_file()
                cls.write_json_dump(new_employee_lst)  # ❗將全新的csv文件内容存入json
                cls(new_employee_lst)
                print("✅Password Updated Successfully!")
            except (IndexError, AssertionError) as e:
                print(e)


def main():
    EmployeeDataSystem.main_page()


if __name__ == "__main__":
    main()
