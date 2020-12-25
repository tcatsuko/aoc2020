f = open('aoc24.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()

directions = ''


# Directions
#e = (0, 1)
#se = (1, 0)
#sw = (1,-1)
#w = (0, -1)
#nw = (-1,0)
#ne = (-1,1)
w = (-1,0)
e = (1,0)
nw = (-1,1)
ne = (0,1)
sw = (0,-1)
se = (1,-1)

grid_tiles = {}
current_coords = (0,0)
x = 0
flipped_once = 0
flipped_twice = 0
black_tiles = set()

for line in problem_input:
    current_coords = (0,0)
    directions = line
    directions_length = len(directions)
    x = 0
    while x < directions_length:
        next_direction = directions[x]
        if next_direction == 's' or next_direction == 'n':
            x += 1
            next_direction += directions[x]
        if next_direction == 'e':
            move = e
        elif next_direction == 'ne':
            move = ne
        elif next_direction == 'se':
            move = se
        elif next_direction == 'w':
            move = w
        elif next_direction == 'sw':
            move = sw
        elif next_direction == 'nw':
            move = nw
        next_coord = (current_coords[0]+move[0], current_coords[1]+move[1])
       
        x += 1
        current_coords = next_coord
    if current_coords not in grid_tiles:
        grid_tiles[current_coords] = True
        flipped_once += 1
        black_tiles.add(current_coords)
    else:
        black_tiles.remove(current_coords)
        flipped_twice += 1
        flipped_once -= 1

num_black = 0
num_black = len(black_tiles)
print('Part 1:')
print('There are ' + str(num_black) + ' black tiles.')


num_black = 0

for x in range(100):
    black_copy = set()
    white_tiles = set()
    for tile in black_tiles:
        # find neighboring tiles
        e_tile = (tile[0] + e[0], tile[1] + e[1])
        ne_tile = (tile[0] + ne[0], tile[1] + ne[1])
        nw_tile = (tile[0] + nw[0], tile[1] + nw[1])
        w_tile = (tile[0] + w[0], tile[1] + w[1])
        sw_tile = (tile[0] + sw[0], tile[1] + sw[1])
        se_tile = (tile[0] + se[0], tile[1] + se[1])
        adjacent_blacks = 0
        neighbors = [e_tile, ne_tile, nw_tile, w_tile, sw_tile, se_tile]
        for neighbor in neighbors:
            if neighbor in black_tiles:
                adjacent_blacks += 1
            else:
                white_tiles.add(neighbor)
        if not ((adjacent_blacks == 0) or (adjacent_blacks > 2)):
            black_copy.add(tile)
    for tile in white_tiles:
        e_tile = (tile[0] + e[0], tile[1] + e[1])
        ne_tile = (tile[0] + ne[0], tile[1] + ne[1])
        nw_tile = (tile[0] + nw[0], tile[1] + nw[1])
        w_tile = (tile[0] + w[0], tile[1] + w[1])
        sw_tile = (tile[0] + sw[0], tile[1] + sw[1])
        se_tile = (tile[0] + se[0], tile[1] + se[1])
        adjacent_blacks = 0
        neighbors = [e_tile, ne_tile, nw_tile, w_tile, sw_tile, se_tile]
        for neighbor in neighbors:
            if neighbor in black_tiles:
                adjacent_blacks += 1
        if adjacent_blacks == 2:
            black_copy.add(tile)
    black_tiles = black_copy
    print len(black_tiles)
    
            