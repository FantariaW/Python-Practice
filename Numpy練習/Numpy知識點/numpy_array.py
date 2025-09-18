# Numpy Practice 2: array
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
import numpy as np


a = np.array([[[2, 3, 4]]], dtype=np.int64)
print(a.dtype)
print(a.ndim)
print(a.shape)

b = np.zeros((3, 4), dtype=np.int64)  # 行列順序
print(b)

# ================================================================================
print("=" * 30)

sold = np.array([2, 5, 3, 4])   # 4个小时的销量
print(sold.sum())   # 总共卖了多少？→ 2+5+3+4
print(sold + 1)     # 每小时都比昨天多卖1个，会变成？
print(sold * 2)     # 做活动，买一送一，总量翻倍？

# ================================================================================
print("=" * 30)

scores = np.array([
    [80, 90, 85],   # 同学1
    [70, 88, 92],   # 同学2
    [60, 75, 95],   # 同学3
])

print(scores.shape)         # (3, 3) → 3行3列
print(scores.ndim)          # 2 → 2维表格

print(scores.sum())         # 全部分数加总
print(scores.sum(axis=0))   # 按列求和：每一科的总分（语/数/英）
print(scores.mean(axis=1))  # 按行求平均：每个同学的平均分
