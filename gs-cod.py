import sys

stones = []
while True:
    input_ = sys.stdin.readline()
    if input_ == '' or input_ == '\n':
        break
    stones.append(input_)

c = 0
for p in stones:
    p = p.split(",")

    dob = p[1].split("-")
    dod = p[2].split("-")
    age = int(dod[0]) - int(dob[0])
    if int(dod[2]) == 13 and age >= 13 and age <= 19:
        c += 1

print(c)