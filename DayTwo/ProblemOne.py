with open('input.txt', 'r') as idfile:
    ids = idfile.read().strip().split(",")

total = 0
for id in ids:
    idranges = id.split("-")
    range_values = range(int(idranges[0]), int(idranges[1]) + 1)
    for value in range_values:
        string_value = str(value)
        half = len(string_value) // 2
        if string_value[:half] == string_value[half:]:
            total += value

print(total)

