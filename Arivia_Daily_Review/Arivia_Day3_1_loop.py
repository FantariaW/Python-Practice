# while + for + .join()


# 🌱 定義一個初始化函式，回傳 i（計數器）與 name_list（名字清單）
def value():
    i = 0  # 計數器，從 0 開始，之後會每加一個名字就 +1
    name_list = []  # 用來存放所有輸入的名字
    return i, name_list  # 將兩個變數傳回給 main()


# 🌟 主函式開始運作
def main():
    i, name_list = value()  # 從 value() 取得初始值

    print("Enter your name (Type in 'done' to stop): ")  # 溫柔提示使用者輸入名字

    # 🔁 無限迴圈等待輸入，直到使用者輸入 done 為止
    while True:
        user_name = input(">> ").strip()  # 接收輸入並去除前後空白

        if user_name.lower() == "done":  # 若輸入為 done（不分大小寫），則停止
            print("Program Stop!")  # 打印停止提示
            break  # 跳出 while 迴圈
        else:
            name_list.append(user_name)  # 否則把名字加入清單中
            continue  # 繼續下一輪輸入

    # 🎉 輸入完成後，開始列印每一個名字
    for name in name_list:
        if i >= 0:  # 保護性條件（其實這句可以省略，但留著也沒錯～）
            i += 1  # 計數器 +1
            print(f"Name {i}: {name.title()}")  # 輸出名字，並讓首字母大寫更好看！


# 🚀 啟動主函式！
main()


print("---------------------------------------------------------------------------------------------------------------")


# 🌸 建立一個用來存放 (名字, 年齡) 的空清單
user_list = []

# 📢 提示使用者輸入格式為「名字, 年齡」，輸入 done 可結束
print("Enter name and age (Type in 'done' to stop): ")

# 🔁 使用 while True 讓使用者可以持續輸入資料
while True:
    user_answer = input(">> ").strip()  # 🧼 去除輸入前後空白

    # ❌ 如果輸入是 'done'（不分大小寫），就結束程式
    if user_answer.lower() == "done":
        print("Program Stop!")  # ✨ 小提示輸出
        break

    try:
        # ✂️ 使用 split(",") 將名字與年齡分開
        user_name2, age = user_answer.split(",")

        # 🎀 美化資料：名字首字母大寫 + 去除空格
        user_name2 = user_name2.strip().title()
        age = age.strip()

        # ✅ 檢查年齡是否為正整數
        if age.isdigit() and int(age) > 0:
            # 🐿️ 將格式正確的資料以 tuple 形式加入清單中
            user_list.append((user_name2, int(age)))
        else:
            # 🚫 年齡格式錯誤提示
            print("Invalid Input! Age must be numeric!!!")
    except ValueError:
        # 🚫 如果 split() 出錯（例如沒逗號），就捕捉錯誤
        print("Must enter name and age!!!")

# 🖨️ 輸出名單，每筆格式為：Name: xxx, Age: xx
for user_name2, age in user_list:
    print(f"Name: {user_name2}, Age: {age}")


print("---------------------------------------------------------------------------------------------------------------")


# 使用.join()將所有人的名字用 "💗" 連接成一行，印出愛心名單！
names_list = []
print("Enter names(Type in 'done' to stop): ")

# 與任務1邏輯一致
while True:
    user_names = input(">> ")

    if user_names.lower() == "done":
        break
    else:
        names_list.append(user_names)
        continue

# 這是先把整個 list 用 "💗" 串起來，再整體 .title()
# 會讓整段輸出變成「每個單字的首字母大寫」
# 缺點是：如果使用者名字是複數詞，可能會把愛心兩邊一起格式化（不夠細緻）
print("💗".join(names_list).title())

# 這是先用 list comprehension（列表推導式）逐個 .title()，再 join 起來
# 格式最乾淨、效果最準確，每一個名字都被單獨修飾
# 這是專業工程師會喜歡的寫法 ✨
# 📌 輸出效果一樣，但細節完美！
print("💗".join([user_names.title() for user_names in names_list]))
