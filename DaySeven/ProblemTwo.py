with open('input.txt', 'r') as input_file:
    manifold = [list(line.strip()) for line in input_file]

start_index = manifold[0].index('S')
start = (0, start_index)
rows = len(manifold)
cols = len(manifold[0])
column_sum = [0] * cols
column_sum[start_index] = 1

for row in range(rows-1):
    for col in range(cols):
        curr_sum = column_sum[col]
        if curr_sum != 0:
            next = manifold[row + 1][col]
            if next == "^":
                if col - 1 >= 0:
                    column_sum[col - 1] = column_sum[col - 1] + curr_sum
                if col + 1 >= 0:
                    column_sum[col + 1] = column_sum[col + 1] + curr_sum
                
                column_sum[col] = 0

print(sum(column_sum))