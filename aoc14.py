f = open('aoc14.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()
def listifyString(string):
    myList = []
    myList[:0] = string
    return myList

memory = {}
mask = []
mask = []
for line in problem_input:
    split_line = line.split(' = ')
    if split_line[0] == 'mask':
        mask = listifyString(split_line[1])
    else:
        address = split_line[0].split('[')[1][:-1]
        value = listifyString("{0:b}".format(long(split_line[1])))
        if len(value) < 36:
            for x in range(36-len(value)):
                value.insert(0, '0')
        for x in range(len(mask)):
            if mask[x] != 'X':
                value[x] = mask[x]
        value = ''.join(value)
        value = long(value, 2)
        memory[address] = value
sum_of_values = 0
for item in memory:
    sum_of_values += memory[item]
print('Part 1:')
print('The sum of all values is ' + str(sum_of_values))

# Part 2
memory = {}

def iterate_address(mask):
    addresses = []
    if 'X' not in mask:
        addresses += [long(''.join(mask), 2)]
    else:
        position = mask.index('X')
        zero_mask = mask[:]
        zero_mask[position] = '0'
        addresses += iterate_address(zero_mask)
        one_mask = mask[:]
        one_mask[position] = '1'
        addresses += iterate_address(one_mask)
        
    return addresses
addresses = []
for line in problem_input:
    split_line = line.split(' = ')
    if split_line[0] == 'mask':
        mask = listifyString(split_line[1])
        
            
    else:
        addresses = []
        address = listifyString('{0:b}'.format(int(split_line[0].split('[')[1][:-1])))
    
        #value = listifyString("{0:b}".format(long(split_line[1])))
        value = long(split_line[1])
        if len(address) < 36:
            for x in range(36-len(address)):
                address.insert(0, '0')
        for x in range(len(address)):
            if mask[x] == '1':
                address[x] = '1'
            elif mask[x] == 'X':
                address[x] = 'X'
        
        if 'X' in address:
            addresses += iterate_address(address)
        else:
            addresses += [long(''.join(value), 2)]
        for item in addresses:
            memory[item] = value
            
sum_of_values = 0
for item in memory:
    sum_of_values += memory[item]
print('Part 2:')
print('The sum of all values is ' + str(sum_of_values))
    
                
        
        