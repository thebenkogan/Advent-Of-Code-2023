from collections import defaultdict
from aoc import read_input

lines = read_input()

p1_total = 0
counts = defaultdict(lambda: 1)

for game in lines:
    a, b = game.split(": ")
    id = int(a.split()[1])
    winning, mine = b.split(" | ")
    winning = [int(n) for n in winning.split()]
    mine = [int(n) for n in mine.split()]

    matching = 0
    score = 0
    for m in mine:
        if m in winning:
            matching += 1
            score = 1 if score == 0 else score * 2

    p1_total += score

    for i in range(id + 1, id + matching + 1):
        counts[i] += counts[id]


p2_total = 1  # to account for ending game
for v in counts.values():
    p2_total += v


print(p1_total)
print(p2_total)
