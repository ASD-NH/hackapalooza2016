import sys

lines = []
while True:
    line = sys.stdin.readline()
    if line == '' or line == '\n':
        break
    lines.append(line)

words = lines[0]
words = words.strip()
words = words.split(" ")
lines.pop(0)

# solutions = list()
# for line in lines:
#     solution = line
#     line = line.replace(" ", "")
#     for word in words:
#         i = line.find(word)
#         if i != -1:
#             solution = ""
#             for j in range(0, len(line)):
#                 c = line[j]
#                 if j < i or j >= i + len(word):
#                     solution += c + " "
#                 else:
#                     solution += c.upper() + " "
#             solution = solution[0:len(solution) - 2]
#         solutions.append(solution)

for i in range(0, len(lines)):
    line = lines[i]
    line = line.replace(" ", "")
    for word in words:
        word_index = line.lower().find(word)
        if word_index != -1:
            for j in range(0, len(line)):
                c = line[j]
                if j >= word_index and j < word_index + len(word):
                    line = line.replace(word, word.upper())
                    j += len(word)

    line = line.strip()
    solution = ""
    for c in line:
        solution += c + " "
    solution = solution[0:len(solution) - 1]
    print(solution)