# Day 9 Training: super

# Day 9 Training:
import re


class PrintList:
    def __init__(self, emp_lst: list):
        self.emp_lst = emp_lst

    def __str__(self):
        result = []
        for index, emp in enumerate(self.emp_lst, 1):
            result.append(f"ID: {index}.{emp}")

        return "\n".join(result)


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name} - Age: {self.age}"


class Designer(Employee):
    def __init__(self, name, age, tool):
        super(Designer, self).__init__(name, age)
        self.tool = tool

    def __str__(self):
        emp_info = f"{super().__str__()} - {self.tool}"
        return emp_info


class PromptInput:
    @staticmethod
    def prompt_validate(prompt_msg, assert_msg, error_msg, allow_stop=False):
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
    def prompt_input(cls, prompt_name="Name: ",
                     prompt_age="Age(20-50): ",
                     prompt_tool="Tool(Excel/Pycharm/VS): "):
        print("📝簡易員工管理系統📝")
        emp_lst = []

        while True:
            try:
                name = cls.prompt_validate(
                    prompt_name,
                    lambda n: re.search(r"^[a-z]+ *[a-z]*$", n),
                    "Invalid Name...",
                    allow_stop=True
                )
                if name is None:
                    print("Bye Bye")
                    break

                age = cls.prompt_validate(
                    prompt_age,
                    lambda a: 20 <= int(a) <= 50,
                    "Invalid Age..."
                )

                tool = cls.prompt_validate(
                    prompt_tool,
                    lambda t: t.lower() in ["excel", "pycharm", "vs"],
                    "Invalid Tool..."
                )
                emp_info = Designer(name, age, tool)
                emp_lst.append(emp_info)
            except ValueError as e:
                print(e)
        return emp_lst


def main():
    emp_lst = PromptInput.prompt_input()
    print(PrintList(emp_lst))


if __name__ == "__main__":
    main()
