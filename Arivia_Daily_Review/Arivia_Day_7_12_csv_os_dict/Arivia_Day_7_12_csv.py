# Day 7 Training: import csv, encapsulation

# Day 7 Training:
import csv
import os


class DrinkOrder:
    def __init__(self, drink_lst: list):
        self.drink_lst = drink_lst

    def __str__(self):
        result = []

        for index, row in enumerate(self.drink_lst, 0):
            drink = row["drink"]
            size = row["size"]
            sugar = row["sugar"]
            ice = row["ice"]
            note = row["note"]
            done = row["done"]

            result.append(f"{index}.{drink.title()} | "
                          f"{size.title()} | "
                          f"{sugar.title()} | "
                          f"{ice.title()} | "
                          f"{note.title()} | "
                          f"{done.title()}")

        return "\n".join(result)

    @staticmethod
    def prompt_validation(prompt_msg, validate_function, error_msg):
        while True:
            try:
                user_input = input(prompt_msg).strip()
                assert validate_function(user_input), error_msg
                return user_input
            except AssertionError as e:
                print(e)

    @staticmethod
    def read_file():
        try:
            with open("orders.csv", "r", encoding="utf-8") as orders_file:
                # 明确指定字段名，不依赖文件标题行
                return list(csv.DictReader(orders_file, fieldnames=["drink", "size", "sugar", "ice", "note", "done"]))
        except FileNotFoundError:
            print("📂File Not Found...")
            return []

    @staticmethod
    def append_file(drink_dict):
        with open("orders.csv", "a", newline="", encoding="utf-8") as orders_file:
            csv_writer = csv.DictWriter(orders_file, fieldnames=["drink", "size", "sugar", "ice", "note", "done"])
            if not os.path.exists("orders.csv") or os.stat("orders.csv").st_size == 0:
                csv_writer.writeheader()
            csv_writer.writerow(drink_dict)

    @staticmethod
    def write_file(drink_lst):
        with open("orders.csv", "w", newline="", encoding="utf-8") as orders_file:
            csv_writer = csv.DictWriter(orders_file, fieldnames=["drink", "size", "sugar", "ice", "note", "done"])
            for row in drink_lst:
                csv_writer.writerow(row)

    @staticmethod
    def main_page(prompt_choice="-> "):
        while True:
            try:
                print("==🧋Drinks Manager🧋==")
                print("1.Add Drink\n2.View Drink\n3.Mark as Done\n4.Exit")

                user_choice = input(prompt_choice).strip()
                match user_choice.lower():
                    case "1":
                        DrinkOrder.add_drink()
                    case "2":
                        DrinkOrder.view_drink()
                    case "3":
                        DrinkOrder.mark_drink()
                    case "4":
                        print("Bye Bye~")
                        break
                    case _:
                        raise ValueError("Please choose 1 - 4.")
            except ValueError as e:
                print(e)

    @classmethod
    def add_drink(cls,
                  prompt_name="Drink Name: ",
                  prompt_size="Drink Size(S/M/L): ",
                  prompt_sugar="Drink Sweetness(Regular/Less/None): ",
                  prompt_ice="Drink Ice Level(Regular/Less/None): ",
                  prompt_note="Special Note(if any): ",
                  prompt_done="Drink Status(Yes/No): "):
        print("==🧋Add Drink🧋==")

        while True:
            try:
                drink_name = input(prompt_name).strip()
                if drink_name.lower() == 'exit':
                    return
                assert drink_name != "", "Please enter Drink Name."

                drink_size = cls.prompt_validation(
                    prompt_size,
                    lambda size: size.lower() in ["s", "m", "l"], "Please Choose 1 of 3 Sizes."
                )
                drink_sugar = cls.prompt_validation(
                   prompt_sugar,
                   lambda sugar: sugar.lower() in ["regular", "less", "none"], "Please Choose Sweetness Level."
                )
                drink_ice = cls.prompt_validation(
                    prompt_ice,
                    lambda i: i.lower() in ["regular", "less", "none"], "Please Choose Ice Level."
                )
                drink_note = cls.prompt_validation(
                    prompt_note,
                    lambda n: True, ""
                )
                drink_done = cls.prompt_validation(
                    prompt_done,
                    lambda d: d.lower() in ["yes", "no"], "Please enter Yes or No."
                )

                drink_dict = {
                    "drink": drink_name.title(),
                    "size": drink_size.title(),
                    "sugar": drink_sugar.title(),
                    "ice": drink_ice.title(),
                    "note": drink_note.title(),
                    "done": drink_done.title()
                }
                cls.append_file(drink_dict)

                drink_lst = cls.read_file()
                cls_drink_lst = cls(drink_lst)
                print(cls_drink_lst.__str__())
            except AssertionError as e:
                print(e)

    @staticmethod
    def view_drink():
        print("==🧋View Drink List🧋==")
        cls_drink_lst = DrinkOrder(DrinkOrder.read_file())
        print(cls_drink_lst.__str__())

    @staticmethod
    def mark_drink():
        print("==🧋Mark Drink as Done🧋==")
        drink_lst = DrinkOrder.read_file()

        while True:
            try:
                drink_id = input("Order Drink ID: ").strip()
                if drink_id.lower() == 'exit':
                    return
                assert drink_id.isdigit() and 1 <= int(drink_id) <= len(drink_lst), "Order ID Not Exist."

                drink_lst[int(drink_id)]["done"] = "Yes"
                DrinkOrder.write_file(drink_lst)
            except AssertionError as e:
                print(e)


def main():
    DrinkOrder.main_page()


if __name__ == "__main__":
    main()
