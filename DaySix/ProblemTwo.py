from functools import reduce

with open('input.txt', 'r') as input_file:
    lines = [line.replace("\n", "") for line in input_file]

rows = len(lines)
cols = len(lines[0])

total = 0
current_section = []
curr_operation = ""
for col in reversed(range(cols)):
    curr_number = ""
    for row in range(rows):
        item = lines[row][col]
        if item == "*" or item == "+":
            curr_operation = item
        elif item:
            curr_number += item
    
    if col == 0 and curr_number.strip():
        current_section.append(int(curr_number))

    if curr_number.strip() and col != 0:
        current_section.append(int(curr_number))
    else:
        if curr_operation == '+':
            total += sum(current_section)
        else:
            total += reduce(lambda x, y: x * y, current_section)
        curr_operation = ""
        current_section = []
        
print(total)
      