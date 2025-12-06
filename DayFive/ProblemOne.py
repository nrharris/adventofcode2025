with open('ranges.txt', 'r') as range_file:
    range_pairs = [line.strip().split('-') for line in range_file]

with open('ids.txt', 'r') as id_file:
    ids = id_file.read().split("\n")

fresh_count = 0
for id in ids:
    for range_pair in range_pairs:
        if int(range_pair[0]) <= int(id) <= int(range_pair[1]):
            fresh_count += 1
            break

print(fresh_count)