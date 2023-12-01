import sys


def read_input():
    day = sys.argv[0].split(".")[0]
    is_test = "test" in sys.argv[1:]
    name = "test" if is_test else "in"
    with open(f"data/{day}/{name}.txt") as f:
        return f.read().splitlines()
