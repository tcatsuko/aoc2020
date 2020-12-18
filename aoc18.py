f = open('aoc18.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()

def reduce_problem(problem):
    new_problem = []
    current_pos = 0
    while current_pos < len(problem):
        current_item = problem[current_pos]
        if current_item == '(':
            while current_pos < len(problem):
                if problem[current_pos] == '(':
                    left_side = current_pos + 1
                    parentheses = 1
                    while parentheses > 0:
                        current_pos += 1
                        if problem[current_pos] == '(':
                            parentheses += 1
                        elif problem[current_pos] == ')':
                            parentheses -= 1
                    right_side = current_pos 
                    new_problem += [reduce_problem(problem[left_side:right_side])]
                    
                    break
        else:
            new_problem += [current_item]
        current_pos += 1
    # Parse through for addition
    while new_problem.count('+') > 0:
        first_plus = new_problem.index('+')
        left_index = first_plus - 1
        left_item = new_problem[left_index]
        right_item = new_problem[first_plus + 1]
        my_sum = left_item + right_item
        del new_problem[left_index:first_plus+2]
        new_problem.insert(left_index, my_sum)
        
    while new_problem.count('*') > 0:
        first_multiply = new_problem.index('*')
        left_index = first_multiply - 1
        left_item = new_problem[left_index]
        right_item = new_problem[first_multiply + 1]
        my_product = left_item * right_item
        del new_problem[left_index:first_multiply + 2]
        new_problem.insert(left_index, my_product)
    return new_problem[0]

def calculate_problem(problem):
    first_item = problem[0]
    current_result = 0
    if first_item == '(':
        current_result = calculate_problem(problem[1:])
        parentheses = 1
        current_pos = 0
        while parentheses > 0:
            current_pos += 1
            if problem[current_pos] == '(':
                parentheses += 1
            elif problem[current_pos] == ')':
                parentheses -= 1
    else:
        current_result = problem[0]
        current_pos = 0
    while current_pos < len(problem) - 1:
        current_pos += 1
        operator = problem[current_pos]
        if operator == ')':
            return current_result
        current_pos += 1
        operand = problem[current_pos]
        if operand == '(':
            operand = calculate_problem(problem[1 + current_pos:])
            parentheses = 1
            
            while parentheses > 0:
                current_pos += 1
                if problem[current_pos] == '(':
                    parentheses += 1
                elif problem[current_pos] == ')':
                    parentheses -= 1            
        if operator == '+':
            current_result += operand
        else:
            current_result *= operand
    return current_result


problems = []
for line in problem_input:
    split_line = line.split(' ')
    new_line = []
    for item in split_line:
        if item == '*':
            new_line += ['*']
        elif item == '+':
            new_line += ['+']
        elif '(' in item:
            split_item = item.split('(')
            for item in split_item[0:-1]:
                new_line += ['(']
            new_line += [int(split_item[-1])]
        elif ')' in item:
            split_item = item.split(')')
            new_line += [int(split_item[0])]
            for item in split_item[1:]:
                new_line += [')']
        else:
            new_line += [int(item)]
    problems += [new_line]

total_sum = 0
problem_results = []
for item in problems:
    problem_results += [calculate_problem(item)]
print('Part 1:')
print('Sum of all problems is ' + str(sum(problem_results)))

part2 = []
for problem in problems:
    part2 += [reduce_problem(problem)]
print('Part 2:')
print('The sum of all problems is ' + str(sum(part2)))
    
    
    
        
        
    

