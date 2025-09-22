# Python + Numpy Practice: 1
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Python + Numpy Practice:
import numpy


class FunctionBuilder:
    @staticmethod
    def calendar_generator():
        cal_array = numpy.arange(1, 31, 1).reshape(5, 6)
        return cal_array

    @staticmethod
    def sale_generator():
        sale_array = numpy.random.randint(20, 250, 30)
        return sale_array


class Calculator:
    @staticmethod
    def cal_daily_sale(cal_array, sale_array):
        sale_2d = sale_array.reshape(5, 6)
        for row_day, row_sale in zip(cal_array, sale_2d):
            for d, s in zip(row_day, row_sale):
                print(f"Day:{d} - Sale:{s}", end=" \t")
            print(f"🔍Total Sales for 6 Days: {numpy.sum(row_sale)}")

        # index = 0
        # for row in cal_array:
        #     for day in row:
        #         print(f"Day:{day} - Sale:{sale_array[index]}", end=" \t")
        #         index += 1
        #     print(numpy.sum(sale_array))

    @staticmethod
    def cal_max(sale_array):
        max_index = numpy.argmax(sale_array)
        max_sale = sale_array[max_index]
        max_day = max_index + 1
        return max_day, max_sale

    @staticmethod
    def cal_min(sale_array):
        min_index = numpy.argmin(sale_array)
        min_sale = sale_array[min_index]
        min_day = min_index + 1
        return min_day, min_sale


class Main:
    @staticmethod
    def main():
        cal_array = FunctionBuilder.calendar_generator()
        sale_array = FunctionBuilder.sale_generator()

        # Calendar Generating
        print("Calendar: \n", cal_array)

        print()

        # Calculates Daily Sale and Sum
        print("Daily Sale: ")
        Calculator.cal_daily_sale(cal_array, sale_array)

        print()

        # Display Cumulate Sum
        print("Cumulate Form: ")
        print(numpy.cumsum(sale_array))

        # Get Max
        max_day, max_sale = Calculator.cal_max(sale_array)
        print(f"\n📈 Max Sale -> Day:{max_day}, Sale:{max_sale}")

        # Get Min
        min_day, min_sale = Calculator.cal_min(sale_array)
        print(f"📉 Min Sale -> Day:{min_day}, Sale:{min_sale}")

        # Get Median
        median_location = numpy.median(sale_array)
        print(f"🎯 Median Sale -> {median_location}")

        print()

        # Only Display 50 - 200 even lower or higher
        print("Clip Daily Sale - Only Show up  50 - 200: ")
        clipped_sale = numpy.clip(sale_array, 50, 200)
        Calculator.cal_daily_sale(cal_array, clipped_sale)

        print()

        # Sort
        print("Sort: ")
        print(f"Top 5 Sales: {numpy.sort(sale_array[:5])}")
        print(f"Lowest 5 Sales: {numpy.sort(sale_array[-5:])}")


if __name__ == "__main__":
    Main.main()
