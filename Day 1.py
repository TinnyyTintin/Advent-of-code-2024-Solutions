"""
Advent of code 2024 / Day 1 solution for Part 2.

example input:
3   4
4   3
2   5
1   3

Part 1 (not fully implemented in the code below):
    - Pair up the smallest number in the left list with the smallest number in the right list
      then the second-smallest left number with the second-smallest right number and so on.
    - Calculate distance between these paired numbers and sum them up.

Part 2:
    - Count appearances from left list's values in right list. example value 3 from left appears 2 times on right
      in example inputs. Iterate through all of left side and do same thing.
    - multiply the values with count of appearances and sum them up.

"""
# Write all lines to inputs_list from file.
with open("Day 1 inputs.txt") as file:
    inputs_list: list = file.readlines()

    left_parsed_list:list = []
    right_parsed_list:list = []
    iterable:int = 1

# Iterate over each line in inputs_list.
for line in inputs_list:

    # Strip whitespaces and split data with whitespace.
    parsing: list = line.strip().split()

    # Iterate over each data in parsing.
    for words in parsing:
        iterable +=1

        # Alternatively append left and right data from parsing to corresponding new lists.
        if iterable % 2 == 0:
            left_parsed_list.append(words)
        else:
            right_parsed_list.append(words)

leftover_list: list = []

for i in range(len(left_parsed_list)):

    # Add value from left_parsed_list to value if found in right_parsed_list.
    if left_parsed_list[i] in right_parsed_list:
        value:int = int(left_parsed_list[i])
        count:int = 0

        # Check the count of values in right_parsed_list.
        for j in right_parsed_list:
            if int(j) == value:
                count +=1

        # Add the multiplication of count * value to leftover_list.
        leftover_list.append(value * count)

# Sum up values from leftover_list to total_sum.
total_sum:int = sum(leftover_list)

print(f"Part 1 answer: {total_sum}")