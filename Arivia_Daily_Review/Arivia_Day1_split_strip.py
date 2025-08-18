# split() + strip()

# .strip() 去除前後多餘的空格，看起來美觀
# 查詢用戶輸入的兩個詞之間有沒有 逗號 ， 有的話就以 逗號 ， 為分界綫分割它們成兩個新的元素或值
user_input = input("Please enter 2 foods: ").strip()
# 開始查找 逗號 ， 并開始分割
food1, food2 = user_input.split(",")

print(f"Food 1: {food1} \nFood 2: {food2}")


print("---------------------------------------------------------------------------------------------------------------")


# .split() 不是「主動去插入拆除符號」🔨
# 而是：
# 「去句子裡尋找指定的符號**，然後以它為分界線把句子拆成多個部分」**
sentence = "I love Fantaria, and Arivia"
words = sentence.split(", ")

print(words)


print("---------------------------------------------------------------------------------------------------------------")


# 請使用者輸入兩本書名（英文），用「.」分開，請自動把書名首字母大寫後印出來：
user_book = input("Enter 2 books: ").strip()
book1, book2 = user_book.split(".")

print(f"📗Book 1: {book1} \n📗Book 2: {book2}")
