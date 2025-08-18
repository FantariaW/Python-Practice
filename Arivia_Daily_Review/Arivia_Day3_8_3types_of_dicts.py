# Day 3 Training 1: Nested dict【嵌套字典】

def dicts():
    manager = {}  # 管理部门與管理者名字對應
    task = {}     # 各個員工與他們任務列表
    all_product = []  # 存放多個 dict的 list，每個 dict 是一種商品

    return manager, task, all_product  # 一次返回三種組合統計組態


def main():
    manager, _, _ = dicts()  # 只需用 manager 字典，其余以 _ 符號忽略

    print("Enter manager's department and name('done' to stop): ")
    while True:
        staff_info = input(">> ").strip()
        if staff_info.lower() == 'done':
            break

        try:
            staff_department, staff_name = staff_info.split(" ")
            manager[staff_department] = staff_name  # 將 department 與 name 錯開後存入 dict
        except ValueError:
            print("Syntax Error!!!")

    # 輸出結果：Department: {"Manager": Name}
    for staff_department, staff_name in manager.items():
        print(f"{staff_department}: {{\"Manager\": {staff_name}}}")


main()


# ======================================================================================================================
print("=" * 80)


# Day 3 Training 2: Dict with List【字典嵌入列表】

def main2():
    _, task, _ = dicts()  # 只需用 task 字典

    print("Enter name and tasks they have('done' to stop):")
    while True:
        staff2_info = input(">> ").strip()
        if staff2_info.lower() == "done":
            break

        try:
            staff2_name, staff2_task = staff2_info.split(" ")
            staff2_name = staff2_name.strip()
            staff2_task = staff2_task.strip()

            if staff2_name not in task:
                # 如果是第一次輸入這名員工，创建空 list
                task[staff2_name] = []
            # 無論重複與否，將任務 append 進對應列表
            task[staff2_name].append(staff2_task)
        except ValueError:
            print("Syntax Error!!!")

    # 輸出格式：Name: task1, task2, task3...
    for staff2_name, staff2_task in task.items():
        print(f"\n{staff2_name.title()}", end=": ")
        print(", ".join([f"{i}" for i in staff2_task]), end="")


main2()


# ======================================================================================================================
print("=" * 80)


# Day 3 Training 3: List of Dicts【字典組成的列表】

def main3():
    _, _, all_product = dicts()  # 只需用 list 存放商品 dicts

    print("Enter product name and price('done' to stop):")
    while True:
        product_info = input(">> ").strip()
        if product_info.lower() == "done":
            break

        try:
            product_name, product_price = product_info.split(",")
            product_name = product_name.strip()
            product_price = product_price.strip()

            # 輸入名稱和價格，價格必須是正數
            if product_price.isdigit() and int(product_price) > 0:
                # 這裡將名稱與價格封裝成一個 dict
                product = {f"Product": product_name, "Price": int(product_price)}
                all_product.append(product)  # 加入大 list
            else:
                print("Price must > 0")
        except ValueError:
            print("Syntax Error!!!")

    # 用 list comprehension + join 格式輸出 dict 內容
    for i in all_product:
        print(": ".join([f"{key}, {value if value is not None else ""}" for key, value in i.items()]))


main3()
