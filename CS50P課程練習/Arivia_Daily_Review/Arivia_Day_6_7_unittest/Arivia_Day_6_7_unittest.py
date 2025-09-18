import unittest
from Arivia_Day_6_7_class_init import BackpackItem


class TestBackpackItem(unittest.TestCase):
    def test_is_text(self):
        self.assertTrue(BackpackItem.is_text("candy"))  # True
        self.assertFalse(BackpackItem.is_text(""))
        self.assertFalse(BackpackItem.is_text("123"))

    def test_is_num(self):
        self.assertTrue(BackpackItem.is_num("1"))  # True
        self.assertFalse(BackpackItem.is_num("abc"))
        self.assertFalse(BackpackItem.is_num("0"))
        self.assertFalse(BackpackItem.is_num("-1"))

    def test_tbl_making(self):
        items = [
            BackpackItem("candy", 1),
            BackpackItem("chocolate", 2)
        ]
        result = BackpackItem.tbl_making(items)

        self.assertIn("candy", result)
        self.assertIn("chocolate", result)


if __name__ == "__main__":
    unittest.main()
