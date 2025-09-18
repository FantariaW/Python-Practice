# Day 4 Training: 水果訂購登記系統
# (主題：parameterized input function + function + while + dict with list + list of dict + raise, except...as...)
def get_order(prompt_order):
    order_list = []  # 🧺 用來儲存每位顧客的訂單資料，每筆是一個 dict！

    print("---Enter name, fruit 1, fruit 2, amount 1, amount 2---")  # 📢 提示輸入格式
    while True:
        try:
            user_info = input(prompt_order).strip()  # 🎤 使用者輸入（去掉首尾空白）
            if user_info.lower() == 'done':  # 🛑 若輸入 done 就跳出迴圈
                break

            # 🧩 拆解輸入內容為五個部分（用逗號分開）
            user_name, fruit1, fruit2, amount1, amount2 = user_info.split(",")

            # 🧼 各欄位清洗空白
            user_name = user_name.strip()
            fruit1 = fruit1.strip()
            fruit2 = fruit2.strip()
            amount1 = amount1.strip()
            amount2 = amount2.strip()

            # ✅ 檢查數量是否為正整數
            valid_amount = amount1.isdigit() and int(amount1) > 0 and amount2.isdigit() and int(amount2) > 0
            # ✅ 檢查名字與水果是否為純英文文字（不能有數字喔～）
            valid_text = user_name.isalpha() and fruit1.isalpha() and fruit2.isalpha()

            if valid_amount and valid_text:
                fruit_list = [fruit1.title(), fruit2.title()]  # 🍎 水果名字首字大寫變得漂漂亮亮～
                amount_list = [int(amount1), int(amount2)]    # 🔢 數量轉成真正的整數

                # 📦 整理成一份完整的訂單字典
                info_dict = {
                    "Name": user_name.title(),
                    "Fruits": fruit_list,
                    "Quantities": amount_list
                }

                order_list.append(info_dict)  # 🧾 加入訂單總清單中
            else:
                # 🚨 若格式錯誤，主動丟出 ValueError 錯誤
                raise ValueError("Name, fruit must be string, amount must be numeric!!!")
        except ValueError as error_msg:
            print(error_msg)  # 🧯 捕捉錯誤並顯示溫柔提示訊息

    return order_list  # 🎁 回傳所有有效訂單


def main():
    order_list = get_order(">> ")  # 📥 取得所有使用者輸入訂單
    for each_dict in order_list:
        qty1, qty2 = each_dict["Quantities"]  # 🔢 取出兩項水果的數量

        print(f"🍓 Name: {each_dict['Name']}")  # 🎀 顯示顧客名字
        print(f"🥭 Fruits Ordered: " + ", ".join(f"{f}" for f in each_dict["Fruits"]))  # 🍍 水果清單美美地列出
        print(f"📦 Quantities: {qty1} + {qty2} = {qty1 + qty2}")  # ➕ 計算兩個水果的總數量

        print("=" * 40)  # 🎨 分隔線裝飾用～

        # # 🧾 備用萬用印出方式（已註解）
        # for key, value in each_dict.items():
        #     print(f"{key}: {value if value is not None else 'N/A'}")


main()  # 🚀 啟動主程式（開始點餐啦！）
