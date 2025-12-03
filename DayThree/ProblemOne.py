with open('input.txt', 'r') as batteryfile:
    batterylines = [line.strip() for line in batteryfile]

total = 0
for batteryline in batterylines:
    local_maximums = []
    local_max = -1
    for battery in batteryline:
        if local_max != -1:
            local_maximums.append(int(str(local_max) + battery))

        if int(battery) > local_max:
            local_max = int(battery)

    total += max(local_maximums)

print(total)