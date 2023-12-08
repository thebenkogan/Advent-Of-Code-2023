from math import lcm
import re
from aoc import read_input

lines = read_input(split_lines=False)

sections = lines.split("\n\n")

lr = sections[0]
adj = {}
starts = []
for line in sections[1].split("\n"):
    ws = re.findall("\w+", line)
    if ws[0][2] == "A":
        starts.append(ws[0])
    adj[ws[0]] = (ws[1], ws[2])


curr = "AAA"
steps = 0
while curr != "ZZZ":
    for c in lr:
        steps += 1
        if c == "L":
            curr = adj[curr][0]
        else:
            curr = adj[curr][1]
        if curr == "ZZZ":
            break

print(steps)


start_steps = []
for s in starts:
    curr = s
    steps = 0
    while curr[2] != "Z":
        for c in lr:
            steps += 1
            if c == "L":
                curr = adj[curr][0]
            else:
                curr = adj[curr][1]
            if curr[2] == "Z":
                break
    start_steps.append(steps)

print(lcm(*start_steps))
