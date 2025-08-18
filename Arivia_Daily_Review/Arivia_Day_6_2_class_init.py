# Day 6 Training: class, assert, def__init__:

# class
class Pet:
    def __init__(self, name: str, age: float):
        self.name = name
        self.age = age

    @staticmethod
    def is_float(age: str) -> bool:
        try:
            float(age)
            return True
        except ValueError:
            return False

    def get_prompt(self, prompt_name: str, prompt_age: str):
        while True:
            try:
                name = input(prompt_name).strip()
                assert name != "", f"Name \'{name}\' can't be space!"
                assert name.isalpha(), f"Name \'{name}\' is invalid!"

                while True:
                    try:
                        age = input(prompt_age).strip()
                        assert age != "", "Age can't be space!"

                        if not self.is_float(age):
                            raise ValueError(f"Age \'{age}\' must be numeric!")

                        age = float(age)
                        assert float(age) >= 0, f"Age \'{age:.0f}\' must be positive number!"

                        return name, age
                    except (ValueError, AssertionError) as error:
                        print(error)

            except AssertionError as error_msg:
                print(error_msg)


# def test(a, b):
#     return f"{a}: {b}"


def main():
    each_pet = Pet("", 0)
    name, age = each_pet.get_prompt("Name-> ", "Age-> ")

    print(f"{name}, {age:.2f}")

    # # test 1
    # print(test("Alice", 2))


if __name__ == "__main__":
    main()
