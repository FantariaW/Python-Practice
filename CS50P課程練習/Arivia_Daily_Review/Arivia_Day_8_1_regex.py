# Day 8 Training: regex

# Day 8 Training:
import re

# # 1: 驗證電話號碼
phone = input("Enter Phone Number: ").strip()
if re.search(r"^\d{10}$", phone):
    print(phone + ": 10-digit phone number verified!")
else:
    print("Invalid Format")

# # 2: 驗證名字必須在 A - Z 之間，且首字母必須大寫
name = input("Enter Your Name: ").strip()
if re.search(r"^[A-Z][a-z]*$", name):
    print(name + ": name verified!")
else:
    print("Invalid Name")

# 3: 驗證密碼不能爲空，且字符至少 4個 最多 8個
password = input("Enter Password: ").strip()
if re.search(r"^\S{4,8}$", password):
    print("password verified")
else:
    print("Invalid Password")
