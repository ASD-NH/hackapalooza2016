import sys


def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, n-1):
        if n % i == 0:
            return False
    return True

values = []
while True:
    input_ = sys.stdin.readline()
    if input_ == '' or input_ == '\n':
        break
    values.append(int(input_))

for val in values:
    if is_prime(val + 1) or is_prime(val + 2) or is_prime(val + 3):
        print(1)
    else:
        print(0)