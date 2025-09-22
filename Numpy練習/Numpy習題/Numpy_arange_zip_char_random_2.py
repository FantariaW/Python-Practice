# Numpy Practice: arange, zip()
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
import numpy as np

print("复习 1")
print("计算随机数阵列每行的总和与平均数: ")
num_list = np.arange(1, 101).reshape(10, 10)
row_sum = num_list.sum(axis=1)
row_average = num_list.mean(axis=1)

for row, total, ave in zip(num_list, row_sum, row_average):
    print(f"{row} - 总和:{total} - 平均数:{ave}.")


# ============================================================================
print()


print("复习 2")
print("计算随机数阵列每行最大值，每列最小值: ")
random_list_2 = np.random.randint(1, 101, size=(10,10))
column_max = random_list_2.max(axis=0)
row_min = random_list_2.min(axis=1)

print(random_list_2)
print(f"每列最大值: {column_max}")
print(f"每行最小值: {row_min}")


# ============================================================================
print()


print("复习 3")
print("9月日历列表: ")
max_sale = []

calendar_list = np.arange(1, 31).reshape(5, 6)
new_calendar_list = calendar_list.astype(str)
new_calendar_list = np.char.add("Day ", new_calendar_list)
# 每个日期都有一个对应的随机销售额，就需要生成 和日历同样大小的数组，所以size需要是 30 对应日历 30 天
sale_list = np.random.randint(1, 100, 30)
new_sale_list = sale_list.astype(str)

for c, s in zip(new_calendar_list, sale_list):
    print(f"{c} - 随机销售额:{s}")
    max_sale.append(s)
print(f"最高销售额: {max(max_sale)}")
