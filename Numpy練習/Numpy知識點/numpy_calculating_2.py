# Numpy Practice: argmax, argmin, median, cumsum, diff, nonzero, sort
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
import numpy as np


a = np.arange(14, 2, -1).reshape(3, 4)
print(np.argmax(a))  # 求 最大值 的 索引位置
print(np.argmin(a))  # 求 最小值 的 索引位置
print(np.median(a))  # 求 中位数
print(np.cumsum(a))  # 计算全部 前缀和
print(np.diff(a))    # 计算 相邻元素之间的差
print(np.nonzero(a)) # 求 非0元素 的 索引位置
print(np.sort(a))    # numpy.sort(x) 直接修改原列表 x 逐行排序， 而 new_x = sorted(x) 用来得到一个新的结果
print(np.transpose(a))  # 转置矩阵 - 行变成列，列变成行 - a.T 是缩写
print(np.transpose(a).dot(a))  # 可以组合起来，计算 转置矩阵a 乘以 原矩阵a
print(np.clip(a, 5, 9))  # 限制最小显示的值和最大显示的值
