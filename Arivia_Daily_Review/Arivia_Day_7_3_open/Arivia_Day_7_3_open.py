# Day 7 Training: open()

# Day 7 Training
class BookTracker:
    def __init__(self, book_name: str, book_author: str, read_status="Unread..."):
        self.book_name = book_name
        self.book_author = book_author
        self.read_status = read_status

    def __str__(self):
        return f"{self.book_name} by {self.book_author} -- {self.read_status}"

    @classmethod
    def add_book(cls, prompt_book_info: str):
        print("==🖊️Adding Books and Authors🖊️==")
        while True:
            try:
                user_input = input(prompt_book_info).strip()
                if user_input.lower() == 'exit':
                    return

                new_book_name, new_book_author = user_input.split(",")
                new_obj = cls(new_book_name, new_book_author)

                # 我們需要先 閲讀 這個文件的 行數，才能告訴程序要把 新的輸入值 加在哪裏
                try:
                    with open("books.txt", "r", encoding="utf-8") as books_file:
                        lines = books_file.readlines()
                        # 因爲要寫入新的行數，需要多加 1 行，否則會寫入同等與目前 行數的數字 了
                        total = len(lines) + 1
                except FileNotFoundError as e:
                    # 因爲剛開始文件沒有行數，需要等於 1
                    total = 1
                    print(e)

                with open("books.txt", "a", encoding="utf-8") as books_file:
                    books_file.write(f"{total}.[📖] {new_obj.__str__()}\n")
            except (ValueError, AssertionError) as e:
                print(e)

    @staticmethod
    def view_book():
        try:
            with open("books.txt", "r", encoding="utf-8") as books_file:
                lines = books_file.readlines()
                for line in lines:
                    print(line, end="")
        except FileNotFoundError as e:
            print(e)

    @classmethod
    def mark_book(cls, prompt_book_num):
        print("==🧮Mark as read by typing series number of book🧮==")
        # 先閲讀文件的 行數，才能定義接下來 輸入的數字 是否在 行數 範圍内
        try:
            with open("books.txt", "r", encoding="utf-8") as books_file:
                # 定義全部行
                lines = books_file.readlines()
        except FileNotFoundError as e:
            print(e)

        while True:
            try:
                new_book_num = input(prompt_book_num).strip()
                if new_book_num.lower() == 'exit':
                    return
                assert new_book_num.isdigit() and int(new_book_num) < len(lines) + 1, f"Series: {new_book_num} not Exist!"

                for index, line in enumerate(lines):
                    if index == int(new_book_num) - 1:
                        # 先分割[📖], 拿到 "[{self.book_name} by {self.book_author} -- {self.read_status}]"
                        new_line = line.split("] ")[1].strip()
                        # 分割含有 by: "[{self.book_name}", "{self.book_author} -- {self.read_status}]"
                        new_book_name, new_author_status = new_line.split(" by ")
                        new_book_author, new_status = new_author_status.split("--")
                        new_status = "Read!"
                        mark_obj = cls(new_book_name.strip(), new_book_author.strip(), new_status)
                        # 先把對應的這行改寫！！！
                        lines[int(new_book_num) - 1] = f"{new_book_num}.[✅] {mark_obj.__str__()}\n"
                # 然後再把改寫完成後的txt文件重新覆寫！！！
                with open("books.txt", "w", encoding="utf-8") as books_file:
                    for line in lines:
                        books_file.write(line)
                with open("books.txt", "r", encoding="utf-8") as books_file:
                    lines = books_file.readlines()
                    for line in lines:
                        print(line, end="")
            except AssertionError as e:
                print(e)

    @classmethod
    def main_page(cls, prompt_choice: str):
        print("==📚The Book Shelf📚==")
        print("Type in 1-4 to manage book shelf")
        while True:
            print("1.Add Book\n2.View Book\n3.Mark as Read\n4.Exit")
            try:
                user_choice = input(prompt_choice).strip()
                match user_choice.lower():
                    case "1":
                        cls.add_book("Book Info -> ")
                    case "2":
                        cls.view_book()
                    case "3":
                        cls.mark_book("Series Number -> ")
                    case "4" | "exit":
                        print("Exit!!!")
                        break
                    case _:
                        raise ValueError("Choose 1 - 4 to start program")
            except ValueError as e:
                print(e)


def main():
    BookTracker.main_page("Choose -> ")


if __name__ == "__main__":
    main()
