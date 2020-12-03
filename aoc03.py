f = open('aoc03.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()
# Determine width of slice
width = len(problem_input[0])
trees_found = 0
current_x = 0
current_y = 0
slope = [[1,1],[3,1],[5,1],[7,1],[1,2]]

current_slope = slope[1]
dx = current_slope[0]
dy = current_slope[1]
for line in problem_input:
    if current_y % dy != 0:
        continue
    if line[current_x % width] == '#':
        trees_found += 1
    current_x += dx
    current_y += dy
print('Part 1:')
print('You encountered ' + str(trees_found) + ' trees.')

# Now for part 2
multiplied_trees = 1

for current_slope in slope:
    current_x = 0
    current_y = 0
    trees_found = 0
    dx = current_slope[0]
    dy = current_slope[1]
    for line in problem_input:
        if current_y % dy != 0:
            current_y += 1
            continue
        if line[current_x % width] == '#':
            trees_found += 1
        current_x += dx
        current_y += 1
    multiplied_trees *= trees_found
print('Part 2:')
print('You encountered ' + str(multiplied_trees) + ' multiplied together')
