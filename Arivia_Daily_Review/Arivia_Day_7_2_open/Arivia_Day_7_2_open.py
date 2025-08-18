# Day 7 Training: open()

# Day 7 Training
class TaskReport:
    def __init__(self, task: str, status="Incomplete"):
        self.task = task
        self.status = status

    def __str__(self):
        return f"{self.task}, {self.status}"

    @classmethod
    def add_task(cls, prompt_task: str):
        print("Type in 'exit' to return back to menu")
        print("📌-Please enter your task:")
        while True:
            try:
                task = input(prompt_task).strip()
                if task.lower() == 'exit':
                    return
                # 異常處理 exception handling
                try:
                    with open("tasks.txt", "r", encoding="utf-8") as tasks_file:
                        lines = tasks_file.readlines()
                        total = len(lines) + 1
                except FileNotFoundError:
                    total = 1

                new_obj = cls(task)  # 建立 TaskReport 物件，只給 task
                with open("tasks.txt", "a", encoding="utf-8") as tasks_file:
                    tasks_file.write(f"{total}.[❌] {new_obj.__str__()}\n")  # 自動透過 __str__(), 包含了task, status
                    print("✅ Added Successfully!")
            except ValueError as e:
                print(e)

    @staticmethod
    def read_task():
        try:
            with open("tasks.txt", "r", encoding="utf-8") as tasks_file:
                print("==📋Task List📋==")
                lines = tasks_file.readlines()
                for line in lines:
                    print(line, end="")
        except FileNotFoundError as e:
            print(e)

    @classmethod
    def mark_task(cls, prompt_task_num):
        print("==🖊️Choose the number of a task, Mark that task as completed🖊️==")
        try:
            with open("tasks.txt", "r", encoding="utf-8") as tasks_file:
                lines = tasks_file.readlines()
        except FileNotFoundError as e:
            print(e)

        while True:
            try:
                task_num = input(prompt_task_num).strip()
                if task_num.lower() == 'exit':
                    return
                assert task_num.isdigit() and int(task_num) <= len(lines), "Please choose a exist number of task"

                for index, line in enumerate(lines):
                    if index == int(task_num) - 1:
                        new_obj = line.split(",")
                        print("The chosen task:")
                        print(new_obj[0].strip(), new_obj[1].strip())

                        new_obj[0] = new_obj[0].replace("❌", "✅")
                        new_obj[1] = "Complete!"
                        mark_obj = cls(new_obj[0], new_obj[1])
                        lines[int(task_num) - 1] = f"{mark_obj.__str__()}\n"

                with open("tasks.txt", "w", encoding="utf-8") as tasks_file:
                    # open(..., "w")：一打開檔案，就把 tasks.txt 裡原本的內容清空了
                    # 然後馬上開始寫入這個 lines 清單的內容
                    for line in lines:
                        tasks_file.write(line)
                    print("✅ Now Marked Complete!")
                with open("tasks.txt", "r", encoding="utf-8") as tasks_file:
                    print("==📋Task List📋==")
                    lines = tasks_file.readlines()
                    for line in lines:
                        print(line, end="")
            except (ValueError, AssertionError) as e:
                print(e)

    @classmethod
    def get_prompt(cls, prompt_choice: str):
        print("==📦Task Tracker📦==")
        print("Please type 1 - 4 to choose what to do:")
        while True:
            print("1.Add Task\n2.Read Task\n3.Mark Finished Task\n4.Exit\n")
            try:
                choice = input(prompt_choice).strip()
                match choice:
                    case "1":
                        cls.add_task("Add Task -> ")
                    case "2":
                        cls.read_task()
                    case "3":
                        cls.mark_task("Mark Task -> ")
                    case "4":
                        print("🔥Have a good day, Bye~Bye~🔥")
                        break
                    case _:
                        raise ValueError("Please choose 1 - 4!")
            except ValueError as e:
                print(e)


def main():
    TaskReport.get_prompt("Choose -> ")


if __name__ == "__main__":
    main()
