# Day 3 綜合練習：水果進貨 + 保质期 + 清單輸出
# 使用 while + for + .join() + tuple，訓練資料輸入與整理邏輯

# 🔧 定義一個初始值函數，返回 i 計數器 和 水果清單 list
def value():
    i = 0  # 用於 for loop 編號（可選）
    fruit_list = []  # 用來儲存水果名稱的 list
    return i, fruit_list


# 🧠 主程式 main()：負責水果名稱輸入 + 愛心輸出
def main():
    i, fruit_list = value()

    print("Enter fruit(Type in 'done' to stop): ")  # 提示用戶輸入水果
    while True:
        user_fruit = input(">> ").strip()  # 去除空白
        if user_fruit.lower() == "done":  # 結束指令
            break
        else:
            fruit_list.append(user_fruit)  # 加入清單

    # 用 .join() + list comprehension 將所有水果印出（每個首字母大寫，💗分隔）
    print("💗".join([user_fruit.title() for user_fruit in fruit_list]))

    # 備用：for + 計數列出所有水果（目前已改用 join 更優雅）
    # for user_fruit in fruit_list:
    #     i += 1
    #     print(f"Fruit {i}: {user_fruit}")


main()


print("---------------------------------------------------------------------------------------------------------------")


# 🍑 Part 2：輸入水果 + 保質天數，用 tuple 儲存進 list
fruit2_list = []

print("Enter fruit and shelf day(Type in 'done' to stop): ")
while True:
    fruit_info = input(">> ").strip()
    if fruit_info.lower() == "done":
        break
    try:
        fruit_name, fruit_day = fruit_info.split(",")  # 用 , 分割水果名與天數
        fruit_name = fruit_name.strip().title()  # 去除空白並首字母大寫
        fruit_day = fruit_day.strip()

        if fruit_day.isdigit() and int(fruit_day) > 0:  # 確保是正整數
            fruit2_list.append((fruit_name, int(fruit_day)))  # 以 tuple 存入 list
        else:
            print("Date must be numeric and greater than 0!🍓")  # 輸入錯誤提示
    except ValueError:
        print("Syntax Error")  # split 失敗時提示格式錯誤

# 🍉 使用 for 解包 tuple，依序列出所有水果與保質期
for fruit_name, fruit_day in fruit2_list:
    print(f"{fruit_name} Could be saved for {fruit_day} days.")
