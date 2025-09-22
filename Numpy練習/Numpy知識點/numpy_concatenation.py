# Numpy Practice: vstack, hstack, newaxis, concatenate
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
import numpy as np


a = np.array([1, 1, 1])
b = np.array([2, 2, 2])

vertical_ab = np.vstack((b, a))  # vertical stack
horizon_ab = np.hstack((b, a))   # horizontal stack

print()

print(vertical_ab, "\n", horizon_ab, "\n")
print(vertical_ab.shape, "\n", horizon_ab.shape)

print()

print(a[np.newaxis, :])
print(a[:, np.newaxis])

print()

c = np.concatenate((a, b, b, a)).reshape(4, 3)
print(c)
