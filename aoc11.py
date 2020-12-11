f = open('aoc11.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()
rows = len(problem_input)
columns = len(problem_input[0])
changed_seat = True

def listifyString(string):
    myList = []
    myList[:0] = string
    return myList
part1_layout = []
for line in problem_input:
    part1_layout += [listifyString(line)]

def upper_left(layout, x, y, rows, columns, adjacent):
    if (x == 0) or (y == 0):
        return False
    else:
        if layout[y-1][x-1] == '#':
            return True
        elif layout[y-1][x-1] == '.' and adjacent == False:
            return upper_left(layout, x-1, y-1, rows, columns, adjacent)
    return False
def upper(layout, x, y, rows, columns, adjacent):
    if (y != 0):
        if layout[y-1][x] == '#':
            return True
        elif layout[y-1][x] == '.' and adjacent == False:
            return upper(layout, x, y-1, rows, columns, adjacent)
        return False
    else:
        return False
def upper_right(layout, x, y, rows, columns, adjacent):
    if (x == columns-1) or (y == 0):
        return False
    else:
        if layout[y-1][x+1] == '#':
            return True
        elif layout[y-1][x+1] == '.' and adjacent == False:
            return upper_right(layout, x+1, y-1, rows, columns, adjacent)
    return False
def right(layout, x, y, rows, columns, adjacent):
    if (x != columns - 1):
        if layout[y][x+1] == '#':
            return True
        elif layout[y][x+1] == '.' and adjacent == False:
            return right(layout, x+1, y, rows, columns, adjacent)
        return False
    else:
        return False
    
def lower_right(layout, x, y, rows, columns, adjacent):
    if (y == rows - 1) or (x == columns - 1):
        return False
    else:
        if layout[y+1][x+1] == '#':
            return True
        elif layout[y+1][x+1] == '.' and adjacent == False:
            return lower_right(layout, x+1, y+1, rows, columns, adjacent)
        
    return False

def lower(layout, x, y, rows, columns, adjacent):
    if (y != rows - 1):
        if layout[y+1][x] == '#':
            return True
        elif layout[y+1][x] == '.' and adjacent == False:
            return lower(layout, x, y+1, rows, columns, adjacent)
        return False
    else:
        return False
def lower_left(layout, x, y, rows, columns, adjacent):
    if (y == rows - 1) or (x == 0):
        return False
    else:
        if layout[y+1][x-1] == '#':
            return True
        elif layout[y+1][x-1] == '.' and adjacent == False:
            return lower_left(layout, x-1, y+1, rows, columns, adjacent)
    return False
def left(layout, x, y, rows, columns, adjacent):
    if (x != 0):
        if layout[y][x-1] == '#':
            return True
        elif layout[y][x-1] == '.' and adjacent == False:
            return left(layout, x-1, y, rows, columns, adjacent)
        return False
    else:
        return False
def occupied_seats(layout, x, y, rows, columns, adjacent):
    occupied_neighbors = 0
    #Upper Left
    #if (x == 0) or (y == 0):
    #    test1 = 1
    #else:
    #    if layout[y-1][x-1] == '#':
    #        occupied_neighbors += 1
    if upper_left(layout, x, y, rows, columns, adjacent) == True:
        occupied_neighbors += 1

    # Upper
    if upper(layout, x, y, rows, columns, adjacent) == True:
        occupied_neighbors += 1
    # Upper Right
    if upper_right(layout, x, y, rows, columns, adjacent) == True:
        occupied_neighbors += 1
    # Right
    if right(layout, x, y, rows, columns, adjacent) == True:
        occupied_neighbors += 1
    # Lower Right
    if lower_right(layout, x, y, rows, columns, adjacent) == True:
        occupied_neighbors += 1
    # Lower
    if lower(layout, x, y, rows, columns, adjacent) == True:
        occupied_neighbors += 1    
    # Lower Left
    if lower_left(layout, x, y, rows, columns, adjacent) == True:
        occupied_neighbors += 1    
    # Left
    if left(layout, x, y, rows, columns, adjacent) == True:
        occupied_neighbors += 1    
    return occupied_neighbors


while changed_seat == True:
    changed_seat = False
    number_of_changes = 0
    new_layout = []
    for y in range(rows):
        new_layout += [part1_layout[y][:]]
    
    for y in range(rows):
        for x in range(columns):
            current_seat = new_layout[y][x]
            if current_seat == "L":
                if occupied_seats(part1_layout, x, y, rows, columns, True) == 0:
                    new_layout[y][x] = '#'
                    number_of_changes += 1
            elif current_seat == "#":
                if occupied_seats(part1_layout, x, y, rows, columns, True) >= 4:
                    new_layout[y][x] = 'L'
                    number_of_changes += 1

    print(str(number_of_changes) + ' changes')
    if number_of_changes > 0:
        changed_seat = True
    part1_layout = new_layout[:]
filled_seats = 0
for row in part1_layout:
    filled_seats += row.count('#')
print('Part 1:')
print('There are ' + str(filled_seats) + ' filled seats.')


part2_layout = []
for line in problem_input:
    part2_layout += [listifyString(line)]
changed_seat = True
while changed_seat == True:
    changed_seat = False
    number_of_changes = 0
    new_layout = []
    for y in range(rows):
        new_layout += [part2_layout[y][:]]
    
    for y in range(rows):
        for x in range(columns):
            current_seat = new_layout[y][x]
            if current_seat == "L":
                if occupied_seats(part2_layout, x, y, rows, columns, False) == 0:
                    new_layout[y][x] = '#'
                    number_of_changes += 1
            elif current_seat == "#":
                if occupied_seats(part2_layout, x, y, rows, columns, False) >= 5:
                    new_layout[y][x] = 'L'
                    number_of_changes += 1

    print(str(number_of_changes) + ' changes')
    if number_of_changes > 0:
        changed_seat = True
    part2_layout = new_layout[:]
filled_seats = 0

for row in part2_layout:
    filled_seats += row.count('#')
print('Part 2:')
print('There are ' + str(filled_seats) + ' filled seats.')