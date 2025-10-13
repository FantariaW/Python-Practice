# Pandas Practice:
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Pandas Practice:
import numpy as np
import pandas as pd


series = pd.Series([1, 3, 6, np.nan, 44, 1])  # numpy.nan 就是 无效数值
print(series)

dates = pd.date_range("20250101", periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6,4),index=dates)
print(df)
