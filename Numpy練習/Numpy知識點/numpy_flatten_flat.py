# Numpy Practice: flatten, flat, .T, transpose()
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
import numpy as np


# b = np.arange(3, 15)
# print(b)
# print(b[2])

a = np.arange(3, 15).reshape(3, 4)
print(a)

print()

# print(a[2])       # 索引行数
# print(a[0, 2])    # 索引对应位置的值
# print(a[:, 0])    # 索引列数
# print(a[1, 1:3])  # ❗索引 第1行，然后取 第1列 - 第3列 之前的值， 但不包含第3列的值  ！


# 作用：返回一个新的 1维数组副本。
# 特点：是 copy，不会影响原数组。
# 用法：b = a.flatten()，这样你就得到了一个独立的数组 b。
flatten_a = a.flatten()
print(f"转换成新的1维数组，打印出来 - {flatten_a}")

# 作用：返回一个 迭代器 (numpy.flatiter)，可以把数组当作 1维来逐个访问。
# 特点：不是 copy，而是直接引用原数组的数据。
# 用法：
# for x in a.flat: → 逐元素遍历
# a.flat[i] → 像访问 1维数组一样访问、修改元素
for item in a.flat:
    print(item, end=" ")
print()

print(f"可以直接打印对应值 - {a.flat[1]}")

for row in np.transpose(a):  # transpose - 转置矩阵 - 行变成列，列变成行 - a.T 是缩写
    print(row)
