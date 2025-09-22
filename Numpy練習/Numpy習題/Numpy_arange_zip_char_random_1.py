# Numpy Practice: arange, zip(), char
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
import numpy as np

calendar_list = np.arange(1, 31)
sales_count = np.random.randint(100, 501, 30).reshape(5, 6)
print(type(calendar_list))

calendar_list = calendar_list.astype(str)
new_calendar = np.char.add("Day", calendar_list).reshape(5, 6)

print("9月份日期表: ")
for day, sale in zip(new_calendar, sales_count):
    for d, s in zip(day, sale):
        print(f"{d}:{s}", end="\t")
    # 這裏的 print() 用處是每寫完一行再換下一行
    # .reshape(5, 6) 定義了5行6列, 因此每寫 6個 換下一行
    print()


print()


print("每6天結算一次: ")
for day, sale in zip(new_calendar, sales_count):
    for d, s in zip(day, sale):
        print(f"{d}: {s}", end="\t")
    print("總和:", sale.sum())
