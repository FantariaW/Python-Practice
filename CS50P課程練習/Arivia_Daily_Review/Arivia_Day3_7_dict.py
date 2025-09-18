# Day 3 Training: dict + items() + if-else + None

# ✅ 書籍上架檢查系統
# 使用 dict 儲存書籍名稱與狀態，如果值為 None，表示尚未上架
books = {
    "Python Basics": "In Stock",
    "AI for Kids": None,
    "The Art of Code": "Out of Stock",
    "Data Wizard": "In Stock"
}

# 使用 .items() 遍歷所有書籍與狀態，並處理 None 為 'Coming Soon'
for key, value in books.items():
    print(f"📘 {key}: {value if value is not None else 'Coming Soon'}")


# ======================================================================================================================
print("=" * 80)


# ✅ 函式：回傳水果庫存 dict
def fruit_dict():
    stock_list = {
        "apple": 15,
        "banana": 0,
        "orange": 12,
        "grape": 8
    }
    return stock_list

# ✅ 主程式入口
# 提供查詢介面，使用者可輸入水果名稱進行查詢
# 若輸入 'done'，則結束並輸出所有庫存


def main():
    stock_list = fruit_dict()

    print("Check fruit product by name('done' to stop): ")
    while True:
        user_fruit = input(">> ").strip().lower()  # 💬 接收輸入，並清除空格轉小寫
        if user_fruit == "done":
            # 🌀 輸出所有水果與庫存，用 join() 組成漂亮的一行文字
            print(" / ".join(
                [f"{key2}: {value2 if value2 is not None else 'N/A'}" for key2, value2 in stock_list.items()]
            ))
            break
        elif user_fruit in stock_list.keys():
            print("Product existing, feel free to add it to your cart!")  # 🎉 商品存在提示
        else:
            print("Product currently out of stock!")  # ❌ 查無此商品提示


main()
