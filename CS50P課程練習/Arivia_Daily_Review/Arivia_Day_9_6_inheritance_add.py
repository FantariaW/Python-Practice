# Day 9 Training: super, __add__
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Day 9 Training:
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Name: {self.name}"


class Student(Person):
    def __init__(self, name, score):
        super(Student, self).__init__(name)
        self.score = int(score)

    def __str__(self):
        return f"{super().__str__()} - Score: {self.score}"

    def __add__(self, other):
        # 這裡要能處理「int + Student」或「Student + Student」
        if isinstance(other, Student):
            return self.score + other.score
        elif isinstance(other, int):
            return self.score + other
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, int):
            return other + self.score
        return NotImplemented


def main():
    student_list = []
    total_score = 0

    while True:
        try:
            user_input = input("Enter Name and Score(Split with ','): ").strip()
            if user_input.lower() == "stop":
                break
            name, score = user_input.split(",")
            student = Student(name, score)
            student_list.append(student)
            # total_score = total_score + student.score
            total_score = student + total_score
        except ValueError as e:
            print(e)

    for index, row in enumerate(student_list, 1):
        print(f"{index}.{row}")
    print(f"Total Score: {total_score}")


if __name__ == "__main__":
    main()
