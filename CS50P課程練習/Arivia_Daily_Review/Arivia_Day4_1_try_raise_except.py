# Day 4 Training:

# Training 1: 錯誤舉報系統 (主題：raise, except...as...)
def get_age(prompt_age):
    print("Enter user age('done' to stop): ")
    while True:
        try:
            age = input(prompt_age)  # 🎤 讓使用者輸入年齡
            if age.lower() == 'done':
                age = None if age is None else "N/A"  # 🙅‍♀️ 若輸入 done，就跳出並設為 N/A（表示沒輸入數字）
                break
            if age.isdigit() and int(age) > 0:  # ✅ 合法數字且大於 0 才接受
                break
            else:
                raise ValueError("Age must be numeric and greater than 0!!!")  # 🚨 自己丟出錯誤！
        except ValueError as error_msg:
            print("Syntax Error!!!", error_msg)  # 🛠 捕捉錯誤並顯示提示訊息

    return age  # 🎁 回傳年齡或 N/A


# Training 2: 錯誤記錄員 (主題：except ... as ...)
def get_num(prompt_num):
    print("Enter a number: ")
    while True:
        try:
            num = int(input(prompt_num))  # 🔢 直接將輸入轉為整數（錯了就會跳 except）
            if num is not str:  # 🧠 雖然這行邏輯有點多餘，但還是加個保險判斷
                break
        except ValueError as error_msg2:
            print(error_msg2)  # ⚠️ 顯示錯誤細節給使用者看（讓他知道哪裡輸入錯啦～）

    return num  # 🎁 回傳正確數字


# Training 3: 報表自動問答機 (主題：parameterized input function + function + while + list with dict)
def get_info(prompt_info):
    info_list = []  # 📋 建立一個空 list 用來儲存每位員工的資訊（用 dict 表示）

    print("Enter staff's name and department: ")
    while True:
        try:
            staff_info = input(prompt_info).strip()  # 🎤 輸入格式：名字,部門
            if staff_info.lower() == 'done':  # 🛑 輸入 done 就結束
                break

            staff_name, staff_department = staff_info.split(",")  # 🧩 用逗號分割成兩項
            staff_name = staff_name.strip()
            staff_department = staff_department.strip()

            if staff_name.isalpha() and staff_department.isalpha():  # ✅ 確保輸入為純文字（不能有數字喔～）
                info_list.append({
                    "name": staff_name.title(),
                    "department": staff_department.title()
                })  # 📦 加入 list，記錄每位員工的資料
            else:
                raise ValueError("Name and Department must be string!!!")  # 🚨 如果格式錯誤，直接報錯提示
        except ValueError as error_msg3:
            print(error_msg3)  # 💡 顯示錯誤訊息（像有多個逗號、空格、數字等）

    return info_list  # 🎁 回傳完整員工資料表


# ======================================================================================================================


# All Training output:
def main():
    # Training 1 output
    age = get_age(">> ")  # 🧪 呼叫第一個測試：年齡輸入
    print(f"User age is: {age}")  # 📝 顯示結果

    # -------------------------------
    print("=" * 80)  # 🎨 美化分隔線～
    # -------------------------------

    # Training 2 output
    num = get_num(">> ")  # 🧪 呼叫第二個測試：數字輸入
    print(f"Correct number is: {num}")  # 📝 顯示結果

    # -------------------------------
    print("=" * 80)  # 🎨 分隔線 Part 2
    # -------------------------------

    # Training 3 output
    info_list = get_info(">> ")  # 🧪 呼叫第三個測試：員工名單填寫

    print(info_list)  # 🧾 原始結構輸出（List of Dicts）
    for each_dict in info_list:
        # 💌 美化輸出：每一筆員工資料都印得漂漂亮亮！
        print(", ".join(
            f"{key.title()}: {value if value is not None else 'N/A'}" for key, value in each_dict.items()
        ))


main()  # 🚀 啟動主程式！
