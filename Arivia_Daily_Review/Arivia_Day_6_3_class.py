# Day 6 Training: class, assert

# Day 6 Training
class NameCard:
    """
    NameCard for stored: is_int, make_card

    is_int: verify integer number is valid or invalid
    make_card: prompt input box for name, age. return name, age
    """
    @staticmethod
    def is_int(str_age: str) -> bool:
        """
        verify an input which is int or str
        :param str_age: new_age = int(str_age)
        :return: True or False
        """
        try:
            new_age = int(str_age)
            return isinstance(new_age, int)
            # 這個是驗證1個值的多種類型的時候會使用的
            # return isinstance(new_age, (int, float))
        except ValueError:
            return False

    def make_card(self, prompt_name: str, prompt_age: str) -> tuple[str, int]:
        """
        prompt user to enter name and age
        :param prompt_name: str - name
        :param prompt_age: int - age
        :return: name, age
        """
        print("==Enter Name and Age==")

        while True:
            try:
                name = input(prompt_name).strip()
                assert name != "", "Name can't be space!"
                assert name.isalpha(), f"Name \'{name}\' is invalid, must be alphabetic!"

                while True:
                    try:
                        age = input(f"{name.title()}{prompt_age}").strip()
                        assert age != "", "Age can't be space!"

                        assert self.is_int(age), f"Age \'{age}\' is invalid, must be numeric!"

                        age = int(age)
                        assert int(age) >= 0, f"Age \'{age}\' must greater than 0!"

                        return name, age
                    except (ValueError, AssertionError) as e:
                        print(e)
            except AssertionError as e_assert:
                print(e_assert)


def main():
    """
    function main use to test and run program only, will not use in import file
    :return: testing whole program
    """
    prompt_name = "Name -> "
    prompt_age = " -> "

    card = NameCard()
    name, age = card.make_card(prompt_name, prompt_age)

    print(f"{name.title()}: {age} years old.")


if __name__ == "__main__":
    main()
