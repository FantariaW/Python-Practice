# 2025/05/02
# Level 1
# 1: User enter name and age, must enter both value in one line, split with space.
# 2: remove space with .strip() before print out First and Last name, capitalize each words with .title().
first_name, last_name, age = input("Level 1: \nPlease enter First name, Last name, and your Age: ").split()
first_name = first_name.title()
last_name = last_name.title()

# First Way
print(f"Hello, \"Name\": {first_name} {last_name} \nYou are currently: {age} years old.".strip(), end="\n\n")
# Second Way:
# result = f"Hello, \"Name\": {first_name} {last_name} \nYou are currently: {age} years old.".strip()
# print(result, end="\n")

# ----------------------------------------------------------------------------------------------------------------------

# Level 2
# Split First name and Last name, need to capitalize them with .upper()
print(f"Level 2: \nFirst: {first_name.upper()} \nLast: {last_name.upper()}".strip(), end="\n\n")

# ----------------------------------------------------------------------------------------------------------------------

# Bonus Trap from Arivia
# Print out JSON formula code with string
print(f"Bonus from Arivia: \n{{\n\"user\": {{ \n   \"name\": {first_name}, \n   \"age\": {age}, "
      f"\n   \"status\": \"💥 Determined to learn!\" \n  }}\n}}")

# ======================================================================================================================
