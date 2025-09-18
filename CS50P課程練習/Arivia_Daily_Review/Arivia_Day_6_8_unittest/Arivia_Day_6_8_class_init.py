# Day 6 Training: Day 1 - Day 6

# Day 6 Training
class ItemPack:
    def __init__(self, new_item_name: str, new_item_qty: int, new_item_category: str):
        self.item_name = new_item_name.title()
        self.item_qty = int(new_item_qty)
        self.item_category = new_item_category.title()

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

    @staticmethod
    def dict_build(food_dict):
        return {
            food_dict["name"]: food_dict["food_info"]
        }

    @classmethod
    def get_prompt(cls, prompt_name: str, prompt_qty: str, prompt_category: str):
        food_obj_lst = []
        count_category_dict = {}

        print("== 📦 Food Pack Summary 🎁 ==")
        print("Please enter Food Name:")
        while True:
            try:
                item_name = input(prompt_name).strip()
                if item_name.lower() == 'done':
                    break
                assert cls.is_text(item_name), f"Item Name: {item_name} is invalid!"

                print("Please enter Food Quantity:")
                while True:
                    try:
                        item_qty = input(f"{item_name.title()}{prompt_qty}").strip()
                        assert item_qty != "", "Item Quantity can't be empty!"
                        assert cls.is_num(item_qty), f"Item Quantity: {item_qty} must be positive numeric value!"
                        break
                    except AssertionError as e:
                        print(e)

                print("Please enter Item Category(Fruit/Snack/Drink):")
                while True:
                    try:
                        item_category = input(f"{item_name.title()}{prompt_category}").strip()
                        assert cls.is_text(item_category), f"Item Category: {item_category} is invalid!"
                        assert item_category.lower() in ['fruit', 'snack', 'drink'], \
                            "Item Category must be the one of 3 types!"
                        break
                    except AssertionError as e:
                        print(e)

                # 把init定義的值成功存入物件
                food_obj = cls(item_name, int(item_qty), item_category)
                food_obj_lst.append(food_obj)

                # 這裏進行出現過的category總額計算
                if food_obj.item_category.title() in count_category_dict:
                    count_category_dict[food_obj.item_category.title()] += int(food_obj.item_qty)
                else:
                    count_category_dict[food_obj.item_category.title()] = int(food_obj.item_qty)
            except AssertionError as e:
                print(e)

        return food_obj_lst, count_category_dict

    @staticmethod
    def tbl_build(food_obj_lst):
        result = []

        for food in food_obj_lst:
            result.append(f"🌿 - {food.item_name} has {food.item_qty} counts | Type - {food.item_category}")
        return "\n".join(result)

    @staticmethod
    def count_build(count_category_dict):
        return "\n".join(f"📦 - {key}: {value} total counts" for key, value in count_category_dict.items())


def main():
    food_obj_lst, count_category_dict = ItemPack.get_prompt(
        "Item Name -> ", "'s Quantity -> ", "'s Category -> "
    )

    # print(food_obj_lst)
    # print(count_category_dict)
    print("== 🎁 Table List 🎁 ==")
    print("-" * 40)
    print(ItemPack.tbl_build(food_obj_lst))
    print("-" * 40)
    print(ItemPack.count_build(count_category_dict))


if __name__ == "__main__":
    main()
