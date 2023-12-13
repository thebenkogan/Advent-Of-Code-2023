from aoc import read_input

lines = read_input(split_lines=False)

patterns = lines.split("\n\n")


def find_line(pattern, skip_line=None):
    for row in range(len(pattern) - 1):
        line = (row, None)
        if line == skip_line:
            continue

        a = pattern[: row + 1][::-1]
        b = pattern[row + 1 :]

        good = True
        for i in range(min(len(a), len(b))):
            if a[i] != b[i]:
                good = False
                break

        if good:
            return line, 100 * len(a)

    for col in range(len(pattern[0]) - 1):
        line = (None, col)
        if line == skip_line:
            continue

        a = [pattern[i][: col + 1][::-1] for i in range(len(pattern))]
        b = [pattern[i][col + 1 :] for i in range(len(pattern))]

        good = True
        for i in range(min(len(a[0]), len(b[0]))):
            if [c[i] for c in a] != [c[i] for c in b]:
                good = False
                break

        if good:
            return line, len(a[0])


def find_line_with_smudge(pattern):
    line, _ = find_line(pattern)

    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            pattern[i][j] = "#" if pattern[i][j] == "." else "."
            new_line = find_line(pattern, line)
            if new_line != None and new_line[0] != line:
                return new_line[1]
            pattern[i][j] = "#" if pattern[i][j] == "." else "."

    raise Exception("No smudge found")


p1_total = 0
p2_total = 0
for pattern in patterns:
    pattern = [[c for c in line] for line in pattern.split("\n")]
    _, amnt = find_line(pattern)
    p1_total += amnt
    p2_total += find_line_with_smudge(pattern)

print(p1_total)
print(p2_total)
