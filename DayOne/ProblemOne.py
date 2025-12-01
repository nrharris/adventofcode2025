with open('input.txt', 'r') as input:
    combinations = [line.strip() for line in input]

zero_count, position = 0, 50

for combination in combinations:
    direction = combination[:1]
    turns = int(combination[1:])

    new_position = position

    if turns > 99:
        turns = turns % 100    

    if direction == 'L':
        new_position = position - turns
    else:
        new_position = position + turns    
    
    if new_position < 0:
        position = 99 + new_position + 1
    elif new_position > 99:
        position = new_position - 99 - 1
    else:
        position = new_position

    if position == 0:
        zero_count += 1

print(zero_count)
