# Lesson 8 regular expression: endswith(), re.search()
import re


# ❗
# r  -  raw string
# ^  -  開頭從這裏開始
# $  -  結尾到這裏結束
# +  -  至少包含 1個 以上的字串
# \  -  用於跳脫字元
# email = input("Email: ").strip()
# if re.search(r"^.+@.+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")

# =============================================================================

# ❗[^@]  -  允許包含除了 '@' 以外的任何字串
# email = input("Email: ").strip()
# if re.search(r"^[^@]+@[^@]+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")

# =============================================================================

# ❗{2}  -  至少包含 2 個字符
# ❗*  -  允許 0個 或 多個 字符
# email = input("Email: ").strip()
# if re.search(r"^.{2}.*@[^@]+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")

# =============================================================================

# ❗[a-z]  -   要求輸入 a - z 之間
# ❗[A-Z]  -   要求輸入大寫 A - Z 之間
# ❗[0-9]  -   要求輸入 0 - 9 之間
# ❗下劃綫 _  -  就是一個單純的允許使用 下劃綫 的符號
# ❗\w  -  所有的文字
# ❗|  -  or 的意思 和 if else 的 | 一樣，但是不能帶空格，否則 r string 會識別字串包含空格
# ❗re.IGNORECASE  -  可以縮寫成 re.I, 忽略大小寫
# email = input("Email: ").strip()
# if re.search(r"^\w+@[A-Za-z0-9_]+\.(edu|com)$", email, re.IGNORECASE):
#     print(f"Valid, {email}")
# else:
#     print("Invalid")

# =============================================================================

# ❗()  -  一個 群組 group, 括號可以把一段規則視為一個整體來應用修飾符（像 ?, +, {n,m}）
# ❗?  -  問號前面的 元素 可以出現 0 次 或者 1 次 (?:	0 或1次, *: 0 或多次, +: 1 或多次)
email = input("Email: ").strip()
if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# =============================================================================

# email = input("Email: ").strip()
#
# user_name, domain = email.split("@")
# if user_name and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")


