# Numpy Practice: vstack, hstack, newaxis, concatenate,
#                 numpy.ones, numpy.around
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
import numpy as np


class StaffData:
    """
    variable for global using
    """
    data_dict = {
        "ids_day1": np.array([201, 202, 203, 204]),
        "ids_day2": np.array([201, 202, 203, 204]),
        "sales_day1": np.array([300, 180, 240, 150]),
        "sales_day2": np.array([320, 170, 260, 190])
    }


class ArrayTransformer:
    """
    function for transforming array only
    """
    @staticmethod
    def vertical_transform(array_name):
        """
        transform 1 dimension array into 1 col, multiple rows
        """
        new_array = array_name[:, np.newaxis]
        return new_array


class ArrayConcatenation:
    @staticmethod
    def h_concatenation(array_1, array_2):
        """
        horizontal concatenate arrays
        """
        concatenate_array = np.concatenate((array_1, array_2))
        return concatenate_array


class Main:
    @staticmethod
    def main():
        """
        main manipulate
        """
        v_transform = ArrayTransformer.vertical_transform

        # 获取数据
        ids_1 = StaffData.data_dict["ids_day1"]      # type: ignore
        ids_2 = StaffData.data_dict["ids_day2"]      # type: ignore
        sales_1 = StaffData.data_dict["sales_day1"]  #  type: ignore
        sales_2 = StaffData.data_dict["sales_day2"]  # type: ignore

        # 转置 2维矩阵
        v_ids_1 = v_transform(ids_1)
        v_ids_2 = v_transform(ids_2)
        v_sales_1 = v_transform(sales_1)
        v_sales_2 = v_transform(sales_2)

        # 创建天数数组
        day_1 = np.ones(4, dtype=int)
        day_2 = np.ones(4, dtype=int) * 2
        days_list = ArrayConcatenation.h_concatenation(day_1, day_2)[:, np.newaxis]

        # 打印合并结果
        ids_list = ArrayConcatenation.h_concatenation(v_ids_1, v_ids_2)
        sales_list = ArrayConcatenation.h_concatenation(v_sales_1, v_sales_2)
        id_sale_list = np.hstack((ids_list, sales_list))
        result_list = np.hstack((id_sale_list, days_list))
        print(f"ID, Sale, Day 合并表格: \n{result_list}")


        # ==================================================================
        print("=" * 60)


        c_list = np.concatenate((v_ids_1, v_sales_1), axis=1)
        c_list_2 = np.concatenate((c_list, v_sales_2), axis=1)

        # 计算销售差
        sale_increase = v_sales_2 - v_sales_1
        result_list_2 = np.concatenate((c_list_2, sale_increase), axis=1)
        print(result_list_2)


        # ==================================================================
        print("=" * 60)


        increase_percent = ((v_sales_2 - v_sales_1) / v_sales_1) * 100
        result_list_3 = np.concatenate((result_list_2, np.around(increase_percent, 1)), axis=1)
        print(result_list_3)


if __name__ == "__main__":
    Main.main()
