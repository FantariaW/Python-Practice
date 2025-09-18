# Day 7 Training: import csv

# Day 7 Training:
import csv


class DessertReport:
    def __init__(self, dessert_lst: list):
        self.dessert_lst = dessert_lst

    def __str__(self):
        # 直接 return f"{i[0]}, {i[1]}, {i[2]}" 的話，只能打印出第一行數據
        result = []
        total = 0
        for i in self.dessert_lst:
            total += 1
            result.append(f"{total}.{i[0]} - {i[1]} - {i[2]}")
        return "\n".join(result)

    @classmethod
    def main_page(cls, prompt_choice):
        print("==🍰我的甜點清單系統🍰==")
        while True:
            try:
                print("1.Add Dessert\n2.View Dessert\n3.Exit")
                user_choice = input(prompt_choice).strip()

                match user_choice.lower():
                    case "1":
                        cls.add_dessert("Dessert: ",
                                        "Category(cake/cookie/pudding): ",
                                        "Sweetness(1~5): ")
                    case "2":
                        cls.view_dessert()
                    case "3":
                        print("Bye Bye~")
                        break
                    case _:
                        raise ValueError("Please choose 1 - 4!")
            except ValueError as e:
                print(e)

    @classmethod
    def add_dessert(cls, prompt_dessert_name: str, prompt_dessert_category: str, prompt_dessert_sweetness: str):
        print("=" * 60)
        print("==🍰Add Dessert🍰==")
        while True:
            try:
                dessert_name = input(prompt_dessert_name).strip()
                if dessert_name.lower() == "exit":
                    break
                assert dessert_name != "" and dessert_name.isalpha(), f"Dessert: '{dessert_name}' must be alphabetic!"

                while True:
                    try:
                        dessert_category = input(prompt_dessert_category).strip()
                        assert dessert_category.lower() in ["cake", "cookie", "pudding"], \
                            f"Category: '{dessert_category}' is not valid in Report!"
                        break
                    except AssertionError as e:
                        print(e)

                while True:
                    try:
                        dessert_sweetness = input(prompt_dessert_sweetness).strip()
                        assert dessert_sweetness.isdigit() and 1 <= int(dessert_sweetness) <= 5, \
                            "Sweetness must between 1~5!"
                        break
                    except AssertionError as e:
                        print(e)

                dessert_obj = dessert_name.title(), dessert_category.title(), int(dessert_sweetness)
                with open("desserts.csv", "a", newline="", encoding="utf-8") as desserts_file:
                    csv_writer = csv.writer(desserts_file)
                    csv_writer.writerow(dessert_obj)

                with open("desserts.csv", "r", encoding="utf-8") as desserts_file:
                    dessert_lst = []
                    csv_reader = csv.reader(desserts_file)
                    # 等於使用 dessert_lst = [row for row in csv_reader]
                    for row in csv_reader:
                        dessert_lst.append(row)

                    print(f"✅New Dessert: [{dessert_name}] has been Added!")
                    print("🍭 All Desserts So Far 🍭")
                    cls_dessert_lst = cls(dessert_lst)  # 等於 DessertReport(dessert_lst)
                    print(cls_dessert_lst)
                    print("=" * 60)

            except AssertionError as e:
                print(e)

    @staticmethod
    def view_dessert():
        try:
            print("=" * 60)
            with open("desserts.csv", "r", encoding="utf-8") as desserts_file:
                csv_reader = csv.reader(desserts_file)

                # 「把 csv_reader 每一行 row 都抓出來，逐一加入到一個 list 中，並存成 cls_dessert_lst」
                cls_dessert_lst = [row for row in csv_reader]
                print(DessertReport(cls_dessert_lst).__str__())
                print("=" * 60)
        except FileNotFoundError:
            print("'desserts.csv' Not Found, Please choose 1 to create a file!")
            return


def main():
    DessertReport.main_page("-> ")


if __name__ == "__main__":
    main()
