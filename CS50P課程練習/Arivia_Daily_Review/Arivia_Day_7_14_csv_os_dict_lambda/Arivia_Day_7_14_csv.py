# Day 7 Training: import csv, encapsulation, lambda

# Day 7 Training:
import csv
import os


class MusicPlayTracker:
    def __init__(self, music_lst: list):
        self.music_lst = music_lst

    def __str__(self):
        result = []

        for index, row in enumerate(self.music_lst, 0):
            title = row["title"]
            artist = row["artist"]
            genre = row["genre"]
            liked = row["liked"]

            result.append(f"{index}."
                          f"{title.title()} | "
                          f"{artist.title()} | "
                          f"{genre.title()} | "
                          f"{liked.title()}")

        return "\n".join(result)

    @staticmethod
    def prompt_validation(prompt_msg, input_validation, error_msg, allow_exit=False):
        while True:
            try:
                user_input = input(prompt_msg).strip()
                if allow_exit is True and user_input.lower() == 'exit':
                    return None
                assert input_validation(user_input), error_msg
                return user_input
            except AssertionError as e:
                print(e)

    @staticmethod
    def read_file():
        try:
            with open("playlist.csv", "r", encoding="utf-8") as playlist_f:
                return list(csv.DictReader(playlist_f, fieldnames=["title", "artist", "genre", "liked"]))
        except FileNotFoundError:
            print("📂File Not Found...")
            return []

    @staticmethod
    def append_file(music_dict):
        with open("playlist.csv", "a", newline="", encoding="utf-8") as playlist_f:
            csv_writer = csv.DictWriter(playlist_f, fieldnames=["title", "artist", "genre", "liked"])
            if not os.path.exists("playlist.csv") or os.stat("playlist.csv").st_size == 0:
                csv_writer.writeheader()
            csv_writer.writerow(music_dict)

    @staticmethod
    def write_file(music_lst):
        with open("playlist.csv", "w", newline="", encoding="utf-8") as playlist_f:
            csv_writer = csv.DictWriter(playlist_f, fieldnames=["title", "artist", "genre", "liked"])
            # writerows 自動識別 list of dict，等同於:
            # for row in music_lst:
            #     csv_writer.writerow(row)
            csv_writer.writerows(music_lst)

    @classmethod
    def main_page(cls, prompt_choice="-> "):
        while True:
            try:
                print("==🎧Music Play List🎧==")
                print("1.Add Music\n2.View Play List\n3.Mark as Favourite\n4.Exit")
                user_choice = input(prompt_choice).strip()

                match user_choice.lower():
                    case "1":
                        cls.add_music()
                    case "2":
                        cls.view_music()
                    case "3":
                        cls.mark_music()
                    case "4":
                        print("Bye Bye~")
                        break
                    case _:
                        raise ValueError("Something Error...")
            except ValueError as e:
                print(e)

    @classmethod
    def add_music(cls,
                  prompt_title="Music Name: ",
                  prompt_artist="Music Artist Name: ",
                  prompt_genre="Music Genre(Pop/Rock/Rap/Electric/Folk): ",
                  prompt_liked="Add to Favourite?(Yes/No): "):

        print("==🎧Add Music🎧==")
        while True:
            try:
                music_title = cls.prompt_validation(
                    prompt_title,
                    lambda name: name != "", "Please enter Music Name.",
                    allow_exit=True
                )
                if music_title is None:
                    return

                music_artist = cls.prompt_validation(
                    prompt_artist,
                    lambda artist: artist != "", "Please enter Artist Name."
                )

                music_genre = cls.prompt_validation(
                    prompt_genre,
                    lambda genre: genre.lower() in ["pop", "rock", "rap", "electric", "folk"],
                    "Please choose a shown Genre from list."
                )

                music_liked = cls.prompt_validation(
                    prompt_liked,
                    lambda liked: liked.lower() in ["yes", "no"],
                    "Please enter Yes or No."
                )
                
                music_dict = {
                    "title": music_title.title(),
                    "artist": music_artist.title(),
                    "genre": music_genre.title(),
                    "liked": music_liked.title()
                }
                # 寫入文件
                cls.append_file(music_dict)
                # 讀取文件， 并將文件内容轉化爲list，再以str格式輸出
                music_lst = cls.read_file()
                cls_music_lst = cls(music_lst)
                print(cls_music_lst.__str__())
            except ValueError as e:
                print(e)

    @classmethod
    def view_music(cls):
        print("==🎧Music List🎧==")
        music_lst = cls.read_file()
        cls_music_lst = cls(music_lst)
        print(cls_music_lst.__str__())

    @classmethod
    def mark_music(cls, prompt_id="Music ID: "):
        music_lst = cls.read_file()
        if not music_lst:
            return

        print("==🎧Mark Music as Favourite🎧==")
        while True:
            try:
                music_id = cls.prompt_validation(
                    prompt_id,
                    lambda i: i != "" and 1 <= int(i) <= len(music_lst), "Music ID Not Exist...",
                    allow_exit=True
                )
                if music_id is None:
                    return

                music_lst[int(music_id)]["liked"] = "Yes"
                cls.write_file(music_lst)
            except (IndexError, ValueError):
                print("Music ID Not Exist...")


def main():
    MusicPlayTracker.main_page()


if __name__ == "__main__":
    main()
