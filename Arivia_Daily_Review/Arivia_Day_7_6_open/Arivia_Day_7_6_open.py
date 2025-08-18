# Day 7 Training: open()

# Day 7 Training
class AnimalTracker:
    def __init__(self, animal_name: str, animal_type: str, animal_status: str):
        self.animal_name = animal_name
        self.animal_type = animal_type
        self.animal_status = animal_status

    def __str__(self):
        return f"{self.animal_name.strip().title()} - {self.animal_type.strip().title()} -- {self.animal_status}"

    @classmethod
    def main_page(cls, prompt_choice):
        print("==🎠Animal Shelter Tracker🎠==")

        while True:
            try:
                print("1.Add Animal\n2.View Animal\n3.Mark as Adopted\n4.Summary of Animals\n5.Exit Program")
                user_choice = input(prompt_choice).strip()
                assert user_choice != "", "Please choose 1 - 5 to start program"

                match user_choice.lower():
                    case '1':
                        cls.add_animal("Animal -> ")
                    case '2':
                        cls.view_animal()
                    case '3':
                        cls.mark_adopted("Animal Number -> ")
                    case '4':
                        cls.summary()
                    case '5' | 'exit':
                        print("Bye Bye!")
                        break
                    case _:
                        print("Please choose 1 - 5")
            except AssertionError as e:
                print(e)

    @classmethod
    def add_animal(cls, prompt_animal_info: str):
        print("==🎠Animal Shelter Tracker🎠==")
        print("Please enter Animal name and 3 types of 'dog, cat, rabbit': ")

        while True:
            try:
                animal_info = input(prompt_animal_info).strip()
                if animal_info.lower() in ['5', 'exit']:
                    return
                animal_name, animal_type = animal_info.split(",")
                assert animal_type.lower() in ['dog', 'cat', 'rabbit'], f"❗We have no animal type '{animal_type}' here."
                animal_obj = cls(animal_name, animal_type, "Haven't Adopt!")

                try:
                    with open("animals.txt", "r", encoding="utf-8") as animals_file:
                        lines = animals_file.readlines()
                        total = len(lines) + 1
                except FileNotFoundError:
                    total = 1
                    print("📂File not Found, New file Created!")

                with open("animals.txt", "a", encoding="utf-8") as animals_file:
                    match animal_type.lower():
                        case 'dog':
                            animals_file.write(f"{total}.[🐶] {animal_obj.__str__()} [❌]\n")
                            print(f"✅Registered [{animal_name.title()}, {animal_type.title()}]")
                        case 'cat':
                            animals_file.write(f"{total}.[🐱] {animal_obj.__str__()} [❌]\n")
                            print(f"✅Registered [{animal_name.title()}, {animal_type.title()}]")
                        case 'rabbit':
                            animals_file.write(f"{total}.[🐰] {animal_obj.__str__()} [❌]\n")
                            print(f"✅Registered [{animal_name.title()}, {animal_type.title()}]")
            except (ValueError, AssertionError) as e:
                print(e)

    @staticmethod
    def view_animal():
        try:
            print("=" * 60)
            print("==🎠View Animal List🎠==")
            with open("animals.txt", "r", encoding="utf-8") as animals_file:
                lines = animals_file.readlines()
                for line in lines:
                    print(line, end="")
            print("=" * 60)
        except FileNotFoundError:
            print("📂File not Found!")

    @classmethod
    def mark_adopted(cls, prompt_animal_number):
        print("=" * 60)
        print("==🎠Mark Animal as Adopted🎠==")
        try:
            with open("animals.txt", "r", encoding="utf-8") as animals_file:
                # 這個代碼有效過濾空行問題
                # lines = [line for line in animals_file.read lines() if line.strip() != ""]
                lines = animals_file.readlines()
        except FileNotFoundError:
            print("📂File not Found!")

        while True:
            try:
                print("Please enter Animal series number: ")
                animal_number = input(prompt_animal_number).strip()
                if animal_number.lower() == 'exit':
                    return
                # ❗最後一行的 “\n” 空行，是 IndexError，由於 assert 抓取問題，所以只通過 AssertError 彈出自定義bug！
                assert animal_number.isdigit and 1 <= int(animal_number) <= len(lines), "❗Series Number Not Exist."

                old_animal_obj = lines[int(animal_number) - 1].split("] ")[1]
                new_animal_name, new_type_status = old_animal_obj.split(" - ")
                new_animal_type, new_animal_status = new_type_status.split(" -- ")

                new_animal_status = "Adopted!"
                new_animal_obj = cls(new_animal_name, new_animal_type, new_animal_status)

                match new_animal_type.lower():
                    case 'dog':
                        lines[int(animal_number) - 1] = f"{animal_number}.[🐶] {new_animal_obj.__str__()} [✅]\n"
                    case 'cat':
                        lines[int(animal_number) - 1] = f"{animal_number}.[🐱] {new_animal_obj.__str__()} [✅]\n"
                    case 'rabbit':
                        lines[int(animal_number) - 1] = f"{animal_number}.[🐰] {new_animal_obj.__str__()} [✅]\n"

                with open("animals.txt", "w", encoding="utf-8") as animals_file:
                    for line in lines:
                        animals_file.write(f"{line}")
                        print(line, end="")
                print("=" * 60)
            except (ValueError, AssertionError) as e:
                print(e)

    @staticmethod
    def summary():
        print("=" * 60)
        print("==🎠Animal Summary🎠==")
        try:
            summary_dict = {
                'dog': 0,
                'dog adopted': 0,
                'cat': 0,
                'cat adopted': 0,
                'rabbit': 0,
                'rabbit adopted': 0,
                'all adopted': 0,
                'all not_adopted': 0,
                'all animal': 0
            }

            with open("animals.txt", "r", encoding="utf-8") as animals_file:
                lines = animals_file.readlines()
                for line in lines:
                    if "🐶" in line:
                        summary_dict['dog'] += 1
                        if "✅" in line:
                            summary_dict['dog adopted'] += 1

                    if "🐱" in line:
                        summary_dict['cat'] += 1
                        if "✅" in line:
                            summary_dict['cat adopted'] += 1

                    if "🐰" in line:
                        summary_dict['rabbit'] += 1
                        if "✅" in line:
                            summary_dict['rabbit adopted'] += 1

                    if "✅" in line:
                        summary_dict['all adopted'] += 1
                    if "❌" in line:
                        summary_dict['all not_adopted'] += 1
                    summary_dict['all animal'] += 1

                adopted_rate = (summary_dict['all adopted'] / summary_dict['all animal']) * 100
                print(f"Dog - {summary_dict['dog']} ({summary_dict['dog adopted']} Adopted!)\n"
                      f"Cat - {summary_dict['cat']} ({summary_dict['cat adopted']} Adopted!)\n"
                      f"Rabbit - {summary_dict['rabbit']} ({summary_dict['rabbit adopted']} Adopted!)\n"
                      f"Summary: {summary_dict['all animal']}"
                      f" / Adopted: {summary_dict['all adopted']}"
                      f" / Adopted Rate: {adopted_rate}%")
            print("=" * 60)
        except FileNotFoundError:
            print("📂File not Found!")


def main():
    AnimalTracker.main_page("-> ")


if __name__ == "__main__":
    main()
