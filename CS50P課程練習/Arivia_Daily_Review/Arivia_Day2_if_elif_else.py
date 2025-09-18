# 🌸 使用 if-elif-else 條件判斷句，來根據輸入的內容給出不同的回應！

user_age = input("Enter your age: ")
# 🎯 Step 2：判斷輸入是否為數字（isdigit() 會檢查這個字串是不是純數字）
if user_age.isdigit():
    # 🍼 # age_input 是字符串，不能直接与 18 比较，需用 age = int(user_age) 转换成數字 age，這樣才能跟數字比較大小～
    age = int(user_age)
    if age >= 18:
        print(f"You are an adult! {age}")
    elif 0 < age < 18:
        print(f"You are underage, minor! {age}")
else:
    print("Invalid input")


print("---------------------------------------------------------------------------------------------------------------")


# ✨ 使用 .strip() 清除前後多餘的空格，乾乾淨淨！
user_name = input("Enter your name: ").strip()
# 🌈 使用 if-elif-else 來驗證用戶輸入的字符是否對應正確的字符
if user_name.lower() == "fantaria" or user_name.lower() == "arivia":
    # 🎉 如果名字是其中之一，就熱烈歡迎回到我們的 Kingdom！
    # 用 .title() 把名字首字母大寫
    print(f"Welcome back to the Kingdom, {user_name.title()}!")
else:
    print(f"I don't know who you are, {user_name.title()}...")
