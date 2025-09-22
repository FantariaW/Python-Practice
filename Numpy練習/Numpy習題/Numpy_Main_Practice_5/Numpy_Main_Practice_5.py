# Numpy Practice: All Practice 5
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
import numpy as np
import csv


class ToySaleGenerator:
    @staticmethod
    def generator():
        sale_array = np.random.randint(5, 31, 24).reshape(4, 6)
        part1 = sale_array[:, :2]  # 取前 2 列 (0, 1) 不包含 2
        part2 = sale_array[:, 2:]  # 取从第 2 列开始往后所有列

        return [part1, part2]


class Calculator:
    @staticmethod
    def cal_sum(split_array):
        sum_array = np.sum(split_array, axis=1)
        return sum_array
    
    @staticmethod
    def cal_ave(split_array):
        ave_array = np.average(split_array, axis=1)
        return np.round(ave_array, 1)


class ToCSV:
    @staticmethod
    def csv_writer(sum_array1, ave_array1, sum_array2, ave_array2):
        with open("toy.csv", "w", newline="", encoding="utf-8") as f:
            csv_writer = csv.DictWriter(f, fieldnames=[
                "Part 1 Sale", "Part 1 Average", "Part 2 Sale", "Part 2 Average"
            ])

            csv_writer.writeheader()

            for p1, a1, p2, a2 in zip(sum_array1, ave_array1, sum_array2, ave_array2):
                csv_writer.writerow({
                    "Part 1 Sale": p1,
                    "Part 1 Average": a1,
                    "Part 2 Sale": p2,
                    "Part 2 Average": a2
                })


class Main:
    @staticmethod
    def main():
        title_list = ["Puzzle", "Bear", "Car", "Yoyo"]
        split_array = ToySaleGenerator.generator()
        # split_array = np.array(split_array)
        sum_array1 = Calculator.cal_sum(split_array[0])
        sum_array2 = Calculator.cal_sum(split_array[1])

        ave_array1 = Calculator.cal_ave(split_array[0])
        ave_array2 = Calculator.cal_ave(split_array[1])

        print(f"测试分割后的数组:\n{split_array}")
        print(f"测试计算前2部分总和后的数组:\n{sum_array1} {ave_array1}")
        print(f"测试计算后4部分总和后的数组:\n{sum_array2} {ave_array2}")

        print("== 🧸 玩具铺周末销售报告 ==")
        print("📆 前段(周五～周六):")
        for index, (p1, a1) in enumerate(zip(sum_array1, ave_array1), start=0):
            print(f"{title_list[index]} \t - 总额 {p1} \t - 平均 {a1}")

        print("📆 前段(周日～周三):")
        for index, (p2, a2) in enumerate(zip(sum_array2, ave_array2), start=0):
            print(f"{title_list[index]} \t - 总额 {p2} \t - 平均 {a2}")

        ToCSV.csv_writer(sum_array1, ave_array1, sum_array2, ave_array2)


if __name__ == "__main__":
    Main.main()
