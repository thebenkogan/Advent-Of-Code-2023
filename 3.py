from collections import defaultdict
from aoc import read_input

lines = read_input()
R = len(lines)
C = len(lines[0])


def get_symbol(x, y):
    if 0 <= x < C and 0 <= y < R and lines[y][x] != "." and not lines[y][x].isdigit():
        return (lines[y][x], (x, y))
    return None


gear_nums = defaultdict(list)


p1_total = 0
for y, line in enumerate(lines):
    i = 0
    while i < len(line):
        if line[i].isdigit():
            left_edge = i - 1

            right_edge = i
            while right_edge < len(line) and line[right_edge].isdigit():
                right_edge += 1

            n = int(line[left_edge + 1 : right_edge])

            symbol_pos = get_symbol(left_edge, y) or get_symbol(right_edge, y)
            for pos in range(left_edge, right_edge + 1):
                symbol_pos = (
                    symbol_pos or get_symbol(pos, y - 1) or get_symbol(pos, y + 1)
                )

            if symbol_pos:
                p1_total += n

                symbol, pos = symbol_pos
                if symbol == "*":
                    gear_nums[pos].append(n)

            i = right_edge
        else:
            i += 1

print(p1_total)

p2_total = 0
for ds in gear_nums.values():
    if len(ds) == 2:
        p2_total += ds[0] * ds[1]

print(p2_total)
