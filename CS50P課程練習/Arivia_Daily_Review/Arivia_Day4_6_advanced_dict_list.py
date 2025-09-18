# Day 4 Training: advanced dict & list training
# 📚 本單元練習進階的統計應用，重點是用 list of dict 處理多欄分類統計與統整資訊！

# Day 4 Training 1: 每位使用者的總點餐數 (list of dict)
def count_user(user_list):
    count_dict = {}  # 📦 用來記錄每位使用者點的總份數

    for user_info in user_list:
        user_name = user_info["Name"].strip().title()  # 🧽 去除空白並轉為標準格式（首字大寫）
        user_qty = user_info["Quantity"]               # 🔢 抓出使用者點的份數
        if user_name in count_dict:
            count_dict[user_name] += user_qty          # ➕ 有紀錄就累加
        else:
            count_dict[user_name] = user_qty           # 🌱 沒紀錄就新增一筆

    return count_dict  # 🎁 回傳每位使用者點餐總數的 dict


# Day 4 Training 2: 每種活動參加人數 (list of dict)
def count_activity(activity_list):
    count_act_dict = {}  # 📋 紀錄每種活動有幾個人參加

    for activity_dict in activity_list:
        activity_key_name = activity_dict["Activity"].strip().title()  # 🧼 處理活動名稱格式
        if activity_key_name in count_act_dict:
            count_act_dict[activity_key_name] += 1     # ➕ 已出現則人數 +1
        else:
            count_act_dict[activity_key_name] = 1      # 🌱 第一次出現，從 1 開始計算

    return count_act_dict  # 🎁 回傳每種活動的人數統計


# Day 4 Training 3: 多欄分類統計（主餐 + 部門） (list of dict)
def count_department_meal(department_meal_list):
    count_both_dict = {}  # 🧠 巢狀 dict：外層是部門，內層是主餐和數量

    for department_meal_dict in department_meal_list:
        department_key_name = department_meal_dict["Department"]  # 🏢 部門名稱
        department_key_meal = department_meal_dict["Meal"]         # 🍱 主餐名稱

        if department_key_name not in count_both_dict:
            count_both_dict[department_key_name] = {}  # 🌱 若部門第一次出現，建立內層 dict

        if department_key_meal in count_both_dict[department_key_name]:
            count_both_dict[department_key_name][department_key_meal] += 1  # ➕ 主餐已存在，數量 +1
        else:
            count_both_dict[department_key_name][department_key_meal] = 1   # 🌱 主餐第一次出現，設為 1

    return count_both_dict  # 🎁 回傳部門 ➜ 主餐 ➜ 數量 的巢狀 dict 統計表


def main():
    # Day 4 Training 1: 每位使用者的總點餐數 (list of dict)
    user_list = [
        {"Name": "   aliCE", "Quantity": 2},  # 👤 名字格式混亂，測試標準化處理
        {"Name": "Bob", "Quantity": 1},
        {"Name": "Alice", "Quantity": 3}
    ]
    count_dict = count_user(user_list)
    print("-User Count-")
    print("\n".join(f"{key_user}: {value_qty}" for key_user, value_qty in count_dict.items()))  # ✅ 印出每個使用者的點餐總數

    print("\n" + "=" * 80 + "\n")  # ✨ 美化分隔線讓報表更清晰

    # Day 4 Training 2: 每種活動參加人數 (list of dict)
    activity_list = [
        {"Activity": "踏青"},
        {"Activity": "聚餐"},
        {"Activity": "踏青"}
    ]
    count_act_dict = count_activity(activity_list)
    print("-Activity Count-")
    print("\n".join(f"{key_act}: {value_act}" for key_act, value_act in count_act_dict.items()))  # ✅ 印出每種活動的參與人數

    print("\n" + "=" * 80 + "\n")  # ✨ 分隔線繼續美化視覺～

    # Day 4 Training 3: 多欄分類統計（主餐 + 部門） (list of dict)
    department_meal_list = [
        {"Department": "設計部", "Meal": "牛肉飯"},
        {"Department": "設計部", "Meal": "牛肉飯"},
        {"Department": "設計部", "Meal": "義大利麵"},
        {"Department": "工程部", "Meal": "義大利麵"},
        {"Department": "工程部", "Meal": "牛肉飯"}
    ]
    count_both_dict = count_department_meal(department_meal_list)
    print("-Department & Meal-")
    for each_dict_key in count_both_dict:
        inner_dict = count_both_dict[each_dict_key]  # 🧩 把內層 dict 拿出來（每個部門的餐點分類）
        print(f"{each_dict_key}: ", end="")  # 🏢 印出部門名稱
        print(", ".join(f"{key_meal}: {value_meal}" for key_meal, value_meal in inner_dict.items()))  # 🍽️ 印出每個餐點的數量


main()  # 🚀 主程式啟動，依序執行三個進階統計任務
