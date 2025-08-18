# Day 5 Training: import random, random.choice()
import random
import sys

# Day 5 Training 1:
fruit_random = random.choice(["   sTraWberRy", "vanilla", "chocolate"])
print(f"Random flavor for today: {fruit_random.strip().title()}")


print("\n", "=" * 80, "\n")  # =========================================================================================


# Day 5 Training 2:
print("--Typing \"python Arivia_Day_5_1_import.py name\" in Terminal to run--")
try:
    if len(sys.argv) > 2:
        raise IndexError("Only 1 single name request!")
    elif len(sys.argv) < 2:
        raise IndexError("Please enter a Name!")
    else:
        print(f"Hello, {sys.argv[1]}")
except IndexError as error_msg:
    print("ERROR - ", error_msg)


print("\n", "=" * 80, "\n")  # =========================================================================================


# Day 5 Training 3:
def user_info(prompt_info):
    user_list = []
    count_all_dict = {}

    print("--Enter name, flavor, amount--")
    while True:
        try:
            user_input = input(prompt_info).strip()
            if user_input.lower() == 'done':
                break

            user_name, user_flavor, user_flavor_amount = user_input.strip().split(",")
            valid_text = user_name.isalpha() and user_flavor.isalpha()
            valid_num = user_flavor_amount.isdigit() and int(user_flavor_amount) > 0
            if valid_text and valid_num:
                user_dict = {
                    "name": user_name.title(),
                    "flavor": user_flavor.title(),
                    "amount": int(user_flavor_amount)
                }
                user_list.append(user_dict)

                new_name = user_dict["name"]
                new_flavor = user_dict["flavor"]
                new_amount = user_dict["amount"]

                if new_name not in count_all_dict:
                    count_all_dict[new_name] = {}

                if new_flavor in count_all_dict[new_name]:
                    count_all_dict[new_name][new_flavor] += new_amount
                else:
                    count_all_dict[new_name][new_flavor] = new_amount
            else:
                raise ValueError("Name, Flavor should be string text, amount must be numeric!!!")
        except ValueError as error_msg_2:
            print(error_msg_2)

    return user_list, count_all_dict


def main():
    prompt_info = ">> "
    user_list, count_all_dict = user_info(prompt_info)

    random.shuffle(user_list)
    print("--🧩Shuffle All Info--")
    for each_dict in user_list:
        print("User-Info: " + ",".join(f"{value}" for value in each_dict.values()))

    print()
    print("--🐻Organizing All Info--")
    for main_key, main_value in count_all_dict.items():
        print(f"{main_key}: ", end="")
        print(" - ".join(f"{sub_key}:{sub_value}" for sub_key, sub_value in main_value.items()))


main()
