import csv

with open("test.csv", "w", newline="", encoding="utf-8") as test_file:
    csv_writer = csv.DictWriter(test_file, fieldnames=["name", "age"])
    staff = {"name": "Alice", "age": 20}
    staff_lst = [
        {"name": "Scarlet", "age": 21},
        {"name": "Diena", "age": 22}
    ]

    # for row in staff_lst:
    #     csv_writer.writerow(row)

    csv_writer.writerows(staff_lst)
