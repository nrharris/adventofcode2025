from functools import reduce

with open('input.txt', 'r') as input_file:
    lines = [line.strip().split(" ") for line in input_file]
    lines = [[item for item in line if item.strip()] for line in lines]

rows = len(lines)
cols = len(lines[0])

total = 0
for col in range(cols):
    col_equation = []
    for row in range(rows):
        if lines[row][col]:
            col_equation.append(lines[row][col])
    
    operation = col_equation.pop()
    if operation == '+':
        total += sum([int(x) for x in col_equation])
    else:
        total += reduce(lambda x, y: int(x) * int(y), col_equation)

print(total)
        
      