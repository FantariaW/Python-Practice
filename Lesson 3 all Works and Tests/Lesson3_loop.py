# loop learning: while, for

# while loop using
i = 0
while i < 5:
    print("Arivia's Wish 5 times")
    i += 1

print("\n".strip())

# for loop using in 2 pythonic ways
# Way 1
for _ in range(3):
    print("Happy Day 3 times")

print("\n".strip())

# Way 2
for i in range(3):
    print(f"Let's count: {i + 1}")

# ----------------------------------------------------------------------------------------------------------------------

# continue and break training
while True:
    x = int(input("\nX: "))
    if x < 0:
        continue
    else:
        break

for _ in range(x):
    print(f"User typed in X: {x}")

print("\n".strip())
# ----------------------------------------------------------------------------------------------------------------------


# define loop function training, def get_num() function to ask for number to run output() inside, and show up main()
def get_num():
    while True:
        y = int(input("Y: "))
        if y < 0:
            continue
        else:
            break
    # must use return, otherwise value 'y' can not be used in other function
    return y


def output(y):
    for _ in range(y):
        print("GO")


def main():
    num = get_num()
    return output(num)


main()
