# Lesson 5: sys

# 關於 sys.argv 的使用，需要在軟件自帶的terminal裏執行指定的文件，比如 python Lesson5_sys.py name 就可以運行這個文件
# import sys, try-except, if-else
import sys

try:
    print("1 - Hello, my name is", sys.argv[1])
except IndexError as error_msg:
    print("1 - ERROR -", error_msg)

# if there's no entering name, print out [your_name]
# sys.argv[0] 顯示的是文件名
if len(sys.argv) < 2 or len(sys.argv) > 2:
    print("2 - ERROR - Too few or too many arguments: ", sys.argv[0])
    # sys.exit("ERROR - Too few or too many arguments")
else:
    print("2 - Hello, my name is", sys.argv[1])

# [1:]表示從第1個 parameter 開始打印，[1:-1]表示從第1個 parameter 打印，但是不打印出最後1個 parameter
if len(sys.argv) < 2:
    sys.exit("3 - Too few arguments")

for arg in sys.argv[1:]:
    print("3 - I'm", arg)

# =============================================================================
