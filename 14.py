from aoc import read_input

lines = read_input()

R = len(lines)
C = len(lines[0])


def pos_gen(dir):
    dx, dy = dir
    y_range = range(R - 1, -1, -1) if dy == 1 else range(R)
    x_range = range(C - 1, -1, -1) if dx == 1 else range(C)
    for y in y_range:
        for x in x_range:
            yield (x, y)


def move_rocks(rocks, dir):
    dx, dy = dir
    for col, row in pos_gen(dir):
        if rocks[row][col] == "O":
            x, y = col, row
            rocks[row][col] = "."
            while 0 <= x < C and 0 <= y < R and rocks[y][x] == ".":
                x += dx
                y += dy
            rocks[y - dy][x - dx] = "O"

    return rocks


def get_load(rocks):
    total = 0
    for row, line in enumerate(rocks):
        for c in line:
            if c == "O":
                total += R - row
    return total


rocks = [[c for c in line] for line in lines]
rocks = move_rocks(rocks, (0, -1))
print(get_load(rocks))

rocks = [[c for c in line] for line in lines]
seen_rocks = {}
totals = []
cycle_num = 0
while True:
    cycle_num += 1
    for dir in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        rocks = move_rocks(rocks, dir)

    total = get_load(rocks)
    totals.append(total)

    rockStr = str(rocks)
    if rockStr in seen_rocks:
        diff = cycle_num - seen_rocks[rockStr]
        cycle = totals[-diff:]
        print(cycle[((1000000000 - cycle_num) % diff) - 1])
        break

    seen_rocks[rockStr] = cycle_num
