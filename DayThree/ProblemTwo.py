with open('input.txt', 'r') as batteryfile:
    batterylines = [line.strip() for line in batteryfile]

total = 0
for batteryline in batterylines:
    monotonic_stack = []
    for i in range(len(batteryline)):
        if not monotonic_stack:
            monotonic_stack.append(int(batteryline[i]))
        else:
            battery = int(batteryline[i])
            if battery > monotonic_stack[-1]:
                while monotonic_stack and battery > monotonic_stack[-1]:
                    if len(monotonic_stack) + len(batteryline) - i > 12:
                        monotonic_stack.pop()
                    else:
                        break
                monotonic_stack.append(battery)
            elif len(monotonic_stack) < 12:
                monotonic_stack.append(battery)
    
    total += int(''.join([str(val) for val in monotonic_stack]))

print(total)