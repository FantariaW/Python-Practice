# Day 10 Training 1: set(), sorted(), "".join(), [:int] - slicing, constants
# (੭ु｡╹▿╹｡)੭ु⁾⁾
# Day 10 Training:

# 1. 使用 x = set() 去重
MAX_DISPLAY: int = 5
fruits_list = [
    "apple", "banana", "apple", "watermelon", "orange", "pear", "peach"
]

new_fruits_list = set()
for fruit in fruits_list:
    new_fruits_list.add(fruit)

# ❗依字母序列打印，[:MAX_DISPLAY] = [:5]最多5次，所以不會打印watermelon
sorted_fruits_list = sorted(new_fruits_list)
for fruit in sorted_fruits_list[:MAX_DISPLAY]:
    print(fruit)

# ------------------------------------------------------------------------------
print()

# 2. 復習 "".join(str(x) for x in list) 延伸寫法，list 裡的元素必須都是字串
# 使用 sorted(set(x)) 先去重，后排序
MIN_STUDENTS: int = 3
student_id_list = [
    {"id": 1002},
    {"id": 1001},
    {"id": 1004},
    {"id": 1003},
    {"id": 1003},
    {"id": 1002}
]
result = []

for student_id in student_id_list:
    result.append(student_id["id"])

# ❗先 set(result) 去重， 再將去重后的所有數據排序， 最後打印對應 0，1，2 的值 - [:MIN_STUDENTS]
# for item in sorted(set(result))[:MIN_STUDENTS]:
#     print(item)
print(",".join(str(item) for item in sorted(set(result))[:MIN_STUDENTS]))

# ------------------------------------------------------------------------------
print()

# 3. 使用 set() 來查詢内部資料
# ❗更進階的寫法: ALLOWED_COLORS: set[str] = {"red", "green", "blue"}
color_list = [
    "red", "green", "blue"
]
ALLOWED_COLORS = set()
for color in color_list:
    ALLOWED_COLORS.add(color)

# ❗記得加上 Type Hint - x: str，提高可讀性
user_input: str = input("Enter Color: ").strip()
if user_input.lower() in ALLOWED_COLORS:
    print("Color Allowed!")
else:
    print("Not Allowed...")

# ------------------------------------------------------------------------------
print()

# 4. set() 查詢字典列表同樣適用
grade_list = [
    {"grade": "a"},
    {"grade": "b"},
    {"grade": "c"}
]
ALLOWED_GRADE = set()
for grade in grade_list:
    ALLOWED_GRADE.add(grade["grade"])

user_grade: str = input("Enter Grade: ").strip()
if user_grade.lower() in ALLOWED_GRADE:
    print("YES!")
else:
    print("NO...")
