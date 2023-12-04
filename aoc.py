from collections import deque
import sys


def read_input():
    day = sys.argv[0].split(".")[0]
    is_test = "test" in sys.argv[1:]
    name = "test" if is_test else "in"
    with open(f"data/{day}/{name}.txt") as f:
        return f.read().splitlines()


DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def in_bounds(a, b):
    return lambda c: 0 <= c[0] < a and 0 <= c[1] < b


# a = deque()
# b = set()


# def bfs(queue, seen):
#     elt = a.popleft()
#     for n in neighbors:
#         if n not in seen:
#             seen.add(n)
#             queue.append(n)
