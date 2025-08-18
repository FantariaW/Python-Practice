import unittest

from Arivia_Day_6_9_class_init import BookLibrary


class TestBookLibrary(unittest.TestCase):
    def test_init(self):
        book = BookLibrary("book - 1", "book 1 writer", 100)
        self.assertEqual(book.book_name, "book - 1")
        self.assertEqual(book.book_author, "book 1 writer")
        self.assertEqual(book.book_pages, 100)

    def test_is_text(self):
        self.assertTrue(BookLibrary.is_text("FairyTale"))  # True
        self.assertFalse(BookLibrary.is_text(""))
        self.assertFalse(BookLibrary.is_text("1"))

    def test_is_num(self):
        self.assertTrue(BookLibrary.is_num("100"))  # True
        self.assertFalse(BookLibrary.is_num(""))
        self.assertFalse(BookLibrary.is_num("-1"))
        self.assertFalse(BookLibrary.is_num("page"))


if __name__ == "__main__":
    unittest.main()
