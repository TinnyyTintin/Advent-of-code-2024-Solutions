"""
Advent of code 2024 / Day 5 solution for Part 1 and 2.

example input:
47|53
97|47
75|29
75|47
61|13
61|53
53|29
47|61
61|29
29|13

75,47,61,53,29
61,13,29

Part 1:
    - From inputs rules are values separated by "|". Value on left HAS to be BEFORE value on right.
      Ordering rules are inputs after empty line, values separated with comma ",". Check if rules satisfy
      every value in ordering rule. If ordering rule is valid, get the middle value. Sum up these values. Example:
      ==================
      Ordering rule: 75,47,61,53,29

      From rules: 75|47 , 47|61, 61|53, 53|29. All rules apply so ordering rule is valid. Add 61 to sum.

      61,13,29 . 61|13. No rules to satisfy ordering rule, making it invalid.
      ==================


Part 2:
    - Change the order of values in INVALID ordering rules so rules are satisfied. Get the middle value.
      Sum up these values. Example:
      ==================
      Ordering rule: 61,13,29

      Swap 13 -> 29. New ordering rule: 61,29,13

      From rules 61|29, 29|13. All rules apply so ordering rule is valid. Add 29 to sum.
      ==================

"""
# Make a dictionary from each rule, left side as key and all right side values that satisfy rule
# in tuple as dictionary value. Append ordering rules to list as lists.
with open("Day 5 inputs.txt") as file:
    order_rules:list = []
    inputs_dict:dict = {}
    list_decider:bool = True
    for line in file:
        if line.strip() =="":
            list_decider = False
            continue
        # After encountering empty line, list_decider:bool = False -> append rest to order_rules:list.
        elif not list_decider:
            temp_list:list = line.strip().split(",")
            order_rules.append(temp_list)
        else:
            temp = line.strip().split("|")
            # If temp[0] (left side value from rules) in inputs_dict:dict, add temp[1] (right side value from rules)
            # as tuple with earlier values tied to the key.
            if temp[0] in inputs_dict:
                inputs_dict[temp[0]] = tuple(inputs_dict[temp[0]] + (temp[1],))
            # If temp[0] not key in inputs_dict:dict, add it as key and (temp[1]) as value.
            else:
                inputs_dict[temp[0]] = (temp[1],)

# Find valid ordering rules based on rules given at the start.
def find_correct_orders(inputs:dict,order:list):
    middle_nums:int = 0
    incorrect_order:list = order.copy()
    incorrect_ones:list = []

    # Check all values in ordering rule to confirm if they satisfy rules.
    for all_rules in order:
        valid = True
        for value in range(len(all_rules)-1):
            if all_rules[value] not in inputs or not valid:
                break
            for rest in range(value+1,len(all_rules)):
                if all_rules[rest] not in inputs[all_rules[value]]:
                    valid = False
                    break
        else:
            middle_point:int = int(len(all_rules)/2-0.5)
            middle_nums += int(all_rules[middle_point])
            incorrect_ones.append(order.index(all_rules))

    incorrect_ones.sort(reverse=True)
    for indx in incorrect_ones:
        incorrect_order.pop(indx)

    return middle_nums, fix_incorrect_orders(inputs,incorrect_order)

# Swap order of values in invalid ordering rules based on given rules at the start.
def fix_incorrect_orders(inputs:dict,incorrect_order:list):
    middle_nums:int = 0

    # Swap values until ordering rules satisfies all rules.
    for rest_rules in incorrect_order:
        while True:
            valid = True
            #print(rest_rules)
            for value in range(len(rest_rules)-1):
                if rest_rules[value] not in inputs:
                    rest_rules[value],rest_rules[value+1] = rest_rules[value+1],rest_rules[value]
                    valid = False
                    break
                for rest in range(value+1,len(rest_rules)):
                    if rest_rules[rest] not in inputs[rest_rules[value]]:
                        rest_rules[value],rest_rules[value+1] = rest_rules[value+1],rest_rules[value]
                        valid = False
                        break
            if valid:
                middle_point:int = int(len(rest_rules)/2-0.5)
                middle_nums += int(rest_rules[middle_point])
                break
    return middle_nums

answers = find_correct_orders(inputs_dict,order_rules)
print(f"Day 5 solution 1: {answers[0]}\nDay 5 solution 2: {answers[1]}")
