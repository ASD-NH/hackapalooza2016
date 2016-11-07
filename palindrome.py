text = input()
reversed = list(text)
reversed.reverse()
reversed.pop(0)
reversed_str = ""
for c in reversed:
    reversed_str = reversed_str + c

print(text + reversed_str)