# 這個是存儲 函數和值 的文件：function and value
def hello(name):
    print(f"Hello, {name}")


def goodbye(name):
    print(f"Goodbye, {name}")


def main():
    name = "world-1"
    hello(name)
    goodbye("world-2")


# ❗重點: 就像是一個密碼，在這個文件可以無條件執行，但是在另一個import的文件就一定要輸入一個值，才可以運行這個文件
# 🧠 __name__ 是 Python 的內建變數～
# 如果這個檔案是「被直接執行」，那 __name__ 就會等於 "__main__"
# ✅ 因此這句話的意思是：
# 「只有我自己被執行時，才會啟動 main() 主程式！」
# 🎁 如果是被其他程式 import，就不會執行這段，讓功能模組更彈性可重用喔～
if __name__ == "__main__":
    main()
