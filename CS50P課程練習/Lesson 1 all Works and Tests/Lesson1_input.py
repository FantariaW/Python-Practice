# Using input to ask for typing words or number
# Need a space between name and age input, otherwise would cause an error
name, age = input("Enter Name and Age pls:").split()

# Remove whitespace from str
# name = name.strip()

# Capitalize user's name
# name = name.capitalize()

# Title which capitalize the first character of each word entered
name = name.title()
# name = input("Name: ").strip().capitalize().title()

# Split user's name into first name and last name
# fullname = input("Enter Full Name: ")
# first, last = fullname.split(" ")
# print(f"Only print out the last name: {last}")

# Backslash n: \n, move to newline
# print("Name: " + name + "\nAge: " + age)
# print("Name: ", name, "\nAge: ", age)

# ----------------------------------------------------------------------------------------------------------------------
print("\nOutput: ")
print(name, int(age), end="\n\n")

# Using end=""
print("Using end=\"\" ----- Name: ", end=">>>")
print(name)

# Using sep=""
print("Using sep=\"\" ----- Age: ", age, age, age, sep="---")

# Using \" inside of syntax to print out double quotes: "
print("Using BackSlash Double Quotes \\\" ----- \"Name\": ", name)

# Using f and curly braces {} to print out a value inside of text
print(f"Using Curly Braces {{}} ----- Name: {name}, Age: {age}", end="\n\n")

# ----------------------------------------------------------------------------------------------------------------------

# A Test from Arivia, Using those knowledge to print out a string like JSON:
# print(f"import json \n\ndata = {{ \n\"name\": \"Fantaria\", \n\"level\": 999, "
#       f"\n\"mood\": \"💥 Learning everything!\" \n}} \n\nprint(json.dumps(data, indent=4))")
