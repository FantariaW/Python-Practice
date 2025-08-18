# Day 8 Training: regex, csv

# Day 8 Training
import csv
import os
import re


class MemberRecord:
    def __init__(self, member_lst: list):
        self.member_lst = member_lst

    def __str__(self):
        print_result = []

        for index, row in enumerate(self.member_lst, 0):
            name = row["name"]
            phone = row["phone"]
            password = row["password"]
            member_id = row["id"]
            member_status = row["status"]

            print_result.append(f"{index}."
                                f"{name.title()} | "
                                f"{phone} | "
                                f"{password} | "
                                f"{member_id} | "
                                f"{member_status}")

        return "\n".join(print_result)

    @staticmethod
    def prompt_validation(prompt_msg, input_validate, error_msg, allow_exit=False):
        while True:
            try:
                user_input = input(prompt_msg).strip()
                if allow_exit is True and user_input.lower() == 'exit':
                    return None
                assert input_validate(user_input), error_msg
                return user_input
            except AssertionError as e:
                print(e)

    @staticmethod
    def read_file():
        try:
            with open("members.csv", "r", encoding="utf-8") as members_f:
                return list(csv.DictReader(members_f, fieldnames=["name", "phone", "password", "id", "status"]))
        except FileNotFoundError:
            print("📂File Not Found...")

    @staticmethod
    def append_file(member_dict):
        with open("members.csv", "a", newline="", encoding="utf-8") as members_f:
            csv_writer = csv.DictWriter(members_f, fieldnames=["name", "phone", "password", "id", "status"])
            if not os.path.exists("members.csv") or os.stat("members.csv").st_size == 0:
                csv_writer.writeheader()
            csv_writer.writerow(member_dict)

    @staticmethod
    def write_file(member_lst):
        with open("members.csv", "w", newline="", encoding="utf-8") as members_f:
            csv_writer = csv.DictWriter(members_f, fieldnames=["name", "phone", "password", "id", "status"])
            csv_writer.writerows(member_lst)

    @classmethod
    def main_page(cls, prompt_choice="-> "):
        while True:
            try:
                print("==📖Member Record📖==")
                print("1.Add Member\n2.View Member\n3.Mark as VIP Member\n4.Exit")
                user_choice = input(prompt_choice).strip()
                match user_choice.lower():
                    case "1":
                        cls.add_member()
                    case "2":
                        cls.view_member()
                    case "3":
                        cls.mark_member()
                    case "4":
                        print("Bye Bye~")
                        break
                    case _:
                        raise ValueError("Please choose 1 - 4.")
            except ValueError as e:
                print(e)

    @classmethod
    def add_member(cls,
                   prompt_name="Member Name(Capitalize, and at least 2 characters): ",
                   prompt_phone="Phone Number(10 digits): ",
                   prompt_password="Member Password(4 - 8 digits): ",
                   prompt_id="Member ID('CND-XXXX'): ",
                   prompt_status="Are you VIP Member(Yes/No): "):
        print("==📖Add New Member📖==")
        while True:
            try:
                name = cls.prompt_validation(
                    prompt_name,
                    lambda n: re.search(r"^[A-Z][a-z]+$", n),
                    "Enter Capitalize Name.",
                    allow_exit=True
                )
                if name is None:
                    return

                phone = cls.prompt_validation(
                    prompt_phone,
                    lambda ph: ph.isdigit() and re.search(r"^\d{10}$", ph),
                    "Phone Number Must be 10 digits."
                )

                password = cls.prompt_validation(
                    prompt_password,
                    lambda pa: re.search(r"^\S{4,8}$", pa),
                    "Password Must between 4 - 8 characters."
                )

                member_id = cls.prompt_validation(
                    prompt_id,
                    lambda i: re.search(r"^CND-[A-Z0-9]{4}$", i),
                    "Format Should Be 'CND-XXXX'."
                )

                member_status = cls.prompt_validation(
                    prompt_status,
                    lambda s: s.lower() in ["yes", "no"],
                    "Please enter Yes or No."
                )
                member_dict = {
                    "name": name.title(),
                    "phone": phone,
                    "password": password,
                    "id": member_id,
                    "status": member_status.title()
                }
                cls.append_file(member_dict)

                member_lst = cls.read_file()
                cls_member_lst = cls(member_lst)
                print(cls_member_lst.__str__())
            except ValueError as e:
                print(e)

    @classmethod
    def view_member(cls):
        print("==📖View All Member📖==")
        member_lst = cls.read_file()
        cls_member_lst = cls(member_lst)
        print(cls_member_lst.__str__())

    @classmethod
    def mark_member(cls, prompt_id="Member Series ID: "):
        print("==📖Mark as Member📖==")
        while True:
            try:
                member_lst = cls.read_file()

                series_id = cls.prompt_validation(
                    prompt_id,
                    lambda s: s.isdigit() and 1 <= int(s) <= len(member_lst) - 1,
                    "Series ID Not Exists.",
                    allow_exit=True
                )
                if series_id is None:
                    return

                member_lst[int(series_id)]["status"] = "Yes"
                cls.write_file(member_lst)
                cls.view_member()
            except (IndexError, ValueError) as e:
                print(e)


def main():
    MemberRecord.main_page()


if __name__ == "__main__":
    main()
