# Numpy Practice: All Practice 3
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
import numpy as np
import csv


class CalendarGenerator:
    @staticmethod
    def generator():
        """
        generate 5 days, tile repeat 5 days for 6 times(shape - (6, 1))
        generate sale number for 30 days totally
        concatenate them together
        """
        result_list = []
        for _ in range(4):
            day_array = np.arange(1, 6, 1).reshape(1, 5).T
            month_array = np.tile(day_array, (6, 1))  # 行向重复6次， 一共30行
            sale_array = np.random.randint(10, 100, 30).reshape(1, 30).T
            calendar_array = np.concatenate((month_array, sale_array), axis=1)
            result_list.append(calendar_array)

        result_array = np.array(result_list)
        concatenate_array = np.concatenate(result_array, axis=1)

        split_array = np.split(concatenate_array, 6, axis=0)

        # 得到一个分割成 6 个部分的总数据
        return split_array


class Calculator:
    """
    计算 前段部分 和 后段部分 的 每行 的 总和， 一段部分一共得到 5 个数字， 默认(5, )格式
    (1, 5).T 转化为 (5, 1) 方便阅读计算
    """
    @staticmethod
    def cal_sum(split_array_1, split_array_2):
        sum_array = (split_array_1 + split_array_2).reshape(1, 5).T
        return sum_array


class ToCSV:
    @staticmethod
    def csv_writer(sum_result_list, ave_result_list):
        with open("sale_report.csv", "w", newline="", encoding="utf-8") as f:
            csv_writer = csv.DictWriter(f, fieldnames = ["Month", "Front Sum", "Front Ave", "Back Sum", "Back Ave"])
            csv_writer.writeheader()

            # 遍历两个列表内的 ndarray 然后写入文件
            # .item() 用于单元素提取，这个是numpy专门针对提取ndarray单个元素用的
            # ❗.item 不是 items()
            for index, (part, ave) in enumerate(zip(sum_result_list, ave_result_list), start=1):
                csv_writer.writerow({
                    "Month": f"第{index}月",
                    "Front Sum": part[:, 0].item(),
                    "Front Ave": ave[:, 0].item(),
                    "Back Sum": part[:, 1].item(),
                    "Back Ave": ave[:, 1].item()
                })


class Main:
    @staticmethod
    def main():
        split_array = CalendarGenerator.generator()
        # print(f"测试-所有的split数据: \n{split_array}")

        # split_array 已经是你用 np.split(..., 6, axis=0) 分好的 6 个月数据，
        # 所以它本身就是一个列表，循环时 each_month 就代表“第 i 月”。
        sum_result_list = []
        ave_result_list = []
        for i, each_month in enumerate(split_array, start=1):
            # 计算 前段部分 与 后段部分
            front_sum = Calculator.cal_sum(each_month[:, 1], each_month[:, 3])
            back_sum = Calculator.cal_sum(each_month[:, 5], each_month[:, 7])
            # 合并 前后两个部分
            sum_array = np.concatenate((front_sum, back_sum), axis=1)
            # 分别计算前后两个部分的两个总和（格式为 5,2）所以需要跨行处理，避免前后部分相加冲突
            part_sum = np.sum(sum_array, axis=0).reshape(1, 2)
            sum_result_list.append(part_sum)

            # 利用前面计算得到的 前后段部分，计算 前后段部分 的 平均数
            front_ave = np.average(front_sum, axis=0).reshape(1, 1)
            back_ave = np.average(back_sum, axis=0).reshape(1, 1)
            # 将平均数结果合并就完成了
            part_ave = np.concatenate((front_ave, back_ave), axis=1)
            ave_result_list.append(part_ave)


        print(f"测试-每部分总和: \n{sum_result_list}")
        print(f"测试-每部分平均: \n{ave_result_list}")


        for index, (part, ave) in enumerate(zip(sum_result_list, ave_result_list), start=1):
            print(f"📆第{index}月: \n前半部分: 总额{part[:, 0]} 平均{ave[:, 0]} \n后半部分: 总额{part[:, 1]} 平均{ave[:, 1]}")

        # 呼叫 ToCSV.csv_writer() 写入 csv 文件
        ToCSV.csv_writer(sum_result_list, ave_result_list)


if __name__ == "__main__":
    Main.main()
