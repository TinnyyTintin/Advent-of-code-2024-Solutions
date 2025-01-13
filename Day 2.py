"""
Advent of code 2024 / Day 2 solution for part 1 and 2.

example input:
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1

Part 1:
Line is considered safe if
    - The all values are either all increasing or all decreasing per line.
    - Any two adjacent values differ by at least one and at most 3

Part 2:
Line is also considered safe if
    - 1 mismatching value is removed from line and rules from Part 1 apply to this new line.
"""

with open("Day 2 inputs.txt") as file:
    new_list:list = []
    for line in file:

        # Make a value:list by stripping and splitting lines one by one.
        value:list = line.strip().split()
        temp_list:list = []

        # Change values inside value:list to integer and append to temp_list:list and append
        # temp_list:list to new_list:list of lists.
        for i in value:
            temp_list.append(int(i))
        new_list.append(temp_list)

clear:int = 0
unsafe_ones:list = []

# Iterate each value:list inside new_list:list of lists.
for value in new_list:
    up:bool = False
    down:bool = False
    # Iterate through each number:int inside value:list and change up:bool or down:bool based on previous number:int.
    # Maximum difference between adjacent numbers is 3.
    for number in range(1, len(value)):
            difference = value[number] - value[number - 1]
            if 0 > difference >=-3 and not up :
                down = True
            elif 0 < difference <=3 and not down:
                up = True
            else:
            # If up:bool or down:bool activates midway, value:list is added to unsafe_ones:list.
                unsafe_ones.append(value)
                break
    # Count of value:lists passing through are added to clear:int.
    else:
        clear +=1

part_one_solution:int = clear

# Iterate through unsafe_value:lists inside unsafe_ones:list of lists.
for unsafe_value in unsafe_ones:
    up = False
    down = False
    list_versions = []

    # Copy unsafe_value:list to new_value:list and remove index one by one.
    for number in range(len(unsafe_value)):
        new_value = unsafe_value.copy()
        new_value.pop(number)

        # Iterate through tolerate:int in new_value:lists and change up:bool or down:bool based on previous number:int.
        for tolerate in range(1, len(new_value)):
                difference = new_value[tolerate] - new_value[tolerate - 1]
                if 0 > difference >=-3 and not up :
                    down = True
                elif 0 < difference <=3 and not down:
                    up = True
                else:
                    break
        # Add count of passing new_value:lists to clear:int.
        else:
            clear +=1
            break
print(f"Part 1 answer: {part_one_solution}\nPart 2 answer: {clear}")
