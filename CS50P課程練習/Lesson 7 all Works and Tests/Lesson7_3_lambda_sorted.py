# Lesson 7: lambda, sorted()
# lambda 是 Anonymous Function
class Students:
    def __init__(self, name: str, house: str):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} is in {self.house}"

    @staticmethod
    def get_name(value):
        # ❗因爲Students存入了name和house這2個物件
        return value.name

    @staticmethod
    def print_out():
        with open("students.csv", "r", encoding="utf-8") as students_file:
            students = []
            # ❗重新復習一下，lines以list形式讀取file
            lines = students_file.readlines()
            for line in lines:
                name, house = line.strip().split(",")
                # ❗現在終於明白@classmethod的含義，
                # ❗在@staticmethod使用Students(name, house)直接呼叫class創建物件
                # ❗在@classmethod中則是使用cls(name, house)創建物件，等同於Students(name, house)
                # ❗__str__只能在class内使用，所以創建物件后，就可以自動根據定義好的str格式輸出出來！
                # ❗6月中到現在7月7日終於理解
                student_obj = Students(name, house)
                students.append(student_obj)

            # 對 students 裡面的 student_obj.name 排序
            # for student_obj in sorted(students, key=Students.get_name):
            #     print(student_obj)
            for student_obj in sorted(students, key=lambda s_obj: s_obj.name):
                print(student_obj)


def main():
    Students.print_out()


if __name__ == "__main__":
    main()
