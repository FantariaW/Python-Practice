# Numpy Practice: arange, linspace
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
import numpy as np


print("從 0 到 4 的 自動生成數組:\n", np.arange(5), "\n")
print("從 2 到 10 每次步長 2 的 自動生成數組:\n", np.arange(2, 10, 2), "\n")
print("從 2 到 2 每次步長 0.2 的 自動生成數組:\n", np.arange(1, 2, 0.2), "\n")

# =============================================================================
print("=" * 40)

a = np.arange(12).reshape((3, 4))
print("從 0 到 .arange(x), 生成一個格式為 .reshape((y, z))大小的數組:\n", a, "\n")

# =============================================================================
print("=" * 40)

b = np.linspace(1, 10, 5)
print("生成一個 linspace(start, stop, num) 數組, "
      "從 start: x 到 stop: y 爲止, 期間生成 num: z 個等間距的數值, "
      "并且間隔都會相等:\n", b, "\n")

c = np.linspace(1, 10, 6).reshape((2, 3))
print("使用.reshape((x, y)) 來定義數組格式:\n", c, "\n")
