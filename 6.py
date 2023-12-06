from math import ceil, floor, sqrt
import re
from aoc import read_input

lines = read_input()

times = [int(n) for n in re.findall("\d+", lines[0])]
dists = [int(n) for n in re.findall("\d+", lines[1])]


# (time - x) * x > dist
# x*time - x**2 > dist
# x**2 - x*time + dist < 0
# find the roots, function is negative between them
#
# since we only care about integer answers, it's the first int
# greater than the smaller root and last int smaller than the larger root
def get_num_ways(time, dist):
    a = 1
    b = -time
    c = dist
    pr = (-b + sqrt((b) ** 2 - (4 * a * c))) / (2 * a)
    nr = (-b - sqrt((b) ** 2 - (4 * a * c))) / (2 * a)

    # exclude the roots if they are integers
    offset = 1
    if pr == floor(pr):
        offset -= 1
    if nr == ceil(nr):
        offset -= 1
    return floor(pr) - ceil(nr) + offset


total = 1
for time, dist in zip(times, dists):
    total *= get_num_ways(time, dist)

print(total)

time = int("".join([str(n) for n in times]))
dist = int("".join([str(n) for n in dists]))

print(get_num_ways(time, dist))
