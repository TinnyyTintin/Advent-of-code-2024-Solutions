"""
Advent of code 2024 / Day 6 solution for Part 1 and 2.

example input:
      ....#.....
      .........#
      ..........
      ..#.......
      .......#..
      ..........
      .#..^.....
      ........#.
      #.........
      ......#...

Part 1:
    - "^" Indicates starting point of Guard. Move to the direction of the arrow until you either encounter "#"
    - or you exit the area. When encountering "#", turn 90 degrees RIGHT. Sum up unique spots visited. Example:
      ==================
      ....#.....
      ....XXXXX#
      ....X...X.
      ..#.X...X.
      ..XXXXX#X.
      ..X.X.X.X.
      .#XXXXXXX.
      .XXXXXXX#.
      #XXXXXXX..
      ......#X..

      Here unique spots have been replaced with X. Totals to 41.
      ==================


Part 2:
    - Same rule of turning when encountering "#" applies. If placing obstacle anywhere but starting position of Guard,
    - can you get the Guard stuck in endless loop. When encountering obstacle, turn 90 degrees RIGHT.
    - Sum up the unique spots for obstacle to achieve endless loops.
      ==================
      ....#.....
      ....+---+#
      ....|...|.
      ..#.|...|.
      ....|..#|.
      ....|...|.
      .#.O^---+.
      ........#.
      #.........
      ......#...

      Here "0" represents obstacle. "|" and "+" represents the movement of Guard. Guard gets into endless loop.
      ==================

"""
# Make 2D matrix from inputs.
with open("Day 6 inputs.txt") as file:
    area_map:list = [[char for char in line.strip()] for line in file]

# Find both unique spots and unique obstacle placements.
def find_unique_positions(area:list):
    marker:dict = { "^":(-1,0),
                    ">":(0,1),
                    "v":(1,0),
                    "<":(0,-1)
    }
    direction_change:dict = { (-1,0):">",
                              (0, 1):"v",
                              (1, 0):"<",
                              (0, -1):"^"
    }
    current_point:list = []
    direction:tuple = ()
    unique_positions:int = 1
    unique_loops:int = 0

    # Find the starting point and save the coordinates and direction.
    for row in area:
        for column in row:
            if column in marker:
                current_point = [area.index(row),row.index(column)]
                direction = marker[column]
    start_point = current_point
    start_direction = direction

    # Loop until out of bounds.
    while True:
        if unique_positions > 1 and not (current_point[0] <(len(area) - 1) and current_point[1] <len(area[0]) - 1):
            break
        current_point = [current_point[0]+direction[0],current_point[1]+direction[1]]
        current_symbol = area[current_point[0]][current_point[1]]

        # Add counter of unique spots and swap symbol from "." to "X". Also check as possible obstacle spot.
        if current_symbol == ".":
            area[current_point[0]][current_point[1]] = "0"
            temp_point = start_point
            temp_direction = start_direction
            valid_direction = ()
            first: bool = True
            steps_map: set = set()

            # Save coordinates and direction to set to determine if endless loop is reached.
            while True:
                if not (0 <= temp_point[0] < len(area) - 1 and 0 <= temp_point[1] < len(area[0]) - 1):
                    break

                temp_point = [temp_point[0] + temp_direction[0], temp_point[1] + temp_direction[1]]
                temp_symbol = area[temp_point[0]][temp_point[1]]
                key = tuple(temp_point) + temp_direction

                if key in steps_map:
                    unique_loops += 1
                    break
                else:
                    steps_map.add(key)

                if temp_symbol in {"#", "0"}:
                    temp_point = [temp_point[0] - temp_direction[0], temp_point[1] - temp_direction[1]]
                    temp_direction = marker[direction_change[temp_direction]]

            area[current_point[0]][current_point[1]] = "X"
            unique_positions +=1

        elif current_symbol == "#":
            current_point = [current_point[0] - direction[0], current_point[1] - direction[1]]
            direction = marker[direction_change[direction]]

    return unique_positions,unique_loops

answers =find_unique_positions(area_map)
print(f"Day 6 solution 1: {answers[0]}\nDay 6 solution 2: {answers[1]}")
