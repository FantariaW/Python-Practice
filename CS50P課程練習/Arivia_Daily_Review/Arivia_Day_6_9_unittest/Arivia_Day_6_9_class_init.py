# Day 6 Training: class, __init__

# Day 6 Training:
class BookLibrary:
    def __init__(self, book_name: str, book_author: str, book_pages: int):
        self.book_name = book_name
        self.book_author = book_author
        self.book_pages = book_pages

    def __str__(self):
        return f"📘- 《{self.book_name}》 by {self.book_author} - {self.book_pages} pages."

    @staticmethod
    def is_text(value):
        return value != "" and value.isalpha()

    @staticmethod
    def is_num(value):
        try:
            value = int(value)
            return isinstance(value, int) and int(value) > 0
        except ValueError:
            return False

    @classmethod
    def get_prompt(cls, prompt_book_info: str):
        book_lst = []
        max_book_record = 5

        print("== 📚 Book Library Management ==")
        print("📕-Please enter book name, author and pages('done' to stop, up to 5 books!):")
        while len(book_lst) < max_book_record:
            try:
                book_info = input(prompt_book_info).strip()
                if book_info.lower() == 'done':
                    break

                new_book_info = book_info.split(",")
                # 如果不用if檢測是否輸入了3個值，系統會識別不出，產生錯誤
                if len != 3:
                    raise ValueError("3 Values needed!")

                book_name, book_author, book_pages = new_book_info
                assert cls.is_text(book_name), f"Book: {book_name} should be alphabetic value!"
                assert cls.is_text(book_author), f"Author: {book_author} should be alphabetic value!"
                assert cls.is_num(book_pages), f"Page amount: {book_pages} must be positive number!"

                new_book_info = cls(book_name.title(), book_author.title(), int(book_pages))
                book_lst.append(new_book_info)
            except (ValueError, AssertionError) as e:
                print(e)

        return book_lst


def main():
    book_lst = BookLibrary.get_prompt("Book📕-> ")

    for book in book_lst:
        print(book.__str__())  # 等於 print(book), python自動執行了 def __str__()


if __name__ == "__main__":
    main()
