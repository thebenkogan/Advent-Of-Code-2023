from aoc import read_input

lines = read_input()

cache = {}


def count_ways(s, nums):
    if (s, tuple(nums)) in cache:
        return cache[(s, tuple(nums))]

    if len(nums) == 0:
        return 1 if "#" not in s else 0

    size = nums[0]
    total = 0

    for i in range(len(s)):
        if (
            i + size <= len(s)
            and all(c != "." for c in s[i : i + size])
            and (i == 0 or s[i - 1] != "#")
            and (i + size == len(s) or s[i + size] != "#")
        ):
            total += count_ways(s[i + size + 1 :], nums[1:])

        if s[i] == "#":
            break

    cache[(s, tuple(nums))] = total

    return total


def get_total(times):
    total = 0

    for line in lines:
        row, nums = line.split()
        row = "?".join([row] * times)
        nums = [int(n) for n in nums.split(",")] * times
        total += count_ways(row, nums)

    return total


print(get_total(1))
print(get_total(5))
