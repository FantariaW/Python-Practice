# Day 8 Training: regex, csv

# Day 8 Training:
import csv
import os
import re


class DessertPlanet:
    def __init__(self, dessert_lst: list):
        self.dessert_lst = dessert_lst

    def __str__(self):
        result_lst = []

        for index, row in enumerate(self.dessert_lst, 0):
            nickname = row["nickname"]
            flavor_code = row["flavor"]
            sugar_level = row["sugar"]
            secret_pass = row["password"]
            dessert_type = row["type"]

            result_lst.append(f"{index}."
                              f"{nickname} | "
                              f"{flavor_code} | "
                              f"{sugar_level} | "
                              f"{secret_pass} | "
                              f"{dessert_type}.")
        return "\n".join(result_lst)

    @staticmethod
    def prompt_validate(prompt_msg, msg_validate, error_msg, allow_exit=False):
        while True:
            try:
                user_input = input(prompt_msg).strip()
                if allow_exit is True and user_input.lower() == 'exit':
                    return None
                assert msg_validate(user_input), error_msg
                return user_input
            except AssertionError as e:
                print(e)

    @staticmethod
    def read_file():
        try:
            with open("dessert_passport.csv", "r", encoding="utf-8") as dessert_f:
                # 直接 return 就可以了，不需要另外定義值
                return list(csv.DictReader(dessert_f, fieldnames=["nickname", "flavor", "sugar", "password", "type"]))
        except FileNotFoundError:
            print("📂File Not Found...")

    @staticmethod
    def append_file(dessert_dict):
        with open("dessert_passport.csv", "a", newline="", encoding="utf-8") as dessert_f:
            csv_writer = csv.DictWriter(dessert_f, fieldnames=["nickname", "flavor", "sugar", "password", "type"])
            if not os.path.exists("dessert_passport.csv") or os.stat("dessert_passport.csv").st_size == 0:
                csv_writer.writeheader()
            csv_writer.writerow(dessert_dict)

    @staticmethod
    def write_file(dessert_lst):
        with open("dessert_passport.csv", "w", newline="", encoding="utf-8") as dessert_f:
            csv_writer = csv.DictWriter(dessert_f, fieldnames=["nickname", "flavor", "sugar", "password", "type"])
            csv_writer.writerows(dessert_lst)

    @classmethod
    def main_page(cls, prompt_choice="-> "):
        while True:
            try:
                print("==🍰Welcome to Dessert Planet Entry System🌎==")
                print("1.Submit New Dessert Entry\n"
                      "2.View All Accepted Entries\n"
                      "3.Update Sugar Level\n"
                      "4.Exit")

                user_choice = input(prompt_choice).strip()
                match user_choice.lower():
                    case "1":
                        cls.new_dessert()
                    case "2":
                        cls.view_dessert()
                    case "3":
                        cls.update_dessert_sugar()
                    case "4":
                        print("Bye Bye~")
                        break
                    case _:
                        raise ValueError("Please choose 1 - 4.")
            except ValueError as e:
                print(e)

    @classmethod
    def new_dessert(cls,
                    prompt_nickname="Dessert Nickname(3 characters at least): ",
                    prompt_flavor_code="Flavor Code(FLV-000): ",
                    prompt_sugar_level="Sugar Level(1-100): ",
                    prompt_secret_pass="Password(6-10 characters): ",
                    prompt_type="Dessert Type(Cake/Pie/Pudding/Icecream): "):
        print("==🍰Submit New Dessert🌎==")
        while True:
            try:
                nickname = cls.prompt_validate(
                    prompt_nickname,
                    lambda n: re.search(r"^[A-Za-z]{3,}$", n),
                    "Invalid Name Format.",
                    allow_exit=True
                )
                if nickname is None:
                    return

                flavor_code = cls.prompt_validate(
                    prompt_flavor_code,
                    lambda f_c: re.search(r"^FLV-\d{3}$", f_c),
                    "Invalid Code."
                )

                sugar_level = cls.prompt_validate(
                    prompt_sugar_level,
                    lambda s_l: 1 <= int(s_l) <= 100,
                    "Sugar Level must between 1 - 100."
                )

                secret_pass = cls.prompt_validate(
                    prompt_secret_pass,
                    lambda s_p: re.search(r"^\S{6,10}$", s_p),
                    "Password Format Invalid."
                )

                dessert_type = cls.prompt_validate(
                    prompt_type,
                    lambda t: t.lower() in ["cake", "pie", "pudding", "icecream"],
                    "Please choose 1 of 4 types."
                )

                dessert_dict = {
                    "nickname": nickname.title(),
                    "flavor": flavor_code,
                    "sugar": sugar_level,
                    "password": secret_pass,
                    "type": dessert_type.title()
                }
                cls.append_file(dessert_dict)  # 寫入文件

                dessert_lst = cls.read_file()  # 讀取文件
                cls_dessert_lst = cls(dessert_lst)
                print(cls_dessert_lst.__str__())
            except ValueError as e:
                print(e)

    @classmethod
    def view_dessert(cls):
        print("==🍰View All Dessert🌎==")
        dessert_lst = cls.read_file()
        cls_dessert_lst = cls(dessert_lst)
        print(cls_dessert_lst.__str__())

    @classmethod
    def update_dessert_sugar(cls,
                             prompt_num="Dessert Series Number: ",
                             prompt_new_sugar_level="Update New Dessert Sugar Level(1-100): "):
        dessert_lst = cls.read_file()

        while True:
            try:
                print("==🍰Update Dessert Sugar Level🌎==")

                series_num = cls.prompt_validate(
                    prompt_num,
                    lambda n: 1 <= int(n) <= len(dessert_lst) - 1,
                    "Series Number Not Exists.",
                    allow_exit=True
                )
                if series_num is None:
                    return

                new_sugar_level = cls.prompt_validate(
                    prompt_new_sugar_level,
                    lambda new_s_l: 1 <= int(new_s_l) <= 100,
                    "Sugar Level must between 1 - 100."
                )

                dessert_lst[int(series_num)]["sugar"] = int(new_sugar_level)
                cls.write_file(dessert_lst)

                new_dessert_lst = cls.read_file()
                cls_dessert_lst = cls(new_dessert_lst)
                print(cls_dessert_lst.__str__())
            except (IndexError, ValueError) as e:
                print(e)


def main():
    DessertPlanet.main_page()


if __name__ == "__main__":
    main()
