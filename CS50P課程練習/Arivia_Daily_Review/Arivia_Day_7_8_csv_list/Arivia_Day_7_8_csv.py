# Day 7 Training: import csv

# Day 7 Training:
import csv


class BirdWatcher:
    def __init__(self, bird_lst: list):
        self.bird_lst = bird_lst

    def __str__(self):
        result = []
        total = 0
        for i in self.bird_lst:
            total += 1
            result.append(f"{total}.{i[0]} - {i[1]} - {i[2]} - {i[3]}")
        return "\n".join(result)

    @classmethod
    def main_page(cls, prompt_choice):
        while True:
            try:
                print("==🐦Bird Record Diary🐦==")
                print("1.Add Bird\n2.View Bird\n3.Mark as Photographed\n4.Exit")
                user_choice = input(prompt_choice).strip()

                match user_choice.lower():
                    case "1":
                        cls.add_bird("Bird Name: ",
                                     "Bird Type(Terrestrial/Waterfowl/Raptor): ",
                                     "Bird Found Location: ",
                                     "Photographed Status(Yes/No): ")
                    case "2":
                        cls.view_bird()
                    case "3":
                        cls.mark_photo("Series Number of Bird -> ")
                    case "4":
                        print("Bye Bye~")
                        break
                    case _:
                        raise ValueError("Please choose 1 - 4")
            except ValueError as e:
                print(e)

    @classmethod
    def add_bird(cls, prompt_bird_name: str, prompt_bird_type, prompt_bird_location, prompt_photographed):
        print("==🐦Add Bird🐦==")
        while True:
            try:
                bird_name = input(prompt_bird_name).strip()
                if bird_name.lower() == 'exit':
                    return
                while True:
                    try:
                        bird_type = input(prompt_bird_type).strip()
                        assert bird_type.lower() in ["terrestrial", "waterfowl", "raptor"], "Please enter 1 of 3 types!"
                        break
                    except AssertionError as e:
                        print(e)

                while True:
                    try:
                        bird_location = input(prompt_bird_location).strip()
                        break
                    except ValueError as e:
                        print(e)

                while True:
                    try:
                        photograph_status = input(prompt_photographed).strip()
                        assert photograph_status.lower() in ["yes", "no"], "Please enter Yes or No!"
                        break
                    except AssertionError as e:
                        print(e)

                bird_obj = bird_name.title(), bird_type.title(), bird_location.title(), photograph_status.title()
                with open("birds.csv", "a", newline="", encoding="utf-8") as birds_file:
                    csv_writer = csv.writer(birds_file)
                    csv_writer.writerow(bird_obj)
                    print("🐦New Bird has been recorded!✅")

                try:
                    with open("birds.csv", "r", encoding="utf-8") as birds_file:
                        bird_lst = []

                        csv_reader = csv.reader(birds_file)
                        for row in csv_reader:
                            bird_lst.append(row)

                        print("🐦All birds so far: ")
                        cls_bird_lst = cls(bird_lst)
                        print(cls_bird_lst.__str__())
                except FileNotFoundError:
                    print("📂File Not Found, New File Created!")
            except (AssertionError, FileNotFoundError) as e:
                print(e)

    @staticmethod
    def view_bird():
        try:
            print("==🐦Bird List🐦==")
            with open("birds.csv", "r", encoding="utf-8") as birds_file:
                result = []
                csv_reader = csv.reader(birds_file)
                for row in csv_reader:
                    result.append(row)

                print(BirdWatcher(result).__str__())

        except FileNotFoundError:
            print("📂File Not Found, Please Add a New Bird!")
            return

    @classmethod
    def mark_photo(cls, prompt_num):
        print("==🐦Mark Bird as Photographed🐦==")
        while True:
            mark_lst = []
            series_num = 0
            try:
                with open("birds.csv", "r", encoding="utf-8") as birds_file:
                    csv_reader = csv.reader(birds_file)
                    for row in csv_reader:
                        series_num += 1
                        mark_lst.append(row)
            except FileNotFoundError:
                print("📂File Not Found, Please Add a New Bird!")

            try:
                # 判斷 用戶輸入的行數 是否對應 文件行數，然後更改 對應行數的數據 Yes
                user_num = input(prompt_num).strip()
                if user_num.lower() == 'exit':
                    return
                assert user_num.isdigit() and 1 <= int(user_num) <= series_num, "Number must between length of List!"

                mark_lst[int(user_num) - 1][3] = "Yes"
                with open("birds.csv", "w", newline="", encoding="utf-8") as birds_file:
                    csv_writer = csv.writer(birds_file)
                    for row in mark_lst:
                        csv_writer.writerow(row)
                    print(f"✅Mark as Photographed! - > {mark_lst[int(user_num) - 1]}")

                # 打印出更改後的數據
                with open("birds.csv", "r", encoding="utf-8") as birds_file:
                    bird_lst = []

                    csv_reader = csv.reader(birds_file)
                    for row in csv_reader:
                        bird_lst.append(row)

                    cls_bird_lst = cls(bird_lst)
                    print(cls_bird_lst.__str__())

            except AssertionError as e:
                print(e)


def main():
    BirdWatcher.main_page("-> ")


if __name__ == "__main__":
    main()
