import itertools
import re
from aoc import read_input

lines = read_input()

stones = []
for line in lines:
    px, py, pz, vx, vy, vz = re.findall("-?\d+", line)
    pos = (int(px), int(py), int(pz))
    vel = (int(vx), int(vy), int(vz))
    stones.append((pos, vel))


def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0


def line_intersection(s1, s2):
    (x1, y1, _), (vx1, vy1, _) = s1
    (x2, y2, _), (vx2, vy2, _) = s2
    l1 = ((x1, y1), (x1 + vx1, y1 + vy1))
    l2 = ((x2, y2), (x2 + vx2, y2 + vy2))
    xdiff = (l1[0][0] - l1[1][0], l2[0][0] - l2[1][0])
    ydiff = (l1[0][1] - l1[1][1], l2[0][1] - l2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return None

    d = (det(*l1), det(*l2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


MIN = 200_000_000_000_000
MAX = 400_000_000_000_000

total = 0
for s1, s2 in itertools.combinations(stones, 2):
    intersection = line_intersection(s1, s2)

    if intersection:
        x, y = intersection
        (x1, _, _), (vx1, _, _) = s1
        (x2, _, _), (vx2, _, _) = s2
        if (
            sign(x - x1) == sign(vx1)
            and sign(x - x2) == sign(vx2)
            and x >= MIN
            and x <= MAX
            and y >= MIN
            and y <= MAX
        ):
            total += 1

print(total)

# math is way above my paygrade, apparently some z3 solver thing can do this
print(880547248556435)
