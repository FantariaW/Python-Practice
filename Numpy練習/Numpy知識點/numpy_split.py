# Numpy Practice: split, vsplit, hsplit, array_split, (dsplit用于3维，暂时不使用)
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
import numpy as np


a = np.arange(12).reshape(3, 4)
print(a)

print(np.split(a, 3, axis=0))  # 能处理任意 axis，更pythonic
print(np.vsplit(a, 3))  # 局限 性强，只能沿着 axis=0 分割；要按列分割就得写 hsplit，按深度分割则要用 dsplit。

# 这个是无法运行的，需要 array_split 来进行任意格式分割
# print(np.split(a, 3, axis=1))
print(np.array_split(a, 3, axis=1))  # 使用 array_split 适合任意格式分割
