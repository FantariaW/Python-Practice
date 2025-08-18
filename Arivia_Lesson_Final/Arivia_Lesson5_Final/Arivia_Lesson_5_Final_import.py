# Lesson 5 Final: 🧭 Day 1～Day 5 知識整合 + 模組封裝 + 進階字典結構

# get input from user
def get_festival_data(prompt_name, prompt_candy_count):
    """
    prompt user to enter name, candy, count
    :param prompt_name: str - user's name
    :param prompt_candy_count: str, int - candy, count = candy_count.split(",")
    :return: {'name': user's name, 'candies': {candy, count}}
    """
    festival_list = []
    total_candy_dict = {}

    print("==🍬Candy Festival🎡==")
    print("-" * 40)
    print("Please enter name('done' to stop)")

    while True:
        try:
            get_name = input(prompt_name).strip()
            if get_name.lower() == 'done':
                break
            if get_name.isalpha():
                candy_dict = {}
                while True:
                    try:
                        get_candy_count = input(f"{get_name.title()}'s candy and count -> {prompt_candy_count}").strip()
                        if get_candy_count.lower() == 'end':
                            break
                        get_candy, get_count = get_candy_count.split(",")
                        valid_candy_text = get_candy.isalpha()
                        valid_count_num = get_count.isdigit() and int(get_count) > 0

                        # store get_candy (candy-name), get_count (candy-count) into candy_dict
                        if valid_candy_text and valid_count_num:
                            if get_candy.title() in candy_dict:
                                candy_dict[get_candy.title()] += int(get_count)
                            else:
                                candy_dict[get_candy.title()] = int(get_count)
                        else:
                            raise ValueError("Candy should be a alphabetic value, Count should be numeric value")

                        # store get_name (user-name), candy_dict into user_info_dict
                        user_info_dict = {
                            "name": get_name.title(),
                            "candies": candy_dict
                        }
                        # add user_info_dict into festival_list (store all information)
                        if user_info_dict not in festival_list:
                            festival_list.append(user_info_dict)

                        # store all candy and count into total_candy_dict
                        if get_candy.title() not in total_candy_dict:
                            total_candy_dict[get_candy.title()] = {"total": 0, "voters": 0}

                        if get_candy.title() in total_candy_dict:
                            total_candy_dict[get_candy.title()]["total"] += int(get_count)
                            total_candy_dict[get_candy.title()]["voters"] += 1
                        else:
                            total_candy_dict[get_candy.title()]["total"] = int(get_count)
                            total_candy_dict[get_candy.title()]["voters"] = 1

                    except ValueError as error_msg_1:
                        print(error_msg_1)
            else:
                raise ValueError(f"Name \'{get_name}\' is invalid, please enter a alphabetic value!")

        except ValueError as error_msg_2:
            print(error_msg_2)

    return festival_list, total_candy_dict


def build_summary_dict(festival_list):
    """
    display formatted table of information
    :param festival_list: lst - name, candies(candy, count)
    :return: name bought: - candy: count
    """
    result = []
    for each_info_dict in festival_list:
        new_name = each_info_dict["name"]
        result.append(f"🍬{new_name} bought:")

        for key_candies, value_count in each_info_dict["candies"].items():
            result.append(f"- {key_candies}: {value_count}")
    return "\n".join(result)


def print_summary_table(total_candy_dict):
    """
    display formatted table of total candy count
    :param total_candy_dict: dict - candy, total, voters
    :return: candy - total: total | voters: voters
    """
    result = []
    for key_candy, value_count in total_candy_dict.items():
        result.append(f"{key_candy} - ")
        new_total = value_count["total"]
        new_voters = value_count["voters"]
        result.append(f"total: {new_total} packs | voters: {new_voters}\n")
    return "".join(result)


def main():
    """
    main program testing function only, will not run in STARTER file!
    :return: run and test whole program
    """
    prompt_name = "Name >> "
    prompt_candy_count = ""

    festival_list, total_candy_dict = get_festival_data(prompt_name, prompt_candy_count)

    print(festival_list)
    print("📦User bought Table📦")
    print("-" * 40)
    print(build_summary_dict(festival_list))

    print("\n")

    print(total_candy_dict)
    print("🎉 Candy Festival Summary 🎉")
    print("-" * 40)
    print(print_summary_table(total_candy_dict))


if __name__ == "__main__":
    main()
