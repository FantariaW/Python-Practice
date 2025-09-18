# Day 8 Training: group

# Day 8 Training:
import re


# 名字首字母大寫練習
while True:
    try:
        name = input("Name: ").strip()
        match = re.search(r"^[A-Z][a-z]*$", name)
        if match:
            print(name)
            break
        else:
            raise ValueError("Syntax Error")
    except ValueError as e:
        print(e)

# 簡易email驗證
while True:
    try:
        email = input("Email: ").strip()
        match = re.search(r"^\w+@(\w+\.)?\w+\.(com|ca)$", email, re.IGNORECASE)
        if match:
            print(email)
            break
        else:
            raise ValueError("Email Format Error")
    except ValueError as e:
        print(e)

# 簡易group練習
while True:
    try:
        full_name = input("Full Name: ").strip()
        match = re.search(r"^ *([A-Z][a-z]*) *, *([A-Z][a-z]*) *$", full_name)
        if match:
            first = match.group(1)
            last = match.group(2)
            print(f"Your Full Name -> {last} {first}")
        else:
            raise ValueError("Name Format Error")
    except ValueError as e:
        print(e)
