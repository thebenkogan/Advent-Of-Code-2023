from collections import defaultdict
from heapq import heappop, heappush
from aoc import DIRS, in_bounds, read_input

lines = [[c for c in line] for line in read_input()]
inb = in_bounds(len(lines[0]), len(lines))


adj = {}

for row, line in enumerate(lines):
    for col, _ in enumerate(line):
        neighbors = []
        for dx, dy in DIRS:
            x, y = col + dx, row + dy
            if inb((x, y)):
                neighbors.append(((x, y), int(lines[y][x])))
        adj[(col, row)] = neighbors


def get_min_loss(min_steps, max_steps):
    # heat loss, position, previous position, number of times moving in direction
    queue = [(0, (0, 0), (-1, -1), 0)]
    weights = defaultdict(lambda: float("inf"))
    weights[((0, 0), (-1, -1), 0)] = 0
    seen = set()
    min_loss = float("inf")
    while len(queue) > 0:
        loss, pos, prev, num = heappop(queue)
        if pos == (len(lines[0]) - 1, len(lines) - 1):
            min_loss = min(min_loss, loss)
        seen.add((pos, prev, num))
        dx, dy = pos[0] - prev[0], pos[1] - prev[1]
        for n, w in adj[pos]:
            if n == prev:
                continue
            same_dir = dx == n[0] - pos[0] and dy == n[1] - pos[1]
            if same_dir and num == max_steps or not same_dir and 0 < num < min_steps:
                continue
            next_num = num + 1 if same_dir else 1
            if (n, pos, next_num) in seen:
                continue
            next_loss = loss + w
            if next_loss < weights[(n, pos, next_num)]:
                weights[(n, pos, next_num)] = next_loss
                heappush(queue, (next_loss, n, pos, next_num))

    return min_loss


print(get_min_loss(1, 3))
print(get_min_loss(4, 10))
