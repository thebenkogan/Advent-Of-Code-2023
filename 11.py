from collections import defaultdict, deque
import heapq
from aoc import in_bounds, read_input

lines = read_input()

R = len(lines)
C = len(lines[0])
inb = in_bounds(C, R)


def get_total(expansion):
    adj = {}  # position to list of (neighbor, weight)
    galaxies = set()

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "#":
                galaxies.add((j, i))

            galaxy_in_row = False
            for o in line:
                if o == "#":
                    galaxy_in_row = True
                    break

            galaxy_in_col = False
            for o in lines:
                if o[j] == "#":
                    galaxy_in_col = True
                    break

            adjs = []
            for dx, dy in [(0, 1), (0, -1)]:
                n = (j + dx, i + dy)
                if inb(n):
                    adjs.append((n, 1 if galaxy_in_row else expansion))

            for dx, dy in [(1, 0), (-1, 0)]:
                n = (j + dx, i + dy)
                if inb(n):
                    adjs.append((n, 1 if galaxy_in_col else expansion))

            adj[(j, i)] = adjs

    total = 0
    seen_ends = set()
    for galaxy in galaxies:
        seen_ends.add(galaxy)
        queue = [(0, galaxy)]
        weights = defaultdict(lambda: float("inf"))
        weights[galaxy] = 0
        seen = set()
        while len(queue) > 0:
            steps, elt = heapq.heappop(queue)
            if elt in seen:
                continue
            else:
                seen.add(elt)
            if elt in galaxies and elt not in seen_ends:
                total += steps
            for n, w in adj[elt]:
                if n not in seen:
                    new_cost = steps + w
                    if new_cost < weights[n]:
                        weights[n] = new_cost
                        heapq.heappush(queue, (new_cost, n))

    return total


print(get_total(2))
print(get_total(1000000))
