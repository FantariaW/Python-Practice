# Day 8 Training: re.search

# Day 8 Training:
import re


def prompt_validation(prompt_msg, assert_msg, error_msg):
    while True:
        try:
            user_input = input(prompt_msg).strip()
            assert assert_msg(user_input), error_msg
            return user_input
        except AssertionError as e_msg:
            print(e_msg)


# 1.簡易email判斷訓練
email = prompt_validation(
    "Enter Email: ",
    lambda em: re.search(r"^\w+@\w+\.(com|edu)$", em),
    "Email Format Invalid"
)
print(email)

# =============================================================================

# 2.簡易name分離訓練
while True:
    try:
        name = input("Enter Name: ").strip()
        if matches := re.search(r"^([a-z]+) *, *([a-z]+)$", name, re.IGNORECASE):
            first = matches.group(1)
            last = matches.group(2)
            print(f"{last} {first}")
            break
        else:
            raise ValueError("Name Format Invalid")
    except ValueError as e:
        print(e)

# =============================================================================

# # 3.簡易removeprefix抓取信息
while True:
    try:
        site = input("Enter Site-2: ").strip()
        name = site.removeprefix("https://twitter.com/")
        print(f"Name: {name}")
        break
    except ValueError as e:
        print(e)

# =============================================================================

# 4.簡易group抓取信息
while True:
    try:
        site_2 = input("Enter Site-2: ").strip()
        if matches := re.search(r"^(?:http://|https://)?twitter\.com/(.+)$", site):
            name_2 = matches.group(1)
            print(f"Name-2: {name_2}")
            break
        else:
            raise ValueError("Site Format Invalid")
    except ValueError as e:
        print(e)

# =============================================================================

# 5.簡易group抓取信息
while True:
    code = input("Enter Code(LQ-XXX): ").strip()
    if matches := re.search(r"^LQ-(\d{3})$", code):
        code_num = int(matches.group(1))
        if 0 <= code_num <= 199:
            print(f"{code} Level: {code_num}🍬")
            break
        elif 200 <= code_num <= 699:
            print(f"{code} Level: {code_num}🍭")
            break
        elif 700 <= code_num <= 999:
            print(f"{code} Level: {code_num}🍯")
            break
    else:
        print("Code Format Invalid")

# =============================================================================

while True:
    password = input("Enter Password(6 - 10 characters): ").strip()
    if matches := re.search(r"^([A-Za-z0-9]{6,10})$", password):
        pw_test = matches.group(1)
        if re.search(r"^[0-9]{6,10}$", pw_test):
            print(f"Password {pw_test}: ❌ Weak")
            break
        elif re.search(r"^[a-z]{6,10}$", pw_test):
            print(f"Password {pw_test}: ❌ Weak")
            break
        elif re.search(r"^[a-z0-9]{6,10}$", pw_test):
            print(f"Password {pw_test}: ❌ Weak")
            break
        else:
            print(f"Password {pw_test}: ✅ Strong")
    else:
        print("Password Format Invalid")

# 更好的驗證版本:
while True:
    password = input("Enter Password(6 - 10 characters): ").strip()
    if matches := re.search(r"^([A-Za-z0-9]{6,10})$", password):
        pw_test = matches.group(1)
    if (re.search(r"[A-Z]", pw_test)
            and re.search(r"[a-z]", pw_test)
            and re.search(r"\d", pw_test)):
        print("✅ Strong")
        break
    else:
        print("❌ Weak")
