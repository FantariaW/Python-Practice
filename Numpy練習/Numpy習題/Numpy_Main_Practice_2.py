# Numpy Practice: All Practice 2: split, vsplit, hsplit, array_split, (dsplit用于3维，暂时不使用)
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
import numpy as np


class CalendarSale:
    @staticmethod
    def generator():
        """
        Generate 10 days array for 12 times, and concatenate them by vertical axis=0
        """

        # ❗传统 for loop 搭配 concatenate/stack 也可以实现 tile 的复制方法
        # test_array = [days_array for _ in range(12)]  # for loop 生成 12 个 ndarray
        # test_array_2 = np.concatenate(test_array, axis=0)  # 合并生成后的 ndarray
        # test_array_3 = np.concatenate([test_array_2 for _ in range(4)], axis=1)  # 二次合并分成4部分
        # test_array_4 = np.split(test_array_3, 2, axis=1)  # split 跨列分割

        record_list = []
        for _ in range(4):
            days_array = np.arange(1, 11, 1).reshape(10, 1)
            calendar_array = np.tile(days_array, (12, 1))
            sales_array = np.random.randint(1, 5, 120).reshape(120, 1)
            day_sale_array = np.concatenate((calendar_array, sales_array), axis=1)

            record_list.append(day_sale_array)

        list_to_array = np.array(record_list)
        result_array = np.concatenate(list_to_array, axis=1)  # 因为上面添加了 4组ndarray 进入list，所以不需要reshape


        split_array = np.split(result_array, 2, axis=1)

        return split_array


class Calculator:
    @staticmethod
    def cal_sum_part_1(split_array):
        """
        Grab total sales
        """
        part = split_array[0]
        sale1 = part[:, 1]  # 抓取split[0]的第 1 列
        sale2 = part[:, 3]
        total_array = (sale1 + sale2).reshape(10, 12).T  # 先保持原数据顺序，再transpose，最后一共12行，每行为一个月10天
        # total_array = (split_array[0][:, 1] + split_array[0][:, 3])  # 同上3行逻辑

        sum_array = np.sum(total_array, axis=1).reshape(12, 1)  # 跨列相加计算
        # final_sum_array = np.sum(sum_array, axis=1)  # 计算第一部分的全部总和

        return sum_array

    @staticmethod
    def cal_ave_part_1(split_array):
        total_array = (split_array[0][:, 1] + split_array[0][:, 3]).reshape(10, 12).T
        ave_array = np.average(total_array, axis=1).reshape(12, 1)

        return ave_array

    @staticmethod
    def cal_sum_part_2(split_array):
        total_array = (split_array[1][:, 1] + split_array[1][:, 3]).reshape(10, 12).T
        sum_array_2 = np.sum(total_array, axis=1).reshape(12, 1)

        return sum_array_2

    @staticmethod
    def cal_ave_part_2(split_array):
        total_array = (split_array[1][:, 1] + split_array[1][:, 3]).reshape(10, 12).T
        ave_array = np.average(total_array, axis=1).reshape(12, 1)

        return ave_array


class Main:
    @staticmethod
    def main():
        split_array = CalendarSale.generator()
        # print(f"Test: \n{split_array}")
        sale_part_1 = Calculator.cal_sum_part_1(split_array)
        sale_part_2 = Calculator.cal_sum_part_2(split_array)
        ave_part_1 = Calculator.cal_ave_part_1(split_array)
        ave_part_2 = Calculator.cal_ave_part_2(split_array)
        # print(ave_part_1)

        i = 0
        for p_1, a_1, p_2, a_2 in zip(sale_part_1, ave_part_1, sale_part_2, ave_part_2):
            i += 1
            print(f"第{i}月: \n第一段: 总额 {p_1} 平均 {a_1} \n第二段: 总额 {p_2} 平均 {a_2}\n")


if __name__ == "__main__":
    Main.main()
