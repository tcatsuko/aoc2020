import re
f = open('aoc20.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()

tiles = {}
new_tile = True
tile_number = -1
current_tile = []

def get_left(tile):
    left_edge = []
    for row in tile:
        left_edge += row[0]
    return left_edge
def get_right(tile):
    right_edge = []
    for row in tile:
        right_edge += row[-1]
    return right_edge
def get_top(tile):
    return tile[0]
def get_bottom(tile):
    return tile[-1]

def listifyString(string):
    myList = []
    myList[:0] = string
    return myList

def rotate_right(tile):
    if len(tile) == 0:
        return
    new_tile = []
    for column in range(len(tile[0])):
        new_row = []
        for row in range(len(tile)-1,-1,-1):
            new_row += tile[row][column]
        new_tile += [new_row]
    if get_top(tile) == get_right(new_tile):
        print('rotation good')
    return new_tile

def flip_horiz(tile):
    new_tile = tile[:]
    new_tile.reverse()
    return new_tile



for line in problem_input:
    if line == '':
        tiles[tile_number] = [current_tile]
        new_tile = True
        current_tile = []
        continue
    if new_tile == True:
        new_tile = False
    split_input = line.split(' ')
    if len(split_input) == 2:
        tile_number = int(split_input[1][:-1])
    else:
        
        tile_data = listifyString(split_input[0])
        current_tile += [tile_data]
#tiles[tile_number] = [current_tile]

for tile in tiles:
    if tile == 3079:
        print()
    orig_tile = tiles[tile][0]
    right_ninety = rotate_right(tiles[tile][0])
    tiles[tile] += [right_ninety]
    right_ninety = rotate_right(right_ninety[:])
    tiles[tile] += [right_ninety]
    right_ninety = rotate_right(right_ninety[:])
    tiles[tile] += [right_ninety]
    flipped_tile = flip_horiz(orig_tile)
    tiles[tile] += [flipped_tile]
    right_ninety = rotate_right(flipped_tile[:])
    tiles[tile] += [right_ninety]
    right_ninety = rotate_right(right_ninety[:])
    tiles[tile] += [right_ninety]
    right_ninety = rotate_right(right_ninety[:])
    tiles[tile] += [right_ninety]    
    print()
tile_positions = {}
unmatched_tiles = list(tiles.keys())
first_tile = unmatched_tiles[0]
for tile in tiles:
    tile_info = {}
    tile_info['number'] = -1
    tile_info['right'] = None
    tile_info['left'] = None
    tile_info['top'] = None
    tile_info['bottom'] = None
    tile_info['free_borders'] = 4
    tile_info['complete'] = False
    tile_positions[tile] = tile_info

tile_positions[first_tile]['number'] = 0

completed_tiles = set()
while len(completed_tiles) < len(tiles):

    for tile in tile_positions:
        if tile_positions[tile]['number'] != -1:
            current_tile_number = tile_positions[tile]['number']
            current_tile = tiles[tile][current_tile_number]
            current_right_edge = get_right(current_tile)
            current_left_edge = get_left(current_tile)
            current_top_edge = get_top(current_tile)
            current_bottom_edge = get_bottom(current_tile)
            if tile_positions[tile]['right'] == None:
                found_right = False
                for neighbor in tiles:
                    if found_right == True:
                        break
                    if neighbor == tile:
                        continue
                    if neighbor == 3079:
                        print()
                    if tile_positions[neighbor]['number'] == -1:
                        # We need to check all possible tiles
                        for neighbor_number in range(len(tiles[neighbor])):
                            neighbor_left_edge = get_left(tiles[neighbor][neighbor_number])
                            if neighbor_left_edge == current_right_edge:
                                
                                tile_positions[neighbor]['number'] = neighbor_number
                                tile_positions[neighbor]['left'] = tile
                                tile_positions[tile]['right'] = neighbor
                                tile_positions[tile]['free_borders'] -= 1
                                tile_positions[neighbor]['free_borders'] -= 1
                                found_right = True
                                break
                    else:
                        neighbor_number = tile_positions[neighbor]['number']
                        neighbor_left_edge = get_left(tiles[neighbor][neighbor_number])
                        if neighbor_left_edge == current_right_edge:
                            tile_positions[neighbor]['left'] = tile
                            tile_positions[neighbor]['free_borders'] -= 1
                            tile_positions[tile]['right'] = neighbor
                            tile_positions[tile]['free_borders'] -= 1
                            found_right = True
                            
            if tile_positions[tile]['left'] == None:
                found_left = False
                for neighbor in tiles:
                    if found_left == True:
                        break
                    if neighbor == tile:
                        continue
                    if tile_positions[neighbor]['number'] == -1:
                        # We need to check all possible tiles
                        for neighbor_number in range(len(tiles[neighbor])):
                            neighbor_right_edge = get_right(tiles[neighbor][neighbor_number])
                            if neighbor_right_edge == current_left_edge:
                                
                                tile_positions[neighbor]['number'] = neighbor_number 
                                tile_positions[neighbor]['right'] = tile
                                tile_positions[tile]['left'] = neighbor
                                tile_positions[tile]['free_borders'] -= 1
                                tile_positions[neighbor]['free_borders'] -= 1
                                found_left = True
                                break
                    else:
                        neighbor_number = tile_positions[neighbor]['number']
                        neighbor_right_edge = get_right(tiles[neighbor][neighbor_number])
                        if neighbor_right_edge == current_left_edge:
                            tile_positions[neighbor]['right'] = tile
                            tile_positions[neighbor]['free_borders'] -= 1
                            tile_positions[tile]['left'] = neighbor
                            tile_positions[tile]['free_borders'] -= 1
                            found_left = True
                    
                
                
    
            if tile_positions[tile]['top'] == None:
                found_top = False
                for neighbor in tiles:
                    if found_top == True:
                        break
                    if neighbor == tile:
                        continue
                    if tile_positions[neighbor]['number'] == -1:
                        for neighbor_number in range(len(tiles[neighbor])):
                            neighbor_bottom_edge = get_bottom(tiles[neighbor][neighbor_number])
                            if neighbor_bottom_edge == current_top_edge:
                                
                                tile_positions[neighbor]['number'] = neighbor_number 
                                tile_positions[neighbor]['bottom'] = tile
                                tile_positions[tile]['top'] = neighbor
                                tile_positions[tile]['free_borders'] -= 1
                                tile_positions[neighbor]['free_borders'] -= 1
                                found_top = True
                                break                        
                    else:
                        neighbor_number = tile_positions[neighbor]['number']
                        neighbor_bottom_edge = get_bottom(tiles[neighbor][neighbor_number])
                        if neighbor_bottom_edge == current_top_edge:
                            tile_positions[neighbor]['bottom'] = tile
                            tile_positions[neighbor]['free_borders'] -= 1
                            tile_positions[tile]['top'] = neighbor
                            tile_positions[tile]['free_borders'] -= 1
                            found_top = True                    
            if tile_positions[tile]['bottom'] == None:
                found_bottom = False
                for neighbor in tiles:
                    if found_bottom == True:
                        break
                    if neighbor == tile:
                        continue
                    if tile_positions[neighbor]['number'] == -1:
                        for neighbor_number in range(len(tiles[neighbor])):
                            neighbor_top_edge = get_top(tiles[neighbor][neighbor_number])
                            if neighbor_top_edge == current_bottom_edge:
                                
                                tile_positions[neighbor]['number'] = neighbor_number 
                                tile_positions[neighbor]['top'] = tile
                                tile_positions[tile]['bottom'] = neighbor
                                tile_positions[tile]['free_borders'] -= 1
                                tile_positions[neighbor]['free_borders'] -= 1
                                found_bottom = True
                                break                        
                    else:
                        neighbor_number = tile_positions[neighbor]['number']
                        neighbor_top_edge = get_top(tiles[neighbor][neighbor_number])
                        if neighbor_top_edge == current_bottom_edge:
                            tile_positions[neighbor]['top'] = tile
                            tile_positions[neighbor]['free_borders'] -= 1
                            tile_positions[tile]['bottom'] = neighbor
                            tile_positions[tile]['free_borders'] -= 1
                            found_bottom = True                            
            print('Completed tile number ' + str(tile))
            completed_tiles.add(tile)
corner_tiles = []
for tile in tile_positions:
    if tile_positions[tile]['free_borders'] == 2:
        corner_tiles += [tile]
product = 1
for number in corner_tiles:
    product *= number
print('Part 1:')
print('The product of all 4 corner tile IDs is ' + str(product))
# 432779307313047843347 too high

# Remove borders
good_tiles = {}

for tile in tile_positions:
    tile_number = tile_positions[tile]['number']
    original_tile = tiles[tile][tile_number]
    # remove first and last rows
    del original_tile[0]
    del original_tile[-1]
    # remove edges
    for row in original_tile:
        del row[0]
        del row[-1]
    good_tiles[tile] = original_tile
print()
# Find top left tile
corner_tile = None
for tile in tile_positions:
    if tile_positions[tile]['left'] == None and tile_positions[tile]['top'] == None:
        corner_tile = tile
        break
print()
bottom = tile_positions[corner_tile]['bottom']
right = tile_positions[corner_tile]['right']
patched_image = []
current_tile = corner_tile
def build_blank_row(tile):
    blank_row = []
    for row in tile:
        blank_row += [[]]
    return blank_row
current_row = build_blank_row(good_tiles[corner_tile])

while corner_tile is not None:
    tile = good_tiles[current_tile]
    for x in range(len(tile)):
        current_row[x] += tile[x]
    next_tile = tile_positions[current_tile]['right']
    if next_tile == None:
        patched_image += current_row
        current_row = build_blank_row(tile)
        corner_tile = tile_positions[corner_tile]['bottom']
        current_tile = corner_tile
    else:
        current_tile = next_tile
print('stitched image')
middle_monster = re.compile('[#][.|#]{4}[#]{2}[.|#]{4}[#]{2}[.|#]{4}[#]{3}')

dragon_found = False
if dragon_found == False:
    for x in range(4):
        if dragon_found == True:
            break
        patched_image = rotate_right(patched_image[:])
        for row in range(1, len(patched_image)-1):
            current_row = patched_image[row]
            for m in middle_monster.finditer(''.join(current_row)):
                upper_row = patched_image[row - 1]
                lower_row = patched_image[row + 1]
                # See if there's a dragon
                dragon_tail = m.start()
                if lower_row[dragon_tail + 1] == '#' and lower_row[dragon_tail + 4] == '#' and lower_row[dragon_tail + 7] == '#' and lower_row[dragon_tail + 10] == '#' and lower_row[dragon_tail + 13] == '#' and lower_row[dragon_tail + 16] == '#' and upper_row[dragon_tail + 18] == '#':
                    dragon_found = True
                    print('Found dragon!')  
                    print('Position: ' + str(dragon_tail))
if dragon_found == False:
    patched_image = flip_horiz(patched_image[:])
    for x in range(4):
        if dragon_found == True:
            break
        patched_image = rotate_right(patched_image[:])
        for row in range(1, len(patched_image)-1):
            current_row = patched_image[row]
            for m in middle_monster.finditer(''.join(current_row)):
                upper_row = patched_image[row - 1]
                lower_row = patched_image[row + 1]
                # See if there's a dragon
                dragon_tail = m.start()
                if lower_row[dragon_tail + 1] == '#' and lower_row[dragon_tail + 4] == '#' and lower_row[dragon_tail + 7] == '#' and lower_row[dragon_tail + 10] == '#' and lower_row[dragon_tail + 13] == '#' and lower_row[dragon_tail + 16] == '#' and upper_row[dragon_tail + 18] == '#':
                    dragon_found = True
                    print('Found dragon!')  
print('Next!')
dragons = 0
waves = 0
for row in patched_image:
    waves += ''.join(row).count('#')
    
for row in range(1, len(patched_image)-1):
    current_row = patched_image[row]

    for m in middle_monster.finditer(''.join(current_row)):
        upper_row = patched_image[row - 1]
        lower_row = patched_image[row + 1]
        # See if there's a dragon
        dragon_tail = m.start()
        if lower_row[dragon_tail + 1] == '#' and lower_row[dragon_tail + 4] == '#' and lower_row[dragon_tail + 7] == '#' and lower_row[dragon_tail + 10] == '#' and lower_row[dragon_tail + 13] == '#' and lower_row[dragon_tail + 16] == '#' and upper_row[dragon_tail + 18] == '#':
            dragons += 1
            print('Found dragon!')
waves -= (dragons * 15)
print('Part 2:' )
print('Roughness is ' + str(waves))
