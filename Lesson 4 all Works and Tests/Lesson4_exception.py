# Lesson 4 exception

# # ValueError:
# try:
#     x = int(input("Number: "))
#     print(f"X = {x}")
# except ValueError:
#     print("Error!")


def get_int(prompt):
    while True:
        try:
            y = int(input(prompt))
            if y < 0:
                # 自己加的限制條件, 但是error會被except直接抓取，因爲使用了int定義input值,使用if判斷之後成功輸出自定義報錯
                raise ValueError("自定義: Y must greater than 0!")
        except ValueError as e:
            # 因爲使用了 int(input),單單使用 except ValueError as e的話，
            # 會提示系統的報錯： invalid literal for int() with base 10: 'a'
            # 所以使用 if "invalid literal" in str(e) 去判斷報錯是否有"invalid literal"，有的話就輸出自己定義的報錯(e)
            if "invalid literal" in str(e):
                print("Y must be integer!")
                # 使用pass然後刪掉print，可以不發出任何問題警告的情況下，直接重複loop，但是會讓用戶不明白爲什麽程序不斷地重複，所以不推薦這樣亂用
                pass
            else:
                print(e)
        else:
            # 用return可以直接進行：break的同時，返回出結果
            return y


def main():
    y = get_int("What is Y: ")
    print(f"Y is: {y}")


main()
# ======================================================================================================================
