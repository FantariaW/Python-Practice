# 2025/05/05
# Arivia Lesson 1 Final Test
# I used "".join(n) to combine first name and last name

# Define even or odd number verify function
def is_even(n):
    return n % 2 == 0


# Define even or odd number verify function
def is_odd(n):
    return n % 2 != 0


# Define user's information
def user_info():
    name = input("Enter your full name: ").strip().split()
    # Split name into first name and last name
    first_name, last_name = name
    age = int(input("Enter your age: "))
    score = float(input("Enter your score: "))
    grade = "Not Assigned"
    even = "Unknown"

    print(f"\nFirst Name: {first_name.title()}")
    print(f"Last Name: {last_name.title()}")

    # if-elif-else checking whether if the entered age is even or odd number
    if is_even(age) and age >= 18:
        even = "True"
        print(f"Age: {age} - Adult - Even Number")
    elif is_odd(age) and age >= 18:
        even = "False"
        print(f"Age: {age} - Adult - Odd Number")
    elif is_even(age) and age < 18:
        even = "True"
        print(f"Age: {age} - Minor - Even Number")
    elif is_odd(age) and age < 18:
        even = "False"
        print(f"Age: {age} - Minor - Odd Number")
    else:
        print("Something Error!")

    # if-elif-else checking grade level
    if 90 <= score <= 100:
        grade = "A"
        print(f"Score: {score} - Grade: A")
    elif 80 <= score < 90:
        grade = "B"
        print(f"Score: {score} - Grade: B")
    elif 70 <= score < 80:
        grade = "C"
        print(f"Score: {score} - Grade: C")
    elif 60 <= score < 70:
        grade = "D"
        print(f"Score: {score} - Grade: D")
    elif 50 <= score < 60:
        grade = "E"
        print(f"Score: {score} - Grade: E")
    elif 0 <= score < 50:
        grade = "F"
        print(f"Score: {score} - Grade: F - Not Pass")
    else:
        print("Score must between 0 - 100")

    # match-case matching 3 special names to print out an exclusive greeting
    # "".join(n) very useful for combine words in list!!!!!!
    match " ".join(name).title():
        case "Fantaria Arivia" | "Arivia Fantaria" | "Silver Moon":
            print(f"\nSpecial Greet: Happy Everyday, {" ".join(name).title()}!!!")
        case _:
            print(f"\nNuh...Good to see you, {" ".join(name).title()}, maybe...")

    # JSON format printing
    print("\nJSON format: ")
    print(f"{{"
          f"\n    \"name\": \"{first_name.title()} {last_name.title()}\","
          f"\n    \"age\": {age},"
          f"\n    \"grade\": {grade},"
          f"\n    \"is_even\": {even}"
          f"\n}}")


user_info()
