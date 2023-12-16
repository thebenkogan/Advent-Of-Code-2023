from collections import deque
from aoc import in_bounds, read_input

lines = [[c for c in line] for line in read_input()]

adj = {}
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        neighbors = {}
        if c == ".":
            neighbors["right"] = [((j + 1, i), "right")]
            neighbors["left"] = [((j - 1, i), "left")]
            neighbors["down"] = [((j, i + 1), "down")]
            neighbors["up"] = [((j, i - 1), "up")]
        elif c == "|":
            neighbors["down"] = [((j, i + 1), "down")]
            neighbors["up"] = [((j, i - 1), "up")]
            neighbors["right"] = [((j, i - 1), "up"), ((j, i + 1), "down")]
            neighbors["left"] = [((j, i - 1), "up"), ((j, i + 1), "down")]
        elif c == "-":
            neighbors["right"] = [((j + 1, i), "right")]
            neighbors["left"] = [((j - 1, i), "left")]
            neighbors["down"] = [((j + 1, i), "right"), ((j - 1, i), "left")]
            neighbors["up"] = [((j + 1, i), "right"), ((j - 1, i), "left")]
        elif c == "/":
            neighbors["right"] = [((j, i - 1), "up")]
            neighbors["left"] = [((j, i + 1), "down")]
            neighbors["down"] = [((j - 1, i), "left")]
            neighbors["up"] = [((j + 1, i), "right")]
        elif c == "\\":
            neighbors["right"] = [((j, i + 1), "down")]
            neighbors["left"] = [((j, i - 1), "up")]
            neighbors["down"] = [((j + 1, i), "right")]
            neighbors["up"] = [((j - 1, i), "left")]
        adj[(j, i)] = neighbors

inb = in_bounds(len(lines[0]), len(lines))


def num_energized(start):
    queue = deque([start])
    seen = set([start])

    while len(queue) > 0:
        pos, dir = queue.popleft()
        for n, next_dir in adj[pos][dir]:
            if (n, next_dir) not in seen and inb(n):
                seen.add((n, next_dir))
                queue.append((n, next_dir))

    return len(set([p for p, _ in seen]))


print(num_energized(((0, 0), "right")))

max_energized = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if i == 0:
            max_energized = max(max_energized, num_energized(((j, i), "down")))
        if i == len(lines) - 1:
            max_energized = max(max_energized, num_energized(((j, i), "up")))
        if j == 0:
            max_energized = max(max_energized, num_energized(((j, i), "right")))
        if j == len(lines[0]) - 1:
            max_energized = max(max_energized, num_energized(((j, i), "left")))

print(max_energized)
