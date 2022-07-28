cnt = 4
m = 5


if cnt == 0:
    px, py = -1, -1
else:
    py = (cnt - 1) // m
    px = cnt - (py * m) - 1

print(px, py)