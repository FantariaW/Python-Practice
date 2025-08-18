# Lesson 9 Training: type
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Lesson 9 Training
import random


print(type(50))
print(type("Arivia"))
print(type([]))  # 不需要賦值也可以檢測
print(type({"a": "a"}))  # 不需要賦值也可以檢測


class Hat:
    def __init__(self):
        self.houses = ["house 1", "house 2"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))


hat = Hat()
hat.sort("Arivia")
