# Day 5 Training
import random
import statistics
import sys


# Day 5 Training 1: import random, random.choice()
def get_flavor(prompt_flavor):
    """
    prompt the user to enter flavors and count their frequency.
    :param prompt_flavor: str - the message to display when asking for flavor input
    :return: tuple - (lists of flavors, dict with flavor counts)
    """
    flavor_list = []
    count_flavor_dict = {}

    print("--Enter flavor--")
    while True:
        try:
            user_flavor = input(prompt_flavor)
            if user_flavor.lower() == 'done':
                break

            if user_flavor.isalpha():
                flavor_list.append(user_flavor)

                if user_flavor in count_flavor_dict:
                    count_flavor_dict[user_flavor] += 1
                else:
                    count_flavor_dict[user_flavor] = 1
            else:
                raise ValueError(f"The value \'{user_flavor}\' is invalid! Please enter alphabetic flavor name.")
        except ValueError as error_msg:
            print("ERROR - ", error_msg)

    return flavor_list, count_flavor_dict


def get_average(prompt_average):
    """
    Prompt the user to enter a list of doughnut counts and calculate the average.
    :param prompt_average: int - the message will display when asking for numeric input
    :return: (list of int, float)
    """
    average_list = []

    print("--Enter amount of doughnut to calculate average--")
    while True:
        try:
            doughnut_amount = input(prompt_average)
            if doughnut_amount.lower() == 'done':
                break

            if doughnut_amount.isdigit() and int(doughnut_amount) > 0:
                average_list.append(int(doughnut_amount))
            else:
                raise ValueError(f"The value \'{doughnut_amount}\' is invalid, Please enter a numeric value")

        except ValueError as error_msg:
            print(error_msg)

    return average_list, statistics.mean(average_list) if average_list else 0


def print_cli_name(prompt_name):
    """
    print the message in CLI to display user's name
    :param prompt_name: str - name of user
    :return: str - prompt_name
    """
    print(f"Name: {prompt_name}")

    return prompt_name


# 本次 main() 僅僅用於測試該模組用的區塊，不會被 import 執行，STARTER 為主要運行文件
# This block is only for local testing during development.
# It will not run when imported as a module.
def main():
    # Day 5 Training 1: import random, random.choice()
    prompt_flavor = ">> "
    flavor_list, count_flavor_dict = get_flavor(prompt_flavor)

    print(f"--🐤Flavor Table--")
    if count_flavor_dict:
        print("\n".join(f"{flavor_key}: {flavor_value}" for flavor_key, flavor_value in count_flavor_dict.items()))
        print("🐣Random flavor for today - ", random.choice(flavor_list))
    else:
        print("No flavors entered 🍃")
        print("🐣Random flavor for today - N/A ")

    print("=" * 80)  # =================================================================================================

    # Day 5 Training 2: import statistics, statistics.mean()
    prompt_average = ">> "
    average_list, average_doughnut = get_average(prompt_average)

    print("--Doughnut Table--")
    for each_doughnut in average_list:
        print(f"{each_doughnut}")

    print(f"Each person ordered an average of {average_doughnut:.2f} doughnut🍩")

    print("=" * 80)  # =================================================================================================

    # Day 5 Training 3: import sys, sys.argv, if __name__ == "__main__":
    if len(sys.argv) == 2:
        print_cli_name(sys.argv[1])
    else:
        print_cli_name(None)


if __name__ == "__main__":
    main()
