f = open('aoc06.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()

def listifyString(string):
    myList = []
    myList[:0] = string
    return myList

group_data = []
current_group=[]

# Parse input into groups, and change each passenger's string response into array of chars
for line in problem_input:
    if line == '':
        group_data += [current_group]
        current_group = []
        continue
    else:
        current_passenger = listifyString(line)
        current_group += [current_passenger]
group_data += [current_group]

# Part 1: find total number of questions answered (no duplicates) in each group
answer_counts = 0
for group in group_data:
    my_set = set()
    for passenger in group:
        for answer in passenger:
            my_set.add(answer)
    answer_counts += len(my_set)
print('Part 1:')
print('The sum of yes counts is ' + str(answer_counts))

# Part 2: Now count up common answers in each group
answer_counts = 0
for group in group_data:
    if len(group) == 1:
        answer_counts += len(group[0])
    else:
        result = set(group[0])
        for passenger in group[1:]:
            result.intersection_update(passenger)
        answer_counts += len(list(result))
print('Part 2:')
print('The sum of common answers in each group is ' + str(answer_counts))
        