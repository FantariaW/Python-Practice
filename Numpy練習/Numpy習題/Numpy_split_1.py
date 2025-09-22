# Numpy Practice: split, vsplit, hsplit, array_split, (dsplit用于3维，暂时不使用)
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
# axis=0 - 跨行操作
# axis=1 - 跨列操作
import numpy as np


print("严格整除分割: ")
a = np.arange(12)
print(np.split(a, 4))


# ==========================================================================
print()


print("宽松分割: ")
b = np.arange(10)
print(np.array_split(b, 3))


# ==========================================================================
print()


print("垂直分割: ")
c = np.arange(16).reshape(4, 4)
print(np.split(c, 2, axis=1))


# ==========================================================================
print()


print("水平分割: ")
d = np.arange(16).reshape(4, 4)
print(np.split(d, 2, axis=0))


# ==========================================================================
print()


e = np.arange(24).reshape(6, 4)
vsplit_e = np.split(e, 3, axis=0)
print(f"垂直分割3份e: \n{vsplit_e}")

hsplit_e_1 = np.split(vsplit_e[0], 2, axis=1)
print(f"水平分割2份第一段 vsplit_e: \n{hsplit_e_1}")
