import re
from aoc import read_input

lines = read_input()

p1_digits = [re.findall("\d", l) for l in lines]

p1_sum = sum([int(d[0] + d[-1]) for d in p1_digits])

print(p1_sum)

p2_digits = [
    re.findall("(?=(\d|one|two|three|four|five|six|seven|eight|nine))", l)
    for l in lines
]


def translate(n):
    if len(n) > 1:
        if n == "one":
            return "1"
        elif n == "two":
            return "2"
        elif n == "three":
            return "3"
        elif n == "four":
            return "4"
        elif n == "five":
            return "5"
        elif n == "six":
            return "6"
        elif n == "seven":
            return "7"
        elif n == "eight":
            return "8"
        elif n == "nine":
            return "9"
    return n


p2_sum = sum([int(translate(d[0]) + translate(d[-1])) for d in p2_digits])

print(p2_sum)
