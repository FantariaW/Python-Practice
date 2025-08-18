# Day 4 Training: 公司活動報名與點餐系統 (Day 1 - Day 4)

def get_info(prompt_info):
    user_list = []     # 📋 用來儲存每位使用者的完整資訊（dict 組成）
    total_qty = 0      # 🔢 累加每個人的點餐份數總量（用來統計總份數）

    print("--Enter name, department, activity, main dish, beverage, order amount--")  # 📢 提示使用者輸入欄位
    while True:
        try:
            user_info = input(prompt_info).strip()  # 🗣️ 接收輸入並去除前後空白
            if user_info.lower() == 'done':        # 🛑 若輸入 'done'，就結束輸入流程
                break

            # split and strip all values
            user_name, user_department, user_activity, user_meal, user_drink, user_qty = user_info.split(",")
            user_name, user_department, user_activity, user_meal, user_drink, user_qty = [
                value.strip() for value in [  # 🧽 把每個欄位都清潔一下（去空白）
                    user_name, user_department, user_activity, user_meal, user_drink, user_qty
                ]
            ]

            # using for if-else
            valid_info = user_name.isalpha() and user_department.isalpha()  # ✅ 基本資料只能是英文字母
            valid_menu = user_activity.isalpha() and user_meal.isalpha() and user_drink.isalpha()  # ✅ 餐點只能是英文字母
            valid_qty = user_qty.isdigit() and int(user_qty) > 0            # ✅ 點餐份數必須是大於 0 的整數

            # write all data into info_dict, then add the dict into user_list
            if valid_info and valid_menu and valid_qty:
                info_dict = {  # 📦 建立一筆使用者點餐記錄（字典）
                    "Name": user_name.title(),              # 🧑‍💼 使用者名字（首字母大寫）
                    "Department": user_department.title(),  # 👔 所屬部門
                    "Activity": user_activity.title(),      # 🎯 報名活動
                    "Meal": user_meal.title(),              # 🍱 主餐
                    "Drink": user_drink.title(),            # 🥤 飲料
                    "Quantity": int(user_qty)               # 🔢 點餐份數（轉成整數）
                }
                user_list.append(info_dict)                 # ➕ 把這筆資料加入 user_list 裡
                # counting all quantities
                total_qty = total_qty + int(user_qty)      # ➕ 將份數累加到總數量中
            else:
                # 🚨 顯示錯誤格式訊息
                raise ValueError("All user information and menus should be string, order amount should be numeric!!!")

        except ValueError as error_msg:
            print(error_msg)  # 💬 捕捉錯誤並回應使用者提示訊息

    return user_list, total_qty  # 🎁 回傳兩個東西：所有使用者資料 + 總點餐份數


def main():
    prompt_info = ">> "  # 多一步定義，更清晰易懂
    user_list, total_qty = get_info(prompt_info)  # 🎙️ 啟動表單輸入函式並接收回傳值

    for each_user_dict in user_list:
        # 🖨️ 印出每位使用者的所有欄位資訊，用分隔格式～
        print(f"👤", " | ".join([f"{each_key}: {each_value}" for each_key, each_value in each_user_dict.items()]))

    print("-" * 80)  # ✨ 分隔線
    print(f"📊 All orders count: ", total_qty)  # 🔢 總共點了幾份餐點～


main()  # 🚀 主程式啟動，開始運行！
