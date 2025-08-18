# Day 5 Training: 🧭 Day 1～Day 5 知識整合 snack collector 📦

# module define
def get_prompt(prompt_name, prompt_snack_pack):
    """
    prompt the user to enter name, snack, pack amount.
    :param prompt_name: str - user's name
    :param prompt_snack_pack: str, int - user's snack, amount of snack
    :return: user's name - user's snack, amount of snack
    """

    customer_dict = {}
    snack_pack_dict = {}

    print("--Enter a name('done' to stop), adding food and amount into cart('end' to stop)--")
    while True:
        try:
            get_name = input(prompt_name)
            if get_name.lower() == 'done':
                break
            if get_name.isalpha() and get_name.title() not in customer_dict:
                customer_dict[get_name.title()] = {}
            else:
                raise ValueError(f"The name \'{get_name}\' is invalid, please enter a alphabetic value")
            while True:
                try:
                    get_snack_pack = input(f"{get_name} {prompt_snack_pack}")

                    if get_snack_pack.lower() == 'end':
                        break

                    get_snack, get_pack = get_snack_pack.split(",")
                    valid_snack = get_snack.isalpha()
                    valid_pack = get_pack.isdigit() and int(get_pack) > 0

                    # adding name, snack, pack into nested dictionary - customer_dict
                    if valid_snack and valid_pack:
                        if get_snack in customer_dict[get_name.title()]:
                            customer_dict[get_name.title()][get_snack] += int(get_pack)
                        else:
                            customer_dict[get_name.title()][get_snack] = int(get_pack)
                    else:
                        raise ValueError("Snack should be alphabetic value, Pack should be numeric value!")

                    # adding whole snack, pack into nested dictionary - snack_pack_dict
                    if valid_snack and valid_pack:
                        if get_snack in snack_pack_dict:
                            snack_pack_dict[get_snack] += int(get_pack)
                        else:
                            snack_pack_dict[get_snack] = int(get_pack)
                except ValueError as error_msg:
                    print(error_msg)
        except ValueError as error_msg_2:
            print(error_msg_2)

    return customer_dict, snack_pack_dict


def say_hello(name):
    """
    prompt the hello message to user.
    :param name: str - user's name
    :return: Hello! user's name
    """
    return f"Hello! {name}"


def user_table(user_table_dict):
    """
    display formatted information table
    :param user_table_dict: list - name, snack, pack
    :return: Hello! name - snack, pack
    """
    result = []
    for key_user, value_snack in user_table_dict.items():
        each_info = (f"{say_hello(key_user)} - " + "🍭".join(
            f"{sub_key_snack}: {sub_value_pack}" for sub_key_snack, sub_value_pack in value_snack.items()))
        result.append(each_info)
    return "\n".join(result)


def snack_table(snack_table_dict):
    """
    display formatted snack table
    :param snack_table_dict: list - snack, pack
    :return: snack: pack
    """
    result_2 = []
    for key_snack, value_pack in snack_table_dict.items():
        result_2.append(f"🍪{key_snack}: {value_pack} packs🛒")
    return "\n".join(result_2)


def main():
    """
    main program testing function only, will not run in STARTER file!
    :return: run and test whole program
    """
    prompt_name = ">> "
    prompt_snack_pack = "- "
    customer_dict, snack_pack_dict = get_prompt(prompt_name, prompt_snack_pack)

    print("🌟 Snack Orders Record 🌟")
    print(user_table(customer_dict))

    print("-" * 40)

    print("🍪 Snack Summary 🍪")
    print(snack_table(snack_pack_dict))

    print(customer_dict)


if __name__ == "__main__":
    main()
