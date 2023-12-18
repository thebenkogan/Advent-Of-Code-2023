from aoc import read_input

lines = read_input()


def get_area(p1):
    boundary = 0
    vertices = [(0, 0)]
    cx, cy = 0, 0
    for line in lines:
        s = line.split()
        if p1:
            num = int(s[1])
            d = s[0]
        else:
            num = int(s[2][2:7], 16)
            d = int(s[2][7])

        if d == "R" or d == 0:
            cx += num
        elif d == "L" or d == 2:
            cx -= num
        elif d == "U" or d == 3:
            cy += num
        elif d == "D" or d == 1:
            cy -= num

        boundary += num
        vertices.append((cx, cy))

    A = 0
    for i in range(len(vertices) - 1):
        x1, y1 = vertices[i]
        x2, y2 = vertices[i + 1]
        A += x1 * y2 - x2 * y1
    A = abs(A) / 2

    interior = A - (boundary / 2) + 1
    return interior + boundary


print(get_area(True))
print(get_area(False))
