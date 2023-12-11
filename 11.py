import itertools
from aoc import read_input

lines = read_input()

R = len(lines)
C = len(lines[0])

galaxies = set()
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "#":
            galaxies.add((j, i))

expanded_rows = set()
expanded_cols = set()
for row, line in enumerate(lines):
    galaxy_in_row = False
    for c in line:
        if c == "#":
            galaxy_in_row = True
            break
    if not galaxy_in_row:
        expanded_rows.add(row)

for col in range(C):
    galaxy_in_col = False
    for row in lines:
        if row[col] == "#":
            galaxy_in_col = True
            break
    if not galaxy_in_col:
        expanded_cols.add(col)


def get_total(expansion):
    total = 0

    for (sx, sy), (ex, ey) in itertools.combinations(galaxies, 2):
        man_dist = abs(sx - ex) + abs(sy - ey)
        in_rows = [
            row for row in expanded_rows if row in range(min(sy, ey) + 1, max(sy, ey))
        ]
        in_cols = [
            col for col in expanded_cols if col in range(min(sx, ex) + 1, max(sx, ex))
        ]
        total += man_dist + ((len(in_rows) + len(in_cols)) * (expansion - 1))

    return total


print(get_total(2))
print(get_total(1_000_000))
