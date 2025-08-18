# Lesson 8: replace, split, removeprefix

url = input("URL: ").strip()

# 1 - replace寫法, 直接替換文本
username = url.replace("https://twitter.com/", "")
print(f"1.Username: {username}")
# 2 - split后變爲list, 直接抓取
url_obj = url.split("/")
# url.split("/")  ➜ ['https:', '', 'twitter.com', 'Fantaria']
i = 0
if len(url_obj) >= 4:
    for i in range(len(url_obj)):
        i += 1
    print(f"2.Username(for loop): {url_obj[int(i) - 1]}")
    print(f"2.Username(url_obj[-1]): {url_obj[-1]}")
else:
    print("❌ 格式錯誤，請輸入正確的 URL！")
# 3 - removeprefix可以從字串前面移除特定開頭文字（prefix）, 如果有的話
# ❗注意事項:
# ⚠️如果開頭不符合，就不動原字串
# ⚠️這是 大小寫敏感的！
username = url.removeprefix("https://twitter.com/")
print(f"3.Username: {username}")
