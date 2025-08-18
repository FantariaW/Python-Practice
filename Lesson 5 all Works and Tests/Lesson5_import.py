# Lesson 5: import, random.choice(), random.randint(), random.shuffle()
# import random - 更推薦使用這個 import ⭐⭐⭐
# random.choice(["heads", "tails"]) 比較長，但一眼就知道這是來自 random 模組的函式。
import random

gacha_coin = random.choice(["heads", "tails"])
print("random.choice() - ", gacha_coin)

# ===================================================
print()

# from random import choice - 不太推薦❗
# 不容易看出 gacha_coin2 = choice(["A", "B"]) 的這個 choice() 是從哪裡來的❗
from random import choice  # 記住import一定要在整個文件最頂上❗

gacha_coin2 = choice(["A", "B"])
print("choice() - ", gacha_coin2)

# ===================================================
print()

# random.randint()
# import random

number = random.randint(1, 10)
print("random.randint() - ", number)

# ===================================================
print()

# random.shuffle()
# import random
cards = ["Jack", "Queen", "King"]
random.shuffle(cards)

print("random.shuffle() - ", end=" ")
for card in cards:
    print(card, end="  ")
