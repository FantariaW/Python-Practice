# Numpy Practice 1: attribute
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
import numpy as np

# ❗NumPy 要求 同一个数组里的所有元素类型必须相同。
num_array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, 0, 0]
])

print(num_array)
print(f"Number of Dimension: {num_array.ndim}")  # 2 - 2維數組 - 數組的維度數
print(f"Shape: {num_array.shape}")  # (4, 3) - 4行3列 - 數組形狀
print(f"Size: {num_array.size}")  # 12 - 元素總數 - 數組元素總數
print(f"Data Type: {num_array.dtype}")  # int64 - 8個字節的整數數據 - 數組元素的數據類型
