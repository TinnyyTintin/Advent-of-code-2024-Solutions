"""
Advent of code 2024 / Day 4 solution for Part 1 and 2.

example input:
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM

Part 1:
    - Search all appearances of "XMAS" from inputs. Can be vertical, diagonal, written backwards,
      or even overlapping other words. For example:
      =====
      ..X...
      .SAMX.
      .A..A.
      XMAS.S
      .X....
      =====
    irrelevant characters have been replaced with '.'.

Part 2:
    - Search for two "MAS" in shape of X. For example:
      =====
      M.S
      .A.
      M.S
      =====
      irrelevant characters have been replaced with '.'.

"""

# Makes 2D matrix from each character in each line.
with open("Day 4 inputs.txt") as file:
    inputs_list: list = [list(line.strip()) for line in file]

# Check all potential neighbour characters to identify "XMAS".
def find_neighbour(x_axis:int,y_axis:int,word_find:str):
    # Coordinates for each potential neighbour.
    find_followup:list =  [(1,0),
                           (-1,0),
                           (0,1),
                           (0,-1),
                           (1,1),
                           (1,-1),
                           (-1,1),
                           (-1,-1)
    ]
    word_count:int = 0
    # Iterate through all potential neighbours. If character at neighbour is next character in word_find:str,
    # repeat same direction(same tuple from find_followup:list). Add to word_count:int if word_find:str exists
    # in said direction.
    for x_add, y_add in find_followup:
        for step in range(1,(len(word_find))):
            x,y = x_axis + x_add* step, y_axis + y_add* step
            if not (0 <= x < len(inputs_list)) or not (0 <= y < len(inputs_list[0])) or inputs_list[x][y] != word_find[step]:
                break
        else:
            word_count +=1
    return word_count

# Find starting character in each list in matrix, in this case "X".
def find_starting_point(inputs:list,word_to_find:str):
    total_times:int = 0
    for row in range(len(inputs)):
        for character in range(len(inputs[0])):
            if inputs[row][character] == word_to_find[0]:
                # call function find_neighbour() if character at location is "X".
                total_times += find_neighbour(row,character,word_to_find)
    return total_times

# Check all corners around potential tree (2 * MAS in X shape).
def find_trees(x_axis:int,y_axis:int):
    find_followup:list =  [(1,1),
                           (-1,-1),
                           (1,-1),
                           (-1,1),
    ]
    word_count:int = 0
    letters:str = ""
    for x_add, y_add in find_followup:
        x,y = x_axis + x_add, y_axis +y_add
        # append character at location to letters:str if rules apply.
        if not (0 <= x < len(inputs_list)) or not (0 <= y < len(inputs_list[0])) or inputs_list[x][y] != "M" and inputs_list[x][y] != "S":
            return word_count
        letters +=inputs_list[x][y]
    # If 2 adjacent characters are different ("S" and "M") add to word_count:int.
    if letters[0] != letters[1] and letters[2] != letters[3]:
        word_count +=1
    return word_count
# Find starting point of tree (find character "A" in this case).
def find_middle_point(inputs:list):
    total_times:int = 0
    for row in range(len(inputs)):
        for character in range(len(inputs[0])):
            if inputs[row][character] == "A":
                total_times += find_trees(row,character)
    return total_times

print("Day 4 solution 1:",find_starting_point(inputs_list,"XMAS"))
print("Day 4 solution 2:",find_middle_point(inputs_list))
