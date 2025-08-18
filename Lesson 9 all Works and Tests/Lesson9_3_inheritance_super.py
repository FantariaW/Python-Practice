# Lesson 9 Training: super

# Lesson 9 Training:
# ❗super().__init__(name)  =  function_name.__init__(self, name)
# base class
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name...")
        self.name = name

    def __str__(self):
        return f"{self.name}"


# subclass
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    def __str__(self):
        return f"{super().__str__()} - {self.house}."


# subclass
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f"{super().__str__()} - {self.subject}"


student = Student("Arivia", "Moon")
professor = Professor("Professor One", "Teaching Python")

# 在 Python 中，print() 会自动调用对象的 __str__() 方法。
# 所以 print(student) 等价于 print(student.__str__())，
# 又等价于 print(Student.__str__(student))。
#
# ✅ 推荐写法：
#     print(student)      # 更简洁、可读性高
# ❗ 不常用写法：
#     print(Student.__str__(student))   # 显式调用 class.__str__(object)
print(Student.__str__(student))
print(professor)
