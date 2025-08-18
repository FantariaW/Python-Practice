# Day 9 Training: super

# Day 9 Training:
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Age: {self.age}\n")


class Developer(Employee):
    def __init__(self, name, age, language):
        super(Developer, self).__init__(name, age)
        self.language = language

    def __str__(self):
        return (f"--Employee Info--\n"
                f"{super().__str__()}"
                f"Language: {self.language}\n")


def prompt_input():
    name = input("Name: ").strip()
    age = input("Age: ").strip()
    language = input("Language: ").strip()

    return Developer(name, age, language)


if __name__ == "__main__":
    print(prompt_input())
