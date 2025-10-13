# Numpy Practice: copy
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
import numpy as np


a = np.arange(4).reshape(1, 4)
b = np.arange(4).reshape(1, 4)
c = a
d = a

print(id(a), a)
d[:, 0:2] = [[88, 99]]  # 抓取全行 0列 - 1列 的数字进行修改，虽然数字改变，但是id一致
print(id(b), b)
print(id(c), c)
print(id(d), d)


print("is 判断的逻辑 - 不是内容是否相等，而是否是同一个对象(id相等)")
print(f"b is a - {b is a}")
print(f"a is c - {a is c}")
print(f"c is d - {c is d}")

# ===========================================================================
print("=" * 40)


# 当我们 不使用硬编码 想获取两个相同的大型数组，且不希望他们的 id 一致时，就需要使用 copy
b = np.copy(a)  # 效果类似于 deepcopy 深拷贝
print("a[:, 3] = 100")
a[:, 3] = 100
print(a)
print(b)
print(f"b is a - {b is a} 使用 copy 后，依旧返回False，并且不受 a 数组改变的影响")
