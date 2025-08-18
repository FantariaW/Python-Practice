# Day 4 Training: advanced dict & list training
# 🎓 本練習專注於統計任務！目標是用 list of dict 結構，進行主餐、飲料與部門的統計處理！

# Day 4 Training 1: 統計每種主餐出現次數 (list of dict)
def all_meal():
    count_dict = {}  # 📊 用來記錄每種主餐出現的次數（Key 是主餐名，Value 是出現次數）

    meal_list = [
        {"Meal": "  beEf riCe "},     # 😴 有空格、有大小寫混亂
        {"Meal": "spaghetti"},
        {"Meal": "beef rice"}         # 😱 和第一筆其實是一樣的餐點
    ]

    for meal in meal_list:
        meal_name = meal["Meal"].strip().title()  # 🧼 清除空格並格式化為標準寫法（首字大寫）
        if meal_name in count_dict:
            count_dict[meal_name] += 1  # ➕ 如果已存在，次數 +1
        else:
            count_dict[meal_name] = 1   # 🌱 如果第一次出現，就設為 1

    return count_dict  # 🎁 回傳整理好的統計字典


# Day 4 Training 2: 統計每種飲料的總訂購數 (list of dict)
def all_drink():
    count_dict_2 = {}  # 📦 用來記錄每種飲料被點了幾杯（Key 是飲料名，Value 是總杯數）

    drink_list = [
        {"Drink": "red tea", "Quantity": 2},
        {"Drink": "orange juice", "Quantity": 1},
        {"Drink": "red tea", "Quantity": 3}
    ]

    for drink_type in drink_list:
        drink_name = drink_type["Drink"].strip().title()  # 🧃 飲料名稱
        drink_qty = drink_type["Quantity"]                # 🧮 訂購杯數
        if drink_name in count_dict_2:
            count_dict_2[drink_name] += drink_qty    # ➕ 若已出現過，加上這次的數量
        else:
            count_dict_2[drink_name] = drink_qty     # 🌱 首次出現，設為該次數量

    return count_dict_2  # 🎁 回傳飲料總訂購統計


# Day 4 Training 3: 統計每個部門報名幾人 (list of dict)
def all_department():
    count_dict_3 = {}  # 🏢 紀錄每個部門報名人數（Key 是部門名，Value 是人數）

    user_list = [
        {"Department": "工程部"},
        {"Department": "設計部"},
        {"Department": "工程部"},
        {"Department": "行銷部"}
    ]

    for department_key in user_list:
        department_value = department_key["Department"].strip().title()  # 🏷️ 取出部門名稱
        if department_value in count_dict_3:
            count_dict_3[department_value] += 1  # ➕ 已出現：人數 +1
        else:
            count_dict_3[department_value] = 1   # 🌱 首次出現：人數設為 1

    return count_dict_3  # 🎁 回傳部門報名統計


def main():
    # Day 4 Training 1: 統計每種主餐出現次數 (list of dict)
    count_dict = all_meal()
    print("📦 Main-Dish Count: ")
    print("\n".join(f"{key}: {value}" for key, value in count_dict.items()))  # 🍝 每種主餐出現幾次～

    print("=" * 80)

    # Day 4 Training 2: 統計每種飲料的總訂購數 (list of dict)
    count_dict_2 = all_drink()
    print("🥤 Beverage Count: ")
    print("\n".join(f"{key_2}: {value_2}" for key_2, value_2 in count_dict_2.items()))  # 🧃 每種飲料被點幾杯～

    print("=" * 80)

    # Day 4 Training 3: 統計每個部門報名幾人 (list of dict)
    count_dict_3 = all_department()
    print("🏢 Department Count: ")
    print("\n".join(f"{key_3}: {value_3}" for key_3, value_3 in count_dict_3.items()))  # 👥 各部門報名人數一覽～


main()  # 🚀 啟動主程式，依序呼叫三個統計任務
