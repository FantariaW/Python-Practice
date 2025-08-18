# Day 7 Training: open()

# Day 7 Training
class StudyPlan:
    def __init__(self, study_subject: str, study_topic: str, study_status="Not Yet"):
        self.study_subject = study_subject
        self.study_topic = study_topic
        self.study_status = study_status

    def __str__(self):
        return f"{self.study_subject.strip().title()} -> {self.study_topic.strip().title()} -- {self.study_status}!"

    @classmethod
    def main_page(cls, prompt_choice):
        print("==🧭StudyPlan Tracker🧭==")
        while True:
            try:
                print("1.Add Plan\n2.View Plan\n3.Mark as Done\n4.Exit")
                choice = input(prompt_choice).strip()

                match choice.lower():
                    case "1":
                        cls.add_plan("Add Plan -> ")
                    case "2":
                        cls.view_plan()
                    case "3":
                        cls.mark_plan("Series Number -> ")
                    case "4":
                        cls.summary_plan()
                        print("🔥Bye Bye~🔥")
                        break
                    case _:
                        raise ValueError("Please type in 1 - 4")
            except ValueError as e:
                print(e)

    @classmethod
    def add_plan(cls, prompt_study_plan: str):
        print("==🧾StudyPlan Tracker Adding Plan🧾==")
        while True:
            try:
                study_plan = input(prompt_study_plan).strip()
                if study_plan.lower() in ["4", "exit"]:
                    return
                study_subject, study_topic = study_plan.split(",")
                study_obj = cls(study_subject, study_topic)

                try:
                    with open("study.txt", "r", encoding="utf-8") as study_file:
                        lines = study_file.readlines()
                        total = len(lines) + 1
                except FileNotFoundError:
                    total = 1
                    print("📂File: 'study.txt' Not Found, New File Created!")
                with open("study.txt", "a", encoding="utf-8") as study_file:
                    study_file.write(f"{total}.[📖] {study_obj.__str__()}\n")
                    print(f"✅{study_subject.strip()}, {study_topic.strip()} Added Successfully!")
            except ValueError as e:
                print(e)

    @staticmethod
    def view_plan():
        print("==🧾StudyPlan List🧾==")
        try:
            with open("study.txt", "r", encoding="utf-8") as study_file:
                lines = study_file.readlines()
                for line in lines:
                    print(line, end="")
        except FileNotFoundError:
            print("📂File: 'study.txt' Not Found, New File Created!")

    @classmethod
    def mark_plan(cls, prompt_plan_num):
        print("==📌Mark Plan as Done!📌==")
        print("Please type in series number of study plan to mark it as done: ")
        try:
            with open("study.txt", "r", encoding="utf-8") as study_file:
                lines = study_file.readlines()
        except FileNotFoundError:
            print("📂File: 'study.txt' Not Found, New File Created!")

        while True:
            try:
                plan_num = input(prompt_plan_num).strip()
                if plan_num.lower() in ["exit"]:
                    return
                assert plan_num.isdigit() and int(plan_num) <= len(lines), "Plan not Exist!"

                for index, line in enumerate(lines):
                    if index == int(plan_num) - 1:
                        new_obj = line.split("] ")[1]
                        new_study_subject, new_topic_status = new_obj.split(" -> ")
                        new_study_topic, new_study_status = new_topic_status.split(" -- ")

                        new_study_status = "Done"
                        new_study_obj = cls(new_study_subject, new_study_topic, new_study_status)
                        # 這才是「真正修改對應那一行」的地方 ✔️ 是我自己用 lines[x] = ... 明確指派的！
                        lines[index] = f"{int(plan_num)}.[✅] {new_study_obj.__str__()}\n"

                with open("study.txt", "w", encoding="utf-8") as study_file:
                    for line in lines:
                        study_file.write(line)
                        print(line, end="")
            except AssertionError as e:
                print(e)

    @staticmethod
    def summary_plan():
        count_done = 0
        count_not_yet = 0

        with open("study.txt", "r", encoding="utf-8") as study_file:
            lines = study_file.readlines()
            for index, line in enumerate(lines):
                index += 1
                if "✅" in line:
                    count_done += 1
                if "📖" in line:
                    count_not_yet += 1
            print(f"📊 總任務數: {index}")
            print(f"✅ 已完成: {count_done}")
            print(f"📖 未完成: {count_not_yet}")
            print(f"完成率: {(count_done / index) * 100:.1f}%")


def main():
    StudyPlan.main_page("-> ")


if __name__ == "__main__":
    main()
