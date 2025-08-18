# Day 7 Training: import csv, encapsulation

# Day 7 Training:
import csv
import os


class DramaTracker:
    def __init__(self, drama_lst: list):
        self.drama_lst = drama_lst

    def __str__(self):
        result = []

        for index, row in enumerate(self.drama_lst, 0):
            title = row["title"]
            genre = row["genre"]
            episode = row["episode"]
            status = row["status"]

            result.append(f"{index}.{title.title()} | "
                          f"{genre.title()} | "
                          f"{episode.title()} | "
                          f"{status.title()}")
        return "\n".join(result)

    @staticmethod
    def prompt_validation(prompt_msg, assertion_msg, error_msg, allow_exit=False):
        while True:
            try:
                user_input = input(prompt_msg).strip()
                if allow_exit is True and user_input.lower() == 'exit':
                    # ✔️ return None 是 Python 裡最常見的「中止輸入流程」寫法，更清晰也更專業。
                    return None
                assert assertion_msg(user_input), error_msg
                return user_input
            except AssertionError as e:
                print(e)

    @staticmethod
    def read_file():
        try:
            with open("dramas.csv", "r", encoding="utf-8") as dramas_f:
                # 固定返回list！！！并且明确指定字段名，不依赖文件标题行
                return list(csv.DictReader(dramas_f, fieldnames=["title", "genre", "episode", "status"]))
        except FileNotFoundError:
            print("📂File Not Found...")
            return []

    @staticmethod
    def append_file(drama_dict):
        with open("dramas.csv", "a", newline="", encoding="utf-8") as dramas_f:
            csv_writer = csv.DictWriter(dramas_f, fieldnames=["title", "genre", "episode", "status"])
            if not os.path.exists("dramas.csv") or os.stat("dramas.csv").st_size == 0:
                csv_writer.writeheader()
            csv_writer.writerow(drama_dict)

    @staticmethod
    def write_file(drama_lst):
        with open("dramas.csv", "w", newline="", encoding="utf-8") as drama_f:
            csv_writer = csv.DictWriter(drama_f, fieldnames=["title", "genre", "episode", "status"])
            csv_writer.writerows(drama_lst)

    @staticmethod
    def main_page(prompt_choice="-> "):
        while True:
            try:
                print("==📺Drama List Tracker📺==")
                print("1.Add Drama\n2.View Drama\n3.Mark Drama as Watched\n4.Exit")

                user_choice = input(prompt_choice).strip()
                match user_choice.lower():
                    case "1":
                        DramaTracker.add_drama()
                    case "2":
                        DramaTracker.view_drama()
                    case "3":
                        DramaTracker.mark_drama()
                    case "4":
                        print("Bye Bye~")
                        break
                    case _:
                        raise ValueError("Please choose 1 - 4")
            except ValueError as e:
                print(e)

    @classmethod
    def add_drama(cls,
                  prompt_drama="Drama Name: ",
                  prompt_genre="Drama Genre(Mystery/Romance/Comedy/Documentary): ",
                  prompt_episode="Drama Episode: ",
                  prompt_status="Drama Watch Status(Yes/No): "):
        print("==📺Add Drama📺==")

        while True:
            try:
                drama_title = cls.prompt_validation(
                    prompt_drama,
                    lambda d: d != "",
                    "Please enter Drama Name.",
                    allow_exit=True
                )
                if drama_title is None:
                    return

                drama_genre = cls.prompt_validation(
                    prompt_genre,
                    lambda g: g.lower() in ["mystery", "romance", "comedy", "documentary"],
                    "Please enter 1 of 4 Genres."
                )

                drama_episode = cls.prompt_validation(
                    prompt_episode,
                    lambda e: e.isdigit() and 1 <= int(e),
                    "Episode must be Positive Numeric Value."
                )

                drama_status = cls.prompt_validation(
                    prompt_status,
                    lambda s: s.lower() in ["yes", "no"],
                    "Please enter Yes or No."
                )

                drama_dict = {
                    "title": drama_title.title(),
                    "genre": drama_genre.title(),
                    "episode": drama_episode.title(),
                    "status": drama_status.title()
                }
                cls.append_file(drama_dict)

                drama_lst = cls.read_file()
                cls_drama_lst = cls(drama_lst)
                print(cls_drama_lst.__str__())
            except ValueError:
                print("Something Error...")

    @staticmethod
    def view_drama():
        print("==📺View Drama📺==")
        cls_drama_lst = DramaTracker(DramaTracker.read_file())
        print(cls_drama_lst.__str__())

    @staticmethod
    def mark_drama():
        drama_lst = DramaTracker.read_file()
        if not drama_lst:
            return
        print("==📺Mark Drama as Watched📺==")
        while True:
            try:
                drama_id = DramaTracker.prompt_validation(
                    "Drama ID: ",
                    lambda i: i != "" and 1 <= int(i) <= len(drama_lst),
                    "Drama ID Not Exist...",
                    allow_exit=True
                )
                if drama_id is None:
                    return

                drama_lst[int(drama_id)]["status"] = "Yes"
                DramaTracker.write_file(drama_lst)
            except (IndexError, ValueError):
                print("Drama ID Not Exist...")


def main():
    DramaTracker.main_page()


if __name__ == "__main__":
    main()
