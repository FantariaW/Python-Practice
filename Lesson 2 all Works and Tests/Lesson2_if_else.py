# if-elif-else training: > >= < <= == !=
x = float(input("X value: "))
y = float(input("Y value: "))

# Regular if, elif, else function using
if x < y:
    print("X less than Y")
elif x > y:
    print("X greater than Y")
else:
    print("X equal to Y")


if x != y:
    print("X is not equal to Y")
else:
    print("X equal to Y")


if x == y:
    print("X equal to Y")
else:
    print("X is not equal to Y")

# ----------------------------------------------------------------------------------------------------------------------

# if-elif-else print out grade after verify a entered score
score = float(input("Score: "))

# usual way using if-elif-else
# if score >= 90 and score <= 100:
#     print("Grade: A")
# elif score >= 80 and score <= 90:
#     print("Grade: B")
# elif score >= 70 and score <= 80:
#     print("Grade: C")
# elif score >= 60 and score <= 70:
#     print("Grade: D")
# else:
#     print("Score: F")

# Much more Pythonic way
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
else:
    print("Score: F")
