# Numpy Practice: All Practice 1
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
import numpy as np


# 1
num_array = np.arange(1, 13, 1).reshape(3, 4)
print(f"Array: \n{num_array}")
print(f"Transpose: \n{np.transpose(num_array)}")


print("=" * 40)  # ============================================================


# 2
random_array = np.random.randint(0, 51, 12).reshape(3, 4)
print(f"Random Array: \n{random_array}")
print(f"Max Num Location: {np.argmax(random_array)}")
print(f"Min Num Location: {np.argmin(random_array)}")
print(f"Minimum and Maximum Number will be limited between 10 - 40: \n{np.clip(random_array, 10, 40)}")


print("=" * 40)  # ============================================================


# 3
num_array_2 = np.arange(1, 16)
print(f"Array 2: {num_array_2}")
print(f"前缀和: \n{np.cumsum(num_array_2)}")
print(f"相邻元素之间的差: \n{np.diff(num_array_2)}")
