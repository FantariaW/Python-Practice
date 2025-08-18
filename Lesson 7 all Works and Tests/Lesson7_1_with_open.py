# Lesson 7: open(), with open()
# "w" - write, "r" - read, "a" - append

# open() 不推薦這麽用 - 因爲中途 f.write(...) 出錯，後面的 f.close() 永遠不會被執行。
# 結果可能是：檔案處於未關閉狀態，內容寫不完整，甚至鎖死無法再操作⚠️

# name = input("Name -> ")
# f = open("names.txt", "a")
# f.write(f"{name}\n")
# f.close()

# =============================================================================

# with open()
# 幾乎所有專業 Python 程式都會優先使用 with open(...) as f: 的寫法，原因是：
# 無論程式是否中斷，檔案都會正確關閉
# 不用手動寫 .close()，語法清楚結構分明
# 一眼就看出這區塊是「處理檔案的區域」
# Python 官方風格指南也推薦這種寫法

# name = input("Name -> ")
# with open("names.txt", "a") as f:
#     f.write(f"{name}\n")

# =============================================================================

# # "r" - read file names.txt
# with open("names.txt", "r") as f:
#     lines = f.readlines()  # 理解爲創建了一個 list 名爲 lines = []
#
# for line in lines:
#     print("Hello! ", line.rstrip())

# =============================================================================

# with open("names.txt", "r") as f:
#     for line in f:
#         print("Hello! ", line.rstrip())

# =============================================================================

# 🪄 這是重點！append() 的意義是：
# line.rstrip()：
# .rstrip() 是去除字串右邊的空白（特別是換行符號 \n）
# "Arivia\n".rstrip() ➜ "Arivia"

# names.append(...)：
# 把處理後的名字「加入 list names 裡」

names = []

with open("names.txt") as f:
    for line in f:
        names.append(line.rstrip())

# sorted() 用於字母排序, reverse 反轉順序
for name in sorted(names, reverse=True):
    print(f"Hello! {name}")
