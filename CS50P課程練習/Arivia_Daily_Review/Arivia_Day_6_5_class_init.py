# Day 6 Training: class, __init__

# Day 6 Training
class ItemBox:
    def __init__(self, name=None, category=None):
        self.name = name
        self.category = category

    @staticmethod
    def is_valid(value: str) -> bool:
        try:
            if value != "" and value.isalpha():
                return True
        except ValueError:
            return False

    @classmethod
    def get_prompt(cls, prompt_name: str, prompt_category: str):
        print("== Enter name and category ==")

        while True:
            try:
                name = input(prompt_name).strip()
                assert cls.is_valid(name), f"Name: '{name}' is invalid!"

                while True:
                    try:
                        category = input(f"{name}{prompt_category}").strip()
                        assert cls.is_valid(category), f"Category: '{category}' is invalid!"

                        return cls(name, category)
                    except AssertionError as error_assert:
                        print(error_assert)
            except AssertionError as e:
                print(e)


def main():
    item_card = ItemBox.get_prompt("Name: ", ": ")

    print(f"Name: {item_card.name.title()}, Category: {item_card.category.title()}")


if __name__ == "__main__":
    main()
