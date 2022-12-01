import os

cwd = os.getcwd()

calories = open(f"{cwd}/calories.txt", "r")

max_calories = 0
current_calories = 0

for calorie in calories:
    if calorie == '\n':
        # we reached a new elf
        # we first want to re-set the max calories
        if current_calories > max_calories:
            max_calories = current_calories

        # and then we need to reset the current calories
        current_calories = 0
        continue

    current_calories += int(calorie)

calories.close()

print(max_calories) # 68292