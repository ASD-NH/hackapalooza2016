units = input()
num = input()
num = int(num)

if units == 'F':
    converted = (num - 32) * (5/9)
else:
    converted = num * (9/5) + 32


converted = int(converted)
print(converted)