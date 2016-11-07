import sys

lines = []
while True:
    line = sys.stdin.readline()
    if line == '' or line == '\n':
        break
    lines.append(line)

coords = lines[len(lines)-1].split(",")
lines.pop(len(lines)-1)

for i in range(0, len(lines)):
    lines[i] = lines[i].strip()
    lines[i] = list(lines[i])
    for j in range(0, len(lines[i])):
        lines[i][j] = int(lines[i][j])

x, y = int(coords[0]), int(coords[1])
bitmap = lines


def fill(x, y):
    bitmap[x][y] = 1
    if x != 0 and bitmap[x-1][y] != 1:
        fill(x - 1, y)
    if x != len(bitmap) - 1 and bitmap[x+1][y] != 1:
        fill(x + 1, y)
    if y != 0 and bitmap[x][y - 1] != 1:
        fill(x, y - 1)
    if y != len(bitmap) - 1 and bitmap[x][y + 1] != 1:
        fill(x, y + 1)

fill(x, y)
for r in bitmap:
    line = ""
    for n in r:
        line += str(n)
    print(line)


