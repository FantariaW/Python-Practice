import unittest
from Arivia_Day_6_8_class_init import ItemPack


class TestItemPack(unittest.TestCase):
    def test_init_values(self):
        item = ItemPack("Apple", 5, "Fruit")
        self.assertEqual(item.item_name, "Apple")
        self.assertEqual(item.item_qty, 5)
        self.assertEqual(item.item_category, "Fruit")

    def test_is_text(self):
        self.assertTrue(ItemPack.is_text("Apple"))
        self.assertFalse(ItemPack.is_text("123"))
        self.assertFalse(ItemPack.is_text(""))
        self.assertFalse(ItemPack.is_text("apple1"))

    def test_is_num(self):
        self.assertTrue(ItemPack.is_num("5"))
        self.assertFalse(ItemPack.is_num("-3"))
        self.assertFalse(ItemPack.is_num(""))
        self.assertFalse(ItemPack.is_num("abc"))

    def test_dict_build(self):
        food_dict = {
            "name": "Banana",
            "food_info": {"quantity": 3, "category": "Fruit"}
        }
        expected_output = {
            "Banana": {"quantity": 3, "category": "Fruit"}
        }
        self.assertEqual(ItemPack.dict_build(food_dict), expected_output)


if __name__ == "__main__":
    unittest.main()
