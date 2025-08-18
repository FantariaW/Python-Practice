# 2025/05/21
# Arivia Lesson 3 Final Test

# define dictionary for all guest's name, age, department, favorite beverage 1, favorite beverage 2
def guest_info_main_dict():
    all_guest_list = []             # 📝 用來儲存所有訪客的總清單（每位是個 dict！）
    guest_info_subdict = {}         # 🧠 這是暫時存單位訪客資料的小字典（會被覆蓋～別拿來存多個人喔！）
    guest_beverage_sublist = []     # 🥤 儲存訪客最愛的兩款飲料～像是 ["Coffee", "Juice"]

    return all_guest_list, guest_info_subdict, guest_beverage_sublist


def main():
    # function call: guest_info_dict
    all_guest_list, guest_info_subdict, guest_beverage_sublist = guest_info_main_dict()

    print("---You may type in 'done' to stop program---")
    print("Please enter Guest information: ")
    while True:
        guest_info = input(">>").strip()  # ✨ 用戶輸入格式：名字,年齡,部門,飲料1,飲料2

        if guest_info.lower() == 'done':
            break  # 🏁 輸入 'done' 結束輸入迴圈（掰掰～）

        # define 5 values for guest information
        try:
            (guest_name,
             guest_age,
             guest_department,
             guest_beverage1,
             guest_beverage2) = guest_info.split(",")  # 🧩 拆成 5 塊資料（靠逗號分隔）

            # 🧼 清理每個輸入值（去頭尾空格）
            guest_name = guest_name.strip()
            guest_age = guest_age.strip()
            guest_department = guest_department.strip()
            guest_beverage1 = guest_beverage1.strip()
            guest_beverage2 = guest_beverage2.strip()

            # ✅ 檢查年齡是否為正整數 & 名字不重複
            if guest_age.isdigit() and int(guest_age) > 0 and guest_name not in guest_info_subdict:
                # 🍹 把飲料變漂亮（首字大寫）並存進小 list
                guest_beverage_sublist = [guest_beverage1.title(), guest_beverage2.title()]

                # # 🏷 建立每位訪客的小資料字典（Name / Age / Department / Drinks）
                # guest_info_subdict = {"Name": guest_name.title(),
                #                       "Age": int(guest_age),
                #                       "Department": guest_department.title(),
                #                       "Drinks": guest_beverage_sublist}

                # # 📥 加入總清單 all_guest_list（每次 append 一個完整 dict！）
                # all_guest_list.append(guest_info_subdict)

                # all_guest_list.append({...})  # 直接建立新 dict 丟進去，這樣做更乾淨，更直接，更專業
                all_guest_list.append({"Name": guest_name.title(),
                                       "Age": int(guest_age),
                                       "Department": guest_department.title(),
                                       "Drinks": guest_beverage_sublist})
            else:
                print("Age must be integer and greater than 0!")  # 🚫 年齡不對或名字重複會拒收！
        except ValueError:
            print("Syntax Error!!!")  # 😵 split 拆不開 5 個項目時會報錯提示～

    # print(all_guest_list)  # 🧾 （原始結構輸出備用）

    for guest_info_subdict in all_guest_list:  # 🌟 開始逐個印出訪客資料啦！
        name = guest_info_subdict["Name"]      # 🎀 訪客名字
        age = guest_info_subdict["Age"]        # 🎂 年齡
        department = guest_info_subdict["Department"]  # 🏢 所屬部門
        drinks = guest_info_subdict["Drinks"]  # 🥤 飲料偏好（是個小 list！）

        print(f"Name: {name} ({age})\n"              # 📄 美化輸出第一行
              f"Department: {department}\n"          # 🧭 部門列
              f"Drinks: " + " 💗 ".join(drinks) +    # 🍹 飲料們中間插入可愛的 💗
              "\n" + "=" * 40)                       # 🎀 分隔線～像個 mini card！


main()
