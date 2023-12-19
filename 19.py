import re
from aoc import read_input

lines = read_input(split_lines=False)
sections = lines.split("\n\n")

rs = sections[0].split("\n")
parts = sections[1].split("\n")

rules = {}
for rule in rs:
    name, rest = rule.split("{")
    rest = rest[:-1].split(",")
    end = rest[-1]
    exprs = []
    for r in rest[:-1]:
        expr, dest = r.split(":")
        exprs.append((expr[0], expr[1], int(expr[2:]), dest))
    exprs.append(end)
    rules[name] = exprs

total = 0
for part in parts:
    nums = [int(n) for n in re.findall("\w=(\d+)", part)]
    part = {
        "x": nums[0],
        "m": nums[1],
        "a": nums[2],
        "s": nums[3],
    }

    curr = "in"
    while curr != "A" and curr != "R":
        exprs = rules[curr]
        goto = exprs[-1]
        for v, op, n, dest in exprs[:-1]:
            if part[v] > n if op == ">" else part[v] < n:
                goto = dest
                break
        curr = goto

    if curr == "A":
        total += part["x"] + part["m"] + part["a"] + part["s"]

print(total)


def accepted_combos(ps, curr):
    if curr == "A":
        return (
            (ps["x"].stop - ps["x"].start)
            * (ps["m"].stop - ps["m"].start)
            * (ps["a"].stop - ps["a"].start)
            * (ps["s"].stop - ps["s"].start)
        )
    elif curr == "R":
        return 0

    ps = ps.copy()
    exprs = rules[curr]

    total = 0

    for v, op, n, dest in exprs[:-1]:
        if op == ">":
            dest_range = range(n + 1, ps[v].stop)
            after_range = range(ps[v].start, n + 1)
        else:
            dest_range = range(ps[v].start, n)
            after_range = range(n, ps[v].stop)

        ps[v] = dest_range
        total += accepted_combos(ps, dest)
        ps[v] = after_range

    total += accepted_combos(ps, exprs[-1])

    return total


start = {
    "x": range(1, 4001),
    "m": range(1, 4001),
    "a": range(1, 4001),
    "s": range(1, 4001),
}


print(accepted_combos(start, "in"))
