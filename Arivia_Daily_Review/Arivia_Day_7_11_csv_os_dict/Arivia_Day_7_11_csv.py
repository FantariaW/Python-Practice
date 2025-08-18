# Day 7 Training: import csv, encapsulation

# Day 7 Training:
import csv
import os


class BookRecorder:
    def __init__(self, book_lst: list):
        self.book_lst = book_lst

    def __str__(self):
        result = []

        for index, row in enumerate(self.book_lst, 0):
            title = row["title"]
            author = row["author"]
            genre = row["genre"]
            read = row["read"]

            result.append(
                f"{index}."
                f"Title: {title.title()} | "
                f"Author: {author.title()} | "
                f"Genre: {genre.title()} | "
                f"Read: {read.title()}")
        return "\n".join(result)

    @staticmethod
    def read_update_file():
        book_lst = []

        try:
            with open("books.csv", "r", encoding="utf-8") as books_file:
                csv_reader = csv.reader(books_file)
                for row in csv_reader:
                    book_dict = {
                        "title": row[0],
                        "author": row[1],
                        "genre": row[2],
                        "read": row[3]
                    }
                    book_lst.append(book_dict)
                # updated_book_lst = BookRecorder(book_lst)
                return book_lst
        except FileNotFoundError:
            print("📂File Not Found...")
            return

    @staticmethod
    def append_file(book_dict):
        with open("books.csv", "a", newline="", encoding="utf-8") as books_file:
            csv_dict_writer = csv.DictWriter(books_file, fieldnames=["title", "author", "genre", "read"])
            if not os.path.exists("books.csv") or os.stat("books.csv").st_size == 0:
                csv_dict_writer.writeheader()
            csv_dict_writer.writerow(book_dict)

    @staticmethod
    def main_page(prompt_choice="-> "):
        while True:
            try:
                print("==📘Book Recorder📘==")
                print("1.Add Book\n2.View Book\n3.Mark as Read\n4.Exit")
                user_choice = input(prompt_choice).strip()

                match user_choice.lower():
                    case "1":
                        BookRecorder.add_book("Book Name: ",
                                              "Book Author: ",
                                              "Book Genre(Fiction/Science/Biography): ",
                                              "Book Read Status(Yes/No): ")
                    case "2":
                        BookRecorder.view_book()
                    case "3":
                        BookRecorder.mark_book()
                    case "4":
                        updated_book_lst = BookRecorder(BookRecorder.read_update_file())
                        print(updated_book_lst.__str__())
                        print("Bye Bye~")
                        break
                    case _:
                        raise ValueError("Please enter 1 - 4.")
            except ValueError as e:
                print(e)

    @classmethod
    def add_book(cls, prompt_title: str, prompt_author: str, prompt_genre: str, prompt_read: str):
        print("==📘Add Book📘==")
        while True:
            try:
                book_title = input(prompt_title).strip()
                assert book_title != "", "Please enter Book Name."
                if book_title.lower() == 'exit':
                    return

                while True:
                    try:
                        book_author = input(prompt_author).strip()
                        assert book_author != "", "Please enter Author."
                        break
                    except AssertionError as e:
                        print(e)
                while True:
                    try:
                        book_genre = input(prompt_genre).strip()
                        assert book_genre.lower() in ["fiction", "science", "biography"], "Please 1 of 3 types."
                        break
                    except AssertionError as e:
                        print(e)
                while True:
                    try:
                        book_read = input(prompt_read).strip()
                        assert book_read.lower() in ["yes", "no"], "Please enter Yes or No."
                        break
                    except AssertionError as e:
                        print(e)

                book_dict = {
                    "title": book_title.title(),
                    "author": book_author.title(),
                    "genre": book_genre.title(),
                    "read": book_read.title()
                }
                cls.append_file(book_dict)
                cls_book_lst = cls(cls.read_update_file())
                print(cls_book_lst.__str__())
            except AssertionError as e:
                print(e)

    @staticmethod
    def view_book():
        print("==📘View Book📘==")
        cls_book_lst = BookRecorder(BookRecorder.read_update_file())
        print(cls_book_lst.__str__())

    # 2.要處理更改文件内容，并且更新更改後的cls物件的函數
    @classmethod
    def mark_book(cls, prompt_book_num="Book ID: "):
        print("==📘Mark Book as Read📘==")
        new_book_lst = cls.read_update_file()

        while True:
            try:
                book_num = input(prompt_book_num).strip()
                if book_num.lower() == 'exit':
                    return

                assert book_num.isdigit() and 1 <= int(book_num) <= len(new_book_lst), "Book ID Not Exist."
                new_book_lst[int(book_num) - 1]["read"] = "Yes"

                with open("books.csv", "w", newline="", encoding="utf-8") as books_file:
                    csv_writer = csv.DictWriter(books_file, fieldnames=["title", "author", "genre", "read"])
                    for row in new_book_lst:
                        csv_writer.writerow(row)
                updated_book_lst = BookRecorder(BookRecorder.read_update_file())
                print(updated_book_lst.__str__())
            except (IndexError, AssertionError) as e:
                print(e)


def main():
    BookRecorder.main_page()


if __name__ == "__main__":
    main()
