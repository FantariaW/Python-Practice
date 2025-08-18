# Day 7 Training: open()

# Day 7 Training
class SnackTracker:
    def __init__(self, snack_name: str, snack_brand: str, snack_status="Uneaten"):
        self.snack_name = snack_name
        self.snack_brand = snack_brand
        self.snack_status = snack_status

    def __str__(self):
        return f"{self.snack_name} by {self.snack_brand} -- {self.snack_status}!"

    @classmethod
    def main_page(cls, prompt_choice: str):
        print("==🍬Snack Tracker Menu🍬==")
        print("Type in 1-4 to manage Snack Tracker")
        while True:
            try:
                print("1.Add Snack\n2.View Snack\n3.Mark as Eaten\n4.Exit")
                choice = input(prompt_choice).strip()
                match choice.lower():
                    case "1":
                        cls.add_snack("Snack -> ")
                    case "2":
                        cls.view_snack()
                    case "3":
                        cls.mark_snack("Choose -> ")
                    case "4":
                        print("Exit!")
                        break
                    case _:
                        raise AssertionError("Type in 1-4 to start Program!")
            except AssertionError as e:
                print(e)

    @classmethod
    def add_snack(cls, prompt_snack_info: str):
        print("==🍬Adding Snack🍬==")
        print("Please type in snack name and brand: ")
        while True:
            try:
                snack_info = input(prompt_snack_info).strip()
                if snack_info.lower() in ["4", "exit"]:
                    return
                assert snack_info != "", f"Snack can't be empty!"

                snack_name, snack_brand = snack_info.split(",")
                snack_obj = cls(snack_name.strip().title(), snack_brand.strip().title())

                try:
                    with open("snacks.txt", "r", encoding="utf-8") as snacks_file:
                        lines = snacks_file.readlines()
                        total = len(lines) + 1
                except FileNotFoundError:
                    total = 1
                    print("File Not Found, New 'snacks.txt' Created!")

                with open("snacks.txt", "a", encoding="utf-8") as snacks_file:
                    snacks_file.write(f"{total}.[🍬] {snack_obj.__str__()}\n")
                    print(f"✅ Added [{snack_name.strip().title()} by {snack_brand.strip().title()}]")
            except (ValueError, AssertionError) as e:
                print(e)

    @staticmethod
    def view_snack():
        print("==🍬Snack List🍬==")
        try:
            with open("snacks.txt", "r", encoding="utf-8") as snacks_file:
                lines = snacks_file.readlines()
                for line in lines:
                    print(line, end="")
        except FileNotFoundError as e:
            print(e)

    @classmethod
    def mark_snack(cls, prompt_snack_num):
        try:
            with open("snacks.txt", "r", encoding="utf-8") as snacks_file:
                lines = snacks_file.readlines()
        except FileNotFoundError as e:
            print(e)

        print("==🍬Mark Snack as Eaten🍬==")
        print("Mark snack as eaten by type in series number of snack")
        while True:
            try:
                snack_num = input(prompt_snack_num).strip()
                if snack_num.lower() == "exit":
                    return
                assert snack_num.isdigit() and int(snack_num) < len(lines) + 1, "Snack Number Not Exist!"

                for index, line in enumerate(lines):
                    if index == int(snack_num) - 1:
                        new_snack_obj = line.split("] ")[1]
                        new_snack_name, new_brand_status = new_snack_obj.split(" by ")
                        new_snack_brand, new_snack_status = new_brand_status.split(" -- ")

                        new_snack_status = "Eaten"
                        new_snack_info = cls(new_snack_name, new_snack_brand, new_snack_status)
                        # 先把對應的這行改寫！！！
                        lines[int(snack_num) - 1] = f"{snack_num}.[😋] {new_snack_info.__str__()}\n"
                # 然後再把改寫完成後的txt文件重新覆寫！！！
                with open("snacks.txt", "w", encoding="utf-8") as snacks_file:
                    for line in lines:
                        snacks_file.write(line)
                with open("snacks.txt", "r", encoding="utf-8") as snacks_file:
                    lines = snacks_file.readlines()
                    for line in lines:
                        print(line, end="")
            except AssertionError as e:
                print(e)


def main():
    SnackTracker.main_page("Choose -> ")


if __name__ == "__main__":
    main()
