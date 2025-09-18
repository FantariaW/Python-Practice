# Lesson 10 Training: constants
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Lesson 10 Training
# ❗ _ 下劃綫命名 表示這個變數不會使用，僅用來執行 for loop
# GO = 3
# for _ in range(GO):
#     print("go")

# ---------------------------------------------------------------------------------

# class Cat:
#     MEOWS = 3
#
#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("Meow")
#
#
# cat = Cat()
# cat.meow()

# ---------------------------------------------------------------------------------

def meow(n: int) -> str:
    return "meow\n" * n
    # for _ in range(n):
    #     print("Meow")


number: int = int(input("Num: "))
meows: str = meow(number)
print(meows)
# meow(number)
