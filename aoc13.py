import fractions
f = open('aoc13.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()

def lcm(input_array):
    if len(input_array) == 1:
        return input_array[0]
    elif len(input_array) == 2:
        return abs(input_array[0]*input_array[1]) // fractions.gcd(input_array[0], input_array[1])
    else:
        new_array = []
        new_array += [abs(input_array[0]*input_array[1]) // fractions.gcd(input_array[0], input_array[1])]
        new_array += input_array[2:]
        return lcm(new_array)
    
depart = int(problem_input[0])
buses_raw = problem_input[1].split(',')
buses = []
wait_times = []
for bus in buses_raw:
    if bus == 'x':
        continue
    buses += [int(bus)]
buses.sort()
print()
for bus in buses:
    wait_times += [bus - depart%bus]
minimum_wait = min(wait_times)
first_bus = buses[wait_times.index(minimum_wait)]
print('Part 1:')
print('Earliest bus * minute wait = ' + str(first_bus * minimum_wait))


buses = []
offsets = []
offset = 0

for bus in buses_raw:
    if bus == 'x':
        offset += 1
    else:
        buses += [int(bus)]
        offsets += [offset]
        offset += 1
time = 0
good_buses = [buses[0]]
multiple = buses[0]
while True:
    if len(good_buses) == len(buses):
        break
    time += multiple
    for x in range(len(buses)):
        if (time + offsets[x]) % buses[x] == 0:
            if buses[x] not in good_buses:
                good_buses += [buses[x]]
                #multiple = np.lcm.reduce(good_buses)
                multiple = lcm(good_buses)
                keep_going = True
        else:
            break
print('Part 2:')
print('The earliest timestamp that all IDs depart at the right offset is ' + str(time))