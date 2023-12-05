import re
from aoc import read_input

lines = read_input(split_lines=False)

sections = lines.split("\n\n")

seeds, maps = sections[0], sections[1:]

seeds = [int(n) for n in re.findall("\d+", seeds)]


def parse_map(s):
    dict = {}
    for l in s.split("\n")[1:]:
        dr, sr, ln = [int(n) for n in l.split()]
        ss = range(sr, sr + ln)
        dd = range(dr, dr + ln)
        dict[ss] = dd
    return dict


maps = [parse_map(s) for s in maps]

results = []
for seed in seeds:
    curr = seed
    for m in maps:
        for k, v in m.items():
            if curr in k:
                offset = curr - k.start
                curr = v.start + offset
                break
    results.append(curr)

print(min(results))

start_ranges = []
for s in range(0, len(seeds), 2):
    start_ranges.append(range(seeds[s], seeds[s] + seeds[s + 1]))


def map_ranges(map, start_ranges):
    mapped = []
    next_ranges = start_ranges
    for k, v in map.items():
        unmapped = []
        for sr in next_ranges:
            inter = None
            if sr.start in k or sr.stop - 1 in k:
                inter = range(max(sr.start, k.start), min(sr.stop, k.stop))

            if inter:
                if sr.start < k.start:
                    unmapped.append(range(sr.start, k.start))

                if sr.stop > k.stop:
                    unmapped.append(range(k.stop, sr.stop))

                mapped_start = (inter.start - k.start) + v.start
                mapped_stop = (inter.stop - k.start) + v.start
                mapped.append(range(mapped_start, mapped_stop))
            else:
                unmapped.append(sr)

        next_ranges = unmapped

    return mapped + next_ranges


for map in maps:
    start_ranges = map_ranges(map, start_ranges)

print(min([r.start for r in start_ranges]))
