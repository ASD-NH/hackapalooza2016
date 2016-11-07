text = input()
data = text.split(" ")

o = data[1]
if o != "+" and o != "-" and o != "*" and o != "/":
    solution = int(data[len(data)-1])
    i = len(data) - 1
    while i >= 0:
        if data[i] == "+":
            solution += int(data[i+1])
        elif data[i] == "-":
            solution = int(data[i+1]) - solution
        elif data[i] == "*":
            solution *= int(data[i+1])
        elif data[i] == "/":
            solution = int(data[i+1]) / solution

        i -= 1

    print(int(solution))

else:
    index = -1
    for i in range(0, len(data)):
        if data[i] != "+" and data[i] != "-" and data[i] != "*" and data[i] != "/":
            index = i
            break

    solution = int(data[index])
    i = index - 1
    while i >= 0:
        if data[i] == "+":
            solution += int(data[index + 1])
        elif data[i] == "-":
            solution = solution - int(data[index+1])
        elif data[i] == "*":
            solution *= int(data[index+1])
        elif data[i] == "/":
            solution = solution / int(data[index+1])

        index += 1
        i -= 1

    print(int(solution))