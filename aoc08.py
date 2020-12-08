f = open('aoc08.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()
# create empty array to count how many times an instruction has been called
def empty_instruction_counter(program):
    ic = []
    for x in xrange(len(program)):
        ic += [0]
    return ic

ic = empty_instruction_counter(problem_input)

def run_program(program):
    pc = 0
    acc = 0
    ic = empty_instruction_counter(program)
    correctly_terminates = False
    while True:
        if pc == len(program):
            correctly_terminates = True
            break
        current_instruction = program[pc]
        split_instruction = current_instruction.split(' ')
        if ic[pc] == 0:
            ic[pc] += 1
        else:
            break    
        if split_instruction[0] == 'nop':
            pc += 1
        elif split_instruction[0] == 'acc':
            acc += int(split_instruction[1])
            pc += 1
        elif split_instruction[0] == 'jmp':
            pc += int(split_instruction[1])
    return (correctly_terminates, acc)

(correctly_terminates, acc) = run_program(problem_input)

    
print('Part 1:')
print('The accumulator is at ' + str(acc) + ' just before the first duplicate instruction')

# Part 2:
# first determine valid places to change jmp to nop
switch_points = []
pc = 0
for command in problem_input:
    split_command = command.split(' ')
    if split_command[0] == 'nop' and int(split_command[1]) != 0:
        switch_points += [pc]
    elif split_command[0] == 'jmp':
        switch_points += [pc]
    pc += 1
acc = 0
for point in switch_points:
    new_program = problem_input[:]
    change_line = new_program[point]
    split_line = change_line.split(' ')
    if split_line[0] == 'nop':
        new_program[point] = 'jmp ' + split_line[1]
    else:
        new_program[point] = 'nop ' + split_line[1]
    (correctly_terminates, acc) = run_program(new_program)
    if correctly_terminates == True:
        break
print('Part 2:')
print('The accumulator is at ' + str(acc) + ' with the program fixed.')

