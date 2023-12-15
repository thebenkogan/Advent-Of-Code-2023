import re
from aoc import read_input

lines = read_input(split_lines=False)


def hash(s):
    curr = 0
    for c in s:
        curr += ord(c)
        curr *= 17
        curr %= 256
    return curr


total = 0
for s in lines.split(","):
    total += hash(s)
print(total)

boxes = [{} for _ in range(256)]
for s in lines.split(","):
    label = re.findall("\w+", s)[0]
    box = hash(label)
    if "-" in s:
        if label in boxes[box]:
            del boxes[box][label]
    else:
        focal_length = int(s.split("=")[1])
        boxes[box][label] = focal_length

total = 0
for i, box in enumerate(boxes):
    power = 0
    for j, focal_length in enumerate(box.values()):
        power += (i + 1) * (j + 1) * focal_length
    total += power
print(total)
