# Day 3 Practice：早餐訂單收集系統 🥐🍩
# 使用 while + for + .join() + tuple + sum 整合所有 Day 3 技能！


# 🧰 定義初始變數的函數：回傳總數計數器 + 早餐清單 list
def value():
    full_count = 0                 # 計算總份數
    breakfast_list = []           # 儲存所有 (早餐名稱, 份數) 的 tuple
    return full_count, breakfast_list

# 🎯 主邏輯開始


def main():
    full_count, breakfast_list = value()  # 初始化變數

    print("Enter Breakfast name and count('done' to stop): ")

    while True:
        breakfast_info = input(">> ")  # 接收輸入

        if breakfast_info.lower() == "done":  # 結束條件
            break

        try:
            # 使用 , 分割輸入：例如 "Bagel, 2"
            breakfast_name, breakfast_count = breakfast_info.split(",")

            # 清除空白與格式化：首字大寫、份數轉整數
            breakfast_name = breakfast_name.strip().title()
            breakfast_count = breakfast_count.strip()

            # 檢查是否為數字且 > 0
            if breakfast_count.isdigit() and int(breakfast_count) > 0:
                breakfast_list.append((breakfast_name, int(breakfast_count)))  # 儲存為 tuple
                full_count += int(breakfast_count)  # 累加總份數
            else:
                print("Count must be a number greater than 0!")
        except ValueError:
            print("Syntax Error!!! 請使用：早餐名, 數量")

    # 📦 輸出所有訂單條目
    for breakfast_name, breakfast_count in breakfast_list:
        print(f"{breakfast_name} - {breakfast_count} servings")

    # 🍩 輸出所有早餐名稱，用 emoji 分隔
    print("🍽Breakfast Items: ", "🍩".join([breakfast_name for breakfast_name, breakfast_count in breakfast_list]))

    # 🧮 輸出總份數
    print(f"Total Servings: {full_count} servings")


main()
