from collections import deque
from aoc import DIRS, read_input

lines = [[c for c in line] for line in read_input()]
R = len(lines)
C = len(lines[0])

start = None

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "." or c == "S":
            if c == "S":
                start = (j, i)


def search(max_steps):
    queue = deque([(0, start)])
    seen = set()
    ps = set()

    while len(queue) > 0:
        steps, pos = queue.popleft()
        if (steps, pos) in seen:
            continue
        else:
            seen.add((steps, pos))
        if steps == max_steps:
            ps.add(pos)
            continue
        for dx, dy in DIRS:
            n = ((pos[0] + dx), (pos[1] + dy))
            if lines[n[1] % C][n[0] % R] != "#":
                queue.append((steps + 1, n))

    return len(ps)


print(search(64))


def f(x):
    return 14688 * x**2 + 14750 * x + 3699


print(f((26501365 - 65) / R))
