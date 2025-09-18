# Day 7 Training: open()

# Day 7 Training
class MemoryRecorder:
    def __init__(self, plan: str):
        self.plan = plan

    def __str__(self):
        # 因為在寫入文本時用了 str(new_plan)，那就需要 __str__() 來定義物件轉字串的樣子
        # 不然輸出會是類似 <__main__.MemoryRecorder object at 0x...>。
        return f"{self.plan}"

    @staticmethod
    def count_total():
        with open("memo.txt", "r") as memo_file:
            lines = memo_file.readlines()
            total = len(lines)
        print(f"✨ {total} Plans Totally")

    @classmethod
    def add_memo(cls, prompt_plan: str):
        print("Type in '3' or 'exit' to stop and back to main page.")
        while True:
            try:
                plan = input(prompt_plan).strip()
                if plan.lower() in ['3', 'exit']:
                    return

                new_plan = cls(plan)
                with open("memo.txt", "r") as memo_file:
                    lines = memo_file.readlines()
                    total = len(lines) + 1
                with open("memo.txt", "a") as memo_file:
                    memo_file.write(f"{total}.{str(new_plan)}\n")
                print("✅  New Memory has been added!")
            except ValueError as e:
                print(e)

    @classmethod
    def read_memo(cls):
        print("=" * 40)
        print("📋 - All Memory Records")
        with open("memo.txt", "r") as memo_file:
            lines = memo_file.readlines()
            for line in lines:
                print(line, end="")

    @classmethod
    def get_choose(cls, prompt_choose: str):
        print("* 📝Memory Recorder📝 *")
        print("Please choose what program suppose to do.")

        while True:
            print("=" * 40)
            print("1.Add\n2.Read\n3.Exit")
            try:
                choose = input(prompt_choose).strip()
                match choose.lower():
                    case "1" | "add" | "1.add":
                        cls.add_memo(prompt_plan="Add Plan: ")
                    case "2" | "read" | "2.read":
                        cls.read_memo()
                    case "3" | "exit" | "3.exit":
                        cls.count_total()
                        print("👋 Bye Bye~")
                        break
                    case _:
                        raise ValueError("You must choose 1 of: 1.Add / 2.Read / 3.Exit")
            except ValueError as e:
                print(e)


def main():
    MemoryRecorder.get_choose(" -> ")


if __name__ == "__main__":
    main()
