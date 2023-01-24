width = 3
height = 3
stage = []
for i in range(height):
    stage.append([False]*width)

def print_stage(stage):
    for row in stage:
        horizontal_line = "-" * (2 * len(row) + 1)
        print(horizontal_line)
        print_row = "|"
        for elem in row:
            if elem:
                print_row += "o"
            else:
                print_row += " "
            print_row += "|"
        print(print_row)
    horizontal_line = "-" * (2 * len(stage[0]) + 1)
    print(horizontal_line)

def count_neighbors(stage, v_pos, h_pos):
    count = 0
    # +2 because range is not inclusive
    for y in range(v_pos - 1, v_pos + 2):
        for x in range(h_pos - 1, h_pos + 2):
            if y == v_pos and x == h_pos:
                continue # skipping element
            # elements outside of the grid are off
            # and do not add to the count
            if y < 0 or y >= len(stage[0]):
                continue 
            if x < 0 or x >= len(stage):
                continue
            if stage[y][x]:
                count += 1
    return count
