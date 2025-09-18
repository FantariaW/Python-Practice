def main():
    print_column(3)
    print_row()
    print_square(3)


def print_column(height):
    # print("\n#" * height)
    for h in range(height):
        print("0")


def print_row():
    for w in range(4):
        print("? ", end="")


def print_square(size):
    print()
    for s in range(size):
        # print("H" * size)
        for s2 in range(size):
            print("H", end="")
        print()


main()
