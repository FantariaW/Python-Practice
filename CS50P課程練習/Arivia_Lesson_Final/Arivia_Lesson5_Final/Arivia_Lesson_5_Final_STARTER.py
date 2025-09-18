# STARTER file for Arivia_Lesson_5_Final_import.py
from Arivia_Lesson_5_Final_import import get_festival_data, build_summary_dict, print_summary_table

prompt_name = "Name >> "
prompt_candy_count = ""

festival_list, total_candy_dict = get_festival_data(prompt_name, prompt_candy_count)

print(festival_list)
print("📦User bought Table📦")
print("-" * 40)
print(build_summary_dict(festival_list))

print("\n")

print(total_candy_dict)
print("🎉 Candy Festival Summary 🎉")
print("-" * 40)
print(print_summary_table(total_candy_dict))
