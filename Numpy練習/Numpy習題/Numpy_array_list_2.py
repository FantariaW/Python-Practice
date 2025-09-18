# Numpy Practice: array, list
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Numpy Practice:
import numpy as np
import pandas as pd


class StudentGradeList:
    def __init__(self, student_list):
        self.student_list = student_list

    def __str__(self):
        result_list = []

        for index, row in enumerate(self.student_list, 1):
            result_list.append(f"{index}.{row}")

        return "\n".join(result_list)


class NumpyList:
    @staticmethod
    def to_np(student_list):
        np_student_list = np.array(student_list)

        return np_student_list


class GetList:
    @staticmethod
    def get_prompt(prompt_msg):
        while True:
            try:
                user_input = int(input(prompt_msg))
                return user_input
            except ValueError:
                print("Invalid Value...")

    @staticmethod
    def get_list():
        student_list = []

        print("=Student Final Form=")

        student_num = GetList.get_prompt("Enter Number of Student: ")
        subject_num = GetList.get_prompt("Enter Number of Subject: ")

        for i in range(student_num):
            subject_list = []
            for g in range(subject_num):
                while True:
                    try:
                        subject_grade = input(f"Student {i + 1}'s Subject Grade {g + 1}: ")
                        if float(subject_grade):
                            subject_list.append(float(subject_grade))
                            break
                        else:
                            print("Invalid Grade...")
                    except AssertionError:
                        print("Invalid Grade...")
            student_list.append(subject_list)

        return student_list


class Main:
    @staticmethod
    def main():
        student_list = GetList.get_list()
        cls_student_list = StudentGradeList(student_list)
        np_student_list = NumpyList.to_np(student_list)

        print("原list表格:\n", student_list, "\n")
        print("存入init的表:\n", cls_student_list, "\n")
        print("Numpy轉化的列表:\n", np_student_list, "\n")
        print("DF格式:\n", pd.DataFrame(student_list), "\n")
        print("每個學生的科目總成績(行向計算):\n", np_student_list.sum(axis=1), "\n")
        print("每種科目的總分數計算(列向計算):\n", np_student_list.sum(axis=0), "\n")
        print("每门科目的最高分:", np_student_list.max(axis=0), "\n")
        print("每门科目的最低分:", np_student_list.min(axis=0), "\n")

    if __name__ == "__main__":
        main()
