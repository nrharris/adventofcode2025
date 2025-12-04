from enum import Enum

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP_LEFT = (-1, -1)
    UP_RIGHT = (1, -1)
    DOWN_LEFT = (-1, 1)
    DOWN_RIGHT = (1, 1)

    def is_out_of_bounds(self, x, y, width, height):
        dx, dy = self.value
        new_x = x + dx
        new_y = y + dy
        return new_x < 0 or new_x >= width or new_y < 0 or new_y >= height


with open('input.txt', 'r') as paper_role_file:
    paper_role_map = [line.strip() for line in paper_role_file]

row_length = len(paper_role_map[0])
col_length = len(paper_role_map)

accessible_positions = 0
for row in range(row_length):
    for col in range(col_length):
        if paper_role_map[row][col] == '@':
            adjacent_paper_rolls = 0
            for direction in Direction:
                if not direction.is_out_of_bounds(row, col, row_length, col_length):
                    if paper_role_map[row + direction.value[0]][col + direction.value[1]] == '@':
                        adjacent_paper_rolls += 1
            if adjacent_paper_rolls < 4:
                accessible_positions += 1

print(accessible_positions)