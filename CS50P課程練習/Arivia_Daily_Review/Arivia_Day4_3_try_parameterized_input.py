# Day 4 Training: 產品意見調查登記表
# (主題: parameterized input function, raise, except as, dict with list, function, while loop)

def get_feedback(prompt_user):
    user_list = []  # 🗃️ 用來存放每筆使用者的回饋資料（List of Dicts）

    print("---Enter name, product, tag 1, tag 2, satisfaction rate---")  # 📢 提示輸入欄位格式
    while True:
        try:
            get_info = input(prompt_user).strip()  # 🎤 接收使用者輸入＋清除前後空白字元
            if get_info.lower() == 'done':  # 🛑 輸入 'done' 就結束輸入流程
                break

            # 🧩 拆分輸入內容為五個部分（用逗號分開）
            user_name, user_product, user_tag1, user_tag2, user_rate = get_info.split(",")

            # 🧼 去除各項資料前後空白，讓輸入乾乾淨淨～
            user_name = user_name.strip()
            user_product = user_product.strip()
            user_tag1 = user_tag1.strip()
            user_tag2 = user_tag2.strip()
            user_rate = user_rate.strip()

            # ✅ 檢查名字、標籤是否是純文字（不能混進數字！）
            valid_text = user_name.isalpha() and user_tag1.isalpha() and user_tag2.isalpha()
            # ✅ 檢查評分是否為 1～10 的整數
            valid_num = user_rate.isdigit() and 1 <= int(user_rate) <= 10

            if valid_text and valid_num:
                tag_list = [user_tag1.title(), user_tag2.title()]  # 🏷️ 把兩個標籤組成 list
                user_dict = {
                    "User": user_name.title(),        # 🙋‍♂️ 使用者名稱
                    "Product": user_product.title(),  # 📦 評價的產品名稱
                    "Tags": tag_list,                 # 🏷️ 標籤清單（dict 裡嵌 list）
                    "Rating": int(user_rate)          # ⭐ 滿意度評分（1~10）
                }
                user_list.append(user_dict)   # ➕ 把這筆資料加入總名單中
            else:
                # 🚨 若輸入格式錯誤，主動拋出錯誤給 except 處理
                raise ValueError("Name, tag must be string, rate must be number between 1 - 10")
        except ValueError as error_msg:
            print(error_msg)  # ❗ 顯示錯誤訊息給使用者看（溫柔糾正～）

    return user_list  # 🎁 回傳所有有效填寫的資料


def main():
    user_list = get_feedback(">> ")  # 📥 呼叫表單收集函式，開始填寫！

    for each_user in user_list:
        print(f"🧑 User: {each_user['User']}")  # 👤 使用者名稱
        print(f"📦 Product: {each_user['Product']}")  # 📦 評價的產品
        print(f"🏷️ Tags: " + ", ".join([f"{each_tag}" for each_tag in each_user["Tags"]]))  # 🏷️ 兩個關鍵字標籤,list拆出來印
        print(f"⭐ Rating: {each_user['Rating']}")  # ⭐ 滿意度分數（1~10）

        # 🎨 美化分隔線（讓多筆資料不會黏在一起！）
        print("=" * 40)


main()  # 🚀 啟動主程式～讓大家開始填回饋啦！
