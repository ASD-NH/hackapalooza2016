import sys

stones = []
while True:
    input_ = sys.stdin.readline()
    if input_ == '' or input_ == '\n':
        break
    stones.append(input_)

eldest = None
eldest_years = 0
for p in stones:
    p = p.split(",")
    age = int(p[2]) - int(p[1])
    if age > eldest_years:
        eldest_years = age
        eldest = p[0]

print(eldest)