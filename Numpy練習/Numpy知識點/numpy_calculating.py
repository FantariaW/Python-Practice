# Numpy Practice: .dot(), @
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
import numpy as np


a = np.array([10, 20, 30, 40]).reshape(2, 2)
b = np.arange(4).reshape(2, 2)  # arange 内只有一个数值时，默认为 stop 值， 其余默认 start=0，step=1
c = a * b
d = np.dot(a, b)  # .dot() - 向量内积 - 一维乘法计算程式，多用于一维矩阵（向量内积）计算
e = a @ b  # 多用于二维以上矩阵乘法计算
# d = list(range(4))
# print(d)


print(c < 60)  # 这里会打印出 bool 值，判断 c 里面所有值是否小于60， 然后打印出True，False结果
print(d)
print(e)


# =============================================================================
print("=" * 40)


random_list = np.random.random((2, 2))
print(random_list)
print(np.sum(random_list, axis = 1))  # 求每行独立总和
