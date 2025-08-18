# Lesson 9 Training: class
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Lesson 9 Training
class Student:
    def __init__(self, name: str, house: str, patronus: str):
        # 等於 if name == ""  -  但 if not name 更加 pythonic
        if not name:
            # 可以自己建立獨特的Error，但不推薦，因爲其他人會讀不懂
            # AriviaError = ValueError("Missing Name")
            # raise AriviaError
            raise ValueError("Missing Name")
        if house.lower() not in ["house"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}, Patronus: {self.patronus}"

    def charm(self):
        match self.patronus.lower():
            case "arivia":
                return "🐱"
            case "destina":
                return "🐦"
            case _:
                return "❌"


def get_student():
    try:
        name = input("Name: ").strip()
        house = input("House: ").strip()
        patronus = input("Patronus: ").strip()
        return Student(name, house, patronus)
    except ValueError as e:
        print(e)


def main():
    student = get_student()
    print(student)
    print(Student.charm(student))


if __name__ == "__main__":
    main()
