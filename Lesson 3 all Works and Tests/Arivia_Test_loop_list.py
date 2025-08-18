# 2025/05/06
# loop and list test from Arivia

# define value and list
def value():
    i = 0
    staff_num = 0
    staff_list = []
    output_list = []
    return i, staff_num, staff_list, output_list


def main():
    # call function value()
    i, staff_num, staff_list, output_list = value()

    # deside how many employee to add in form
    while True:
        num = input("Please type a number to deside how many employees you want to add in form: ".strip())
        if num.isdigit() and int(num) > 0:
            staff_num = int(num)
            break
        else:
            print("Entered value must greater than 0")
            continue

    # entering full name first and last, and age, test if age is numeric
    while i < staff_num:
        set_name = input("Employee's full name: ").strip().split()
        name = " ".join(set_name)
        while True:
            try:
                age = int(input("Employee's age: "))
                break
            except ValueError:
                print("Age must be numeric!")
        staff_list.append((name, age))

        i += 1

    # output: print out every thing in JSON form
    print("[")
    for name, age in staff_list:
        first, last = name.split()
        output_list.append(f"  {{ \n    \"Name\": \"{first.title()} {last.title()}\" \n    \"Age\": {age} \n  }}")

    print(",\n".join(output_list))
    print("]")


main()
