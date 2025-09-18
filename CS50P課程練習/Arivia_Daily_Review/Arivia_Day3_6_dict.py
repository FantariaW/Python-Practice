# Day 3 Training: dict + input + key + if-else

# ✅ 建立學生出席資料，key 是學生名字，value 是 True (出席) 或 False (缺席)
students = {
    "Alice": True,
    "Bob": False,
    "Clara": True
}

print("Check students status: ")
while True:
    # 💬 要求使用者輸入名字，並用 strip 清除空格，lower+title 統一格式
    user_name = input(">> ").strip()
    if user_name.lower() == "done":
        break
    elif user_name.lower().title() in students:
        # 🌀 巢狀遍歷字典的 key-value，用來比對輸入者與學生名
        for key, value in students.items():
            if user_name.lower().title() == key:
                if value is True:
                    print(key, value)
                    print(f"{key} is Present!")  # 🎉 輸出出席訊息
                elif value is False:
                    print(key, value)
                    print(f"{key} is Absent!")   # ❌ 輸出缺席訊息
    else:
        print(f"Sorry! {user_name} is Not Found!")  # ❓ 若名字不在字典內，提示查無資料

# ======================================================================================================================
print("=" * 80)

# ✅ 建立庫存資料，None 代表尚未盤點
inventory = {
    "Keyboard": 25,
    "Monitor": 12,
    "Mouse": None,
    "Chair": 7
}

# 🌀 用 .items() 逐一輸出 key 與 value，如果為 None 則顯示為 "N/A"
for key, value in inventory.items():
    print(f"{key}: {value if value is not None else 'N/A'}")

# 💎 額外 bonus：印出所有商品名稱，用 join() 加入可愛分隔符
print("🔹".join([f"{key}" for key in inventory.keys()]))
