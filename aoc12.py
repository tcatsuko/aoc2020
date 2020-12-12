import math
f = open('aoc12.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()
ship = [0,0]
facing = 90
for line in problem_input:
    command = line[0]
    value = int(line[1:])
    if command == 'N':
        ship[1] += value
    elif command == 'S':
        ship[1] -= value
    elif command == 'E':
        ship[0] += value
    elif command == 'W':
        ship[0]-= value
    elif command == 'R':
        facing += value
    elif command == 'L':
        facing -= value
    elif command == 'F':
        # Get direction
        direction = facing % 360
        if direction == 0:
            ship[1] += value
        elif direction == 90:
            ship[0] += value
        elif direction == 180:
            ship[1] -= value
        elif direction == 270:
            ship[0] -= value

part1 = abs(ship[0]) + abs(ship[1])
print('Part 1:')
print('Manhattan distance between current location and starting position is ' + str(part1))

ship = [0,0]
waypoint = [10,1]
for line in problem_input:
    command = line[0]
    value = int(line[1:])
    if command == 'N':
        waypoint[1] += value
    elif command == 'S':
        waypoint[1] -= value
    elif command == 'E':
        waypoint[0] += value
    elif command == 'W':
        waypoint[0] -= value
    elif command == 'R':
        s = math.sin(math.radians(-1 * value))
        c = math.cos(math.radians(-1 * value))
        new_point = [waypoint[0], waypoint[1]]
        x_new = int(new_point[0]*c) - int(new_point[1]*s)
        y_new = int(new_point[0]*s) + int(new_point[1]*c)
        waypoint = [x_new, y_new]
    elif command == 'L':
        s = math.sin(math.radians(value))
        c = math.cos(math.radians(value))
        new_point = [waypoint[0],waypoint[1]]
        x_new = int(new_point[0]*c) - int(new_point[1]*s)
        y_new = int(new_point[0]*s) + int(new_point[1]*c)
        waypoint = [x_new, y_new]
    elif command == 'F':
        # Get direction
        ship[0] += value * waypoint[0]
        ship[1] += value * waypoint[1]
part2 = abs(ship[0]) + abs(ship[1])
print('Part 2:')
print('Manhattan distance between current location and starting position is ' + str(part2))
            