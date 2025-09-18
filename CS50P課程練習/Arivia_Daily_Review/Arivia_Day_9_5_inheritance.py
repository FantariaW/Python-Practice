# Day 9 Training: super
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Day 9 Training:
import re


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Name: {self.name}"


class Student(Person):
    def __init__(self, name, score):
        super(Student, self).__init__(name)
        self.score = int(score)

    # ❌ 這次沒能實現 __add__ 方法
    # def __add__(self, other):
    #     return self.score + other.score

    def __str__(self):
        name = super().__str__()
        return f"{name} - Score: {self.score}"


class PromptInput:
    @staticmethod
    def prompt_input(prompt_msg, assert_msg, error_msg, allow_stop=False):
        while True:
            try:
                user_input = input(prompt_msg).strip()
                if allow_stop is True and user_input.lower() == "stop":
                    return None
                assert assert_msg(user_input), error_msg
                return user_input
            except AssertionError as e:
                print(e)

    @classmethod
    def get_input(cls):
        print("==📝Student Information📝==")
        student_list = []

        while True:
            try:
                name = cls.prompt_input(
                    "Enter Name: ",
                    lambda n: re.fullmatch(r"^[a-z]+ *[a-z]*$", n, re.IGNORECASE),
                    "Invalid Name...",
                    allow_stop=True
                )
                if name is None:
                    break

                score = cls.prompt_input(
                    "Enter Score: ",
                    lambda s: s.isdigit() and 0 <= int(s) <= 100,
                    "Invalid Score..."
                )

                # ❗如果使用 student_obj = Student(name, score) 的話
                # ❗再存入student_list就會變成 存入字串
                # ❗不推薦
                # student_obj = Student(name, score)
                # student_list.append(student_obj.__str__())
                student_list.append(Student(name, score))

            except ValueError as e:
                print(e)
        return student_list


class MainResult:
    def __init__(self, student_list):
        self.student_list = student_list

    def __str__(self):
        result = []
        total_score = 0
        for index, row in enumerate(self.student_list, 1):

            # ❗因爲 student_list 存入的是物件 Student(name, score)
            # ❗所以可以直接使用 row.score 來抓取 score 值
            # total_score += row.score
            total_score += row.score

            result.append(f"{index}.{row}")

        return "\n".join(result) + f"\nTotal Score: {str(total_score)}!"


def main():
    student_list = PromptInput.get_input()
    print(MainResult(student_list))


if __name__ == "__main__":
    main()
