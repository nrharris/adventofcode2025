import re

with open('input.txt', 'r') as idfile:
    ids = idfile.read().strip().split(",")

total = 0
for id in ids:
    idranges = id.split("-")
    range_values = range(int(idranges[0]), int(idranges[1]) + 1)
    for value in range_values:
        string_value = str(value)
        half = len(string_value) // 2
        for i in range(half + 1):
            search_value = string_value[:i]
            if re.fullmatch(rf"({search_value})+", string_value):
                total += value
                break
print(total)

