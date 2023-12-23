from collections import deque
from aoc import DIRS, in_bounds, read_input

lines = [[c for c in line] for line in read_input()]
R = len(lines)
C = len(lines[0])
inb = in_bounds(C, R)


def longest_path(part1):
    adj = {}
    critical_nodes = set()
    start = None
    end = None
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c != "#":
                neighbors = []

                if i == 0:
                    start = (j, i)

                if i == R - 1:
                    end = (j, i)

                dirs = (
                    DIRS
                    if c == "."
                    else [(0, 1)]
                    if c == "v"
                    else [(0, -1)]
                    if c == "^"
                    else [(1, 0)]
                    if c == ">"
                    else [(-1, 0)]
                )

                is_critical = True
                for dx, dy in dirs if part1 else DIRS:
                    n = (j + dx, i + dy)
                    if inb(n) and lines[n[1]][n[0]] != "#":
                        neighbors.append(n)
                        if lines[n[1]][n[0]] not in "^v<>":
                            is_critical = False
                adj[(j, i)] = neighbors
                if is_critical:
                    critical_nodes.add((j, i))
    critical_nodes.add(start)
    critical_nodes.add(end)

    def nearest_criticals(start):
        queue = deque([(start, 0)])
        seen = set([start])
        lens = []
        while len(queue) > 0:
            pos, steps = queue.popleft()
            if pos != start and pos in critical_nodes:
                lens.append((pos, steps))
                continue
            for n in adj[pos]:
                if n not in seen:
                    seen.add(n)
                    queue.append((n, steps + 1))

        return lens

    adj2 = {}
    for node in critical_nodes:
        lens = nearest_criticals(node)
        adj2[node] = lens

    stack = deque([(0, start, set([start]))])
    max_steps = 0
    while len(stack) > 0:
        steps, pos, seen = stack.pop()
        if pos[1] == R - 1:
            max_steps = max(max_steps, steps)
            continue
        for n, w in adj2[pos]:
            if n not in seen:
                next_seen = seen.copy()
                next_seen.add(n)
                stack.append((steps + w, n, next_seen))

    return max_steps


print(longest_path(True))
print(longest_path(False))
