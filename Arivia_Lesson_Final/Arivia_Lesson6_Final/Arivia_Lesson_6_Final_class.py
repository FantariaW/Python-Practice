# Day 6 Final: class, __init__

# Day 6 Final
class ProductStock:
    """
    class for stored:

    __init__: stored product_name, product_type, product_qty
    __str__: return list into string
    is_text: return valid alphabetic value
    is_type: return 3 valid types of product
    is_num: return valid numeric value
    tbl_build: return styling list table
    summary_tbl_build: return styling summary list table
    get_prompt: prompt the user to enter input value
    """
    def __init__(self, product_name: str, product_type: str, product_qty: int):
        """
        initialize value define
        :param product_name: str - product name
        :param product_type: str - product type
        :param product_qty: int - product quantity
        """
        self.product_name = product_name
        self.product_type = product_type
        self.product_qty = product_qty

    def __str__(self):
        """
        :return: str - name, type, qty
        """
        return f"{self.product_name}, {self.product_type}, {self.product_qty}"

    @staticmethod
    def is_text(value):
        """
        test valid alphabetic value
        :param value: str - product_name
        :return: True
        """
        return value != "" and value.isalpha()

    @staticmethod
    def is_type(value):
        """
        test 3 valid types
        :param value: str - "daily", "food", "tool"
        :return: True
        """
        return value.lower() in ["daily", "food", "tool"]

    @staticmethod
    def is_num(value):
        """
        test valid numeric value
        :param value: int - product_qty
        :return: True
        """
        try:
            value = int(value)
            return isinstance(value, int) and int(value) > 0
        except ValueError:
            return False

    @staticmethod
    def tbl_build(lst):
        """
        build up styling list table
        :param lst: list - product_lst
        :return: styling string of list
        """
        result = []

        for each_item in lst:
            match each_item.product_type.lower():
                case "daily":
                    result.append(
                        f"🛒 {each_item.product_name} - {each_item.product_type} - {each_item.product_qty} packs."
                    )
                case "food":
                    result.append(
                        f"🍔 {each_item.product_name} - {each_item.product_type} - {each_item.product_qty} packs."
                    )
                case "tool":
                    result.append(
                        f"🔧 {each_item.product_name} - {each_item.product_type} - {each_item.product_qty} packs."
                    )
        return "\n".join(result)

    @staticmethod
    def summary_tbl_build(lst):
        """
        build up styling summary list table
        :param lst: list - product_lst
        :return: styling string of summary list
        """
        sum_dict = {}

        for each_item in lst:
            if each_item.product_type in sum_dict:
                sum_dict[each_item.product_type] += int(each_item.product_qty)
            else:
                sum_dict[each_item.product_type] = int(each_item.product_qty)
        return "\n".join(f"{key} - {value} packs." for key, value in sum_dict.items())

    @classmethod
    def get_prompt(cls, prompt_name: str, prompt_type_qty: str):
        """
        prompt the user to enter input value
        :param prompt_name: str - name
        :param prompt_type_qty: str - type, quantity(qty)
        :return: product_name, product_type, product_qty
        """
        maximum = 3
        product_lst = []

        print("== 📦 Product Stock Tracker ==")
        print("📦Please enter a product name:")
        while len(product_lst) < maximum:
            try:
                product_name = input(prompt_name).strip()
                if product_name.lower() == 'done':
                    break

                assert cls.is_text(product_name), f"Product: '{product_name}' is invalid!(alphabetic value only!)"

                print("📝Please enter type 1 of (daily/food/tool), and quantity:")
                while True:
                    try:
                        product_type_qty = input(f"{product_name.title()}{prompt_type_qty}").strip()
                        new_product_type_qty = product_type_qty.split(",")
                        if len(new_product_type_qty) != 2:
                            raise ValueError("'Type' and 'Quantity' required, only 2 values required!")

                        product_type, product_qty = new_product_type_qty
                        assert cls.is_type(product_type), f"Type: '{product_type}' must be 1 of 3 types!"
                        assert cls.is_num(product_qty), f"Quantity '{product_qty}' must be positive numeric value!"

                        product_lst.append(cls(product_name.title(), product_type.title(), int(product_qty)))
                        break
                    except (ValueError, AssertionError) as e:
                        print(e)
            except AssertionError as e:
                print(e)

        return product_lst


def main():
    """
    only use for testing whole program, will not run in other files
    :return: whole program
    """
    product_lst = ProductStock.get_prompt("📦 - Product Name -> ", "'s Type and Quantity - > ")

    # list print out only
    print("== 📦Product List📦 ==")
    for product in product_lst:
        print(product.__str__())
    print("-" * 40)

    # styling table list
    print("== ✨Product Table Style✨ ==")
    print(ProductStock.tbl_build(product_lst))
    print("-" * 40)

    # summary styling table list
    print("== 📊Summary Table📊 ==")
    print(ProductStock.summary_tbl_build(product_lst))


if __name__ == "__main__":
    main()
