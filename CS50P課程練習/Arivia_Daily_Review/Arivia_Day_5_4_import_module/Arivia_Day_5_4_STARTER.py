from Arivia_Day_5_4_import import get_prompt, user_table, snack_table

prompt_name = ">> "
prompt_snack_pack = "- "
customer_dict, snack_pack_dict = get_prompt(prompt_name, prompt_snack_pack)

print("🌟 Snack Orders Record 🌟")
print(user_table(customer_dict))

print("-" * 40)

print("🍪 Snack Summary 🍪")
print(snack_table(snack_pack_dict))
