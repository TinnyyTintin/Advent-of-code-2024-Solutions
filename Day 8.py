"""
Advent of code 2024 / Day 6 solution for Part 1 and 2.

example input:
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............

Part 1:
    - All Symbols represent antennas and same symbols have same frequency . Antidotes appear behind distance between
      all same frequencies within boundaries. Can appear on top of another antenna. Calculate all antidotes. Example:
      ==================
      ............                  ......#....#
      ........0...                  ...#....0...
      .....0......                  ....#0....#.
      .......0....                  ..#....0....
      ....0.......                  ....0....#..
      ......A.....        -->       .#....A.....
      ............                  ...#........
      ............                  #......#....
      ........A...                  ........A...
      .........A..                  .........A..
      ............                  ..........#.
      ............                  ..........#.

      Topmost 0 is at [1][8], one below [2][6]. Distance between them is [-1][2]. antidote would appear at [0][10].
      Repeat for each remaining same frequency. Then move to next same frequency and repeat again. Right side above
      shows all the antidote locations marked with #.
      ==================


Part 2:
    - Same rules as part 1 but the antidotes appear repeatedly in whole line of the "direction" (distance) AND at the
     positions of each antenna, same distance between each other. Calculate all antidotes. Example:
      ==================
      ............                    ##....#....#
      ........0...                    .#.#....0...
      .....0......                    ..#.#0....#.
      .......0....                    ..##...0....
      ....0.......                    ....0....#..
      ......A.....         -->        .#...#A....#
      ............                    ...#..#.....
      ............                    #....#.#....
      ........A...                    ..#.....A...
      .........A..                    ....#....A..
      ............                    .#........#.
      ............                    ...#......##

      Right side above shows all the antidote locations marked with #.
      ==================

"""
# Open input as 2D matrix, each line having individual characters
with open ("Day 8 inputs.txt") as file:
    antenna_map:list = [[char for char in line.strip()] for line in file]

# Find all antidotes.
def find_antidotes(map_to_search:list):
    all_antennas:dict = {}
    total_antidotes_part2:int = 0
    antidote_locations_1: set = set()
    antidote_locations_2:set = set()
    tot = 0
    # Find all unique characters and save them as key: value is coordinates of them.
    for row in range(len(map_to_search)):
        for i,antenna in enumerate(map_to_search[row]):
            if antenna == ".":
                continue
            elif antenna in all_antennas:
                all_antennas[antenna].append((row,i))
            else:
                all_antennas[antenna] = [(row,i)]

    # Iterate through all values of all characters.
    for antenna in all_antennas:
        iterations = len(all_antennas[antenna])
        for coord in range(iterations):
            total_antidotes_part2 += 1
            for potential in range(iterations):
                other_coord = all_antennas[antenna][potential]
                current_coord = all_antennas[antenna][coord]
                # Skips current location.
                if other_coord == current_coord:
                    continue
                else:
                    # Calculates distance and then position of potential antidote.
                    potential_antidote = (current_coord[0]-other_coord[0],current_coord[1]-other_coord[1])
                    validate = (current_coord[0]+potential_antidote[0],current_coord[1]+potential_antidote[1])
                    # Boolean to skip repeated steps to get answer for solution 1 at the same time.
                    first_value:bool = True
                    if validate in antidote_locations_1:
                        first_value = False
                    # Repeat steps until out of bounds and save unique antidotes and locations to set.
                    while 0 <= validate[0] < len(map_to_search) and 0 <= validate[1] < len(map_to_search[0]):
                        if first_value:
                            antidote_locations_1.add(validate)
                            first_value = False
                        if validate in antidote_locations_2:
                            validate = (validate[0] + potential_antidote[0], validate[1] + potential_antidote[1])
                            continue
                        if map_to_search[validate[0]][validate[1]] in all_antennas:
                            total_antidotes_part2 -=1
                        total_antidotes_part2 +=1
                        antidote_locations_2.add(validate)
                        validate = (validate[0] + potential_antidote[0], validate[1] + potential_antidote[1])

    return len(antidote_locations_1), total_antidotes_part2

answers = find_antidotes(antenna_map)
print("Day 8 solution 1: ",answers[0],"\nDay 8 solution 2: ",answers[1])
