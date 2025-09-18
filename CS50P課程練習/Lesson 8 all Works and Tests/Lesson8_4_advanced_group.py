# Lesson 8: group, (?: )

import re


url = input("URL: ").strip()

# ❗(?: )  -  表示這個 group 不捕獲, 不抓取
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")
else:
    print("Format Error...")
