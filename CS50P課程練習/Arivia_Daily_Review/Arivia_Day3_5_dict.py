# Day 3 Practice 1 : dict + for + items()
menu = {
    "Salad": 8,
    "Burger": 12,
    "Ramen": 10
}
# 第一種寫法：基本輸出格式 + 處理 None 為 "N/A"
for key, value in menu.items():
    print(key + ":", value if value is not None else "N/A")

print("-" * 10)
# 第二種寫法（延伸）：將價格轉為字串後使用 join 組合
print("\n".join([f"{key}: {value if value is not None else "N/A"}" for key, value in menu.items()]))


# ======================================================================================================================
print("=" * 100)


# Day 3 Practice 2: dict + for + key()
# 🧃 小任務 2：飲料機列印器
# 使用 dict 儲存飲料是否可用，使用 if 過濾 True 狀態的 key
drinks = {
    "Coke": True,
    "Sprite": True,
    "Juice": False,
    "Coffee": True
}

print("Available Drinks: ", end="\n")
# 使用 .items() 遍歷，篩選 True 的 key 並印出
for key, value in drinks.items():
    if value is True:
        print(key)
    # # 備註：也可以簡寫為 if value:
    # # 甚至可以使用三元條件寫成 print(key if value else "")
    # if value: print(key)
    # print(key if value is True else "")


# ======================================================================================================================
print("=" * 100)


# Day 3 Practice 3: dict + input + if-elif-else
# 📞 小任務 3：員工分機查詢系統
# 使用 input 接收查詢名稱，判斷是否在 dict 中
employees = {
    "Alice": "101",
    "Bob": "102",
    "Clara": "103"
}

# 接收使用者輸入 + 處理大小寫與空格
key_name = input("Type in name: ").strip().title()

# 如果有這個員工，就印出分機號碼
if key_name.lower().title() in employees.keys():
    print(f"Found {key_name.lower().title()}!!!")
    for key, value in employees.items():
        if key_name.lower().title() == key:
            print(f"{key}'s extension: {value}")
else:
    print(f"{key_name} Not Found!")

# # 將用戶輸入寫入dictionary
# employees["AAA"] = input(">> ").strip()
# for key, value in employees.items():
#     print(f"{key}: {value}")
