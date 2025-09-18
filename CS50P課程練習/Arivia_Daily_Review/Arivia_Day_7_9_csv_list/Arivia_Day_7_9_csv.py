# Day 7 Training: import csv, encapsulation

# Day 7 Training:
import csv


class GameLog:
    def __init__(self, games_lst: list):
        self.games_lst = games_lst

    def __str__(self):
        result = []
        total = 0

        for i in self.games_lst:
            total += 1
            match i[3].lower():
                case "yes":
                    result.append(f"{total}.{i[0]} | {i[1]} | {i[2]} | {i[3]} | ✅")
                case "no":
                    result.append(f"{total}.{i[0]} | {i[1]} | {i[2]} | {i[3]} | ❌")
        return "\n".join(result)

    @staticmethod
    def read_update_file():
        try:
            with open("games.csv", "r", encoding="utf-8") as games_file:
                result = []
                csv_reader = csv.reader(games_file)
                for row in csv_reader:
                    result.append(row)
                # 包含更新數據
                cls_result = GameLog(result)
                return cls_result.__str__()
        except FileNotFoundError:
            print("📂File Not Found!")

    @staticmethod
    def append_file(value):
        with open("games.csv", "a", newline="", encoding="utf-8") as games_file:
            csv_writer = csv.writer(games_file)
            csv_writer.writerow(value)

    @staticmethod
    def write_file(value):
        with open("games.csv", "w", newline="", encoding="utf-8") as games_file:
            csv_writer = csv.writer(games_file)
            csv_writer.writerow(value)

    @staticmethod
    def mark_file():
        while True:
            result = []
            total_id = 0

            try:
                with open("games.csv", "r", encoding="utf-8") as games_file:
                    csv_reader = csv.reader(games_file)
                    for row in csv_reader:
                        total_id += 1
                        result.append(row)
            except FileNotFoundError:
                print("📂File Not Found!")

            try:
                value_id = input("Game Series ID: ").strip()
                if value_id.lower() == "exit":
                    return
                assert value_id.isdigit() and int(value_id) <= total_id, "Game ID Not Exist!"

                result[int(value_id) - 1][3] = "Yes"
                with open("games.csv", "w", newline="", encoding="utf-8") as games_file:
                    csv_writer = csv.writer(games_file)
                    for row in result:
                        csv_writer.writerow(row)

                print(f"✅-{result[int(value_id) - 1][0]} Marked as Completed!")
                print(GameLog.read_update_file())
            except AssertionError as e:
                print(e)

    @classmethod
    def main_page(cls, prompt_choice="-> "):
        while True:
            try:
                print("==🎮Game Log Recorder🎮==")
                print("1.Add Record\n2.View Record\n3.Mark as Complete\n4.Exit")

                user_choice = input(prompt_choice).strip()
                match user_choice.lower():
                    case "1":
                        cls.add_game("Game Name: ",
                                     "Game Platform(PC/Switch/PS5): ",
                                     "Game Rate(1 ~ 10): ",
                                     "Game Complete(Yes/No)")
                    case "2":
                        cls.view_game()
                    case "3":
                        cls.mark_complete()
                    case "4":
                        print("Bye Bye~")
                        break
                    case _:
                        raise ValueError("Please choose 1 - 4")
            except ValueError as e:
                print(e)

    @classmethod
    def add_game(cls, prompt_game_name, prompt_game_platform, prompt_game_rate, prompt_game_complete):
        print("==🎮Add Game🎮==")
        while True:
            try:
                game_name = input(prompt_game_name).strip()
                if game_name.lower() == 'exit':
                    return

                while True:
                    try:
                        game_platform = input(prompt_game_platform).strip()
                        assert game_platform.lower() in ["pc", "switch", "ps5"], "Please enter 1 of 3 Platforms!"
                        break
                    except AssertionError as e:
                        print(e)

                while True:
                    try:
                        game_rate = input(prompt_game_rate).strip()
                        assert game_rate.isdigit() and 1 <= int(game_rate) <= 10, "Rate must between 1 - 10!"
                        break
                    except AssertionError as e:
                        print(e)
                while True:
                    try:
                        game_complete = input(prompt_game_complete).strip()
                        assert game_complete.lower() in ["yes", "no"], "Please enter Yes or No!"
                        break
                    except AssertionError as e:
                        print(e)

                game_obj = game_name.title(), game_platform.title(), game_rate.title(), game_complete.title()
                GameLog.append_file(game_obj)
                print(f"✅-Added {game_name.title()}!")
                GameLog.read_update_file()
            except ValueError:
                print("")

    @staticmethod
    def view_game():
        print("==🎮Game List🎮==")
        print(GameLog.read_update_file())

    @staticmethod
    def mark_complete():
        print("==🎮Mark Game as Complete🎮==")
        GameLog.mark_file()


def main():
    GameLog.main_page()


if __name__ == "__main__":
    main()
