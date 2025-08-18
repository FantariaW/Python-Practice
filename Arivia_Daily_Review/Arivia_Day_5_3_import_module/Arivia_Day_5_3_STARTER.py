from Arivia_Day_5_3_import import get_prompt, say_hello, square, double_list

prompt_name = "Name: "
prompt_num = f"'s Number: "
user_dict = get_prompt(prompt_name, prompt_num)

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
