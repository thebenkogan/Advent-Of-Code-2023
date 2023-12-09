from aoc import read_input

lines = read_input()


def is_all_zero(nums):
    for n in nums:
        if n != 0:
            return False
    return True


p1_total = 0
p2_total = 0
for hist in lines:
    nums = [int(n) for n in hist.split()]
    sets = [nums]

    while not is_all_zero(sets[-1]):
        ns = []
        for i in range(0, len(sets[-1]) - 1):
            ns.append(sets[-1][i + 1] - sets[-1][i])
        sets.append(ns)

    next_last = 0
    next_start = 0
    for i in range(len(sets) - 2, -1, -1):
        next_last = sets[i][-1] + next_last
        next_start = sets[i][0] - next_start

    p1_total += next_last
    p2_total += next_start


print(p1_total)
print(p2_total)
