# Day 3 Training 1: 水果進貨紀錄器（List of Dicts）

# ✅ 任務 1：水果進貨紀錄器（List of Dicts）
# 結構：[{"fruit": xxx, "price": xxx}, ...]
def dicts():
    # main1()
    all_fruits = []
    fruits = {}

    # main2()
    all_foods = {}

    # main3()
    all_flavor = {}

    return all_fruits, fruits, all_foods, all_flavor


def main1():
    all_fruits, fruits, _, _ = dicts()

    print("Enter fruit name and price('done' to stop): ")
    while True:
        user_fruit = input(">> ").strip()

        if user_fruit.lower() == 'done':
            break

        try:
            # 💡 以逗號分隔輸入資料
            fruit_name, fruit_price = user_fruit.split(",")
            fruit_name = fruit_name.strip()
            fruit_price = fruit_price.strip()

            if fruit_price.isdigit() and int(fruit_price) > 0:
                # ✅ 寫入 list of dict
                fruits = {"Fruit": fruit_name.title(), "Price": int(fruit_price)}
                all_fruits.append(fruits)
            else:
                print("Price must be numeric!!!")
        except ValueError:
            print("Syntax Error!!!")

    for fruits in all_fruits:
        print(", ".join([f"{fruits_name}: {fruit_price}" for fruits_name, fruit_price in fruits.items()]))


main1()


# ======================================================================================================================
print("=" * 80)


# Day 3 Training 2: 便當菜單表（Nested Dict）

# ✅ 任務 2：便當菜單表（Nested Dict）
# 結構：{"紅燒牛肉": {"type": "葷", "price": 90}}
def main2():
    _, _, all_foods, _ = dicts()

    print("Enter food name, type(meat/vegan) and price('done' to stop): ")
    while True:
        user_food = input(">> ").strip()
        if user_food.lower() == 'done':
            break

        try:
            food_name, food_type, food_price = user_food.split(",")
            food_name = food_name.strip()
            food_type = food_type.strip()
            food_price = food_price.strip()

            # ✅ 寫入嵌套字典
            if food_type.lower() == 'meat' and food_price.isdigit() and int(food_price) > 0:
                all_foods[food_name] = {"Type": food_type.lower(), "Price": int(food_price)}
            elif food_type.lower() == 'vegan' and food_price.isdigit() and int(food_price) > 0:
                all_foods[food_name] = {"Type": food_type.lower(), "Price": int(food_price)}
            else:
                print("Type must be one of meat/vegan, Price must be numeric!!!")
        except ValueError:
            print("Syntax Error!!!")

    for main_key, main_value in all_foods.items():
        print(f"{main_key}: ", end="")
        print(", ".join([f"{sub_key}: {sub_value}" for sub_key, sub_value in main_value.items()]))


main2()


# ======================================================================================================================
print("=" * 80)


# Day 3 Training 3: 顧客喜好口味登記表（Dict with List）

# ✅ 任務 3：顧客口味登記表（Dict with List）
# 結構：{"Fantaria": ["草莓", "抹茶"]}
def main3():
    _, _, _, all_flavor = dicts()

    print("Enter name and their favorite flavor('done' to stop): ")
    while True:
        user_name = input("Name >> ").strip()
        try:
            if user_name.lower() == 'done':
                break
            else:
                print("!--You may type in 'end' to move to next user--!")
                while True:
                    user_flavor = input(f"{user_name.title()}'s favorite flavor >> ").strip()
                    if user_flavor.lower() == 'end':
                        break
                    # 若顧客尚未出現，先初始化為空 list
                    elif user_name not in all_flavor:
                        all_flavor[user_name] = []
                        # ✅ 這是添加第一個口味，不寫這個的話添加不了第一個輸入的口味，新口味寫入對應 list 中 / 也可以把這行寫到elif外，就不需要else了
                        all_flavor[user_name].append(user_flavor.title())
                    else:
                        # ✅ 這個可以寫入之後輸入的每一個口味，新口味寫入對應 list 中
                        all_flavor[user_name].append(user_flavor.title())
        except ValueError:
            print("Syntax Error!!!")

    for key, value in all_flavor.items():
        print(key.title(), "💗".join(value))


main3()
