import unittest
from Arivia_Lesson_6_Final_class import ProductStock


class TestProductStock(unittest.TestCase):
    def test_init(self):
        product = ProductStock("hamburger", "food", 1)
        self.assertEqual(product.product_name, "hamburger")
        self.assertEqual(product.product_type, "food")
        self.assertEqual(product.product_qty, 1)

    def test_is_text(self):
        self.assertTrue(ProductStock.is_text("abc"))  # True
        self.assertFalse(ProductStock.is_text(""))
        self.assertFalse(ProductStock.is_text("1"))

    def test_is_num(self):
        self.assertTrue(ProductStock.is_num("1"))  # True
        self.assertFalse(ProductStock.is_num(""))
        self.assertFalse(ProductStock.is_num("abc"))
        self.assertFalse(ProductStock.is_num("0"))
        self.assertFalse(ProductStock.is_num("-1"))


if __name__ == "__main__":
    unittest.main()
