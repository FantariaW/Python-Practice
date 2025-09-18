import random
# import statistics
import sys
from Arivia_Day_5_2_import import get_flavor, get_average, print_cli_name


# main() function from Arivia_Day_5_2_import.py
# Day 5 Training 1: import random, random.choice()
prompt_flavor = ">> "
flavor_list, count_flavor_dict = get_flavor(prompt_flavor)

print(f"--🐤Flavor Table--")
if count_flavor_dict:
    print("\n".join(f"{flavor_key}: {flavor_value}" for flavor_key, flavor_value in count_flavor_dict.items()))
    print("🐣Random flavor for today - ", random.choice(flavor_list))
else:
    print("No flavors entered 🍃")
    print("🐣Random flavor for today - N/A ")

print("=" * 80)  # =================================================================================================

# Day 5 Training 2: import statistics, statistics.mean()
prompt_average = ">> "
average_list, average_doughnut = get_average(prompt_average)

print("--Doughnut Table--")
for each_doughnut in average_list:
    print(f"{each_doughnut}")

print(f"Each person ordered an average of {average_doughnut:.2f} doughnut🍩")

print("=" * 80)  # =================================================================================================

# Day 5 Training 3: import sys, sys.argv, if __name__ == "__main__":

if len(sys.argv) == 2:
    print_cli_name(sys.argv[1])
else:
    print_cli_name(None)
