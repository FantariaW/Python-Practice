# Day 5 Training

# Day 5 Training 1: square(n), say_hello(name), double_list(lst)
def get_prompt(prompt_name, prompt_num):
    """
    prompt the user to enter a number, calculate the number they entered
    :param prompt_name: str - user's name
    :param prompt_num: int - user's number
    :return: user's name - numbers
    """
    user_dict = {}

    print("--Please enter a name('done' to stop), then add any number('end' to stop)--")
    while True:
        try:
            user_name = input(prompt_name)
            if user_name.lower() == 'done':
                break
            if user_name.isalpha():
                if user_name.title() not in user_dict:
                    user_dict[user_name.title()] = []
                while True:
                    try:
                        user_num = input(f"{user_name.title()}{prompt_num}")
                        if user_num.lower() == 'end':
                            break
                        try:
                            user_num = float(user_num)
                            user_dict[user_name.title()].append(float(user_num))
                        except ValueError:
                            raise ValueError(f"The value \'{user_num:.2f}\' is invalid, please enter a numeric value!")
                    except ValueError as error_msg_num:
                        print(error_msg_num)
            else:
                raise ValueError(f"The value \'{user_name}\' is invalid, please enter a alphabetic name value!")
        except ValueError as error_msg_name:
            print(error_msg_name)

    return user_dict


def say_hello(name):
    """
    print a text paragraph
    :param name: str - user's name
    :return: print out Hello, user
    """
    return f"Hello, {name}"


def square(num_lst):
    """
    calculating square for a list of numbers
    :param num_lst: list - number of list
    :return: square of all number in the list
    """
    # print(", ".join([f"{i ** 2:.2f}" for i in num_lst]))
    return [f"{i ** 2:.2f}" for i in num_lst]


def double_list(num_lst):
    """
    each number in a list times 2
    :param num_lst: list - number of list
    :return: all numbers times 2 in the list
    """
    # print(", ".join(f"{i * 2}" for i in num_lst))
    return [f"{i * 2:.2f}" for i in num_lst]


# 本次 main() 僅僅用於測試該模組用的區塊，不會被 import 執行，STARTER 為主要運行文件
# This block is only for local testing during development.
# It will not run when imported as a module.
def main():
    prompt_name = "Name: "
    prompt_num = "\'s Number: "
    user_dict = get_prompt(prompt_name, prompt_num)
    print(user_dict)

    print(f"\n--User Table--")
    for each_user_name, each_user_num in user_dict.items():
        print(f"{each_user_name}: {each_user_num}")

    print("\n" + "=" * 80, "\n")  # ====================================================================================

    for key_name, value_num_list in user_dict.items():
        print(f"{key_name}", end="")
        # print(", ".join(square_num_list))

        print("-" * 40)
        print(f"Say Hello:", say_hello(key_name))
        print("-" * 40)
        print(f"Square {key_name}'s Number List:", ", ".join(square(value_num_list)))
        print("-" * 40)
        print(f"Double {key_name}'s Number List:", ", ".join(double_list(value_num_list)))
        print("\n" + "=" * 80, "\n")  # ================================================================================


if __name__ == "__main__":
    main()
