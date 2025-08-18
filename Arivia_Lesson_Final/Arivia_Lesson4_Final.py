# Day 4 Training also Final: 寵物小舖點心統計系統
# ✨ 本練習融合了多種 Day 1～4 的核心技巧：list of dict、dict with list、巢狀結構、錯誤處理與統計輸出！

def get_pet_info(prompt_pet_info):
    pet_list = []  # 📋 儲存所有使用者輸入的資料，每筆是一隻寵物的完整訂單資訊
    count_owner_dict = {}  # 🐶 儲存每位飼主總共訂購了幾包點心
    count_pet_dict = {}    # 🐾 統計每種寵物出現的次數（幾隻狗、幾隻貓～）
    count_snack_dict = {}  # 🍖 巢狀字典，統計每種寵物吃了哪種口味的點心、各幾包

    print("--Enter owner name, pet type, pet snack type, pack of snack--")  # 📢 輸入格式提示
    while True:
        try:
            pet_input = input(prompt_pet_info).strip()  # 🗣️ 接收使用者輸入＋清除空白
            if pet_input.lower() == 'done':  # 🛑 若輸入 'done' 就結束輸入流程
                break

            # 🧩 分割輸入欄位並用 title() 美化，strip() 清除多餘空格
            get_owner, get_pet, get_snack, get_pack = pet_input.split(",")
            get_owner, get_pet, get_snack, get_pack = [
                title_get_value.strip().title() for title_get_value in
                [get_owner, get_pet, get_snack, get_pack]
            ]

            # ✅ 驗證格式：文字類都要是字母；數字必須為正整數
            valid_info_text = get_owner.isalpha() and get_pet.isalpha() and get_snack.isalpha()
            valid_pack_num = get_pack.isdigit() and int(get_pack) > 0

            if valid_info_text and valid_pack_num:
                sub_pet_dict = {
                    "Owner": get_owner,           # 👩‍⚕️ 飼主姓名
                    "Pet": get_pet,               # 🐕 寵物種類
                    "Pet-Snack": get_snack,       # 🍪 點心口味
                    "Quantity": int(get_pack)     # 🔢 購買的包數（轉成整數）
                }
                pet_list.append(sub_pet_dict)     # ➕ 加入總資料清單中

                count_owner = sub_pet_dict["Owner"]
                count_pet = sub_pet_dict["Pet"]
                count_snack = sub_pet_dict["Pet-Snack"]
                count_pack = sub_pet_dict["Quantity"]

                # 🐶 統計每位飼主總共買了幾包
                if count_owner in count_owner_dict:
                    count_owner_dict[count_owner] += count_pack
                else:
                    count_owner_dict[count_owner] = count_pack

                # 🐾 統計每種寵物出現次數（飼主有幾隻狗、幾隻貓）
                if count_pet in count_pet_dict:
                    count_pet_dict[count_pet] += 1
                else:
                    count_pet_dict[count_pet] = 1

                # 🍖 巢狀結構：每種寵物 ➜ 吃了哪些點心 ➜ 幾包
                if count_pet not in count_snack_dict:
                    count_snack_dict[count_pet] = {}  # 🧺 沒這個寵物就先建立一個子字典
                if count_snack in count_snack_dict[count_pet]:
                    count_snack_dict[count_pet][count_snack] += count_pack  # ➕ 點心已出現，加總
                else:
                    count_snack_dict[count_pet][count_snack] = count_pack   # 🌱 新點心，建立並設定份數

            else:
                raise ValueError("Owner, pet, snack must be text string, pack amount must be numeric!!!")  # 🚨 錯誤輸入提示
        except ValueError as error_msg:
            print(error_msg)  # 💬 顯示錯誤訊息

    return pet_list, count_owner_dict, count_pet_dict, count_snack_dict  # 🎁 回傳所有統計資料


def main():
    prompt_pet_info = ">> "
    pet_list, count_owner_dict, count_pet_dict, count_snack_dict = get_pet_info(prompt_pet_info)

    # == Full Table Output ==
    print("==Full Info Table==")
    for info_dict in pet_list:
        print(", ".join(f"{key_info}: {value_info}" for key_info, value_info in info_dict.items()))  # 📄 美美印出每筆資料

    print("=" * 80)  # ✨ 分隔線美化報表

    # 🐶 飼主總購買數
    print("🐶 Owner Total Buys:")
    for key_owner, value_owner in count_owner_dict.items():
        print(f"{key_owner}: {value_owner}")  # 🧾 每位飼主總共買了幾包點心
    print()

    # 🐾 寵物類型出現次數
    print("🐾 Pet Type Count:")
    for key_pet, value_pet in count_pet_dict.items():
        print(f"{key_pet}: {value_pet}")  # 🐕 幾隻狗、幾隻貓～
    print()

    # 🍖 每種寵物吃了哪些口味、幾包
    print("🍖 Flavor Count per Pet:")
    for key_pet_2, value_snack in count_snack_dict.items():
        print(f"{key_pet_2} - ", end="")  # 🐶 印出寵物種類
        print(", ".join(
            f"{sub_key_snack}: {sub_value_snack}" for sub_key_snack, sub_value_snack in value_snack.items()
        ))  # 🍗 再印出該寵物吃了哪幾種點心＆數量


main()  # 🚀 啟動主程式～開張啦小舖老闆！
