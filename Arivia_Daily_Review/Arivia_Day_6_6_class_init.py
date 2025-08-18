# Day 6 Training: class, init

# Day 6 Training
class Fruit:
    def __init__(self, new_name=None, new_quantity=None):
        self.name = new_name
        self.quantity = new_quantity

    @staticmethod
    def is_text(value):
        try:
            value != "" and value.isalpha()
            return True
        except ValueError:
            return False

    @staticmethod
    def is_num(value):
        try:
            value = int(value)
            return int(value) > 0 and isinstance(value, int)
        except ValueError:
            return False

    @staticmethod
    def fruit_tbl(lst):
        result = ["== Fruit Table =="]

        for each_dict in lst:
            each_name = each_dict['name']
            each_qty = each_dict['quantity']

            result.append(f"🌿 - {each_name}: {each_qty} packs.")

        return "\n".join(result)

    @classmethod
    def get_prompt(cls, prompt_name: str, prompt_quantity: str):
        fruit_list = []

        print("== Enter Name and Quantity ==")
        while True:
            try:
                name = input(prompt_name).strip()
                if name.lower() == 'done':
                    break
                assert cls.is_text(name), f"Name: '{name}' is invalid!"
                while True:
                    try:
                        quantity = input(f"{name.title()}{prompt_quantity}")
                        assert cls.is_num(quantity), f"Quantity: '{quantity}' is invalid!(Positive Number Only!)"

                        fruit_dict = {
                            "name": name.title(),
                            "quantity": int(quantity)
                        }

                        fruit_list.append(fruit_dict)

                        break
                    except AssertionError as e:
                        print(e)
            except AssertionError as e:
                print(e)

        return fruit_list


def main():
    fruit_list = Fruit.get_prompt("Name >>", " 's Quantity >> ")
    fruit_table = Fruit.fruit_tbl(fruit_list)

    print(fruit_table)


if __name__ == "__main__":
    main()
