f = open('test_aoc20.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()

tiles = {}
new_tile = True
tile_number = -1
current_tile = []
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
            new_row += tile[column][row]
        new_tile += [new_row]
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

for tile in tiles:
    right_ninety = rotate_right(tiles[tile][0])