import copy

with open('ranges.txt', 'r') as ranges_file:
    ranges = [[int(x) for x in line.strip().split("-")] for line in ranges_file]

ranges.sort(key=lambda range:range[0])
max_range = max(ranges, key=lambda range:range[1])[1]
max_possible = max_range - ranges[0][0]

deep_ranges = copy.deepcopy(ranges)
for first_range in deep_ranges:
    for second_range in deep_ranges:
        if first_range != second_range:
            if first_range[0] <= second_range[0] and first_range[1] >= second_range[1]:
                if second_range in ranges:
                    ranges.remove(second_range)

gap_total = 0

i = 0
while i < len(ranges):
    if i + 1 < len(ranges):
        current_end = ranges[i][1]
        next_beg = ranges[i+1][0]
        if current_end < next_beg:
            gap_total += next_beg - current_end - 1
    i += 1

print(max_possible - gap_total + 1)