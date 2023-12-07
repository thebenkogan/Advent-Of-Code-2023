from collections import Counter
from aoc import read_input

lines = read_input()

scores = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}

part = 1


def get_type(h):
    c = Counter(h)

    if part == 2 and "J" in h:
        j_count = c["J"]
        del c["J"]
        if len(c) == 0:
            c["A"] = 5
        else:
            mc, _ = c.most_common()[0]
            c[mc] += j_count

    match sorted(c.values()):
        case [5]:
            return 7
        case [1, 4]:
            return 6
        case [2, 3]:
            return 5
        case [1, 1, 3]:
            return 4
        case [1, 2, 2]:
            return 3
        case [1, 1, 1, 2]:
            return 2
        case _:
            return 1


def key(hb):
    h = hb[0]
    t = get_type(h)
    return [t] + [scores[c] for c in h]


hand_bids = []

for hand in lines:
    hand, b = hand.split()
    hand_bids.append((hand, int(b)))


def get_winnings(hand_bids):
    in_order = sorted(hand_bids, key=key)
    total = 0
    rank = 1
    for _, bid in in_order:
        total += bid * rank
        rank += 1
    return total


print(get_winnings(hand_bids))

scores["J"] = 0
part = 2

print(get_winnings(hand_bids))
