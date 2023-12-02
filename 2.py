import re
from aoc import read_input

lines = read_input()

p1_total = 0
p2_total = 0
for game in lines:
    id = int(game.split(":")[0].split(" ")[1])
    sets = game.split(":")[1].split(";")

    good = True
    max_red, max_blue, max_green = 0, 0, 0

    for s in sets:
        matches = re.findall("(\d+) (blue|red|green)", s)
        nred, ngreen, nblue = 0, 0, 0
        for n, color in matches:
            n = int(n)
            if color == "blue":
                nblue += n
            elif color == "green":
                ngreen += n
            elif color == "red":
                nred += n

        if nred > 12 or ngreen > 13 or nblue > 14:
            good = False

        max_red = max(nred, max_red)
        max_blue = max(nblue, max_blue)
        max_green = max(ngreen, max_green)

    if good:
        p1_total += id

    p2_total += max_red * max_blue * max_green


print(p1_total)
print(p2_total)
