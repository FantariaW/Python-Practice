from Lesson6_1_import import square


# 在 terminal 使用 pytest 來測試
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0


def main():
    test_square()


if __name__ == "__main__":
    main()
