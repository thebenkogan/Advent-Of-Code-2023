from collections import deque
from aoc import DIRS, in_bounds, read_input

lines = read_input()

# double the resolution
new_graph = []
for line in lines:
    new_row1 = []
    new_row2 = []
    for c in line:
        if c == "S":
            # manually specified for my input so start still has original directions
            new_row1 += ["S", "."]
            new_row2 += ["|", "."]
        if c == "|":
            new_row1 += ["|", "."]
            new_row2 += ["|", "."]
        if c == "-":
            new_row1 += ["-", "-"]
            new_row2 += [".", "."]
        if c == "L":
            new_row1 += ["L", "-"]
            new_row2 += [".", "."]
        if c == "F":
            new_row1 += ["F", "-"]
            new_row2 += ["|", "."]
        if c == "7":
            new_row1 += ["7", "."]
            new_row2 += ["|", "."]
        if c == "J":
            new_row1 += ["J", "."]
            new_row2 += [".", "."]
        if c == ".":
            new_row1 += [".", "."]
            new_row2 += [".", "."]
    new_graph.append(new_row1)
    new_graph.append(new_row2)

lines = new_graph


def is_original(pos):
    return pos[0] % 2 == 0 and pos[1] % 2 == 0


adj = {}
start = None
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "S":
            start = (x, y)
            adjs = []
            if lines[y][x + 1] in ["-", "7", "J"]:
                adjs.append((x + 1, y))
            if lines[y][x - 1] in ["-", "F", "L"]:
                adjs.append((x - 1, y))
            if lines[y + 1][x] in ["|", "L", "J"]:
                adjs.append((x, y + 1))
            if lines[y - 1][x] in ["|", "7", "F"]:
                adjs.append((x, y - 1))
            adj[(x, y)] = adjs
        if c == "|":
            adj[(x, y)] = [(x, y - 1), (x, y + 1)]
        if c == "-":
            adj[(x, y)] = [(x - 1, y), (x + 1, y)]
        if c == "L":
            adj[(x, y)] = [(x + 1, y), (x, y - 1)]
        if c == "F":
            adj[(x, y)] = [(x + 1, y), (x, y + 1)]
        if c == "7":
            adj[(x, y)] = [(x - 1, y), (x, y + 1)]
        if c == "J":
            adj[(x, y)] = [(x - 1, y), (x, y - 1)]

queue = deque()
queue.append((start, 0))
cycle_nodes = set([start])
inb = in_bounds(len(lines[0]), len(lines))
max_steps = 0
while len(queue) > 0:
    pos, steps = queue.popleft()
    max_steps = max(max_steps, steps)
    next_steps = steps + 1 if is_original(pos) else steps
    for n in adj[pos]:
        if n not in cycle_nodes and inb(n):
            cycle_nodes.add(n)
            queue.append((n, next_steps))

print(max_steps)

adj2 = {}  # fully connected graph ignoring pipes, original cycle nodes are walls
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if (x, y) not in cycle_nodes:
            adjs = []
            for dx, dy in DIRS:
                if (x + dx, y + dy) not in cycle_nodes:
                    adjs.append((x + dx, y + dy))
            adj2[(x, y)] = adjs

outsiders = set()  # nodes outside the cycle
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if (x, y) not in cycle_nodes and (x, y) not in outsiders:
            queue = deque()
            queue.append((x, y))
            seen = set([(x, y)])
            outside_region = False
            while len(queue) > 0:
                pos = queue.popleft()
                for n in adj2[pos]:
                    if not inb(n):
                        outside_region = True
                    if n not in seen and inb(n):
                        seen.add(n)
                        queue.append(n)

            if outside_region:
                outsiders = outsiders.union(seen)
            else:
                total = 0
                for p in seen:
                    if is_original(p):
                        total += 1
                print(total)
                exit()
