# Lesson 8 regular expression: group, walrus operator
import re

# ❗walrus operator  -  海象運算符, 能在表達式中 直接賦值并使用, 提高可讀性和運算效率
name = input("Name: ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    last = matches.group(1)
    first = matches.group(2)
    # name = matches.group(2) + " " + matches.group(1)
    name = f"{first} {last}"
print(f"Hi, {name}")

# ❗walrus operator  -  海象運算符, 能在表達式中 直接賦值并使用, 提高可讀性和運算效率
if (line := input("Line: ")) != "":
    print(line)


# ============================================================================
