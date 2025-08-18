# Day 8 Training: group

# Day 8 Training:
import csv
import os
import re


class DessertIdStation:
    def __init__(self, dessert_lst):
        self.dessert_lst = dessert_lst

    def __str__(self):
        flavor_symbol = ""
        result = []

        for index, row in enumerate(self.dessert_lst, 0):
            nickname = row["nickname"]
            phone = row["phone"]
            password = row["password"]
            flavor_code = row["flavor-code"]
            dessert_type = row["type"]
            status = row["status"]

            matches = re.search(r"^FLV-(\d{3})$", flavor_code)
            if matches:
                code_num = int(matches.group(1))
                if 000 <= int(code_num) <= 199:
                    flavor_symbol = "🍬"
                elif 200 <= int(code_num) <= 699:
                    flavor_symbol = "🍭"
                elif 700 <= int(code_num) <= 999:
                    flavor_symbol = "🍯"
            else:
                flavor_symbol = ""

            # 星星 乘以 密碼字符長度，打印出對應數量的 星星，隱藏密碼
            masked = "*" * len(password)

            result.append(f"{index}."
                          f"{nickname} | "
                          f"{phone} | "
                          f"{masked} | "
                          f"{flavor_code}{flavor_symbol} | "
                          f"{dessert_type} | "
                          f"{status}.")

        return "\n".join(result)

    @staticmethod
    def prompt_validate(prompt_msg, msg_validate, error_msg, allow_exit=False):
        while True:
            try:
                user_input = input(prompt_msg).strip()
                if allow_exit is True and user_input.lower() == "exit":
                    return None
                assert msg_validate(user_input), error_msg
                return user_input
            except AssertionError as e:
                print(e)

    @staticmethod
    def read_file():
        try:
            with open("passport.csv", "r", encoding="utf-8") as f:
                return list(csv.DictReader(f, fieldnames=[
                    "nickname", "phone", "password", "flavor-code", "type", "status"
                ]))
        except FileNotFoundError:
            print("📂File Doesn't Exists...")

    @staticmethod
    def append_file(dessert_dict):
        with open("passport.csv", "a", newline="", encoding="utf-8") as f:
            csv_writer = csv.DictWriter(f, fieldnames=[
                "nickname", "phone", "password", "flavor-code", "type", "status"
            ])
            if not os.path.exists("passport.csv") or os.stat("passport.csv").st_size == 0:
                csv_writer.writeheader()
            csv_writer.writerow(dessert_dict)

    @staticmethod
    def write_file(dessert_lst):
        with open("passport.csv", "w", newline="", encoding="utf-8") as f:
            csv_writer = csv.DictWriter(f, fieldnames=[
                "nickname", "phone", "password", "flavor-code", "type", "status"
            ])
            csv_writer.writerows(dessert_lst)

    @classmethod
    def main_page(cls, prompt_choice="-> "):
        while True:
            try:
                print("==🍦Dessert ID Station🍦==")
                print("1.Add Dessert\n2.View Dessert\n3.Update Sweetness\n4.Update Password\n5.Mark as VIP\n6.Exit")

                user_choice = input(prompt_choice).strip()
                match user_choice.lower():
                    case "1":
                        cls.add_dessert()
                    case "2":
                        cls.view_dessert()
                    case "3":
                        cls.update_flavor_code()
                    case "4":
                        cls.update_password()
                    case "5":
                        cls.mark_dessert_vip()
                    case "6":
                        print("Exit from program...Bye Bye~")
                        break
                    case _:
                        raise ValueError("Please choose 1 - 6.")
            except ValueError as e:
                print(e)

    @classmethod
    def add_dessert(cls,
                    prompt_nickname="Dessert Name(Capitalized, At least 3 characters, English Only): ",
                    prompt_phone="Phone(10 digits start with 09): ",
                    prompt_password="Password(6-10 characters): ",
                    prompt_code="Flavor Code(3 digits from 000 - 999 'FLV-XXX'): ",
                    prompt_type="Dessert Type(Cake/Pudding/Pie/Donut): ",
                    prompt_status="VIP Status(Yes/No): "):
        print("==🍦Add New Dessert🍦==")
        while True:
            try:
                nickname = cls.prompt_validate(
                    prompt_nickname,
                    lambda n: re.search(r"^[A-Za-z]{3,}$", n),
                    "Name Format Incorrect...",
                    allow_exit=True
                )
                if nickname is None:
                    return

                phone = cls.prompt_validate(
                    prompt_phone,
                    lambda ph: re.search(r"^09\d{8}$", ph),
                    "Phone Format Incorrect..."
                )

                password = cls.prompt_validate(
                    prompt_password,
                    lambda pw: re.search(r"^\S{6,10}$", pw),
                    "Password Format Incorrect..."
                )

                flavor_code = cls.prompt_validate(
                    prompt_code,
                    lambda fc: re.search(r"^FLV-(\d{3})$", fc),
                    "Flavor Code Invalid..."
                )

                dessert_type = cls.prompt_validate(
                    prompt_type,
                    lambda t: t.lower() in ["cake", "pudding", "pie", "donut"],
                    "Type doesn't Exists, Please Choose 1 of 4 Types..."
                )

                status = cls.prompt_validate(
                    prompt_status,
                    lambda s: s.lower() in ["yes", "no"],
                    "Please Choose Yes or No..."
                )

                dessert_dict = {
                    "nickname": nickname.title(),
                    "phone": phone,
                    "password": password,
                    "flavor-code": flavor_code,
                    "type": dessert_type.title(),
                    "status": status.title()
                }
                cls.append_file(dessert_dict)
                print(f"✅登記成功，甜點名稱:{nickname}")
                dessert_lst = cls.read_file()
                cls_dessert_lst = cls(dessert_lst)
                print(cls_dessert_lst.__str__())
            except ValueError as e:
                print(e)

    @classmethod
    def view_dessert(cls):
        print("==🍦Dessert List🍦==")
        dessert_lst = cls.read_file()
        cls_dessert_lst = cls(dessert_lst)
        print(cls_dessert_lst.__str__())

    @classmethod
    def update_flavor_code(cls,
                           prompt_num="Dessert Series ID: ",
                           prompt_new_code="Update New Flavor Code(3 digits from 000 - 999 'FLV-XXX'): "):
        print("==🍦Update Dessert's Flavor-Code🍦==")
        dessert_lst = cls.read_file()
        while True:
            try:
                dessert_num = cls.prompt_validate(
                    prompt_num,
                    lambda n: n != "" and 1 <= int(n) <= len(dessert_lst) - 1,
                    "Series ID Number Doesn't Exists...",
                    allow_exit=True
                )
                if dessert_num is None:
                    return

                new_flavor_code = cls.prompt_validate(
                    prompt_new_code,
                    lambda new_fc: re.search(r"^FLV-\d{3}$", new_fc),
                    "Flavor Code Invalid..."
                )

                dessert_lst[int(dessert_num)]["flavor-code"] = new_flavor_code
                print(f"✅New Flavor-Code has been updated: {new_flavor_code}.")
                cls.write_file(dessert_lst)
                new_dessert_lst = cls.read_file()
                cls_dessert_lst = cls(new_dessert_lst)
                print(cls_dessert_lst.__str__())
            except (IndexError, AssertionError) as e:
                print(e)

    @classmethod
    def update_password(cls,
                        prompt_num="Dessert Series ID: ",
                        prompt_new_password="Update New Password(6-10 characters): "):
        print("==🍦Update Dessert's Password🍦==")
        dessert_lst = cls.read_file()
        while True:
            try:
                dessert_num = cls.prompt_validate(
                    prompt_num,
                    lambda n: 1 <= int(n) <= len(dessert_lst) - 1,
                    "Series ID Number Doesn't Exists...",
                    allow_exit=True
                )
                if dessert_num is None:
                    return

                new_password = cls.prompt_validate(
                    prompt_new_password,
                    lambda new_pw: re.search(r"^\S{6,10}$", new_pw),
                    "Password Format Incorrect..."
                )

                dessert_lst[int(dessert_num)]["password"] = new_password
                print(f"✅New Password has been updated: {new_password}.")
                cls.write_file(dessert_lst)
                new_dessert_lst = cls.read_file()
                cls_dessert_lst = cls(new_dessert_lst)
                print(cls_dessert_lst.__str__())
            except (IndexError, ValueError) as e:
                print(e)

    @classmethod
    def mark_dessert_vip(cls, prompt_num="Dessert Series ID: "):
        print("==🍦Mark Dessert as VIP🍦==")
        dessert_lst = cls.read_file()

        while True:
            try:
                dessert_num = cls.prompt_validate(
                    prompt_num,
                    lambda n: 1 <= int(n) <= len(dessert_lst) - 1,
                    "Series ID Number Doesn't Exists...",
                    allow_exit=True
                )
                if dessert_num is None:
                    return

                dessert_lst[int(dessert_num)]["status"] = "Yes"
                cls.write_file(dessert_lst)
                new_dessert_lst = cls.read_file()
                cls_dessert_lst = cls(new_dessert_lst)
                print(cls_dessert_lst.__str__())
            except (IndexError, ValueError) as e:
                print(e)


def main():
    DessertIdStation.main_page()


if __name__ == "__main__":
    main()
