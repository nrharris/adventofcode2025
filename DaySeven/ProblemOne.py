with open('input.txt', 'r') as input_file:
    manifold = [line.strip() for line in input_file]

visited_locations = set()

def traverse_down(location, split_locations):
    if location != start and (location[1] == len(manifold) or location[0] == len(manifold[0]) or location[0] == 0 or location[1] == 0):
        return
    
    if location in visited_locations:
        return
    
    visited_locations.add(location)

    next_location = manifold[location[0] + 1][location[1]]
    if next_location == "^":
        split_left = (location[0] + 1, location[1] - 1)
        split_right = (location[0] + 1, location[1] + 1)
        split_locations.add((location[0] + 1, location[1]))
        traverse_down(split_left, split_locations)
        traverse_down(split_right, split_locations)
    else:
        traverse_down((location[0] + 1, location[1]), split_locations)


start = (0, manifold[0].index('S'))
split_locations = set()
traverse_down(start, split_locations)
print(len(split_locations))