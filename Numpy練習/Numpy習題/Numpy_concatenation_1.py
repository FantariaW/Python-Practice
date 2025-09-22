# Numpy Practice: vstack, hstack, newaxis, concatenate
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
import numpy as np


# 1
# 原数组
ids = np.array([101, 102, 103, 104])
sales = np.array([200, 180, 250, 300])

# 使用 newaxis 升维， 列向量新增一个维度
new_ids = ids[:, np.newaxis]
new_sales = sales[:, np.newaxis]

# 使用 hstack 进行水平堆叠
concatenation_array = np.hstack((new_ids, new_sales))

print(f"升维合并后的结果: \n{concatenation_array}")


# ============================================================================
print()


# 2
# 原数组
ids_2 = np.array([101, 102, 103, 104])
sales_2 = np.array([220, 210, 260, 280])

# 合并两个大表格
concatenation_array_2 = np.transpose(np.vstack((ids_2, sales_2)))
two_days_table = np.vstack((concatenation_array, concatenation_array_2))
print(f"两天的合并结果: \n{two_days_table}")
print(two_days_table.shape)


# ============================================================================
print()


# 3
# 原数组
bonus = np.array([1.1, 1.0, 1.2, 1.3])
bonus_2 = np.array([1.05, 1.0, 1.15, 1.25])

two_days_bonus = np.hstack((bonus, bonus_2))[:, np.newaxis]

final_result = np.hstack((two_days_table, two_days_bonus))
print(f"最终合并2表格结果: \n{final_result}")
print(final_result.shape)


# ============================================================================
print()


# concatenate 用法:
ids_all = np.concatenate((ids, ids_2))[:, np.newaxis]
sales_all = np.concatenate((sales, sales_2))[:, np.newaxis]
bonus_all = np.concatenate((bonus, bonus_2))[:, np.newaxis]

concatenation_table = np.concatenate((ids_all, sales_all, bonus_all), axis=1)
print(f"Concatenate合并方式: \n{concatenation_table}")
