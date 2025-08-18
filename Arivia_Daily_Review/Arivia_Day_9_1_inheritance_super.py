# Day 9 Training: super

# Day 9 Training:
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Dog(Animal):
    def __init__(self, name, breed):
        super(Dog, self).__init__(name)
        self.breed = breed

    def speak(self):
        # ❌return Animal.speak(self) + "woof"  -  硬編碼不推薦！！！
        return super().speak() + " woof"


def main():
    name = input("Dog: ").strip()
    breed = input("Breed: ").strip()
    d = Dog(name, breed)

    print(d.name, d.breed)
    print(d.speak())


if __name__ == "__main__":
    main()
