# 2025/05/03
# Arivia Lesson 1 Final Test

# Define square, (n)**2
def square(n):
    return n * n


# Using define function call to print out every thing
def result():
    first_name, last_name, age, fav_num, height = (
        input("Please enter First name, Last name, Age, Favourite number, Height: ").split())

    print(f"\nWelcome, {first_name.strip().title().upper()} {last_name.strip().title().upper()}! \nYou are {age} years old."
          f"\nYour lucky number squared is: {square(int(fav_num))}"
          f"\nYour height rounded to 1 decimal place: {float(height):.1f}m", end="\n\n")

    print("JSON format: ")
    print(f"{{\n  \"user\": {{"
          f"\n    \"name\": \"{first_name.strip().title().upper()} {last_name.strip().title().upper()}\","
          f"\n    \"age\": {age},"
          f"\n    \"height\": {float(height):.1f}m,"
          f"\n    \"favorite_number_squared\": {square(int(fav_num))}"
          f"\n  }}"
          f"\n}}")


result()
