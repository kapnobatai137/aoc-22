import os

cwd = os.getcwd()

calories = open(f"{cwd}/calories.txt", "r")

current_calories = 0

summed_calories_list = []

for calorie in calories:
    if calorie == '\n':
        summed_calories_list.append(current_calories)
        current_calories = 0
        continue
    
    current_calories += int(calorie)

calories.close()

sorted_summed_calories_list = sorted(summed_calories_list, reverse=True)

top_three_elf_calories = sum(sorted_summed_calories_list[:3])

print(top_three_elf_calories) # 203203