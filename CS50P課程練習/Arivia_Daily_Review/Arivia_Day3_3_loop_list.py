# Day 3 Practice：每日點名報告系統 🧑‍💼📝
# 使用 while + for + .join() + tuple 分類員工出勤與缺勤狀態

# 🧰 定義初始函式：建立三個 list（出勤名單、缺勤名單、完整資料）
def value():
    employee_list = []  # 儲存所有資料的總清單（tuple 結構）
    employee_present_list = []  # 儲存出勤員工的名字
    employee_absent_list = []  # 儲存缺勤員工的名字
    return employee_present_list, employee_absent_list, employee_list


# 🎯 主邏輯 main()
def main():
    employee_present_list, employee_absent_list, employee_list = value()

    print("Enter employee's name, status with 'present' or 'absent', "
          "and how many days they have been worked('done' to stop): ")

    while True:
        employee_info = input(">> ")  # 例如：Alice, present, 5

        if employee_info.lower() == "done":
            break

        try:
            # 拆分輸入內容為三部分
            employee_name, employee_status, employee_workday = employee_info.split(",")

            # 格式清理與格式化
            employee_name = employee_name.strip().title()
            employee_status = employee_status.strip().title()
            employee_workday = employee_workday.strip()

            # 資料驗證與分類存入不同清單
            if employee_status.lower() == "present" and employee_workday.isdigit() and int(employee_workday) > 0:
                employee_list.append((employee_name, employee_status, int(employee_workday)))
                employee_present_list.append(employee_name)
            elif employee_status.lower() == "absent" and employee_workday.isdigit() and int(employee_workday) > 0:
                employee_list.append((employee_name, employee_status, int(employee_workday)))
                employee_absent_list.append(employee_name)
            else:
                print("Status must type in 'present' or 'absent', Work days must greater than 0!!!")

        except ValueError:
            print("Syntax Error!!! 格式請用：名字, 狀態, 天數")

    # 📋 印出所有完整記錄資料（tuple 解包）
    for employee_name, employee_status, employee_workday in employee_list:
        print(f"{employee_name}, {employee_status}, {employee_workday}")

    # 💼 出勤清單輸出，使用 .join() 串接名字
    print("Today's Attendance Report: ", end="")
    print("💼".join([employee_name.title() for employee_name in employee_present_list]))

    # ❌ 缺勤清單輸出
    print("Today's Absence Report: ", end="")
    print("❌".join([employee_name.title() for employee_name in employee_absent_list]))


main()
