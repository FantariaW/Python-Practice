# Day 7 Training: import csv, encapsulation

# Day 7 Training:
import csv
import os


class HouseHoldRecord:
    def __init__(self, household_lst: list):
        self.household_lst = household_lst

    def __str__(self):
        result = []
        # ❗全新邏輯知識
        for index, item in enumerate(self.household_lst, 0):
            name = item["name"]
            category = item["category"]
            stock = item["stock"]
            urgent = item["urgent"]
            result.append(
                f"{index}.\"Name\": {name} | "
                f"\"Category\": {category} | "
                f"\"Stock\": {stock} | "
                f"\"Urgent\": {urgent}"
            )
        return "\n".join(result)

        # ❗用於臨時開發，和未知數據，以及頻繁變更内部數據的時候 才會使用，容易輸出泄露隱私數據，不是很推薦
        # for index, record in self.household_dict.items():
        #     result.append(f"{index}.")
        #     for key, value in record.items():
        #         result.append("|".join(f"\"{key.title()}\": {value}"))
        # return "\n".join(result)

    @staticmethod
    def check_file_header():
        # ❗全新邏輯知識
        try:
            with open("supplies.csv", "r", encoding="utf-8"):
                if not os.path.exists("supplies.csv") or os.stat("supplies.csv").st_size == 0:
                    write_header = True
                else:
                    write_header = False
                return write_header
        except FileNotFoundError:
            print("📂File Not Found!")

    @staticmethod
    def read_update_file():
        try:
            # ❗全新邏輯知識
            with open("supplies.csv", "r", encoding="utf-8") as supplies_file:
                result = []

                csv_reader = csv.reader(supplies_file)
                for row in csv_reader:
                    updated_file = {
                        "name": row[0],
                        "category": row[1],
                        "stock": row[2],
                        "urgent": row[3]
                    }
                    result.append(updated_file)

                cls_result = HouseHoldRecord(result)
                return cls_result.__str__()
        except FileNotFoundError:
            print("📂File Not Found!")

    @staticmethod
    def append_file(dict_value):
        # ❗全新邏輯知識
        with open("supplies.csv", "a", newline="", encoding="utf-8") as supplies_file:
            csv_writer = csv.DictWriter(supplies_file, fieldnames=["name", "category", "stock", "urgent"])

            if HouseHoldRecord.check_file_header() is True:
                csv_writer.writeheader()

            csv_writer.writerow(dict_value)

    @classmethod
    def main_page(cls, prompt_choice="-> "):
        while True:
            try:
                print("==📦Household Item Record==")
                print("1.Add Item\n2.View Item\n3.Exit")
                user_choice = input(prompt_choice).strip()

                match user_choice.lower():
                    case "1":
                        cls.add_household("Household Name: ",
                                          "Household Category(Cleaning/Food/Miscellaneous): ",
                                          "Household Stock: ",
                                          "Urgent Restocking(Yes/No): ")
                    case "2":
                        cls.view_household()
                    # case "3":
                    #     cls.mark_household()
                    case "3":
                        print(cls.read_update_file())
                        print("Bye Bye~")
                        break
                    case _:
                        raise ValueError("Please choose 1 - 4!")
            except ValueError as e:
                print(e)

    @classmethod
    def add_household(cls, prompt_name: str, prompt_category: str, prompt_stock: str, prompt_urgent: str):
        print("==📦Add Household Item==")
        while True:
            try:
                household_name = input(prompt_name).strip()
                if household_name.lower() == 'exit':
                    return
                assert household_name != "", "Please enter Household Item Name."

                while True:
                    try:
                        household_category = input(prompt_category).strip()
                        assert household_category.lower() in ['cleaning', 'food', 'miscellaneous'], \
                            "Please enter 1 of 3 types."
                        break
                    except AssertionError as e:
                        print(e)
                while True:
                    try:
                        household_stock = input(prompt_stock).strip()
                        assert household_stock.isdigit() and 0 <= int(household_stock), "Please enter positive value."
                        break
                    except AssertionError as e:
                        print(e)
                while True:
                    try:
                        household_urgent = input(prompt_urgent).strip()
                        assert household_urgent.lower() in ["yes", "no"], "Please enter Yes or No."
                        break
                    except AssertionError as e:
                        print(e)

                household_dict = {
                    "name": household_name.title(),
                    "category": household_category.title(),
                    "stock": int(household_stock),
                    "urgent": household_urgent.title()
                }
                cls.append_file(household_dict)
                print(cls.read_update_file())
            except AssertionError as e:
                print(e)

    @staticmethod
    def view_household():
        print(HouseHoldRecord.read_update_file())


def main():
    HouseHoldRecord.main_page()


if __name__ == "__main__":
    main()
