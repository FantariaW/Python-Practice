# Numpy Practice: All Practice 4
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
import numpy as np
import csv


class DesertGenerator:
    @staticmethod
    def generator():
        sales_array = np.random.randint(10, 61, 28).reshape(7, 4)
        split_1 = sales_array[:3]  # 取前 3 行 (0, 1, 2行) 不包含 3
        split_2 = sales_array[3:]  # 取从第 3 行开始往后所有行

        return np.array([split_1, split_2], dtype=object)


class Calculator:
    @staticmethod
    def cal_sum(split_array):
        sum_array = np.sum(split_array, axis=0)
        return sum_array

    @staticmethod
    def cal_ave(split_array):
        ave_array = np.average(split_array, axis=0)
        return ave_array


class ToCSV:
    @staticmethod
    def csv_writer(sum_array_1, ave_array_1, sum_array_2, ave_array_2):
        with open("desert.csv", "w", newline="", encoding="utf-8") as f:
            csv_writer = csv.DictWriter(f, fieldnames=[
                "Part 1 Total", "Part 1 Average", "Part 2 Total", "Part 2 Average"
            ])
            csv_writer.writeheader()

            for p1, a1, p2, a2 in zip(sum_array_1, ave_array_1, sum_array_2, ave_array_2):
                csv_writer.writerow({
                    "Part 1 Total": p1,
                    "Part 1 Average": a1,
                    "Part 2 Total": p2,
                    "Part 2 Average": a2
                })


class Main:
    @staticmethod
    def main():
        title_list = ["Cake", "Cookie", "Muffin", "Donut"]
        split_array = DesertGenerator.generator()
        split_array = np.array(split_array)
        print(f"测试分割后的结果:\n{split_array}")

        sum_array_1 = Calculator.cal_sum(split_array[0])
        sum_array_2 = Calculator.cal_sum(split_array[1])

        ave_array_1 = np.round(Calculator.cal_ave(split_array[0]), 1)
        ave_array_2 = np.round(Calculator.cal_ave(split_array[1]), 1)
        desert_array = np.concatenate((sum_array_1, ave_array_1, sum_array_2, ave_array_2), axis=0).reshape(4, 4)
        print(f"测试最终打印结果:\n{desert_array}")

        ToCSV.csv_writer(sum_array_1, ave_array_1, sum_array_2, ave_array_2)
        print("\n== 🍰 甜品店一周销售报告 ==")
        for index, (p1, a1, p2, a2) in enumerate(zip(sum_array_1, ave_array_1, sum_array_2, ave_array_2), start=0):
            print(f"{title_list[index]}\t - 前3部分总额:{p1} \t | 前3部分平均数:{a1} \t | 后4部分总额:{p2} \t | 后4部分总额:{a2}.")


if __name__ == "__main__":
    Main.main()
