"""
Advent of code 2024 / Day 6 solution for Part 1 and 2.

example input:
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13

Part 1:
    - Values AFTER colon must equal to value BEFORE colon. You can only use operations "+" and "*", and they are always
      executed from left to right. Look through all combinations for operations. Add together all correct lines.
    -  Example:
      ==================
      190: 10 19
      83: 17 5

      10 + 19 = 29... 10 * 19 = 190. Correct. Sum up value 190 with other correct ones.
      17*5 = 85. 17+5 = 22. Incorrect.
      ==================


Part 2:
    - Same rules as part 1 but extra operation, " || " known as concatenation. This joins the 2 values together.
    - Check all lines again with this new operation as possible usage. Example:
      ==================
      156: 15 6

      15*6 = 90. 15+6 = 21. "15"+"6" = 156. Correct. Sum up value 156 with other correct ones.
      ==================

"""
# Make a list of lists with all values separated.
with open("Day 7 inputs.txt") as file:
    calibration_equations = [[line.split(":", 1)[0]] + line.split(":", 1)[1].split() for line in file]

# Find correct lines and return total sum.
def calibration(all_equations:list):
    total_sum:int = 0
    for equation in all_equations:
        if not equation:
            break
        all_sums:list = [int(equation[1])]
        new_value:list = []
        for iterations in range(2,len(equation)):
            current_value = int(equation[iterations])
            # Do all operations with all previous operations and save all values to list.
            for old_value in all_sums:
                new_value.append(current_value+old_value)
                new_value.append(current_value*old_value)
                # Exclude for part 1. Does concatenation
                new_value.append(int(str(old_value)+str(current_value)))
            all_sums = new_value
            new_value = []
        if int(equation[0]) in all_sums:
            total_sum += int(equation[0])
    return total_sum

answers = calibration(calibration_equations)
print("Day 7 Part 2: ",answers)
