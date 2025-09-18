# Training 1: dict + key-value + items() + for
# 🗂️ 建立一个 employee 字典，每个员工编号是 key，对应的资料是另一个小字典
employee = {
    "001": {"name": "Alice", "position": "Engineer", "location": "Toronto"},
    "002": {"name": "Bob", "position": "Designer", "location": "Vancouver"},
    "003": {"name": "Clara", "position": "Manager", "location": "Calgary"}
}

# 🧾 现在我们要一个一个打印出员工资料（可爱又整齐那种）
for num in employee:
    # 💡 num 是像 "001"、"002" 这种编号 👉 先打印编号，比如 "001:"
    print(f"{num}: ",
          # 🪄 接着拼接这位员工的所有资料，格式是：key: value
          " | ".join(
              [
                  # 🍰 每个 key-value 对都变成 "key: value" 的样子
                  f"{key}: {value if value is not None else 'N/A'}"
                  # 🔍 我们从 employee[workers]（员工字典）里拿出所有字段
                  # 比如 key 是 name、position，value 是 Alice、Engineer
                  # 嵌套字典會需要x[y].items()
                  for key, value in employee[num].items()
              ]
          )
          )


print("=" * 100)


# Training 2:  list + dict + join() + for + def-function
# ✅ 建立角色資料字典，每個角色是個 dict，包含名字與技能（技能用 list 表示）
def dicts():
    characters = [
        {"name": "Arivia", "skills": ["Light Arrow", "Heal", "Barrier"]},
        {"name": "Fantaria", "skills": ["Slash", "Counter", "Berserk"]},
        {"name": "Destina", "skills": ["Revive", None, "Blessing"]}  # 👈 有一個技能是 None（表示空）
    ]
    return characters


def main():
    characters = dicts()  # 拿到角色資料列表

    # 🍭 使用 .join() 方法來將技能合併輸出（用🔹連接每個技能）
    for key in characters:
        print(f"{key['name']}", end=": ")  # 先打印名字後不換行
        print("🔹".join([
            skill if skill is not None else ""  # 👉 遇到 None 就用空字串取代
            for skill in key["skills"]         # 🔁 遍歷每個角色的技能列表
        ]))


main()


print("=" * 100)  # 🌟 分隔線，讓上下輸出區塊清楚一點


# Training 3: 使用 def-function + for + dict + list + join()
def dicts2():
    # 📦 建立產品列表，每個產品是個 dict，含產品名稱、價格、庫存
    products = [
        {"Product": "Laptop", "Price": "$999", "Stock": "25"},
        {"Product": "Tablet", "Price": "$499", "Stock": "100"},
        {"Product": "Phone", "Price": "$799", "Stock": "0"},
        {"Product": "Watch", "Price": "$199", "Stock": None}  # 👈 有的產品沒有庫存（None）
    ]
    return products


def main2():
    products = dicts2()

    # 🏷️ 自動抓第一個字典的所有 key 當作表頭
    print(" | ".join(products[0].keys()))
    # 🔻 輸出一條分隔線，美觀用
    print("-" * 30)

    # 🧾 一個一個印出每個產品資料（用 " | " 隔開）
    for items in products:
        print(" | ".join([
            each_item if each_item is not None else "N/A"  # 👈 如果某個值是 None，就換成 N/A
            for each_item in items.values()                # 🔁 遍歷這筆資料的所有值
        ]))

    # # 大家喜歡看到的簡潔易讀懂
    # # 自动打印表头
    # print(" | ".join(products[0].keys()))
    # print("-" * 40)
    #
    # # 打印内容
    # for item in products:
    #     print(" | ".join(
    #         [item[k] if item[k] is not None else "N/A" for k in item]
    #     ))


main2()
