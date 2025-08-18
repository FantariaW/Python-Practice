# parity training: + - * / %:
x = float(input("X: "))

if x % 2 == 0:
    print("X is even number")
else:
    print("X is odd number")


# Using define to achieve an even/odd number testing
# Calculate the number whether can or can not divided by 2 exactly
def is_even(n):
    # return n % 2 == 0
    # Using boolean way and all return,true-false boolean,if-elif-else functions compile in 1 single line!!!
    return True if n % 2 == 0 else False


def main():
    y = float(input("Y:"))
    if is_even(y):
        print("Y is even number")
    else:
        print("Y is odd number")


main()
