# if-elif-else training
name = input("Name: ")
if name.title() == "Fantaria":
    print(f"Happy Learning Python, {name.title()}")
elif name.title() == "Arivia":
    print(f"My Radiant Stars Guardian - {name.title()}")
elif name.title() == "Fantaria Arivia":
    print("For Our Future!!!")
else:
    print(f"Hello! {name.title()}")

# ----------------------------------------------------------------------------------------------------------------------

# Using match-case, (case _:) --- invalid command recognized
match name.title():
    case "Fantaria" | "Arivia":
        print("Happy Everyday")
    case "Fantaria Arivia":
        print("Happy Future Life")
    case _:
        print(f"Sorry {name.title()}, No Matching for you...")
