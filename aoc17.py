f = open('aoc17.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()

            
def check_neighbors(pocket, x, y, z,w):
    active_neighbors = 0
    for check_w in range(w - 1, w + 2):
        for check_x in range(x-1, x + 2):
            for check_y in range(y - 1, y + 2):
                for check_z in range(z - 1, z + 2):
                    if (check_x, check_y, check_z,check_w) not in pocket:
                        continue
                    if (check_x, check_y, check_z,check_w) == (x,y,z,w):
                        continue
                    else:
                        test1 = pocket[(check_x, check_y, check_z,check_w)]
                        active_neighbors += pocket[(check_x, check_y, check_z,check_w)]
    return active_neighbors

def expand_pocket(pocket, min_mag, max_mag, z_mag, w_mag, expand_w):
    if expand_w == True:
        for x in range(min_mag, max_mag):
            for y in range(min_mag, max_mag):
                for z in range(-1 * z_mag, z_mag + 1):
                    for w in range(-1 * w_mag, w_mag + 1):
                        if (x,y,z,w) not in pocket: 
                            pocket[(x,y,z,w)] = 0
    else:
        for x in range(min_mag, max_mag):
            for y in range(min_mag, max_mag):
                for z in range(-1 * z_mag, z_mag + 1):
                    if (x,y,z,0) not in pocket: 
                        pocket[(x,y,z,0)] = 0        
    return pocket

def print_grid(pocket, min_mag, max_mag, z_mag, w_mag):
    for z in range(-1 * w_mag, w_mag + 1):
        for z in range(-1 * z_mag, z_mag + 1):
            print('z = ' + str(z))
            
            for y in range(min_mag, max_mag):
                current_line = ''
                for x in range(min_mag, max_mag):
                    current_line += str(pocket[(x,y,z,w)])
                print(current_line)
            print()
        
rounds = 6

pocket = {}
min_mag = 0
max_mag = len(problem_input)
z_mag = 0
w_mag = 0


num_active = 0
for y in range(len(problem_input)):
    for x in range(len(problem_input[y])):
        if problem_input[y][x] == '.':
            pocket[(x,y,0,0)] = 0
        else:
            pocket[(x,y,0,0)] = 1
            num_active += 1
            

for cycle in range(rounds):
    num_active = 0
    min_mag -= 1
    max_mag += 1
    z_mag += 1
    pocket = expand_pocket(pocket, min_mag, max_mag, z_mag, w_mag, False)
    new_pocket = {}
    for item in pocket:
        is_active = pocket[item]
        neighbors = check_neighbors(pocket, item[0], item[1], item[2], item[3])
        if is_active == 1:
            if neighbors in [2,3]:
                num_active += 1
                new_pocket[item] = 1
            else:
                new_pocket[item] = 0
        else:
            if (neighbors == 3):
                num_active += 1
                new_pocket[item] = 1
            else:
                new_pocket[item] = 0
    pocket = new_pocket.copy()
    #print_grid(pocket, min_mag, max_mag, z_mag)
    
    print('After ' + str(cycle + 1) + ' cycle: ' + str(num_active))
    
print('Part 1:')
print('There are ' + str(num_active) + ' active.')

# part 2
pocket = {}
num_active = 0
for y in range(len(problem_input)):
    for x in range(len(problem_input[y])):
        if problem_input[y][x] == '.':
            pocket[(x,y,0,0)] = 0
        else:
            pocket[(x,y,0,0)] = 1
            num_active += 1
for cycle in range(rounds):
    num_active = 0
    min_mag -= 1
    max_mag += 1
    z_mag += 1
    w_mag += 1
    
    pocket = expand_pocket(pocket, min_mag, max_mag, z_mag, w_mag, True)
    new_pocket = {}
    for item in pocket:
        is_active = pocket[item]
        neighbors = check_neighbors(pocket, item[0], item[1], item[2], item[3])
        if is_active == 1:
            if neighbors in [2,3]:
                num_active += 1
                new_pocket[item] = 1
            else:
                new_pocket[item] = 0
        else:
            if (neighbors == 3):
                num_active += 1
                new_pocket[item] = 1
            else:
                new_pocket[item] = 0
    pocket = new_pocket.copy()
    print('After ' + str(cycle + 1) + ' cycle: ' + str(num_active))
print('Part 2:')
print('There are ' + str(num_active) + ' active.')