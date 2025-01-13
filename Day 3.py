"""
Advent of code 2024 / Day 3 solution for Part 2.

example input:
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

Part 1 (not fully implemented in the code below):
    - find sequences that starts with "mul(", has numeric values separated by comma and is closed with ")". example
      in example inputs "mul(2,4) is valid, but "mul(32,64]" is not.
    - Multiply the values inside valid sequences and sum them up.

Part 2:
    - find sequences "don't()" and "do()"s. After encountering "don't()", all "mul()" sequences are invalid.
    - Encountering "do()" makes the following "mul()" sequences valid again.

"""

# Read and file line by line, strip them and join to single, long text:str.
with open("Day 3 inputs.txt") as file:
    text:str = " ".join(line.strip() for line in file)

to_find:str = "mul("

def find_index(file_to_process:str, what_to_find:str):

    disable = []
    disable_index = file_to_process.find("don't()")
    activate = []
    activate_index = file_to_process.find("do()")

    # Parse through file_to_process:list and find indexes of "don't()" and "do()" and append them to lists.
    while disable_index !=-1:
        disable.append(disable_index)
        disable_index = file_to_process.find("don't()", disable_index + 7)

    while activate_index !=-1:
        activate.append(activate_index)
        activate_index = file_to_process.find("do()", activate_index + 4)

    # Split string from start to first index of "don't()".
    working_file:str = file_to_process[:disable[0]]
    k:int = 0
    i:int = 0

    # Append characters from file_to_process:str to working_file:str based on if "don't()" or "do()" is active.
    while True:
        # Append characters from last appearance of "do()" to working_file:str.
        if i >= len(disable):
            working_file += file_to_process[activate[-1]:]
            break
        elif activate[k]>disable[i]:
            i +=1
        elif disable[i]>activate[k]:
            working_file += file_to_process[activate[k]:disable[i]]
            while activate[k] <= disable[i]:
                k+=1

    all_mul:list = []
    mul_index = working_file.find(what_to_find)

    # Parse through working_file:str and append indexes of what_to_find:str to all_mul:list.
    while mul_index !=-1:
        all_mul.append(mul_index)
        mul_index = working_file.find(what_to_find, mul_index + 4)

    values:list = []
    total_sum:int = 0

    for i in range(0,len(all_mul)):
        temp = ""
        # Parse through characters of  working_file:str by every index what_to_find:str.
        # Skip 4 characters to start from first value.
        # Append temp:str to values:list when encountering ")".
        for j in range(all_mul[i]+4,len(working_file)):
            if j == len(working_file) and working_file[-1]==")":
                values.append(temp)
                break
            if working_file[j]==")":
                values.append(temp)
                break
            # Add characters to temp if character is not ")".
            else:
                temp += working_file[j]
    # Iterate through all lists inside values:list and separate by comma and try multiplying these values and adding to
    # total_sum:int. Raise ValueError if encountering non numbers.
    for value_pair in values:
        try:
            to_sum = value_pair.split(",")
            total_sum +=int(to_sum[0])*int(to_sum[1])
        except ValueError:
            pass
    return total_sum

print(f"{f"Part 2 answer: {find_index(text,to_find)}"}")