import sys
f = open('aoc09.txt','r')
problem_input = []
for line in f:
    problem_input += [int(line[:-1])]
f.close()

def find_addend(my_array, target):
    for number in my_array:
        if number >= target:
            continue
        other_number = target - number
        if other_number in my_array:
            return True
        
    return False

def find_contig(my_array, target):
    min_number = sys.maxint * sys.maxint
    max_number = 0
    current_sum = 0
    for x in range(len(my_array)):
        for y in range(x, len(my_array)):
            current_number = my_array[y]
            if current_number >= target:
                min_number = sys.maxint * sys.maxint
                max_number = 0
                current_sum = 0
                break
            current_sum += current_number
            if current_sum > target:
                current_sum = 0
                min_number = sys.maxint * sys.maxint
                max_number = 0 
                break
            
            if current_number < min_number:
                min_number = current_number
            if current_number > max_number:
                max_number = current_number
            if current_sum == target:
                return min_number + max_number
    return 0

preamble = 25
current_position = preamble
for x in range(preamble, len(problem_input)):
    target = problem_input[x]
    choices = problem_input[x - preamble:x]
    if find_addend(choices, target) == False:
        
        break
print('Part 1: ')
print('First number without property is ' + str(target))
# Part 2
weakness = find_contig(problem_input, target)
print('Part 2:')
print('Encryption weakness is ' + str(weakness))
            
        