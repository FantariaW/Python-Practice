# Day 6 Training: class, __init__

# Day 6 Training:
class BackpackItem:
    """
    class for stored: is_text, is_num, get_prompt, tbl_making
    """
    def __init__(self, item_name: str, item_qty: int):
        self.item_name = item_name
        self.item_qty = item_qty

    @staticmethod
    def is_text(value):
        """
        testing if value is an alphabetic value
        :param value: str - item_name
        :return: item_name
        """
        return value != "" and value.isalpha()

    @staticmethod
    def is_num(value):
        """
        test if value is a numeric integer value
        :param value: int - item_qty
        :return: item_qty
        """
        try:
            value = int(value)
            return isinstance(value, int) and int(value) > 0
        except ValueError:
            return False

    @classmethod
    def get_prompt(cls, prompt_name: str, prompt_qty: str):
        """
        prompt the user to enter name and quantity of item
        :param prompt_name: str - item_name
        :param prompt_qty: str - item_qty
        :return: item_lst
        """
        item_lst = []

        print("== Enter Name and Quantity ==")
        while True:
            try:
                item_name = input(prompt_name).strip()
                if item_name.lower() == 'done':
                    break

                assert cls.is_text(item_name), f"Item Name: '{item_name}' is invalid!"

                while True:
                    try:
                        item_qty = input(f"{item_name.title()}{prompt_qty}").strip()

                        assert item_qty != "", "Item Quantity can't be empty!"
                        assert cls.is_num(item_qty), f"Item Quantity '{item_qty}' must be positive integer number!"

                        # item_info = cls(item_name.title(), int(item_qty))
                        # cls(item_name.title(), int(item_qty)) 用參數去創建 class 的一個物件」，然後 __init__ 負責把值存在那個物件的屬性中
                        item_lst.append(cls(item_name.title(), int(item_qty)))
                        break
                    except AssertionError as e:
                        print(e)
            except AssertionError as e:
                print(e)

        return item_lst

    @staticmethod
    def tbl_making(lst):
        """
        transform the item_lst into a formatted table
        :param lst: list - item_lst
        :return: result_tbl
        """
        result_tbl = []

        for each_item in lst:
            result_tbl.append(f"📋 - {each_item.item_name} with {each_item.item_qty} packs!")

        return "\n".join(result_tbl)


def main():
    """
    test and run the whole program only, will not use in other file
    :return: whole program
    """
    item_lst = BackpackItem.get_prompt("Item Name -> ", " 's Quantity -> ")
    print(BackpackItem.tbl_making(item_lst))


if __name__ == "__main__":
    main()
