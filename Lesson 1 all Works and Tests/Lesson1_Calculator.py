# Using int and float to define user input
x = int(input("Enter x value: "))
y = float(input("Enter y value: "))

# All print and input and int, float etc, in one line. Really Important!!!!!!
# print(int(input("X: ")) + float(input("Y: ")))

# Without using round(), will cause an floating point precision issue error!!!!!!
print("")
print(f"First way using {{x + y}}: {x + y}")
print("Second way using x - y:", x - y)
print(f"Third way using x / y: {x / y}")
print(f"Fourth way using x * y: {x * y}")

# Using: round(number[ , ndigits]) to round off number, don't need [], the actual count of round off it's not necessary
print(f"Fifth way using {{round(x + y, 2)}}: {round(x + y, 2)}")

# Using format string to round off number
print(f"Sixth way using format string(f\"\") --- print(f\"{{x + y:.2f}}\"): {x + y:.2f}")

# ----------------------------------------------------------------------------------------------------------------------

print("")


# Using define function: def, really important!!!!!!
# First way to calling function result():
def result():
    print(f"1 --- Using \'def result():\' to define and calling the function - result(): {x + y}")


# calling function result()
result()


# Second way to calling function result(to="")
def result(to=x + y):
    print(f"2 --- Using\'def result(to)\' and call \'result(to=x + y)\' to calling function - result(to=x + y):", to)


result()


# Third way to calling function result(to) to print out (x + y)**2
def result(to):
    print(f"3 --- Using\'def result(to)\' and call \'result((x + y)**2)\' to calling function - result(to):", to)


result((x + y)**2)


# Fourth way to calling function result() with square(), to achieve (x + y)**2
# Define square(n)
def square(n):
    return n * n


def result():
    print(f"4 --- Using a square(x + y) function to achieve (x + y)**2:", square(x + y))


result()
